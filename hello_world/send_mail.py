# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱
sender = "1017313484@qq.com"
# 接收邮箱
receiver = "tuchunlai@ancun.com"
# 发送邮件主题
subject = 'python send email test'
# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户/密码
username = '1017313484@qq.com'
password = 'uujktiyijjkxbbii'
# 中文需参数‘utf-8’，单字节字符不需要
msg = MIMEText('你好','text','utf-8')
msg['Subject'] = Header(subject,'utf-8')
smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
# smtp.connect('smtp.qq.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
