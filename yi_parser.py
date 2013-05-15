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

class Yi_parser():

	def __init__(self, xmlfile, gflag, yflag):
		self.xmlfile = xmlfile
		self.gflag = gflag
		self.yflag = yflag

	def output(self):
		return ' '.join([self.xmlfile, str(self.gflag), str(self.yflag)])

class ArgOutofRangeError(Exception): pass

def usage():
	print __doc__

def main(argv):
		xmlfile = 'yi.xml'
		gflag = 0
		yflag = 0

		try:
			opts ,args = getopt.getopt(argv, 's:g:y:ah')
		except getopt.GetoptError:
			usage()
			sys.exit(2)

		try:
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
					(gflag, yflag) = (0, 0)		#if have -a, disregard -g and -y
		except:
			usage()
			sys.exit(3)

		y = Yi_parser(xmlfile, gflag, yflag)
		print y.output()

if __name__ == '__main__':
	main(sys.argv[1:])
