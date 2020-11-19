# @saulpanders
#
#	Dokilly : the brainfuck variant for Ned Flanders
#	
#	source(s): https://en.wikipedia.org/wiki/Brainfuck
#	pseudo-inspiration: https://github.com/omkarjc27/OooWee/blob/master/Ooo
#
# diddily
# doodley
# daddely
# ding
# dong
# dokilly

import argparse
import os


def interpret(word, mode, line):
	print(1)


def main():
	suffix = "simp"
	file_in= ""
	array = [0]*30000
	ptr = 0
	words = []
	parser = argparse.ArgumentParser(description='Dokilly: the brainfuck variant for Ned Flanders')
	parser.add_argument('-i', '--input', type=str, help="dokilly file to run (.simp)")
	args = parser.parse_args()

	if(args.input):
		if args.input.endswith('.'+suffix):
			filename = args.input
			if os.path.exists(filename):
				with open(filename, 'r') as f:
					file_in = f.read()
		else:
			print("Can't find file\n")
			exit(0)
				
		words = file_in.split()
		interpret(words[0],"f",0)

	else:
		print("error, need a file")
		exit(0)



if __name__ == "__main__":
	main()