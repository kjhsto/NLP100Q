#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("hightemp.txt",encoding="utf-8")
lines = f.readlines()
f.close()

result = len(lines)

print(result)