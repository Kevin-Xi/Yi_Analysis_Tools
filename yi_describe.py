#-- coding: utf-8 --#
import sys
#import codecs
from xml.dom import minidom
#from django.utils.encoding import smart_str				# Way 1: Work

name = ['坤', '艮', '坎', '巽', '震', '离', '兑', '乾']

def describe(gua_no):
	#yi_xml_file = codecs.open('yi.xml', 'a+', 'utf-8')		# Way 0: Failed
	#yi_xml_doc = minidom.parse(yi_xml_file)
	reload(sys)												# Way 2: Work
	sys.setdefaultencoding('utf-8')

	yi_xml_doc = minidom.parse('yi.xml')
	yi_content = yi_xml_doc.childNodes[0]
	gua = yi_content.childNodes[gua_no*2-1]

	gua_name = gua.attributes['name'].value
	#gua_name = smart_str(gua_name)

	down = up =0

	for i in range(1, 6, 2):
		down = down*2 + int(gua.childNodes[i].attributes['p'].value)

	for i in range(7, 12, 2):
		up = up*2 + int(gua.childNodes[i].attributes['p'].value)

	print '{0}：{1}下{2}上\n'.format(gua_name, name[down], name[up])


if __name__ == '__main__':
	try:
		describe(int(sys.argv[1]))
	except:
		for i in range(1, 65):
			describe(i)
