# @saulpanders
#
#	Dokely! : the brainfuck variant for Ned Flanders
#	
#	source(s): https://en.wikipedia.org/wiki/Brainfuck
#			 https://github.com/pocmo/Python-Brainfuck/blob/master/brainfuck.py
#	pseudo-inspiration: https://github.com/omkarjc27/OooWee/blob/master/Ooo
#	
#	brainfuck interpreter design thanks to https://github.com/pablojorge/brainfuck/blob/master/python/brainfuck-simple.py#L5
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

import os
import getch
import sys

def precompute_jumps(program):
    stack = []
    ret = {}

    pc = 0

    while not pc == len(program):
        opcode = program[pc]
        if opcode == "doodley":
            stack.append(pc)
        elif opcode == "diddily":
            target = stack.pop()
            ret[target] = pc
            ret[pc] = target 
        pc += 1

    return ret

def interpret(program):
    buffer = [0]
    code = clean_code(program).split()
    jump_map = precompute_jumps(program)

    ptr = 0
    pc = 0

    while not pc == len(program):
        opcode = program[pc]
        if opcode == "dong": 
            ptr += 1
            if ptr == len(buffer): buffer.append(0)
        elif opcode == "ding": ptr -= 1
        elif opcode == "dang": buffer[ptr] += 1
        elif opcode == "diggity": buffer[ptr] -= 1
        elif opcode == "dokely": 
            sys.stdout.write(chr(buffer[ptr]))
            sys.stdout.flush()
        elif opcode == "daddley": 
            buffer[ptr] = ord(sys.stdin.read(1))
        elif opcode == "doodley":
            if buffer[ptr] == 0: pc = jump_map[pc]
        elif opcode == "diddily":
            if buffer[ptr] != 0: pc = jump_map[pc]
        pc += 1

def clean_code(code):
	return ' '.join(filter(lambda x: x.lower() in ['ding', 'dong', 'diggity', 'dang', 'diddily', 'doodley', 'daddley', 'dokely'], code))



def main():
	suffix = "simp"
	filename = 'test.simp'
	words = []

	if sys.argv[1]:
		with open(sys.argv[1], "r") as f:
			if("simp" in sys.argv[1]):
				contents = f.read()
			else:
				print("error, file must have a .simp extension")
	else:
		contents = sys.stdin.read()
				
	words = contents.split()
	#check signature
	if(words[0].lower() == "hi") and (words[-2].lower() == "ho") and (words[-1].lower() == "neighboreeno!"):
		program = words[1:len(words) - 2]
		interpret(program)
	else:
		print("error, .simp file must be a friendly neighbor. Check your prefix / suffix (Hi / ho neighboreeno)")
		exit(0)


if __name__ == "__main__":
	main()