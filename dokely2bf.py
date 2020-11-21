# @saulpanders
#
#	dokely2bf: convert between dokely and brainfuck programs (textual replace/substitution)
import argparse


def bf2dok(code):
	print("[+] parsing brainfuck to dokely...")
	code = clean_bf_code(code).split()
	print(code)
	retstr = ""
	for cmd in code:
		if cmd.lower() == "<":
			retstr+="ding "
		if cmd.lower() == ">":
			retstr+="dong "
		if cmd.lower() == "+":
			retstr+="dang "
		if cmd.lower() == "-":
			retstr +="diggity "
		if cmd.lower() == ".":
			retstr +="dokely "
		if cmd.lower() == ",":
			retstr +="daddley "
		if cmd.lower() == "[":
			retstr +="doodley "
		if cmd.lower() == "]":
			retstr +="diddily "
	return retstr



def dok2bf(code):
	print("[+] parsing dokely to brainfuck...")
	code = clean_dok_code(code.split()).split()
	print(code) 
	retstr = ""
	for cmd in code:
		if cmd.lower() == "ding":
			retstr+="<"
		if cmd.lower() == "dong":
			retstr+=">"
		if cmd.lower() == "dang":
			retstr+="+"
		if cmd.lower() == "diggity":
			retstr +="-"
		if cmd.lower() == "dokely":
			retstr +="."
		if cmd.lower() == "daddley":
			retstr +=","
		if cmd.lower() == "doodley":
			retstr +="["
		if cmd.lower() == "diddily":
			retstr +="]"
	return retstr

def clean_dok_code(code):
	return ' '.join(filter(lambda x: x.lower() in ['ding', 'dong', 'diggity', 'dang', 'diddily', 'doodley', 'daddley', 'dokely'], code))


def clean_bf_code(code):
	return ' '.join(filter(lambda x: x.lower() in ['<', '>', '+', '-', '.', ',', '[', ']'], code))


def main():
	code = ""
	bad_mode = False

	parser = argparse.ArgumentParser(description='utility for Brainfuck-Dokely conversions')
	parser.add_argument('-i', '--input', type=str, help="input file")
	parser.add_argument('-o', '--output', type=str, help="output file", default="out")
	parser.add_argument('-m', '--mode', type = str, help ="conversion mode: d2b (dokely to brainfuck); b2d (brainfuck to dokely)")
	args = parser.parse_args()
	if (args.input):
		filename = args.input
		with open(filename) as f:
			code = f.read()
			if (args.mode == "d2b"):
				code = dok2bf(code)
			elif (args.mode == "b2d"):
				code = bf2dok(code)
			else:
				bad_mode = True
				print("[-] error, select either mode d2b or mode b2d (see help [-h] for info)")
		
		if (args.output and not bad_mode):
			with open(args.output, 'w') as o:
				print("[+] writing conversion....")
				if(args.mode =="b2d"):
					#write valid file
					code = "Hi " + code + "ho neighboreeno!"
				o.write(code)

if __name__ == "__main__":
	main()