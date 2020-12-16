#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] == 2:
    import _winreg as winreg
else:
    import winreg

  
winreg.SetValue(
    winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Classes\\.md',
    winreg.REG_SZ,'MarkDown.Document')
winreg.SetValue(
    winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\Classes\\MarkDown.Document\\shell\\open\\command',
    winreg.REG_SZ,'"D:\\Python2.7.11\\pythonw.exe" "D:\\markdown\\main.py" -i "%1"')

winreg.SetValue(
    winreg.HKEY_CLASSES_ROOT,'.md',
    winreg.REG_SZ,'MarkDown.Document')

winreg.SetValue(
    winreg.HKEY_CLASSES_ROOT,'xuui',
    winreg.REG_NONE,'XuuiProtocol')

