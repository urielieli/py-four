import os
import sys
import argparse
import subprocess
from tempfile import NamedTemporaryFile

import optimizer
from four_parser import FourParser


if __name__ == '__main__':
	# parse arguments
	parser = argparse.ArgumentParser(description='4 language interpreter (esolangs.org/wiki/4)')

	source = parser.add_mutually_exclusive_group(required=True)
	source.add_argument('file', nargs='?', type=argparse.FileType(), help='source file')
	source.add_argument('-e', '--eval', dest='eval', nargs='?', type=str, help='provided code as argument')

	parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='show python source')
	parser.add_argument('-o', '--optimize', dest='optimize', action='store_true', help='source optimization')

	args = parser.parse_args()

	# parse
	code = args.file.read() if args.file else args.eval
	tokens = FourParser.tokenize(FourParser.strip(code))
	if args.optimize:
		tokens = optimizer.optimize(tokens)
	root = FourParser.parse(tokens)

	# verbose
	if args.verbose:
		sys.stderr.write('\n<< python source >>\n')
		sys.stderr.write('\n'.join([
			'{0:<10} | {1}'.format(f, p) for f, p in
			zip(str(root).split('\n'), root.python.split('\n'))
		]))

	# run
	with NamedTemporaryFile(mode='w', delete=False) as _file:
		boilerplate = open(os.path.join(os.path.dirname(__file__), 'runner.py')).read()
		_file.write(boilerplate)
		_file.write(root.python)
	subprocess.call(['python', _file.name])
	os.remove(_file.name)
