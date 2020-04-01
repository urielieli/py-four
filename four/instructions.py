import re
import operator

from operands import GridAccess, Constant



def indent_multiline(string):
	return '\n'.join('    {}'.format(line) for line in string.split('\n'))


class classproperty:
	def __init__(self, method):
		self.method = method

	def __get__(self, obj, owner):
		return self.method(owner)


class Instruction:
	arity = None
	opcode = None

	def __init__(self, *params):
		self.params = list(params)

	def __getitem__(self, key):
		if key >= self.arity:
			raise IndexError('parameter index exceeds indtruction arity')
		return self.params[key]

	def __setitem__(self, key, value):
		if key >= self.arity:
			raise IndexError('parameter index exceeds indtruction arity')
		self.params[key] = value

	@classproperty
	def offset(cls):
		return 1 + cls.arity * 2

	def __str__(self):
		return ('{}' + ' {:0>2}' * self.arity).format(self.opcode, *[(param.value if hasattr(param, 'value') else param) for param in self.params])

	@property
	def python(self):
		return str(self)


class RootInstruction(Instruction):
	def __init__(self, *params):
		super().__init__(*params)
		self.instructions = []

	def __str__(self):
		return '\n'.join(map(str, self.instructions))

	@property
	def python(self):
		return '\n'.join([inst.python for inst in self.instructions])

	def __iadd__(self, inst):
		self.instructions.append(inst)
		return self


# Assignment #


class SetInstruction(Instruction):
	arity = 2
	opcode = 6

	@property
	def python(self):
		return '{0} = {1}'.format(self.params[0].python, self.params[1].python)


# Exit #


class ExitInstruction(Instruction):
	arity = 0
	opcode = 4

	@property
	def python(self):
		return 'exit(0)'


# Arithmatics #


class ArithmaticInstruction(Instruction):
	arity = 3
	operation = None

	python_operators = {
		operator.add: '+',
		operator.sub: '-',
		operator.mul: '*',
		operator.truediv: '//'
	}

	@property
	def python(self):
		python_operator = self.python_operators.get(self.operation)
		
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


# IO #


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


# Branching #


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
