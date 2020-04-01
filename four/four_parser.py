import re

from operands import GridAccess, Constant
from instructions import ExitInstruction, SetInstruction, RootInstruction
from io_instructions import OutputInstruction, InputInstruction
from loop_instructions import LoopInstruction, EndLoopInstruction
from arithmatic_instructions import AdditionInstruction, SubtractionInstruction, MultiplicationInstruction, DivisionInstruction


def chunks(itearble, size=1):
	return [itearble[offset: offset+size] for offset in range(0, len(itearble), size)]


class FourParser:
	instructions = {
		0: (AdditionInstruction, [GridAccess, GridAccess, GridAccess]),
		1: (SubtractionInstruction, [GridAccess, GridAccess, GridAccess]),
		2: (MultiplicationInstruction, [GridAccess, GridAccess, GridAccess]),
		3: (DivisionInstruction, [GridAccess, GridAccess, GridAccess]),
		4: (ExitInstruction, [None]),
		5: (OutputInstruction, [GridAccess]),
		6: (SetInstruction, [GridAccess, Constant]),
		7: (InputInstruction, [GridAccess]),
		8: (LoopInstruction, [GridAccess]),
		9: (EndLoopInstruction, [None])
	}

	@staticmethod
	def strip(code):
		constraints = {
			'^3\.' : 'Program must begin with \'3.\'',
			'.*4$' : 'Program must end with \'4\'',
			'^3\.\d*4$' : 'Program must not contain anything but digits'
		}

		for constraint, error_msg in constraints.items():
			if not re.match(constraint, code):
				raise SyntaxError(error_msg)

		return re.match('^3\.(\d*)4$', code).group(1)

	@staticmethod
	def tokenize(code):
		tokens = []

		while code:
			opcode = int(code[0])
			_type, _operands = FourParser.instructions[opcode]
			_token = _type(*[
				operand(value) for operand, value in
				zip(_operands, chunks(code[1:_type.offset], 2))
			])
			#print('Tokenizing {:<18} as <{}>'.format('<{}>'.format(_token), _type.__name__))
			tokens.append(_token)
			code = code[_type.offset:]

		return tokens

	@staticmethod
	def parse(tokens):
		results = []
		parents = []
		root = RootInstruction(10)

		while tokens:
			inst = tokens.pop(0)

			if isinstance(inst, LoopInstruction):
				parents.append(root)
				root = inst
			elif isinstance(inst, EndLoopInstruction):
				root, loop = parents.pop(-1), root
				root += loop
			else:
				root += inst

		if parents:
			raise Exception('Some loops were left not closed')

		return root
