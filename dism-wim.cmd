Prompt $p$_#$s
cls
Dism /Get-WimInfo /WimFile:sources\install.wim
pause

rem index:1
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:1 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Capture-Image /ImageFile:install_dism.wim /CaptureDir:dism_mount /Name:"Windows 10 ��ͥ��" /Description:"Windows 10 ��ͥ�� (x64)" /Compress:max /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism.wim
pause

rem index:2
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:2 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Append-Image /ImageFile:install_dism.wim /CaptureDir:dism_mount /Name:"Windows 10 ��ͥ�����԰�" /Description:"Windows 10 ��ͥ�����԰� (x64)" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism.wim
pause

rem index:3
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:3 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Append-Image /ImageFile:install_dism.wim /CaptureDir:dism_mount /Name:"Windows 10 ������" /Description:"Windows 10 ������ (x64)" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism.wim
pause

rem index:4
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:4 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Append-Image /ImageFile:install_dism.wim /CaptureDir:dism_mount /Name:"Windows 10 רҵ��" /Description:"Windows 10 רҵ�� (x64)" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism.wim
pause

rem index:5
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:5 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Append-Image /ImageFile:install_dism.wim /CaptureDir:dism_mount /Name:"Windows 10 רҵ������" /Description:"Windows 10 רҵ������ (x64)" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism.wim
pause

rem index:6
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:6 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Append-Image /ImageFile:install_dism.wim /CaptureDir:dism_mount /Name:"Windows 10 רҵ����վ��" /Description:"Windows 10 רҵ����վ�� (x64)" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount

cls
Dism /Get-WimInfo /WimFile:install_dism.wim