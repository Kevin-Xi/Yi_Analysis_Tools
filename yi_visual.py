# -*- coding : utf-8 -*- #
import sys
import Image
from xml.dom import minidom

def sumOfYangYao(gua_no):
	yi_xml_doc = minidom.parse('yi.xml')
	yi_content = yi_xml_doc.childNodes[0]
	gua = yi_content.childNodes[gua_no*2-1]
	yaos = gua.childNodes
	
	no_sum = 0
	for i in range(1, 12, 2):
		no_sum += int(yaos[i].attributes['p'].value)
	
	return no_sum

def merge(column):
	imgs_sum = []
	for i in range(1, 65):
		imgs_sum.append(sumOfYangYao(i))

	imgs = []
	for i in range(7):
		imgs.append(Image.new('L', (128, 128), 255*i/6))
	
	img_h = imgs[0].size[1]
	img_w = imgs[0].size[0]
	row = 64 / column

	merge_img = Image.new('L', (img_w*column, img_h*row), 0)
	for no, img_sum in enumerate(imgs_sum):
		merge_img.paste(imgs[img_sum], (no%column*img_w, no/column*img_h))

	merge_img.save('Visual/yi{}x{}.png'.format(row, column), quality=70)

def singleHexagram(gua_no, mode=1, save=0):
	reload(sys)
	sys.setdefaultencoding('utf-8')
	
	yin = Image.new('L', (8, 8), 0)
	yang = Image.new('L', (8, 8), 255)
	imgs = [yin, yang]

	yi_xml_doc = minidom.parse('yi.xml')
	yi_content = yi_xml_doc.childNodes[0]
	gua = yi_content.childNodes[gua_no*2-1]
	yaos = gua.childNodes

	hexagram_name = gua.attributes['name'].value

	if mode == 1:
		merge_img = Image.new('L', (8, 48), 0)
		for i in range(11, 0, -2):
			p = int(yaos[i].attributes['p'].value)
			merge_img.paste(imgs[p], (0, (11-i) * 4))
	elif mode == 2:
		merge_img = Image.new('L', (24, 16), 0)
		for i in range(1, 6, 2):
			p = int(yaos[i].attributes['p'].value)
			merge_img.paste(imgs[p], ((i/2 * 8, 8)))

		for i in range(7, 12, 2):
			p = int(yaos[i].attributes['p'].value)
			merge_img.paste(imgs[p], ((i-6)/2 * 8, 0))

	if save:
		merge_img.save('Visual/{}_{}_mode{}.png'.format(gua_no, hexagram_name, mode), quality=70)
	else:
		return merge_img

def allHexagram(mode=1):
	if mode == 1:
		merge_img = Image.new('L', (512, 48), 0)
		for i in range(1, 65):
			merge_img.paste(singleHexagram(i), ((i-1) * 8, 0))

	elif mode == 2:
		merge_img = Image.new('L', (192, 128), 0)
		for i in range(1, 65):
			merge_img.paste(singleHexagram(i, 2), ((i-1)%8*24, (i-1)/8*16))
		

	merge_img.save('Visual/yao_mode{}.png'.format(mode), quality=70)

if __name__ == '__main__':
	try:
		merge(int(sys.argv[1]))
	except:
		merge(8)
