cd "C:\Users\runneradmin"
mkdir .pktriot
echo '{
"version": "v0.15.3",
"key": "c6f287e4cf8162149151acf8d67933135002f1d2e1cbc607dd9408104add356a",
"hostname": "green-pine-76806.pktriot.net",
"serverKey": "a07157e2fe136c09eacc0755a364256c6b596b57b7c27f02b9629bceb5f8fb0c",
 "serverHost": "us-east-65319.packetriot.net"
}' > .pktriot\config.json
cd "C:\Users\runneradmin\Desktop"
mkdir proxy_utils
$ProgressPreference="silentlycontinue"
iwr "https://www.charlesproxy.com/assets/release/4.6.5/charles-proxy-4.6.5-win64.msi" -OutFile proxy_utils\charles-proxy.msi
iwr "https://www.proxifier.com/download/ProxifierSetup.exe" -OutFile proxy_utils\ProxifierSetup.exe


iwr "https://laptop-updates.brave.com/download/BRV010" -OutFile proxy_utils\BraveBrowserSetup-BRV010.exe
iwr "https://downloads.vivaldi.com/stable/Vivaldi.6.6.3271.50.x64.exe" -OutFile proxy_utils\Vivaldi.6.6.3271.50.x64.exe
iwr "https://github.com/maxthon/Maxthon/releases/download/7.1.8.6001/maxthon_7.1.8.6001_x64.exe" -OutFile proxy_utils\maxthon_7.1.8.6001_x64.exe
iwr "https://net.geo.opera.com/opera/stable/windows?utm_source=google&utm_medium=ose&utm_campaign=(none)&http_referrer=https://www.google.com/&utm_site=opera_com&dl_token=78326158" -OutFile proxy_utils\Opera.exe
iwr "https://download.packetriot.com//windows/pktriot-0.15.3.win64.zip" -OutFile proxy_utils\pktriot-0.15.3.win64.zip
Expand-Archive proxy_utils\pktriot-0.15.3.win64.zip
msiexec /i proxy_utils\charles-proxy.msi /quiet /qn /norestart

Import-Module -Name International -UseWindowsPowerShell
Set-WinUserLanguageList tr-TR -Confirm:$false -Force
& "proxy_utils\BraveBrowserSetup-BRV010.exe"
& "proxy_utils\Vivaldi.6.6.3271.50.x64.exe" --vivaldi-silent --do-not-launch-chrome --system-level > 1.txt

while (!(Test-Path "C:\Program Files\Charles\lib\charles.jar")) {}
iwr "https://github.com/yusuf202021/heee_nothing/raw/main/charles.jar" -OutFile "C:\Program Files\Charles\lib\charles.jar"

