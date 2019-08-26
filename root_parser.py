from instructions import RootInstruction
from loop_instructions import LoopInstruction, EndLoopInstruction

def parse(tokens):
	results = []
	roots_track = []
	root = RootInstruction(10)

	while tokens:
		inst = tokens.pop(0)

		if isinstance(inst, LoopInstruction):
			roots_track.append(root)
			root = inst

		elif isinstance(inst, EndLoopInstruction):
			restored_root = roots_track.pop(-1)
			restored_root += root
			root = restored_root

		else:
			root += inst

	if roots_track:
		raise Exception('Some loops were left not closed')

	return root