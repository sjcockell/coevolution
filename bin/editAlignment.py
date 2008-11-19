import sys
from Bio import AlignIO
align_file = sys.argv[1]
alignment = AlignIO.read(open(align_file), "fasta")
#print "Alignment length %i" % alignment.get_alignment_length()
for record in alignment:
	print record.id+"\t",
	print record.seq
