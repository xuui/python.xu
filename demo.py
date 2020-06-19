#!/usr/bin/python3
# encoding:utf-8
# pip install GitPython

# print('hello','World!')
# name = input('please enter your name: ')
# print('hello,', name)

import sys
import os
import getpass

print('I\'m \"OK\"!')
print('''line1
... line2
... line3''')
print('''hello,\n
world''')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#print os.getlogin()
print getpass.getuser()
#print getpass.getpass()

content = os.popen('net user '+ getpass.getuser() +' /domain').read()
print content


print('37 ∷ ∴ ∵ × ÷ ° ℃ ‰')