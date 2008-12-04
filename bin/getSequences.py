import os
import sys
from coevolution import GetSequence


class getSequences:
	def __init__(self, file):
		directory = os.getcwd()
#		directory = os.path.join(directory, "bin")
#		directory = os.path.join(directory, "data")
		self.aList = []
		self.bList = []
		data_file = os.path.join(directory, file)
		f = open(data_file, 'r')
		self.lines = f.readlines()
		for line in self.lines:
			line = line.rstrip()
			tokens = line.partition('\t')
			acc1 = tokens[0]
			acc2 = tokens[2]
			self.aList.append(acc1)
			self.bList.append(acc2)
		
	def getAllSequences(self):
		length = len(self.aList)
		i = 0
		while i < length:
			acc1 = self.aList[i]
			acc2 = self.bList[i]
			filename1 = "out/"+acc1+".seq"
			filename2 = "out/"+acc2+".seq"
			if os.path.exists(filename1) is False:
				seq1 = GetSequence.GetSequence(acc1)
				seq1.write_sequence_file()
			if os.path.exists(filename2) is False:
				seq2 = GetSequence.GetSequence(acc2)
				seq2.write_sequence_file()
			i += 1
	
	def getAList(self):
		return self.aList

	def getBList(self):
		return self.bList

if __name__ == '__main__':
	try:
		filename = sys.argv[1]
	except IndexError:
		filename = 'vapBC.gi'
	getAllSequences(filename)
