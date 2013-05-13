#-- coding: utf-8 --#

f_ori=open('yi_yao_only')

count=0
mystr='1'
strtemp=''
while mystr:
	mystr=f_ori.readline()
	if mystr[:3] == '第':
		if count != 0 and count != 6:
			print strtemp, count
		count=0
		strtemp = mystr
	elif mystr[:3] == '\xe3\x80\x80':
		count+=1

f_ori.close()
