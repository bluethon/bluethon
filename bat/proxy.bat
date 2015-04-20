@echo off
cls
color 0A
::Echo The program is running...
::Echo Setting the ip and dns...
::netsh interface ip set address name="Local Connection" source=dhcp
::netsh interface ip delete dns "Local Connection" all
::ipconfig /flushdns
::ipconfig /all
::Echo Done.
Echo Setting the proxy
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "proxy-gg:8080" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyOverride /t REG_SZ /d "<local>" /f
ipconfig /flushdns
Echo Done.
Echo Press any key to leave...
Pause
