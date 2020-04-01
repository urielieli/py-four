import operator

from instructions import Instruction


class ArithmaticInstruction(Instruction):
	arity = 3
	operators = {
		operator.add: '+',
		operator.sub: '-',
		operator.mul: '*',
		operator.truediv: '//'
	}

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	@property
	def python(self):
		python_operator = self.operators.get(self.operation)
		
		if self.params[0] == self.params[1]:
			return '{1} {0}= {2}'.format(
				python_operator,
				self.params[0].python,
				self.params[2].python
			)
		elif self.params[0] == self.params[2] and self.operation in [operator.add, operator.mul]:
			return '{1} {0}= {2}'.format(
				python_operator,
				self.params[0].python,
				self.params[1].python
			)
		return '{1} = {2} {0} {3}'.format(
			python_operator,
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
