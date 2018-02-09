#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(target,N=2): 
	#targetにはリスト型しか入らないよ
	#N=2の時は単語のバイグラム、N=1の時は文字のバイグラム
	
	result = []

	if(N==2):
		for i in range(len(target)-1):
			result.append(target[i:i+2])
	if(N==1):
		hs = "".join(target)
		for i in range(len(hs)-1):
			result.append(hs[i:i+2])
	
	return(result)

x="paraparaparadise"
y="paragraph"

x1 = set(ngram(x,2))
y1 = set(ngram(y,2))

print(x1 | y1)
print(x1 & y1)
print(x1 - y1)
print(y1 - x1)

s1=set(["se"])

print(s1.issubset(x1))
print(s1.issubset(y1))



