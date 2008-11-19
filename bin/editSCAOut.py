import sys
import os
import numpy
import math
import Gnuplot

def run():
	file = sys.argv[1]
	print file
	handle = open(file, 'r')
	lines = handle.readlines()
	lines.pop(0)
	l = len(lines)
	print l
	factor = l * -2
	limit = quadratic(factor)
	print limit
	limit_sq = limit**2
	array = numpy.empty((limit_sq, 3))
	a = 0
	i1 = 0
	j1 = 0
	lastI = -1
	for line in lines:
		line = line.rstrip()
		tokens = line.split('\t')
		i = int(tokens[0])
		j = int(tokens[1])
		score = tokens[2]
		if i != lastI:
			lastI = i
			while i1 <= i:
				while j1 < j:
					array[a] = [i1, j1, 0.0]
					j1 += 1
					a += 1
				j1 = 0
				i1+=1
		array[a] = [i, j, score]
		a+=1
	while a < limit_sq:
		array[a] = [i1, j1, 0.0]
		j1+=1
		a+=1
	data = print_result(array, file)
	print_plotcmd(limit, data, array)

def quadratic(l):
	a = 1
	b = 1
	c = l
	b = float(b) / float(a)
	c = float(c) / float(a)
	
	before_the_square = 0.5 * b * -1
	the_square = (0.5 * b)**2 - c
	if the_square < 0:
		print "Imaginary" #fail-safe for imaginary numbers.
		exit()
	else:
		value_of_square = math.sqrt(the_square)
		x1 = before_the_square + value_of_square
		x2 = before_the_square - value_of_square
		if math.fabs(x1) > math.fabs(x2):
			return int(math.fabs(x1))
		else:
			return int(math.fabs(x2))

def print_result(scores, f):
	outname = f+".ed"
	h = open(outname, 'w')
	lastI = 0
	for score in scores:
		i = int(score[0])
		j = int(score[1])
		s = score[2]
		if i != lastI:
			lastI = i
			h.write("\n")
		h.write(str(i)+"\t"+str(j)+"\t"+str(s)+"\n")
	h.close()
	return outname

def print_plotcmd(l,d,a):
	data_test = Gnuplot.Data(a, with='image')
	plot = Gnuplot.Gnuplot()
	plot('set terminal png')
	plot('set output "plot.png"')
	plot('set view map')
	plot('set xrange [0:'+str(l)+']')
	plot('set yrange [0:'+str(l)+']')
	plot('set tics out')
	plot.splot(data_test)
	h = open('plt.cmd', 'w')
	h.write("set terminal png\nset output 'plot.png'\nset view map\nset xrange [0:"+str(l)+"]\nset yrange [0:"+str(l)+"]\nset tics out\nsplot '"+d+"' w image\n")
	h.close()

if __name__ == '__main__':
	run()
