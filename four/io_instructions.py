from instructions import Instruction


class IOInstruction(Instruction):
	arity = 1


class InputInstruction(IOInstruction):
	opcode = 7

	@property
	def python(self):
		return '{0} = getc()'.format(self.params[0].python)


class OutputInstruction(IOInstruction):
	opcode = 5

	@property
	def python(self):
		return 'putc({0})'.format(self.params[0].python)
