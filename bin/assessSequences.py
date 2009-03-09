import sys
import getSequences
from Bio import SeqIO
from rpy import *

def main():
	try:
		pairs_file = sys.argv[1]
	except IndexError:
		print "Usage: python bin/masterControl.py /path/to/pairs_file"
		print "Defaulting to VapBC"
		pairs_file = 'bin/data/vapBC.gi'
	gs = getSequences.getSequences(pairs_file)
	gs.getAllSequences()
	al = gs.getAssociationList()
	excludeSeqs(al)

def excludeSeqs(assocList):
	aLengths = []
	bLengths = []
	totalLengths = []
	for item in assocList:
		a = item[0][0]
		b = item[1][0]
		lengthA = getSequenceLength(a)
		lengthB = getSequenceLength(b)
		aLengths.append(float(lengthA))
		bLengths.append(float(lengthB))
		totalLengths.append(float(lengthA+lengthB))
	sum_total = r.summary(totalLengths)
	sd_total = r.sd(totalLengths)
	sum_a = r.summary(aLengths)
	sd_a = r.sd(aLengths)
	sum_b = r.summary(bLengths)
	sd_b = r.sd(bLengths)
	upper_limit_total = sum_total["Mean"] + (sd_total*2)
	lower_limit_total = sum_total["Mean"] - (sd_total*2)
	upper_limit_a = sum_a["Mean"] + (sd_a*2)
	lower_limit_a = sum_a["Mean"] - (sd_a*2)
	upper_limit_b = sum_b["Mean"] + (sd_b*2)
	lower_limit_b = sum_b["Mean"] - (sd_b*2)
	num_excluded = 0
	exclusionList = []
	for item in assocList:
		if getSequenceLength(item[0][0]) + getSequenceLength(item[1][0]) > upper_limit_total:
			num_excluded += 1
			exclusionList.append((item[0][0], item[1][0]))
		elif getSequenceLength(item[0][0]) + getSequenceLength(item[1][0]) < lower_limit_total:
			num_excluded += 1
			exclusionList.append((item[0][0], item[1][0]))
		elif getSequenceLength(item[0][0]) > upper_limit_a:
			num_excluded += 1
			exclusionList.append((item[0][0], item[1][0]))
		elif getSequenceLength(item[0][0]) < lower_limit_a:
			num_excluded += 1
			exclusionList.append((item[0][0], item[1][0]))
		elif getSequenceLength(item[1][0]) > upper_limit_b:
			num_excluded += 1
			exclusionList.append((item[0][0], item[1][0]))
		elif getSequenceLength(item[1][0]) < lower_limit_b:
			num_excluded += 1
			exclusionList.append((item[0][0], item[1][0]))
	return exclusionList

def meanArray(array):
	total = 0.0
	for a in array:
		total = total + float(a)
	mean = total/float(len(array))
	return mean

def getSequenceLength(id):
		seqFile = "out/"+id+".seq"
		handle = open(seqFile, 'r')
		record = SeqIO.read(handle, 'fasta')
		return len(record.seq)


if __name__ == '__main__':
	main()
