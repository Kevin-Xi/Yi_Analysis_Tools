# -- coding=utf-8 -- #
"""Parser of Yi

Analyse specified Yao of a Gua

Usage:
	python yi_parser.py [options]

Options:
	-s ...			use specified xml file
	-g ...			specify a Gua, between 1 and 64
	-y ...			specify a Yao, between 1 and 6
	-a			analyse all
	-h			show help document

Examples:
	yi_parser.py -s new_yi.xml		use 'new_yi.xml' as source xml file
	yi_parser.py -g 32			analyse all Yao of Gua no.32
	yi_parser.py -y 5			analyse Yao no.5 of every Gua
	yi_parser.py -g 16 -y 3			analyse the third Yao of Gua no.16
	yi_parser.py -a			analyse all

Visit https://github.com/Kevin-Xi/Yi_Analysis_Tools for the latest version.
"""

from xml.dom import minidom
import sys
import getopt
import time

class Yi_parser():
	result = {}

	def __init__(self, xmlfile, gflag, yflag):
		xmldoc = minidom.parse(xmlfile)
		self.xmlroot = xmldoc.childNodes[0]
		target_gua = self.xmlroot.childNodes[gflag*2-1]
		self.yao_bucket = target_gua.childNodes
		self.target_yao = self.yao_bucket[yflag*2-1]
		self.gflag = gflag
		self.yflag = yflag
		self.parse()

	def parse(self):
		self.target_p = int(self.target_yao.attributes['p'].value)
		self.dangwei()
		self.dezhong()
		self.ying()
		self.cheng_up()			#乘
		self.cheng_down()		#承

	def dangwei(self):
		if self.yflag % 2 == self.target_p % 2:
			self.result['当位'] = 1
		else:
			self.result['当位'] = 0

	def dezhong(self):
		if self.yflag == 2 or self.yflag == 5:
			self.result['得中'] = 1
		else:
			self.result['得中'] = 0

	def ying(self):
		ying_no = self.yflag-3 > 0 and self.yflag-3 or self.yflag+3
		ying_p = int(self.yao_bucket[ying_no*2-1].attributes['p'].value)
		if self.target_p != ying_p:
			self.result['应'] = 1
		else:
			self.result['应'] = 0

	def cheng_up(self):
		try:
			cheng_p = int(self.yao_bucket[self.yflag*2-3].attributes['p'].value)
			if self.target_p == 1 and cheng_p == 0:
				self.result['乘'] = 1
			else:
				self.result['乘'] = 0
		except:
			self.result['乘'] = -1
		
	def cheng_down(self):
		try:
			cheng_p = int(self.yao_bucket[self.yflag*2+1].attributes['p'].value)
			if self.target_p == 0 and cheng_p == 1:
				self.result['承'] = 1
			else:
				self.result['承'] = 0
		except:
			self.result['承'] = -1

	def output(self):
		return ', '.join(['%s = %s' % (k, v) for k, v in self.result.items() if self.result[k] != -1]) + '\n'

class ArgOutofRangeError(Exception): pass

def usage():
	print __doc__

def main(argv):
	xmlfile = 'yi.xml'
	gflag = 0
	yflag = 0

	try:
		opts, args = getopt.getopt(argv, 's:g:y:ah')	#the args should be here to take the junk

		for opt, arg in opts:
			if opt == 'h':
				usage()
				sys.exit()
			elif opt == '-s':
				xmlfile = arg
			elif opt == '-g':
				gflag = int(arg)
				if gflag > 64 or gflag < 1:
					raise ArgOutofRangeError
			elif opt == '-y':
				yflag = int(arg)
				if yflag > 6 or yflag < 1:
					raise ArgOutofRangeError
			elif opt == '-a':
				(gflag, yflag) = (0, 0)		#HOW TO PROCESS OVERWRITE CONFLICT BETWEEN g, y and a
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	#except ArgOutofRangeError, ValueError:			#WHY CANNOT???????
	except:
		usage()
		sys.exit(3)

	if gflag != 0 and yflag != 0:
		run(xmlfile, gflag, yflag)
	elif gflag == 0 and yflag != 0:
		for i in range(64):					# A big memory comsumer, but I think let the class only parse one yao is right. How to do? Cache?
			run(xmlfile, i+1, yflag)
	elif gflag != 0 and yflag == 0:
		for i in range(6):
			run(xmlfile, gflag, i+1)
	else:
		for i in range(64):
			for j in range(6):
				run(xmlfile, i+1, j+1)
	
def run(xmlfile, gflag, yflag):	
	y = Yi_parser(xmlfile, gflag, yflag)
	print y.output()

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		usage()
		sys.exit()

	main(sys.argv[1:])
