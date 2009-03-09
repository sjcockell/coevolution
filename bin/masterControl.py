import sys
import getSequences, assessSequences
from coevolution import Alignment, StatisticalCouplingAnalysis

def reportProgress(index):
	progressList = ["Reading Pairs File", 
				"Preparing sequences for alignment",
				"Aligning",
				"Concatenating alignments",
				"Formatting alignment for Statistical Coupling Analysis",
				"Performing SCA",
				"Editing SCA output for Gnuplot",
				"Plotting SCA results",
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
	excludeList = assessSequences.excludeSeqs(al)
	excludeA = []
	excludeB = []
	for ex in excludeList:
		excludeA.append(ex[0])
		excludeB.append(ex[1])
	reportProgress(1)
	alignA = Alignment.Align(partnerAs)
	alignA.makeInfile('partner1ed.fa', excludeA)
	alignB = Alignment.Align(partnerBs)
	alignB.makeInfile('partner2ed.fa', excludeB)
	reportProgress(2)
	threads = []
	thread1 = Alignment.AlignmentThread('partner1ed.fa', 'partner1ed.aln')
	thread2 = Alignment.AlignmentThread('partner2ed.fa', 'partner2ed.aln')
	threads.append(thread1)
	threads.append(thread2)
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	reportProgress(3)
	catAlign = Alignment.ConcatenateAlignment('partner1ed.aln', 'partner2ed.aln', al)
	catAlign.padAlignment()
	catted = catAlign.concatenate()
	catAlign.writeResult('catteded.aln')
	reportProgress(4)
	formAlign = Alignment.FormatAlignment('catteded.aln', 'f_catteded.aln')
	formAlign.editBlankColumns()
	formAlign.format()
	reportProgress(5)
	sca = StatisticalCouplingAnalysis.StatisticalCouplingAnalysis('f_catteded.aln')
	sca.doSCA('edvapbc.sca')
	reportProgress(6)
	sca.editSCAOut('edvapbc.sca')
	reportProgress(7)
	sca.plotSCA()

if __name__ == '__main__':
	main()
