Prompt $p$_#$s
Dism /Get-WimInfo /WimFile:sources\install.wim

rem /Export-Image index-1
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:1 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Unmount-Wim /MountDir:dism_mount /commit
Dism /Export-Image /SourceImageFile:sources\install.wim /SourceIndex:1 /DestinationImageFile:install_dism-x64.wim /Compress:max /CheckIntegrity
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem /Capture-Image index-1
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:1 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Capture-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Name" /Description:"Description" /Compress:max /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem /Append-Image index-2
md dism_mount
Dism /Mount-Wim /WimFile:sources\install.wim /index:2 /MountDir:dism_mount
Dism /image:dism_mount /enable-feature /featurename:NetFX3 /All /Source:.\sources\sxs /LimitAccess
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Name" /Description:"Description" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim


