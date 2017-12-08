import os, glob, sys
import smtplib
import email.mime.multipart
import email.mime.text
from urllib import request
import zlib


def testOS():
    print(os.getcwd())
    print(dir(os))
    print(help(os))


def testGlob():
    return glob.glob("*.txt")


def testArgv():
    return sys.argv


def testMail():
    msg = email.mime.multipart.MIMEMultipart
    msg['from'] = 'minghzhang@163.com'
    msg['to'] = 'zhangminghua01@corp.netease.com'
    msg['subject'] = 'test'
    content = '你好！这是一封自动发送的邮件！'
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect(host='smtp.163.com')
    smtp.login('minghzhang@163.com', '1017635978asd')
    smtp.sendmail('minghzhang@163.com', 'zhangminghua01@corp.netease.com', str(msg))
    smtp.quit()


def testZlib():
    s = b'witch which has which witches wrist watch'
    print(len(s))
    t = zlib.compress(s)
    print(len(t))
    ss = zlib.decompress(t)
    print(ss)
    crc = zlib.crc32(s)
    print(crc)


testZlib()
