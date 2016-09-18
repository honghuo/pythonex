# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "1017313484@qq.com"
receivers = ['tuchunlai@ancun.com']
message = MIMEMultipart()
message['From'] = Header("TCL",'utf-8')
message["To"] = Header("TEST",'utf-8')
subject = "添加产品测试报告"
message['Subject'] = Header(subject,'utf-8')
message.attach(MIMEText())