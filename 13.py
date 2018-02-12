#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("col1.txt","r",encoding="utf-8")
col1 = f.readlines()
f.close()

f2 = open("col2.txt","r",encoding="utf-8")
col2 = f2.readlines()
f2.close()

result = ""

sb = zip(col1,col2)

for i in sb:
	result += i[0].replace("\n","") + "\t" + i[1]

f3 = open("col1t2.txt","w",encoding="utf-8")
f3.write(result)
f3.close()