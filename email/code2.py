#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# -------------------------------------------->
mail_addr = '发件人地址'
mail_pass = '密码'
to_mail = '收件人'
mail_head = 'test email 测试邮件'
mail_content = '''
    这是测试文件
'''
# 添加的附件
filepath = r'C:\Users\Administrator\Desktop\123.pdf'
# -------------------------------------------->
'''创建一个带附件的实例'''
message = MIMEMultipart()
message['From'] = Header(mail_addr)
message['To'] = Header(to_mail)
message['Subject'] = Header(mail_head, 'utf-8')
# 邮件正文内容
message.attach(MIMEText(mail_content, 'plain', 'utf-8'))
# 构建附件
att1 = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = "application/octet-stream"
att1["Content-Disposition"] = "attachment; filename=123.pdf"
message.attach(att1)

smTp = smtplib.SMTP()
smTp.connect('SMTP.163.com', 25)
# 打印debug日志
# smTp.set_debuglevel(1)
try:
    smTp.login(mail_addr, mail_pass)
except smtplib.SMTPAuthenticationError:
    print('用户认证失败！')
    exit()
smTp.sendmail(mail_addr, to_mail, message.as_string())
smTp.close()
