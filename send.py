#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

to_addr = ["xiechangcai@southtv.cn", "longjinquan@southtv.cn"]

def cSend(gid):
    from_addr = "18910158363@163.com"
    password = "aa11bb22"
    smtp_server = "smtp.163.com"
    content =  '系统故障:链接直播地址失败:%s'%(gid)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'SLP系统<%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'系统故障请排查', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def mSend(gid):
    from_addr = "18910158363@163.com"
    password = "aa11bb22"
    smtp_server = "smtp.163.com"
    content =  '系统故障:直播源未更新:%s'%(gid)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'SLP系统<%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'系统故障请排查', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    #server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()



if __name__ == "__main__":
    cSend("cctv8")
    mSend("cctv8")
