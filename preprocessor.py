import re

def get_raw_code(code):

	constraints = {
		'^3\.' : 'Program must begin with \'3.\'',
		'.*4$' : 'Program must end with \'4\'',
		'^3\.\d*4$' : 'Program must not contain anything but digits'
	}

	for constraint, error_msg in constraints.items():
		if not re.match(constraint, code):
			raise Exception(error_msg)

	return re.match('^3\.(\d*4)$', code).group(1)