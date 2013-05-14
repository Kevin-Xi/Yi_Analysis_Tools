import sys
import random

flag=0

def siyingsanbian():
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
#	if flag:
#		print shicao
	return shicao/4

def jinqiangua():
	pass

def main(count):
	count = int(count)
	dictof7896 = {7:0, 8:0, 9:0, 6:0}
	for i in range(count):
		dictof7896[siyingsanbian()] += 1

	print '\n'.join(['%d: %f%%' %(k, float(v)/count*100) for k, v in dictof7896.items()])
	print '\n'
	print '--- : %f%%\n'  % (float(dictof7896[7]+dictof7896[9])/count*100)
	print '- - : %f%%\n'  % (float(dictof7896[8]+dictof7896[6])/count*100)

if __name__ == '__main__':
	main(sys.argv[1])
else:
	flag = 1
