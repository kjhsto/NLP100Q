#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("hightemp.txt",encoding="utf-8")
naiyou = f.read()
f.close()

naiyou2 = naiyou.replace("\t"," ")

print(naiyou2)