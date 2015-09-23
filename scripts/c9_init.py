#!/usr/bin/env python
# encoding: utf-8

import os


os.system("git clone https://github.com/MrLYC/mkenv.git")
os.system("cd mkenv/mkenv; make git-alias")
os.system("git config --global user.name MrLYC")
os.system("git config --global user.email imyikong@gmail.com")
