#!/usr/bin/python2.7
# encoding:utf-8
import shutil
import winreg

# Updata Registry.
regKey=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\xuui\Classes\CLSID\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\shell\DevMgr", 0, winreg.KEY_WRITE)
#winreg.SetValueEx(regKey,"OEMBackground",0,winreg.REG_DWORD,1)
winreg.SetValue(regKey,"@",0,winreg.REG_SZ,'设备(&Q)')
winreg.SetValue(regKey,"icon",0,winreg.REG_SZ,'CompMgmtLauncher.exe')
winreg.CloseKey(regKey)
