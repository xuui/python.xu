#!/usr/bin/python3
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 配置 SMTP 服务器
mail_host="ccc"                 #设置服务器域名或者IP
mail_user="wangxu@ccc.net"      #用户名
mail_pass="123"                 #口令

#mail_host="127.0.0.1"           #设置服务器域名或者IP
#mail_user=""                    #用户名
#mail_pass=""                    #口令


sender = 'wangxu@ccc.net'       # 发件人的邮件地址
#receivers = ['luotao@ccc.net']  # 接收人的邮件地址
receivers = ['wangxu@ccc.net']  # 接收人的邮件地址
#receivers = ['wangchangyi@ccc.net']  # 接收人的邮件地址

#message = MIMEText(mail_msg, 'html', 'utf-8')
message = MIMEMultipart('related')
message['From'] = Header(u"TD 提醒", 'utf-8')
message['To'] =  Header(u"luotao@ccc.net", 'utf-8')
message['X-Priority'] = '1'
subject = u'Python 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

mail_msg = """
<div style="background-color:#ff9101;color:#fff;line-height:1;padding:12px;">
<img src="cid:mail_logo"><!-- mail_logo.png -->
</div>
<p>Python 邮件发送HTML测试...</p>
<p><a href="http://git.ccc.net">这是一个链接</a></p>
"""

msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

fp = open('mail_logo.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<mail_logo>')
message.attach(msgImage)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print u"邮件发送成功"
except smtplib.SMTPException:
    print u"Error: 无法发送邮件"
