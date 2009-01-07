import sys
import getSequences
from coevolution import Alignment

def main():
	try:
		pairs_file = sys.argv[1]
	except IndexError:
		print "Usage:"
		print "Defaulting to VapBC"
		pairs_file = 'bin/data/vapBC.gi'
	gs = getSequences.getSequences(pairs_file)
	gs.getAllSequences()
	al = gs.getAssociationList()
	partnerAs = gs.getAList()
	partnerBs = gs.getBList()
	alignA = Alignment.Align(partnerAs)
	alignA.makeInfile('partner1.fa')
	alignB = Alignment.Align(partnerBs)
	alignB.makeInfile('partner2.fa')
	#Alignment.AlignmentThread('partner1.fa', 'partner1.aln').start()
	#Alignment.AlignmentThread('partner2.fa', 'partner2.aln').start()
	catAlign = Alignment.ConcatenateAlignment('partner1.aln', 'partner2.aln', al)
	catAlign.padAlignment()
	catted = catAlign.concatenate()
	catAlign.writeResult('catted.aln')

if __name__ == '__main__':
	main()
