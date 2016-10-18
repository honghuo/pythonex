# coding=utf-8
import smtplib,py_zip_file
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
def sendemial():
    # 发送邮箱
    sender = "1017313484@qq.com"
    # 接收邮箱
    receiver = "tuchunlai@ancun.com"
    # receiver = "2737181033@qq.com"
    # 发送邮件主题
    subject = 'python send html test'
    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户/密码
    username = '1017313484@qq.com'
    password = 'uujktiyijjkxbbii'
    # 中文需参数‘utf-8’，单字节字符不需要
    # Multipart
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    # 中的文字部分
    part = MIMEText("hi，all:附件是基础平台本次测试的测试用例、日志和测试报告，请检阅",'plain','utf-8')
    msg.attach(part)
    # 这是附件部分
    filename = r"attach_file/"+ datetime.datetime.now().date().isoformat()
    filepath = py_zip_file.py_zip(filename,)
    part = MIMEApplication(open(filepath,'rb').read())
    part.add_header("Content-Dispositon",'attachment',filename = "安存基础平台测试结果")
    msg.attach(part)
    smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
    # smtp.connect('smtp.qq.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    """删除"""
sendemial()