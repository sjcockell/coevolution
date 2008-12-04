import sys
import getSequences

def main():
	try:
		pairs_file = sys.argv[1]
	except IndexError:
		print "Usage:"
		print "Defaulting to VapBC"
		pairs_file = 'bin/data/vapBC.gi'
	getSequences.getAllSequences(pairs_file)

if __name__ == '__main__':
	main()
