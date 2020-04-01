class Operand:
	def __init__(self, value):
		if isinstance(value, str):
			value = int(value)
		self.value = value

	@property
	def python(self):
		return str(self.value)

class Constant(Operand):
	def __eq__(self, other):
		return isinstance(other, Constant) and (self.value == other.value)

class GridAccess(Operand):
	def __eq__(self, other):
		return isinstance(other, GridAccess) and (self.value == other.value)

	@property
	def python(self):
		return 'grid[{}]'.format(self.value)
