#!/usr/bin/env python
# encoding: utf-8

source_list = set(l.strip() for l in
"""
deb http://mirrors.163.com/ubuntu/ precise-updates main restricted
deb-src http://mirrors.163.com/ubuntu/ precise-updates main restricted
deb http://mirrors.163.com/ubuntu/ precise universe
deb-src http://mirrors.163.com/ubuntu/ precise universe
deb http://mirrors.163.com/ubuntu/ precise-updates universe
deb-src http://mirrors.163.com/ubuntu/ precise-updates universe
deb http://mirrors.163.com/ubuntu/ precise multiverse
deb-src http://mirrors.163.com/ubuntu/ precise multiverse
deb http://mirrors.163.com/ubuntu/ precise-updates multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-updates multiverse
deb http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
""".split("\n") if l)

source_list_path = "/etc/apt/sources.list"

sys_source_list = set()

with open(source_list_path, "a+") as fp:
    sys_source_list.update(l.strip() for l in fp)

    source_list = source_list - sys_source_list

    fp.writelines("\n%s" % source for source in source_list)
