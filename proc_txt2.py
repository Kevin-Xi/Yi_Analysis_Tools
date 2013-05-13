#-- coding: utf-8 --#

f_ori=open('yi_withoutxiang')
f_pro=file('yi_yaoonly', 'w')

str='1'
while str:
	str=f_ori.readline()
	#if str[:3] == '第' or str[6:9] == ('初' or '上' or '六' or '九'):
	if str[:3] == '第' or str[6:9] == '初' or str[6:9] == '上' or str[6:9] == '六' or str[6:9] == '九':
		f_pro.write(str)

f_pro.flush()
f_pro.close()
f_ori.close()
