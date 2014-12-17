#!/usr/bin/env python
# encoding: utf-8

import re


if raw_input("create a new user[y]?").lower() == "y":
    with open("/etc/ppp/chap-secrets", "a+") as fp:
        user = raw_input("user:")
        if user:
            passwd = raw_input("password:")
            if passwd:
                fp.write("\n%s\tpptpd\t%s\n" % (user, passwd))

with open("/etc/pptpd.conf", "rt+") as fp:
    txt = fp.read()
    if not re.search(r"^localip\s", txt, re.M):
        print("set local ip: 192.168.0.1")
        fp.write("\nlocalip 192.168.0.1\n")
    if not re.search(r"^remoteip\s", txt, re.M):
        print("set remote ip: 192.168.0.234-238")
        fp.write("\nremoteip 192.168.0.234-238\n")

with open("/etc/ppp/pptpd-options", "rt+") as fp:
    txt = fp.read()
    if not re.search(r"^ms-dns\s", txt, re.M):
        print("set ms-dns: 114.114.114.114")
        fp.write("\nms-dns 114.114.114.114\n")

with open("/etc/sysctl.conf", "rt+") as fp:
    txt = fp.read()
    if not re.search(r"^net\.ipv4\.ip_forward\b", txt, re.M):
        print("set net.ipv4.ip_forward")
        fp.write("\nnet.ipv4.ip_forward = 1\n")
