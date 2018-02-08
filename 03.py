#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = ""

#.と,を省くよ。
s2 = re.sub("[,.]" , "" , s1)

#リストを作るよ
s3 = s2.split(" ")

for i in s3:
	result = result + str(len(i))

print(result)