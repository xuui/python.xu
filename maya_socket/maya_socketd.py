#!/usr/bin/python3
# -*- coding:utf-8 -*-
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0',16900)) # 绑定端口

print('Server Open POST: 16900...')

while True:
    # 接收数据:
    data, addr = server.recvfrom(255)
    print('Client from %s:%s.' % addr)
    print('Say:', data.decode('utf-8'))
    reply = 'Hello, %s!' % data.decode('utf-8')
    server.sendto(reply.encode('utf-8'), addr)
