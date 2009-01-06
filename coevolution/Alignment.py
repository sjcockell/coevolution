import os
import threading
import Bio.AlignIO

class Align:
	def __init__(self, seq_list):
		self.sl = seq_list

	def makeInfile(self, infile):
		for seq in self.sl:
			command = 'cat out/' + seq + '.seq >> ' + infile
			os.system(command)
	
class AlignmentThread(threading.Thread):
	def __init__(self, infile, outfile):
		self.infile = infile
		self.outfile = outfile
		threading.Thread.__init__(self) #this line is needed, as we are overriding the origingal __init__

	def run(self):
		command = 'muscle -in ' + self.infile + ' -out ' + self.outfile
		print command
		#os.system(command)

class ConcatenateAlignment():
	def __init__(self, first, second):
		h1 = open(first)
		h2 = open(second)
		self.a1 = Bio.AlignIO.read(h1, "fasta")
		self.a2 = Bio.AlignIO.read(h2, "fasta")
	def padAlignment(self):
		print self.a1.get_alignment_length()
		for record in self.a1 :
			print record.seq, record.id
