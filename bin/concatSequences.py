import os
import sys
from coevolution import GetSequence
from Bio import SeqIO

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
	n = len(vapBs)
	i = 0
#	while i < n:
	while i < 50:
		filename1 = "out/"+vapBs[i]+".seq"
		filename2 = "out/"+vapCs[i]+".seq"
		command = "cat "+filename1+" "+filename2+" > temp.fa"
		os.system(command)
		han = open('temp.fa', "rU")
		print ">"+vapBs[i]+"|"+vapCs[i]
		j = 0
		seq = ""
		for rec in SeqIO.parse(han, "fasta"):
			s = str(rec.seq)
			s = s.rstrip()
			seq = seq+s
			j += 1
		print seq
		i += 1
#	for B in vapBs:
#		filename = "out/"+B+".seq"
#	i = 0
#	while i < 51:
#		filename = "out/"+vapBs[i]+".seq"
#		command = "cat "+filename+" >> vapB50.fa"
#		os.system(command)
#		i += 1
#	for C in vapCs:
#		filename = "out/"+C+".seq"
#	i = 0
#	while i < 51:
#		filename = "out/"+vapCs[i]+".seq"
#		command = "cat "+filename+" >> vapC50.fa"
#		os.system(command)
#		i += 1

if __name__ == '__main__':
	run()
