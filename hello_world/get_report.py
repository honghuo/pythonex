# coding=utf-8
import os,datetime,time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 设定根目录
result_dir = r"E:\codings\ancunbase\report"

# 发送邮箱
sender = "1017313484@qq.com"
# 接收邮箱
receiver = "tuchunlai@ancun.com"
# 发送邮件主题
subject = 'python send html test'
# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户/密码
username = '1017313484@qq.com'
password = 'uujktiyijjkxbbii'
# 中文需参数‘utf-8’，单字节字符不需要
fp = open(filepath,"rb")
mail_body = fp.read()
message = MIMEText(mail_body,'html','utf-8')
message['From'] = Header("TCL",'utf-8')
message["To"] = Header("TEST",'utf-8')
subject = "添加产品测试报告"
message['Subject'] = Header(subject,'utf-8')
smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
# smtp.connect('smtp.qq.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,message.as_string())
smtp.quit()