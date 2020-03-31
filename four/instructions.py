import re

from formatting import indent_multiline
from operands import GridAccess, Constant


class classproperty:
	def __init__(self, method):
		self.method = method

	def __get__(self, obj, owner):
		return self.method(owner)


class Instruction:
	arity = 0

	def __init__(self, opcode, *params):
		self.opcode = opcode
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
		return ('{}' + ' {:0>2}' * self.arity).format(self.opcode, *[param.value for param in self.params])

	@property
	def python(self):
		return str(self)

class RootInstruction(Instruction):
	arity = 0
	indent = 0

	def __init__(self, opcode, *params):
		super().__init__(opcode, *params)
		self.instructions = []

	def __str__(self):
		return '\n'.join(map(str, self.instructions))

	@property
	def python(self):
		return indent_multiline('\n'.join([inst.python for inst in self.instructions]), self.indent)

	def __iadd__(self, inst):
		self.instructions.append(inst)
		return self

class SetInstruction(Instruction):
	arity = 2
	opcode = 6

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	@property
	def python(self):
		return '{0} = {1}'.format(self.params[0].python, self.params[1].python)

	@property
	def cell(self):
		return self[0]
	@cell.setter
	def cell(self, value):
		self[0] = value

	@property
	def value(self):
		return self[1]
	@value.setter
	def value(self, value):
		self[1] = value

class ExitInstruction(Instruction):
	arity = 0
	opcode = 4

	def __init__(self, *params):
		super().__init__(self.opcode, *params)

	@property
	def python(self):
		return 'exit(0)'