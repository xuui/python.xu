﻿#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import shutil
import winreg

# OEM Login Registry.
# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background]
# "OEMBackground"=dword:00000001

# C:\Windows\System32\oobe\info\backgrounds\backgroundDefault.jpg
path='C:/Windows/System32/oobe/info/backgrounds'
logofile='C:/Windows/System32/oobe/info/backgrounds/backgroundDefault.jpg'

#repo.is_dirty()

def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fKb" % (kb)

if os.path.exists(path):
    #print "Path's Y"
    if os.path.exists(logofile):
        #print "logo's Y"
        size = os.path.getsize(logofile)
        #shutil.copy('oemlogo.jpg',logofile)
        print 'OEM logo: ' + formatSize(size)
    else:
        #print "logo's N"
        shutil.copy('oemlogo.jpg',logofile)
else:
    #print "Path's a N"
    os.makedirs(path)
    shutil.copy('oemlogo.jpg',logofile)

# Updata Registry.
regKey=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background", 0, winreg.KEY_WRITE)
winreg.SetValueEx(regKey,"OEMBackground",0,winreg.REG_DWORD,1)
winreg.CloseKey(regKey)

