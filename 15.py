#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

clh = sys.argv
N = int(clh[1])

f = open("hightemp.txt","r",encoding="utf-8")
hightemp = f.readlines()
f.close()

result = ""

for i in hightemp[-N:]:
	result += i

result = result[:-1]

print(result)