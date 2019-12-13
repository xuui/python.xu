#!/usr/bin/python2.7
# encoding:utf-8

# OEM Login
# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background]
# "OEMBackground"=dword:00000001

# C:\Windows\System32\oobe\info\backgrounds\backgroundDefault.jpg
path='C:/Windows/System32/oobe/info/backgrounds'
oemfile='C:/Windows/System32/oobe/info/backgrounds/backgroundDefault.jpg'

import os
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
        return "%fkb" % (kb)

if os.path.exists(path):
    print "Path's Y"
    if os.path.exists(oemfile):
        print "logo's Y"
        size = os.path.getsize(oemfile)
        print formatSize(size)
    else:
        print "logo's N"
else:
  print "Path's a N"

    