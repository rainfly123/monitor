#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import os
import requests
import time
import aes
import threading
import daemon
import hashlib
import send

URL = "http://new.southtv.cn:9180"
gids = {"cctv1":"", "cctv3":"", "cctv6":"", "cctv13":"", "cctv8":"", "cctv5":"", "cctv5p":"", "zjws":"", "bjws":"", "jsws":"", "gdws":"", "gdty":"", "gdxw":"", "gdgg":"", "tvs2":"", "zjpd":""}

class cdn(threading.Thread):

    def __init__(self, gid):
        threading.Thread.__init__(self)
        self.gid = gid

    def run(self):
        encrypt_data = aes.Encrypt()
        url = "%s/%s/live.m3u8?token=%s"%(URL,self.gid, encrypt_data)
        md5 = ""
        try:
            q = requests.get(url, headers={"User-Agent":"ijkplayer"})
            #print q.content
            q.connection.close()
            m2 = hashlib.md5()
            m2.update(q.content)
            md5 = m2.hexdigest()
        except:
            print "ERROR"
            send.cSend(self.gid)
        if gids[self.gid] == md5:
            print "ERROR"
            send.mSend(self.gid)
        else:
            gids[self.gid] = md5

if __name__ == "__main__":
    daemon.daemonize("/tmp/cdn.pid")
    os.chdir("/data")

    while True:
        for gid in gids.keys():
            t = cdn(gid)
            t.start()
        time.sleep(15)

