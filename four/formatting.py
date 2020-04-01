def indent_multiline(text, indent=0):
	return '\n'.join(' ' * 4 * indent + line for line in text.split('\n'))

def combine_multiline(left, right, cformat='{0} {1}'):
	return '\n'.join(
		map(lambda pair: cformat.format(pair[0], pair[1]),
		zip(left.split('\n'), right.split('\n')))
	)
