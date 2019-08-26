from utils import chunks

from operands import GridAccess, Constant

from instructions import ExitInstruction, SetInstruction
from io_instructions import OutputInstruction, InputInstruction
from loop_instructions import LoopInstruction, EndLoopInstruction
from arithmatic_instructions import AdditionInstruction, SubtractionInstruction, MultiplicationInstruction, DivisionInstruction

def tokenize(code):
	inst_types = [
		(AdditionInstruction, GridAccess, GridAccess, GridAccess),
		(SubtractionInstruction, GridAccess, GridAccess, GridAccess),
		(MultiplicationInstruction, GridAccess, GridAccess, GridAccess),
		(DivisionInstruction, GridAccess, GridAccess, GridAccess),
		(ExitInstruction, None),
		(OutputInstruction, GridAccess),
		(SetInstruction, GridAccess, Constant),
		(InputInstruction, GridAccess),
		(LoopInstruction, GridAccess),
		(EndLoopInstruction, None)
	]
	tokens = []

	while code:
		inst_type, *operand_types = inst_types[int(code[0])]
		new_token = inst_type(*map(lambda pair: pair[0](pair[1]),
									zip(operand_types, chunks(code[1:inst_type.offset], 2))))
		print('Tokenizing {:<18} as <{}>'.format('<{}>'.format(new_token), inst_type.__name__))
		tokens.append(new_token)
		code = code[inst_type.offset:]

	return tokens