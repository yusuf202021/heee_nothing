import re


cpp_code = r"""__declspec(noinline, safebuffers) bool DownloadFile(const char* URL, const char* OutPath)
{
    char extraInfo[1024] = { 0 };
    char hostName[1024] = { 0 };
    char passwordSet[1024] = { 0 };
    char schemeUrl[1024] = { 0 };
    char fileUrlPath[1024] = { 0 };
    char userName[1024] = { 0 };
    URL_COMPONENTSA urlcomponents;

    RtlZeroMemory(&urlcomponents, sizeof urlcomponents);

    urlcomponents.dwStructSize = sizeof(URL_COMPONENTS);
    urlcomponents.dwHostNameLength = 1024;
    urlcomponents.dwPasswordLength = 1024;
    urlcomponents.dwSchemeLength = 1024;
    urlcomponents.dwUrlPathLength = 1024;
    urlcomponents.dwUserNameLength = 1024;
    urlcomponents.dwExtraInfoLength = 1024;
    urlcomponents.lpszExtraInfo = extraInfo;
    urlcomponents.lpszHostName = hostName;
    urlcomponents.lpszPassword = passwordSet;
    urlcomponents.lpszScheme = schemeUrl;
    urlcomponents.lpszUrlPath = fileUrlPath;
    urlcomponents.lpszUserName = userName;



    ASSERT(LI_FN(InternetCrackUrlA)(URL, strlen(URL), 0, &urlcomponents));


    DWORD dwRequestFlags = (strcmp(urlcomponents.lpszScheme, "https") == 0) ? INTERNET_FLAG_SECURE : 0;

    HINTERNET hInternet = InternetOpenA("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);

    ASSERT(hInternet)

    HINTERNET hConnect = InternetConnectA(hInternet, urlcomponents.lpszHostName, urlcomponents.nPort, NULL, NULL, INTERNET_SERVICE_HTTP, 0, 0);

    ASSERT(hConnect)

    HINTERNET hRequest = HttpOpenRequestA(hConnect, NULL, urlcomponents.lpszUrlPath, "HTTP/1.0", NULL, NULL, dwRequestFlags, 0);

    ASSERT(hRequest)

    ASSERT(HttpSendRequestA(hRequest, NULL, 0, NULL, NULL));

    DWORD statusCode = 0;
    DWORD length = sizeof(DWORD);
    ASSERT(HttpQueryInfoA(
        hRequest,
        HTTP_QUERY_STATUS_CODE | HTTP_QUERY_FLAG_NUMBER,
        &statusCode,
        &length,
        NULL
    ));

    if (!(200 <= statusCode < 400))
        return false;



    HANDLE hFile = CreateFileA(
        OutPath,
        GENERIC_WRITE,
        0,
        NULL,
        CREATE_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL
    );

    if (hFile == INVALID_HANDLE_VALUE)
        return false;


    char buffer[1025] = {'\00'};
    DWORD wrt = 1;
    while (wrt)
    {
        ASSERT(InternetReadFile(hRequest, buffer, sizeof buffer - 1, &wrt));
        buffer[wrt] = 0;
        if (wrt)
            ASSERT(WriteFile(hFile, buffer, wrt, NULL, NULL));
    }
    return true;
}"""



def inline_string(string):
    encoded = string.encode()
    size = len(encoded) + (8 - len(encoded)%8)
    
    variable_name = string[:8].replace('/', '_').replace('+', '_').replace('-', '_').replace(chr(92), '_').replace('.', '_') + "_string"
    
    result = f"    SIZE_T {variable_name}[{size // 8}] = {chr(123)}{'0, '*(size//8)}{chr(125)};\n"
    
    idx = 0

    while encoded:
        result += f"    {variable_name}[{idx}] = {hex(int.from_bytes(encoded[:8], 'little'))};\n"
        encoded = encoded[8:]
        idx+=1
    return variable_name, result
string_pattern = re.compile(r'\"(.*?)\"|\'(.*?)\'', re.DOTALL)

strings = [s[0] if s[0] else s[1] for s in string_pattern.findall(cpp_code) if s[0] or s[1]]


for string in strings:
    variable_name, inlined_string = inline_string(string)
    
    cpp_code = cpp_code.replace(f'"{string}"', f"(LPCSTR){variable_name}")
    
    splited_lines = cpp_code.splitlines()
    
    splited_lines.insert(2, inlined_string)
    cpp_code = "\n".join(splited_lines)
    

print(cpp_code)
