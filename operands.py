class GridAccess:
	def __init__(self, index):
		if isinstance(index, str):
			index = int(index)
		self.index = index

	def __str__(self):
		return '[{:0>2}]'.format(self.index)

	@property
	def python(self):
		return 'grid[{}]'.format(self.index)

class Constant:
	def __init__(self, value):
		if isinstance(value, str):
			value = int(value)
		self.value = value

	def __str__(self):
		return '~{:0>2}~'.format(self.value)

	@property
	def python(self):
		return '{}'.format(self.value)