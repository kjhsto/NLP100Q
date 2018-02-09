#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

result = ""

st = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
st_list = st.split(" ")

for i in st_list: 
	if(len(i) >= 4):
		first = i[0:1]
		end = i[len(i)-1:len(i)]
		i = i[1:len(i)-1]
		i = random.sample(list(i),len(i))
		i = first + "".join(i) + end
	result = (result + " " + i)

result = result[1:]
print(result)