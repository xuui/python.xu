#!/usr/bin/python2.7
# encoding:gbk
import shutil
import winreg

# Computer Right menus Registry.
# 设备管理器
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\DevMgr") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "设备(&Q)")
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, "CompMgmtLauncher.exe")
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\DevMgr\command") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "mmc devmgmt.msc")

# 卸载程序
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\Dezinstall") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "卸载(&U)")
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, "OptionalFeatures.exe")
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\Dezinstall\command") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl")

#控制面板
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\Control") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "控制(&C)")
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, "Control.exe")
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\Control\command") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Control.exe")

# 服务管理
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\services") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "服务(&V)")
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, "UI0Detect.exe")
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\services\command") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "mmc services.msc")

# 组策略对象编辑器
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\GroupPolicyEditor") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "组策略(&Z)")
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, "mmc.exe")
with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\GroupPolicyEditor\command") as key:
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "mmc gpedit.msc")

