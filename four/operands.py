class Operand:
	def __init__(self, value):
		if isinstance(value, str):
			value = int(value)
		self.value = value

	@property
	def python(self):
		return str(self.value)

class Constant(Operand):
	pass

class GridAccess(Operand):
	@property
	def python(self):
		return 'grid[{}]'.format(self.value)
