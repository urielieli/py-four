from instructions import Instruction, RootInstruction


def indent_multiline(string):
	return '\n'.join('    {}'.format(line) for line in string.split('\n'))


class LoopInstruction(RootInstruction):
	arity = 1
	opcode = 8

	def __str__(self):
		string = Instruction.__str__(self)
		return '{}\n{}'.format(string, super().__str__()) if self.instructions else string

	@property
	def python(self):
		transpiled = 'while {0}:'.format(self.params[0].python)

		return '{}\n{}'.format(
			transpiled,
			'\n'.join([indent_multiline(inst.python) for inst in self.instructions])
		) if self.instructions else transpiled


class EndLoopInstruction(Instruction):
	arity = 0
	opcode = 9

	@property
	def python(self):
		return ''