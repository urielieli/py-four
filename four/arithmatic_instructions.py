import operator

from instructions import Instruction


class ArithmaticInstruction(Instruction):
	arity = 3

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	@property
	def python(self):
		return '{1} = {2} {0} {3}'.format(
			{
				operator.add: '+',
				operator.sub: '-',
				operator.mul: '*',
				operator.truediv: '//',
			}.get(self.operation),
			self.params[0].python,
			self.params[1].python,
			self.params[2].python
		)


class AdditionInstruction(ArithmaticInstruction):
	opcode = 0
	operation = operator.add

class SubtractionInstruction(ArithmaticInstruction):
	opcode = 1
	operation = operator.sub

class MultiplicationInstruction(ArithmaticInstruction):
	opcode = 2
	operation = operator.mul

class DivisionInstruction(ArithmaticInstruction):
	opcode = 3
	operation = operator.truediv
