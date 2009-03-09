import os
import threading
import Bio.AlignIO
import Bio.Seq
import re
from scipy import *

class Align:
	def __init__(self, seq_list):
		self.sl = seq_list

	def makeInfile(self, infile, exc_list):
		for seq in self.sl:
			exclude = 0
			for e in exc_list:
				if seq == e:
					exclude = 1
			if exclude == 0:
				command = 'cat out/' + seq + '.seq >> ' + infile
				os.system(command)
	
class AlignmentThread(threading.Thread):
	def __init__(self, infile, outfile):
		self.infile = infile
		self.outfile = outfile
		threading.Thread.__init__(self) #this line is needed, as we are overriding the original __init__

	def run(self):
		command = 'muscle -in ' + self.infile + ' -out ' + self.outfile
		print command
		os.system(command)

class ConcatenateAlignment():
	def __init__(self, first, second, associations):
		h1 = open(first)
		h2 = open(second)
		self.a1 = Bio.AlignIO.read(h1, "fasta")
		self.a2 = Bio.AlignIO.read(h2, "fasta")
		self.aList = associations
	def padAlignment(self):
		for record in self.a1:
			pass
	
	def concatenate(self):
		self.alignment = ""
		for association in self.aList:
			id1 = association[0][1]
			id2 = association[1][1]
			for record1 in self.a1:
				if record1.id == id1:
					for record2 in self.a2:
						if record2.id == id2:
							#print ">"+association[0][0]+"|"+association[1][0]
							#print record1.seq+record2.seq
							self.alignment = self.alignment+ ">"+str(association[0][0])+"|"+str(association[1][0])+"\n"
							self.alignment = self.alignment+str(record1.seq)+str(record2.seq)+"\n"
							break
					break
		return self.alignment
	
	def writeResult(self, outfile):
		f = open(outfile, 'w')
		string = self.alignment
		f.write(string)
		f.close()

class FormatAlignment():
	def __init__(self, align_file, outfile):
		self.alignment = Bio.AlignIO.read(open(align_file), "fasta")
		self.out_handle = open(outfile, "w")
		self.fasta_out_handle = open('edited_align.fa', "w")
		self.pattern = re.compile('[BJOUXZ]')
	def editBlankColumns(self):
		length = len(self.alignment[0].seq)
		position = zeros(length)
		for record in self.alignment:
			match = self.pattern.search(str(record.seq))
			if match:
				pass
			else:
				index = 0
				for char in record.seq:
					if char != '-':
						position[index] = 1
					index += 1
		for record in self.alignment:
			place = 0
			tmpSeq = ''
			for pos in position:
				if pos == 1:
					tmpSeq = tmpSeq+record.seq[place]
				if pos == 0:
					if record.seq[place] != '-':
						print '(!)\tYou appear to be omitting a non-gap character from this sequence'
				place += 1
			record.seq = tmpSeq 
	def format(self):
		for record in self.alignment:
			match = self.pattern.search(str(record.seq))
			if match:
				print "(!)\tSequence "+record.id+" contains invalid characters, omitting"
			else:
				self.out_handle.write(record.id+"\t")
				self.out_handle.write(str(record.seq)+"\n")
				self.fasta_out_handle.write(">"+record.id+"\n")
				self.fasta_out_handle.write(str(record.seq)+"\n")
		self.out_handle.close()

class ScreenAlignment():
	def __init__(self, align_file, outfile):
		self.alignment = Bio.AlignIO.read(open(align_file), "fasta")
		self.outhandle = open(outfile, "w")
		self.alignarray = []
		for record in self.alignment:
			alignarray.push(record.seq)
