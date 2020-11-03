#!/usr/bin/python3
# -*- coding:utf-8 -*-
import poplib
import os
from email.parser import Parser

# 输入邮件地址, 口令和POP3服务器地址:
pop3_server = "ccc"
email = "wangxu@ccc.net"
password = "123"

print(u"Connecting to %s ..." % pop3_server)
server = poplib.POP3(pop3_server)
#server.set_debuglevel(1)       # 可以打开或关闭调试信息
print(server.getwelcome().decode('utf-8'))  # 可选:打印POP3服务器的欢迎文字
server.user(email)
server.pass_(password)
print(u"Scanning InBox...")
mblist = server.list()[1]
print(u'Messages: %s. Size: %s' % server.stat())        # stat()返回邮件数量和占用空间:
resp, mails, octets = server.list()     # list()返回所有邮件的编号
#print(mails)  # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)

# get email from, to, subject attribute value.
Message_ID = msg.get('Message-ID')

print( '\nNew Mail:' )
print('Mail ID: ' + Message_ID )
print('From: ' + msg.get('From') )
print('To: ' + msg.get('To') )
print('Subject: ' + msg.get('Subject') )
print('\n')

os.system("msg /server:127.0.0.1 * /w \"Hello World\"")

userDir = os.environ['USERPROFILE']

#print( userDir + "\emailcheck.log" )
with open(userDir +"\emailcheck.log","w") as f:
    f.write(Message_ID)


server.quit()
