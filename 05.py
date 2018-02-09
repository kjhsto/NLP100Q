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

qw = "I am an NLPer"
qw2 = qw.split(" ")

print(ngram(qw2,N=2))
print(ngram(qw2,N=1))
