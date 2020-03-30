from instructions import Instruction


class IOInstruction(Instruction):
	arity = 1

	def __init__(self, opcode, *params):
		super().__init__(opcode, *params)

	@property
	def operand(self):
		return self[0]
	@operand.setter
	def operand(self, value):
		self[0] = value


class InputInstruction(IOInstruction):
	opcode = 7

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	@property
	def python(self):
		return '{0} = getc()'.format(self.params[0].python)


class OutputInstruction(IOInstruction):
	opcode = 5

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	@property
	def python(self):
		return 'putc({0})'.format(self.params[0].python)
