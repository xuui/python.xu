rem  Windows 10 家庭版
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_consumer_1903-x64.wim /index:1 /MountDir:dism_mount
Dism /Capture-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 家庭版" /Description:"Windows 10 家庭版" /Compress:max /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem  Windows 10 家庭单语言版
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_consumer_1903-x64.wim /index:2 /MountDir:dism_mount
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 家庭单语言版" /Description:"Windows 10 家庭单语言版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem  Windows 10 教育版
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_business_1903-x64.wim /index:1 /MountDir:dism_mount
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 教育版" /Description:"Windows 10 教育版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem  Windows 10 专业版
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_business_1903-x64.wim /index:3 /MountDir:dism_mount
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 专业版" /Description:"Windows 10 专业版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem  Windows 10 专业教育版
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_business_1903-x64.wim /index:4 /MountDir:dism_mount
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 专业教育版" /Description:"Windows 10 专业教育版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem  Windows 10 专业工作站版
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_business_1903-x64.wim /index:5 /MountDir:dism_mount
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 专业工作站版" /Description:"Windows 10 专业工作站版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem  Windows 10 企业版
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_business_1903-x64.wim /index:2 /MountDir:dism_mount
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 企业版" /Description:"Windows 10 企业版" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim

rem  Windows 10 企业版 LTSC
md dism_mount
Dism /Mount-Wim /WimFile:windows_10_enterprise_ltsc_2019-x64.wim /index:1 /MountDir:dism_mount
Dism /Append-Image /ImageFile:install_dism-x64.wim /CaptureDir:dism_mount /Name:"Windows 10 企业版 LTSC" /Description:"Windows 10 企业版 LTSC" /CheckIntegrity /Verify
Dism /Unmount-Wim /MountDir:dism_mount /discard
rd /s /q dism_mount
Dism /Get-WimInfo /WimFile:install_dism-x64.wim
