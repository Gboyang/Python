#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_addr = '发件邮箱'
mail_pass = '密码'
to_mail = '收件人'
# 邮件标题
mail_head = '邮件测试'
# 邮件内容
mail_content = '''
    This is an email
'''

if __name__ == '__main__':
    smTp = smtplib.SMTP()
    smTp.connect('SMTP.163.com', 25)
    # 打印debug日志
    smTp.set_debuglevel(1)
    smTp.login(mail_addr, mail_pass)
    info = MIMEText(mail_content, 'plain', 'utf-8')
    info['From'] = Header(mail_addr, 'utf-8')
    info['To'] = Header(to_mail)
    info['Subject'] = Header(mail_head)
    smTp.sendmail(mail_addr, to_mail, info.as_string())
    smTp.close()
