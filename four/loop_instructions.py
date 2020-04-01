from formatting import indent_multiline
from instructions import Instruction, RootInstruction


class LoopInstruction(RootInstruction):
	arity = 1
	indent = 1
	opcode = 8

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	def __str__(self):
		string = Instruction.__str__(self)

		if self.instructions:
			return '{}\n{}'.format(string,
								   super().__str__())
		return string

	@property
	def python(self):
		transpiled = 'while {0}:'.format(self.params[0].python)

		if self.instructions:
			return '{}\n{}'.format(transpiled,
								   indent_multiline('\n'.join(map(lambda inst: inst.python, self.instructions)),
										            self.indent))
		return transpiled


class EndLoopInstruction(Instruction):
	arity = 0
	opcode = 9

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	@property
	def python(self):
		return ''