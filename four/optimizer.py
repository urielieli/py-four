"""def optimize_constants(tokens):

	print('Optimizing for constants...')

	constants = {}

	for cell in range(GRID_SIZE):
		sets = []

		for token in tokens:
			if isinstance(token, SetInstruction) and token.cell.index == cell:
				sets.append(token)

		if len(sets) == 1:
			constants[cell] = sets[0]

	for cell in list(constants.keys()):
		for token in tokens:
			if isinstance(token, LoopInstruction) and token.cell.index == cell:
				del constants[cell]

	for token in constants.values():
		print('Removing constant setter {}'.format(token))
		tokens.remove(token)

	for token in tokens:
		if isinstance(token, ArithmaticInstruction):
			for index, param in enumerate(token.params):
				if index > 0 and isinstance(param, GridAccess) and param.index in constants.keys():
					token[index] = constants[param.index].value
		if isinstance(token, OutputInstruction):
			if isinstance(token.operand, GridAccess) and token.operand.index in constants.keys():
				token.operand = constants[token.operand.index].value

	return tokens, len(constants) > 0

def optimize_arithmatics(tokens):

	print('Optimizing for constant arithmatics...')

	optimized = False

	for index, token in enumerate(tokens):
		if isinstance(token, ArithmaticInstruction):
			if isinstance(token.operand1, int) and isinstance(token.operand2, int):
				print('Replacing token {} with a constant setter'.format(token))
				tokens[index] = SetInstruction(6, token.cell.index, token.operation(token.operand1, token.operand2))
				optimized = True

	return tokens, optimized"""

def optimize_constants(tokens):
	return tokens, False
def optimize_arithmatics(tokens):
	return tokens, False

def optimize(tokens):
	optimized = True

	while optimized:
		for optimization in [optimize_constants, optimize_arithmatics]:
			tokens, _optimized = optimization(tokens)
			optimized |= _optimized

	return tokens