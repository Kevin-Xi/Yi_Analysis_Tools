import sys
import random
import getopt

flag=0
class Divine():
	def siyingsanbian(self):
		shicao = 49
		shicao -= 1
		yushu = 0

		for i in range(3):
			fener = random.randint(1, shicao-1)
			#fener = random.randint(0, shicao)
			shesi = fener % 4
			if shesi == 0:
				shicao -= 8
			else:
				shicao -= 4
#		if flag:
#			print shicao
		return shicao/4

	def jinqiangua(self):
		first = random.randint(0, 1)
		second = random.randint(0, 1)
		third = random.randint(0, 1)
		
		total = first + second + third

		if total == 3:
			return 9
		elif total == 0:
			return 6
		elif total == 2:
			return 8
		else:
			return 7

	def __init__(self, argv):
		try:
			opts, args = getopt.getopt(argv, 'm:')
		except getopt.GetoptError:
			sys.exit(1)

		count = int(args[0])
		method = getattr(self, opts[0][1])
		dictof7896 = {7:0, 8:0, 9:0, 6:0}
		for i in range(count):
			dictof7896[method()] += 1

		print '\n'.join(['%d: %f%%' %(k, float(v)/count*100) for k, v in dictof7896.items()])
		print '\n'
		print '--- : %f%%\n'  % (float(dictof7896[7]+dictof7896[9])/count*100)
		print '- - : %f%%\n'  % (float(dictof7896[8]+dictof7896[6])/count*100)

if __name__ == '__main__':
	Divine(sys.argv[1:])
else:
	flag = 1
