import os
import sys
from coevolution import GetSequence

def getAllSequences():
	directory = os.getcwd()
	data_directory = os.path.join(directory, "bin")
	data_directory = os.path.join(data_directory, "data")
	data_file = os.path.join(data_directory, "vapBC.gi")
	f = open(data_file, 'r')
	lines = f.readlines()
	for line in lines:
		line = line.rstrip()
		tokens = line.partition('\t')
		acc1 = tokens[0]
		acc2 = tokens[2]
		filename1 = "out/"+acc1+".seq"
		filename2 = "out/"+acc2+".seq"
		if os.path.exists(filename1) is False:
			seq1 = GetSequence.GetSequence(acc1)
			seq1.write_sequence_file()
		if os.path.exists(filename2) is False:
			seq2 = GetSequence.GetSequence(acc2)
			seq2.write_sequence_file()

if __name__ == '__main__':
	getAllSequences()