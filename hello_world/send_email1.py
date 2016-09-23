# coding=utf-8
import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = "smtp.qq.com"
mail_user = '1017313484@qq.com'
mail_pass = 'uujktiyijjkxbbii'

sender = "1017313484@qq.com"
receivers = ['tuchunlai@ancun.com']
# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("TCL",'utf-8')
message["To"] = Header("TEST",'utf-8')
subject = "添加产品测试报告"
message['Subject'] = Header(subject,'utf-8')
# 邮件正文内容
message.attach(MIMEText("hi，附件是本次测试所得的测试报告，请检阅",'plain','utf-8'))
# 构造附件1，传送测试报告
# 设定根目录
result_dir = r"E:\codings\ancunbase\report"
# 获取根目录下的所有文件
lists = os.listdir(result_dir)
# 将根目录下的文件按创建时间升序排序；
lists.sort(key=lambda fn:   os.path.getatime(result_dir+"\\"+fn)if not os.path.isdir(result_dir+"\\"+fn) else 0)
# -1 表示文件列表中的最大值
print ('最新文件为：'+ lists[-1])
# join连接字符串，得到文件的完整路径；
filepath = os.path.join(result_dir,lists[-1])
# 这里的base64 也许可以改成html
att1 = MIMEText(open(filepath,'rb').read(),'plain','utf-8')
att1['Content-Type'] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1['Content-Dispositon'] = 'attachment;filename="产品测试报告.html"'
att1.add_header('Content-Dispositon','attachment',filename="产品测试报告.html")
message.attach(att1)
try:
    smtp = smtplib.SMTP_SSL(mail_host,465)
    # smtp.connect('smtp.qq.com')
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receivers,message.as_string())
    print "发送成功"
    smtp.quit()
except Exception:
    print "发送失败"
finally:
    print "that's all"