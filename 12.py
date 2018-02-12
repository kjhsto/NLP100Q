#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("hightemp.txt","r",encoding="utf-8")
naiyou = f.readlines()
f.close()

lis = []
result1 = ""
result2 = ""

for i in naiyou:
	sb = i.split("\t")
	lis.append(sb)

for b in lis:
	result1 += b[0] + "\n"
	result2 += b[1] + "\n"

result1 = result1[:-1]
result2 = result2[:-1]

f= open("col1.txt","w",encoding="utf-8")
f.write(result1)
f.close()

f= open("col2.txt","w",encoding="utf-8")
f.write(result2)
f.close()