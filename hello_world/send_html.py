# coding=utf-8
import os,datetime,time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 设定根目录
result_dir = r"E:\codings\ancunbase\report"
# 获取根目录下的所有文件
lists = os.listdir(result_dir)
# 将根目录下的文件按创建时间升序排序；
lists.sort(key=lambda fn:   os.path.getatime(result_dir+"\\"+fn)if not os.path.isdir(result_dir+"\\"+fn) else 0)
# -1 表示文件列表中的最大值
# print ('最新文件为：'+ lists[-1])
# join连接字符串，得到文件的完整路径；
filepath = os.path.join(result_dir,lists[-1])
# print filepath
# 发送邮箱
sender = "1017313484@qq.com"
# 接收邮箱
# receiver = "tuchunlai@ancun.com"
receiver = "2737181033@qq.com"
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
msg = MIMEText(mail_body,'html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
# smtp.connect('smtp.qq.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()