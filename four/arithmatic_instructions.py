import operator

from instructions import Instruction


class ArithmaticInstruction(Instruction):
	arity = 3

	def __init__(self, opcode, operation, *params):
		super().__init__(opcode, *params)
		self.operation = operation

	@property
	def python(self):
		return '{1} = {0}({2}, {3})'.format(
			self.operation.__name__,
			self.params[0].python,
			self.params[1].python,
			self.params[2].python
		)

	@property
	def cell(self):
		return self[0]
	@cell.setter
	def cell(self, value):
		self[0] = value

	@property
	def operand1(self):
		return self[1]
	@operand1.setter
	def operand1(self, value):
		self[1] = value

	@property
	def operand2(self):
		return self[2]
	@operand2.setter
	def operand2(self, value):
		self[2] = value


class AdditionInstruction(ArithmaticInstruction):
	opcode = 0
	operation = operator.add

	def __init__(self, *params):
		super().__init__(self.opcode, self.operation, *params)


class SubtractionInstruction(ArithmaticInstruction):
	opcode = 1
	operation = operator.sub

	def __init__(self, *params):
		super().__init__(self.opcode, self.operation, *params)


class MultiplicationInstruction(ArithmaticInstruction):
	opcode = 2
	operation = operator.mul

	def __init__(self, *params):
		super().__init__(self.opcode, self.operation, *params)


class DivisionInstruction(ArithmaticInstruction):
	opcode = 3
	operation = operator.truediv

	def __init__(self, *params):
		super().__init__(self.opcode, self.operation, *params)