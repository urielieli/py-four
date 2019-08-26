import operator

GRID_SIZE = 100

def chunks(itearble, size=1):
	return [itearble[offset: offset+size] for offset in range(0, len(itearble), size)]

def indent_multiline(text, indent=0):
	return '\n'.join(' ' * 4 * indent + line for line in text.split('\n'))

def combine_multiline(left, right, cformat='{0} {1}'):
	return '\n'.join(map(lambda pair: cformat.format(pair[0], pair[1]),
		zip(left.split('\n'), right.split('\n'))))

class classproperty:
	def __init__(self, method):
		self.method = method

	def __get__(self, obj, owner):
		return self.method(owner)

pythonize = operator.attrgetter('python')