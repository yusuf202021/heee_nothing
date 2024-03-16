$ProgressPreference="silentlycontinue"
iwr "https://pixeldrain.com/api/file/nTooqKca?download=a" -OutFile proxy_utils.zip
Expand-Archive proxy_utils.zip
rm proxy_utils.zip


iwr "https://laptop-updates.brave.com/download/BRV010" -OutFile proxy_utils\BraveBrowserSetup-BRV010.exe
iwr "https://downloads.vivaldi.com/stable/Vivaldi.6.6.3271.50.x64.exe" -OutFile proxy_utils\Vivaldi.6.6.3271.50.x64.exe
iwr "https://github.com/maxthon/Maxthon/releases/download/7.1.8.6001/maxthon_7.1.8.6001_x64.exe" -OutFile proxy_utils\maxthon_7.1.8.6001_x64.exe
iwr "https://net.geo.opera.com/opera/stable/windows?utm_source=google&utm_medium=ose&utm_campaign=(none)&http_referrer=https://www.google.com/&utm_site=opera_com&dl_token=78326158" -OutFile proxy_utils\Opera.exe
