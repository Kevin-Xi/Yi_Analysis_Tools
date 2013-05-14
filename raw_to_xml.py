#-- coding: utf-8 --#

f_ori = open('yi_yao_only')
f_xml = file('yi.xml', 'w')

line = '1'
no_gua = 0
no_yao = 0

while line:
	line = f_ori.readline()
	if line[:3] == '第':
		no_yao = 0
		no_gua += 1
		if no_gua > 1 and no_gua <= 64:
			f_xml.write('</gua>\n\n')
		if no_gua <= 10 :
			f_xml.write('<gua name="%s" no="%d">\n' % (line[10:line.find('　' , 10)], no_gua))
		elif no_gua <= 20 or no_gua % 10 == 0:
			f_xml.write('<gua name="%s" no="%d">\n' % (line[13:line.find('　' , 13)], no_gua))
		else:
			f_xml.write('<gua name="%s" no="%d">\n' % (line[16:line.find('　' , 16)], no_gua))
	else:
		no_yao += 1
		if no_yao == 1 or no_yao == 6:
			f_xml.write('    <yao p="%s" no="%d">%s</yao>\n' % (line[9:line.find('：', 9)], no_yao, line[18:line.find('\n', 18)]))
		else:
			f_xml.write('    <yao p="%s" no="%d">%s</yao>\n' % (line[6:line.find('：', 6)], no_yao, line[18:line.find('\n', 18)]))

f_xml.write('</gua>\n\n')

f_xml.flush()
f_xml.close()
f_ori.close()
