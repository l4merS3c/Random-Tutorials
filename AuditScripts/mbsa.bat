@echo OFF
echo === Gathering information for %COMPUTERNAME% ===
mkdir %COMPUTERNAME%
mbsacli.exe /nvc /xmlout /wi /unicode /catalog "%CD%\wsusscn2.cab" > %COMPUTERNAME%/%COMPUTERNAME%_MBSA.xml
