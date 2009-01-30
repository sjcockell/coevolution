import sys
import os
import numpy
import math
import Gnuplot

class StatisticalCouplingAnalysis:
	"takes an alignment, performs SCA, and tidies the results for graphing"
	def __init__(self, alignment_file=None):
		"sets variables for instance"
		self.file_pointer = os.path.abspath(alignment_file)
		self.starting_point = os.getcwd()
		self.java_location = '/home/sjcockell/git/Coevolution/java'
		
	def doSCA(self, output):
		"performs SCA on the file_pointer of the instance"
		output_file = os.path.abspath(output)
		os.chdir(self.java_location)
		command = 'java covariance.algorithms.JavaSCA '+self.file_pointer+' '+output_file
		os.system(command)
		os.chdir(self.starting_point)

	def quadratic(self, l):
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

	def print_result(self, scores, file):
		outname = file+'.ed'
		handle = open(outname, 'w')
		lastI = 0
		for score in scores:
			i = int(score[0])
			j = int(score[1])
			s = score[2]
			if i != lastI:
				lastI = i
				handle.write("\n")
			handle.write(str(i)+"\t"+str(j)+"\t"+str(s)+"\n")
		handle.close()
		return outname

	def editSCAOut(self, scaFile):
		"formats SCA output for gnuplot"
		handle = open(scaFile, 'r')
		lines = handle.readlines()
		handle.close()
		lines.pop(0)
		l = len(lines)
		print l
		factor = l * -2
		limit = self.quadratic(factor)
		print limit
		limit_sq = limit ** 2
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
						try:
							array[a] = [i1, j1, 0.0]
						except IndexError:
							print a, i, i1, j, j1
							exit()
						j1 += 1
						a += 1
					j1 = 0
					i1 += 1
			array[a] = [i, j, score]
			a += 1
		while a < limit_sq:
			array[a] = [i1, j1, 0.0]
			j1 += 1
			a += 1
		data = self.print_result(array, scaFile)
		return data
