#!/usr/bin/env python
# encoding: utf-8

import os


os.system("git clone https://github.com/MrLYC/mkenv.git /tmp/mkenv")
os.system("cd /tmp/mkenv/mkenv; make git-alias")
os.system("git config --global user.name MrLYC")
os.system("git config --global user.email imyikong@gmail.com")
os.system("git config --global core.editor vim")
