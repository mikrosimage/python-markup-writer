def transformSpecialCharacters( text ):
	string = text
	string = string.replace('*', '\*')
	string = string.replace('`', '\`')
	string = string.replace('_', '\_')
	# string = string.replace('{', '\{')
	# string = string.replace('}', '\}')
	# string = string.replace('[', '\[')
	# string = string.replace(']', '\]')
	# string = string.replace('(', '\(')
	# string = string.replace(')', '\)')
	string = string.replace('#', '\#')
	string = string.replace('+', '\+')
	# string = string.replace('-', '\-')
	string = string.replace('!', '\!')
	# string = string.replace('\\', '\textbackslash{}')
	string = string.replace('&', '&amp;')
	string = string.replace('<', '&lt;')
	return string;