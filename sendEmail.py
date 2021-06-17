#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Email:
    def __init__(self):
        self.mail_host = "smtp.qq.com"
        self.mail_user = "416090014@qq.com"
        self.mail_pass = "liocpcbaerppbhij"
        self.sender = 'jason@t.com'
        self.receivers = ['j542397cly@qq.com']

        self.message = MIMEText('京东抢购商品已抢到货, 请速度登陆京东APP查看并支付', 'plain', 'utf-8')
        self.message['From'] = Header("jason", 'utf-8')
        self.message['To'] = Header("j542397cly", 'utf-8')

        self.subject = 'JASON: 脚本京东抢购商品已抢到，请火速登陆App'
        self.message['Subject'] = Header(self.subject, 'utf-8')

    def sendEmail(self):
        try:
            # smtpObj = smtplib.SMTP()
            # smtpObj.connect(mail_host, 465)
            # smtpObj.login(mail_user,mail_pass)
            # smtpObj.sendmail(sender, receivers, message.as_string())
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(self.mail_user, self.mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.sendmail(self.mail_user, ['j542397cly@qq.com', ], self.message.as_string())
            server.quit()
            print(" 成功 send email success")
        except smtplib.SMTPException as e:
            print("Error: sned email error" + str(e))
