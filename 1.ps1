cd "C:\Users\runneradmin\Desktop"
mkdir proxy_utils
$ProgressPreference="silentlycontinue"
iwr "https://www.charlesproxy.com/assets/release/4.6.5/charles-proxy-4.6.5-win64.msi" -OutFile proxy_utils\charles-proxy.msi
iwr "https://www.proxifier.com/download/ProxifierSetup.exe" -OutFile proxy_utils\ProxifierSetup.exe


iwr "https://laptop-updates.brave.com/download/BRV010" -OutFile proxy_utils\BraveBrowserSetup-BRV010.exe
iwr "https://downloads.vivaldi.com/stable/Vivaldi.6.6.3271.50.x64.exe" -OutFile proxy_utils\Vivaldi.6.6.3271.50.x64.exe
iwr "https://github.com/maxthon/Maxthon/releases/download/7.1.8.6001/maxthon_7.1.8.6001_x64.exe" -OutFile proxy_utils\maxthon_7.1.8.6001_x64.exe
iwr "https://net.geo.opera.com/opera/stable/windows?utm_source=google&utm_medium=ose&utm_campaign=(none)&http_referrer=https://www.google.com/&utm_site=opera_com&dl_token=78326158" -OutFile proxy_utils\Opera.exe

msiexec /i proxy_utils\charles-proxy.msi /quiet /qn /norestart

Import-Module -Name International -UseWindowsPowerShell
Set-WinUserLanguageList tr-TR -Confirm:$false -Force
Start-Job {
  while (!(Test-Path "C:\Program Files\Charles\lib\charles.jar")) {}
  iwr "https://github.com/yusuf202021/heee_nothing/raw/main/charles.jar" -OutFile "https://github.com/yusuf202021/heee_nothing/raw/main/charles.jar"
}
