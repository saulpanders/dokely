# @saulpanders
#
#	Dokely! : the brainfuck variant for Ned Flanders
#	
#	source(s): https://en.wikipedia.org/wiki/Brainfuck
#			 https://github.com/pocmo/Python-Brainfuck/blob/master/brainfuck.py
#	pseudo-inspiration: https://github.com/omkarjc27/OooWee/blob/master/Ooo
#	
#	getch thanks to https://github.com/joeyespo/py-getch
#
# Dokely 		Brainfuck 		action
# 
# ding		-> 		<			increment data ptr (ptr++)
# dong		-> 		>			decrement data ptr (ptr--)
# dang		->		+			increase by 1 the byte at the data ptr (*ptr++)
# diggity	->		-			decrease by 1 the byte at the data ptr (*ptr--)
# dokely 	-> 		.			output byte at data ptr (print(*ptr))
# daddley	->		,			read 1 byte of input and store its value at byte pointed to by data ptr 
# doodley	->		[			if byte at data ptr is zero, instead of increasing instruction pointer JUMP to instruction after subsequent "]"
# diddily	->		]			if byte at data ptr is zero, instead of increasing instruction pointer JUMP to instruction after previous "["
#
#	Dokely programs must be friendly (i.e prefix "Hi", suffix "ho neighboreeno!") to run 
#

import argparse
import os
import getch


def interpret(program):
	code = clean_code(program).split()
	bracemap = bracket_stack(code)

	cells, codeptr, cellptr = [0], 0, 0

	while codeptr < len(code):
		try:
			command = code[codeptr]
			if command.lower() == "ding":
				cellptr += 1
				if cellptr == len(cells): 
					cells.append(0)

			if command.lower() == "dong":
				if cellptr <= 0:
					cellptr = 0
				else: 
					cellptr = cellptr - 1

			if command.lower() == "dang":
				if cells[cellptr] < 255:
					cells[cellptr] = cells[cellptr] + 1 
				else: 
					cells[cellptr] = 0

			if command.lower() == "diggity":
				if cells[cellptr] > 0:
					cells[cellptr] = cells[cellptr] - 1 
				else: 
					cells[cellptr] = 255

			if command.lower() == "doodley" and cells[cellptr] == 0: 
				codeptr = bracemap[codeptr]

			if command.lower() == "diddily" and cells[cellptr] != 0: 
				codeptr = bracemap[codeptr]

			if command == "dokely": 
				print(chr(cells[cellptr]))

			if command == "daddley": 
				cells[cellptr] = ord(getch.getch())

			#keep reading
			codeptr += 1
		except:
			raise

def clean_code(code):
	return ' '.join(filter(lambda x: x.lower() in ['ding', 'dong', 'diggity', 'dang', 'diddily', 'doodley', 'daddley', 'dokely'], code))

def bracket_stack(code):
	temp_bracestack, bracemap = [], {}
	for position, command in enumerate(code):
		# [
		if command.lower() == "doodley": 
			temp_bracestack.append(position)
		
		# ]
		if command.lower() == "diddily":
			start = temp_bracestack.pop()
			bracemap[start] = position
			bracemap[position] = start
	return bracemap


def main():
	suffix = "simp"
	filename = 'test.simp'
	words = []
	parser = argparse.ArgumentParser(description='Dokely: the brainfuck variant for Ned Flanders')
	parser.add_argument('-i', '--input', type=str, help="dokely file to run (.simp)")
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
		#check signature
		if(words[0].lower() == "hi") and (words[-2].lower() == "ho") and (words[-1].lower() == "neighboreeno!"):
			program = words[1:len(words) - 2]
			interpret(program)
		else:
			print("error, .simp file must be a friendly neighbor. Check your prefix / suffix (Hi / ho neighboreeno)")
			exit(0)
	else:
		print("error, need a file")
		exit(0)



if __name__ == "__main__":
	main()