#coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import random
mail_info = {
    "from": "m17865313385@163.com",
    "to": "12391@moe.edu.cn",
    "hostname": "smtp.163.com",
    "username": "m17865313385@163.com",
    "password": "sunjinhua123",
    "mail_subject": "举报·广东茂名幼儿师范专科学校·",
    "mail_text": "这并不是儿戏，其学校之行为实在令人气愤。前半个月学校突然通知学校安排实习，为了这次实习，学校安排原本的课程都不上了，都停课，让上创业课。然后接着开会，通知我们必须实习，不实习不给毕业证。其做法实在令人气愤。今日前去广州，原来实习并不是学校安排的，是一个中介！！！而且，其合同实在令人不齿，要求每天6点起床，去接送孩子，中午孩子休息老师不能休息，必须从6点上到晚上，甚至要熬夜做手工，说是副班的工作，实际上是保育员的工作！在这每天12+小时的工作量下，每个月的工资只有1200元！！！希望政府及时处理此事，希望看到大中国政府的办事效率，还我们大学生一片净土。（这是否是学校和中介的钱权交易。国家教育部的《中等职业学校学生实习管理办法》有明文规定不得通过中介，不得安排学生每天顶岗超过8小时。希望政府查出幕后交易链，做一个为人民服务的政府，而不是让人民为其服务的政府!）\n政府着手处理此事时希望得到邮件回复。本人电话17865313385。",
    "mail_encoding": "utf-8"
}

def main():
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])
    msg = MIMEText(mail_info["mail_text"]+str(random.random()), "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

    smtp.quit()


import threading

def start():
    try:
        while True:
            main() 
    except Exception as e:
        print e
        start()



threads = []

start()
for i in range(5):
    t = threading.Thread(target=start)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
    
