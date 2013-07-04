def transformSpecialCharacters( text ):
	string = text
	string = string.replace('`', '\\`')
	string = string.replace('_', '\\_')
	string = string.replace('{', '\\{')
	string = string.replace('}', '\\}')
	string = string.replace('#', '\\#')
	return string;