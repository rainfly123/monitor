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
cgids = {"cctv1":0, "cctv3":0, "cctv6":0, "cctv13":0, "cctv8":0, "cctv5":0, "cctv5p":0, "zjws":0, "bjws":0, "jsws":0, "gdws":0, "gdty":0, "gdxw":0, "gdgg":0, "tvs2":0, "zjpd":0}

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
            if q.status_code != 200:
                print "Server Reply ERROR"
                cgids[self.gid] += 1
                if cgids[self.gid] % 4 == 0:
                    send.cSend(self.gid)
                return
        except:
            print "Connect ERROR"
            cgids[self.gid] += 1
            if cgids[self.gid] % 4 == 0:
                send.cSend(self.gid)
            return
        if gids[self.gid] == md5:
            print "Md5 ERROR"
            cgids[self.gid] += 1
            if cgids[self.gid] % 4 == 0:
                send.mSend(self.gid)
        else:
            gids[self.gid] = md5
            if cgids[self.gid] > 3:
                cgids[self.gid] = 0
                send.okSend(self.gid)

if __name__ == "__main__":
    daemon.daemonize("/tmp/cdn.pid")
    os.chdir("/data")

    while True:
        for gid in gids.keys():
            t = cdn(gid)
            t.start()
        time.sleep(25)

