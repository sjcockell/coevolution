import os
import threading

class Alignment:
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
