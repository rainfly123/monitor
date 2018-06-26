#!/usr/bin/env python
#coding:utf-8
import sys
import os
import time
import aes
import daemon

URL = "http://new.southtv.cn:9180"
gids = {"cctv1":"", "cctv3":"", "cctv6":"", "cctv13":"", "cctv8":"", "cctv5":"", "cctv5p":"", "zjws":"", "bjws":"", "jsws":"", "gdws":"", "gdty":"", "gdxw":"", "gdgg":"", "tvs2":"", "zjpd":""}


if __name__ == "__main__":
    daemon.daemonize("/tmp/watch.pid")
    while 1:
        try:
            os.remove(".chan")
        except:
            pass

        f = open(".chan", "w")
        for gid in gids.keys():
            encrypt_data = aes.Encrypt()
            url = "%s/%s/live.m3u8?token=%s\n"%(URL, gid, encrypt_data)
            f.write(url)
        f.close()

        time.sleep(7100)
