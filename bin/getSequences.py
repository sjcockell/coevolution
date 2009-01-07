import os
import sys
from coevolution import GetSequence
from Bio import SeqIO

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
		
	def get_id(self, file):
		handle = open(file, 'r')
		seq_record = SeqIO.read(handle, "fasta")
		handle.close()
		return seq_record.id
	
	def makeAssociationList(self, int, file1, accession1, file2, accession2):
		y_number1 = self.get_id(file1)
		y_number2 = self.get_id(file2)
		tuple = ((accession1, y_number1), (accession2, y_number2))
		self.assocList[int] = tuple
	
	def getAssociationList(self):
		return self.assocList

	def getAllSequences(self):
		length = len(self.aList)
		i = 0
		self.assocList = [0] * length
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
			self.makeAssociationList(i, filename1, acc1, filename2, acc2)
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
