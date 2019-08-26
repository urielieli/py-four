import argparse

def parse_args():
	parser = argparse.ArgumentParser(
		description='4 language interpreter (esolangs.org/wiki/4)')

	source = parser.add_mutually_exclusive_group(required=True)

	source.add_argument('file', nargs='?', type=argparse.FileType(),
		help='file to interpret')
	source.add_argument('-e', '--eval', dest='eval', nargs='?', type=str,
		help='interpret 4 code provided through the command line')

	parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
		help='show the transpiled python source')
	parser.add_argument('-o', '--optimize', dest='optimize', action='store_true',
		help='perform source optimization')
	parser.add_argument('-d', '--debug', dest='debug', action='store_true',
		help='run the code step by step')

	return parser.parse_args()