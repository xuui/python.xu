#!/usr/bin/python3
# -*- coding:utf-8 -*-
import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据:
sckt.sendto(b'Maya',('127.0.0.1',16900))
# 接收数据:
print(sckt.recv(255).decode('utf-8'))

sckt.close()
