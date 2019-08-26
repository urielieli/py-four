import subprocess
import copy
import sys
import os

from utils import chunks, combine_multiline, GRID_SIZE
import argparser, preprocessor, tokenizer, root_parser as parser

from operands import GridAccess
from io_instructions import InputInstruction


"""
def optimize_constants(tokens):

	print('Optimizing for constants...')

	constants = {}

	for cell in range(GRID_SIZE):
		sets = []

		for token in tokens:
			if isinstance(token, SetInstruction) and token.cell.index == cell:
				sets.append(token)

		if len(sets) == 1:
			constants[cell] = sets[0]

	for cell in list(constants.keys()):
		for token in tokens:
			if isinstance(token, LoopInstruction) and token.cell.index == cell:
				del constants[cell]

	for token in constants.values():
		print('Removing constant setter {}'.format(token))
		tokens.remove(token)

	for token in tokens:
		if isinstance(token, ArithmaticInstruction):
			for index, param in enumerate(token.params):
				if index > 0 and isinstance(param, GridAccess) and param.index in constants.keys():
					token[index] = constants[param.index].value
		if isinstance(token, OutputInstruction):
			if isinstance(token.operand, GridAccess) and token.operand.index in constants.keys():
				token.operand = constants[token.operand.index].value

	return tokens, len(constants) > 0

def optimize_arithmatics(tokens):

	print('Optimizing for constant arithmatics...')

	optimized = False

	for index, token in enumerate(tokens):
		if isinstance(token, ArithmaticInstruction):
			if isinstance(token.operand1, int) and isinstance(token.operand2, int):
				print('Replacing token {} with a constant setter'.format(token))
				tokens[index] = SetInstruction(6, token.cell.index, token.operation(token.operand1, token.operand2))
				optimized = True

	return tokens, optimized"""

def optimize_constants(tokens):
	return tokens, False
def optimize_arithmatics(tokens):
	return tokens, False

def transpile(root):
	return root.python

def verbose(root):
	return combine_multiline(str(root),
							 root.python,
							 '  {0:<16} | {1}')

def run(code):
	boilerplate = f"""
import sys, os
from operator import add, sub, mul, truediv
from msvcrt import getch

def putc(value):
	if not isinstance(value, str):
		value = chr(value)
	sys.stdout.write(value)
	sys.stdout.flush()

def getc():
	return ord(getch())

def exit(exit_code):
	os._exit(exit_code)

grid = [0] * {GRID_SIZE + 1}

"""

	tempfile_filename = os.path.join(os.path.dirname(__file__), '.tmp.py')

	with open(tempfile_filename, 'w') as tempfile:
		tempfile.write(boilerplate + code)

	subprocess.call(['python', tempfile_filename])
	#os.remove(tempfile_filename)

if __name__ == '__main__':
	try:
		args = argparser.parse_args()
		code = args.file.read() if args.file else args.eval
		raw_code = preprocessor.get_raw_code(code)
		tokens = tokenizer.tokenize(raw_code)

		if args.optimize:
			optimized = True
			while optimized:
				optimized = False
				tokens, _optimized = optimize_constants(tokens)
				optimized |= _optimized
				tokens, _optimized = optimize_arithmatics(tokens)
				optimized |= _optimized

		if args.debug:
			tokens = [_token for token in tokens for _token in (token, InputInstruction(GridAccess(100)))]

		root = parser.parse(tokens)

		if args.verbose:
			verbose_target = sys.stderr
			if args.file:
				verbose_target.write('{:=^30}\n{}\n'.format(' SOURCE ', args.file.name))
			verbose_target.write('{:=^30}\n{}\n'.format(' CODE ', '\n'.join(chunks(code, 30))))
			verbose_target.write('{:=^30}\n{}\n'.format(' TRANSPILED ', verbose(root)))
			verbose_target.write('{:=^30}\n'.format(''))
		
		transpiled = transpile(root)
		run(transpiled)

	except Exception as e:
		sys.stderr.write('Error: {}\n'.format(' '.join(e.args)))
		#__import__('traceback').print_exc()
		os._exit(1)