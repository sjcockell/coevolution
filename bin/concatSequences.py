import os
import sys
from coevolution import GetSequence

def run():
	vapBs = []
	vapCs = []
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
		vapBs.append(acc1)
		vapCs.append(acc2)
	for B in vapBs:
		seq = GetSequence.GetSequence(B)
		filename = "out/"+seq.get_sequence_id+".seq"
		command = "cat "+filename+" >> vapB.fa"
		os.system(command)
	for C in vapCs:
		seq = GetSequence.GetSequence(C)
		filename = "out/"+seq.get_sequence_id+".seq"
		command = "cat "+filename+" >> vapC.fa"
		os.system(command)

if __name__ == '__main__':
	run()
