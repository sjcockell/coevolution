import coevolution.alignment as aln

class SCA:
	def __init__(self, a, mfr=None, i=None):
		background = [0.072658, 0.024692, 0.050007, 0.061087,
	        0.041774, 0.071589, 0.023392, 0.052691, 0.063923,
		0.089093, 0.023150, 0.042931, 0.052228, 0.039871,
		0.052012, 0.073087, 0.055606, 0.063321, 0.012720,
		0.032955]
		#ensure right arguments are passed - 2 types of object possible
		if mfr == None:
			if i != None:
				#exception handling code
				pass
			else:
				self.type = 2
		else:
			if i == None:
				#exception handling code
				pass
			else:
				self.type = 1
		if a == None:
			#exception handling code
			pass
		else:
			if self.type == 1:
				if mfr[i] != '-':
					self.alignment = self.getSubsetAlignment(a, i, mfr[i])
					self.initializeLocklessScores()
			else:
				self.alignment = a
				self.initializeLocklessScores()
				self.mostFrequentResidues = aln.getMostFrequentResidues(self.alignment)

	def getSubsetAlignment(self, a, i, c):
		#need some checks for validity here
		self.lines = a.getAlignmentLines()
		for l in lines:
			pass
			#if charAt i == c
			#add line to list of lines
		#return alignment made from list
