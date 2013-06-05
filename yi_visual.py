import sys
import Image
from xml.dom import minidom

def visual(gua_no):
	yi_xml_doc = minidom.parse('yi.xml')
	yi_content = yi_xml_doc.childNodes[0]
	gua = yi_content.childNodes[gua_no*2-1]
	yaos = gua.childNodes
	
	no_sum = 0
#	no_sum = sum([int(yao.attributes['p'].value) for yao in yaos
	for i in range(1, 12, 2):
		no_sum += int(yaos[i].attributes['p'].value)
	
	return no_sum

def merge(column):
	imgs_sum = []
	for i in range(1, 65):
		imgs_sum.append(visual(i))

	imgs = []
	for i in range(7):
		imgs.append(Image.new('L', (128, 128), 255*i/6))
	
	img_h = imgs[0].size[1]
	img_w = imgs[0].size[0]
	row = 64 / column

	merge_img = Image.new('L', (img_w*column, img_h*row), 0)
	for no, img_sum in enumerate(imgs_sum):
		merge_img.paste(imgs[img_sum], (no%column*img_w, no/column*img_h))

	merge_img.save('yi{}x{}.png'.format(row, column), quality=70)

if __name__ == '__main__':
	try:
		merge(int(sys.argv[1]))
	except:
		merge(8)
