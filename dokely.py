# @saulpanders
#
#	Dokely : the brainfuck variant for Ned Flanders
#	
#	source(s): https://en.wikipedia.org/wiki/Brainfuck
#			 https://github.com/pocmo/Python-Brainfuck/blob/master/brainfuck.py
#	pseudo-inspiration: https://github.com/omkarjc27/OooWee/blob/master/Ooo
#
# Dokely 		Brainfuck 		action
# 
# ding		-> 		<			increment data ptr (ptr++)
# dong		-> 		>			decrement data ptr (ptr--)
# dang		->		+			increase by 1 the byte at the data ptr (*ptr++)
# dag		->		-			decrease by 1 the byte at the data ptr (*ptr--)
# dokely 	-> 		.			output byte at data ptr (print(*ptr))
# daddely	->		,			read 1 byte of input and store its value at byte pointed to by data ptr 
# doodely	->		[			if byte at data ptr is zero, instead of increasing instruction pointer JUMP to instruction after subsequent "]"
# diddily	->		]			if byte at data ptr is zero, instead of increasing instruction pointer JUMP to instruction after previous "["
#
#	Dokely programs must be friendly (i.e prefix "Hi", suffix "ho neighboreeno!") to run 
#

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
		if(words[0].tolower() == "hi") and (words[-2].tolower() == "ho") and (words[-1].tolower() == "neighboreeno"):
			interpret(words[0],"f",0)
		else:
			print("error, .simp file must be a friendly neighbor. Check your prefix / suffix (Hi / ho neighboreeno)")

	else:
		print("error, need a file")
		exit(0)



if __name__ == "__main__":
	main()