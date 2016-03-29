#!/usr/bin/python
# -*- coding: UTF-8 -*-

def text_create(name,msg):
	local = 'E:\Python27\\'''
	full_path = name+'.txt'
	filea = open(full_path,'w')
	filea.write(msg)
	filea.close()
	print 'Done'
def filter(word,censored_word='lame',change_word='Awesome'):
	return word.replace(censored_word,change_word)

def fulltext(name,msg):
	clean = filter(msg)
	text_create(name,clean)
print fulltext('try','lame,lame,lame,lame')
