#!/usr/bin/env python
# -*- coding: utf-8 -*-

s1 = "I have a pen"
st_ls = list(s1)
result = ""

for i in st_ls:
	asc = ord(i)
	if(97 <= asc <= 122):
		asc = 219 - asc
		i = chr(asc)	
	result = result + i

print(result)