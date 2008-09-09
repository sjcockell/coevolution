#######################################################
## Copyright (c) Simon J Cockell                     ##
## Bioinformatics Support Unit, Newcastle University ##
## 2008                                              ##
## s.j.cockell@ncl.ac.uk +441912227253               ##
#######################################################

import sys
import coevolution.pythonSCA as psca
import coevolution.alignment as aln

def main():
	try:
		inFile = sys.argv[1]
	except IndexError:
		usageError()
	try:
		outFile = sys.argv[2]
	except IndexError:
		usageError()
	#alignment = aln.alignment(inFile)
	try:
		output = open(outFile, 'w')
	except IOError:
		print "Unable to open "+outFile+" for writing, try again"
		sys.exit()
#	sca = psca.SCA(alignment)
#	i = 0
#	while i < alignment.getNumberColumns():
#		if alignment.columnHasValidResidue(i) == 1:
#			j = 0
#			while j < alignment.getNumberColumns():
#				if alignment.columnHasValidResidue(j) == 1:
#					
#				j+= 1
#		getScore(alignment, i, j)
#		i += 1

def getScore(align, x, y):
	pass	

def usageError():
	print "Usage:\npython trace_coevolution.py inAln outFile"
	sys.exit()

if __name__ == "__main__":
	main()
