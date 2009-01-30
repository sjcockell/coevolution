import sys
import getSequences
from coevolution import Alignment, StatisticalCouplingAnalysis

def reportProgress(index):
	progressList = ["Reading Pairs File", 
				"Preparing sequences for alignment",
				"Aligning",
				"Concatenating alignments",
				"Formatting alignment for Statistical Coupling Analysis",
				"Performing SCA",
				"Editing SCA output for Gnuplot"
				]
	print "(o)\t"+progressList[index]

def main():
	try:
		pairs_file = sys.argv[1]
	except IndexError:
		print "Usage: python bin/masterControl.py /path/to/pairs_file"
		print "Defaulting to VapBC"
		pairs_file = 'bin/data/vapBC.gi'
	reportProgress(0)
	gs = getSequences.getSequences(pairs_file)
	gs.getAllSequences()
	al = gs.getAssociationList()
	partnerAs = gs.getAList()
	partnerBs = gs.getBList()
	reportProgress(1)
	alignA = Alignment.Align(partnerAs)
	alignA.makeInfile('partner1.fa')
	alignB = Alignment.Align(partnerBs)
	alignB.makeInfile('partner2.fa')
	reportProgress(2)
	#Alignment.AlignmentThread('partner1.fa', 'partner1.aln').start()
	#Alignment.AlignmentThread('partner2.fa', 'partner2.aln').start()
	reportProgress(3)
	catAlign = Alignment.ConcatenateAlignment('partner1.aln', 'partner2.aln', al)
	catAlign.padAlignment()
	catted = catAlign.concatenate()
	catAlign.writeResult('catted.aln')
	reportProgress(4)
	formAlign = Alignment.FormatAlignment('catted.aln', 'f_catted.aln')
	formAlign.format()
	reportProgress(5)
	sca = StatisticalCouplingAnalysis.StatisticalCouplingAnalysis('f_catted.aln')
#	sca.doSCA('vapbc.sca')
	reportProgress(6)
	#sca.editSCAOut('vapbc.sca')

if __name__ == '__main__':
	main()
