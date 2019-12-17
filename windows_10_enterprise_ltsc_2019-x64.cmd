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
