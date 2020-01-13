Prompt $p$_#$s
Dism /Get-WimInfo /WimFile:sources\install.wim

rem /Capture-Image index-1
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:1 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /image:dism_mount /enable-feature /featurename:SMB1Protocol
Dism /Capture-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 家庭版" /Description:"Windows 10 家庭版" /Compress:max /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem /Append-Image index-2
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:2 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /image:dism_mount /enable-feature /featurename:SMB1Protocol
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 家庭单语言版" /Description:"Windows 10 家庭单语言版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem /Append-Image index-3
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:3 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /image:dism_mount /enable-feature /featurename:SMB1Protocol
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 教育版" /Description:"Windows 10 教育版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem /Append-Image index-4
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:4 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /image:dism_mount /enable-feature /featurename:SMB1Protocol
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 专业版" /Description:"Windows 10 专业版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem /Append-Image index-5
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:5 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /image:dism_mount /enable-feature /featurename:SMB1Protocol
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 专业教育版" /Description:"Windows 10 专业教育版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem /Append-Image index-6
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:6 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /image:dism_mount /enable-feature /featurename:SMB1Protocol
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 专业工作站版" /Description:"Windows 10 专业工作站版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim
