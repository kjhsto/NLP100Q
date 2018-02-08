#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

st1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
st2 = st1.split(" ")
num = {1,5,6,7,8,9,15,16,19}
result = {}
n = 0

for i in st2:
	n = n + 1
	if n in num:
		result[i[0:1]] = n
	else:
		result[i[0:2]] = n


print(result)

#for i in st2:
#	 = 