#-- coding: utf-8 --#

f_ori=open('yi_complete')
f_pro=file('yi', 'w')

str='1'
while str:
	str=f_ori.readline()
	if str != '\n' and str[6:12] != '象曰':
		f_pro.write(str)

f_pro.flush()
f_pro.close()
f_ori.close()
