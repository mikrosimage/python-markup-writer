# coding: utf-8
def transformSpecialCharacters( text ):
	string = text

	string = string.replace('`', '&#96;')
	string = string.replace('"', '&quot;')
	string = string.replace('&', '&amp;')
	# string = string.replace('>', '&gt;')
	# string = string.replace('<', '&lt;')

	string = string.replace('\n', '<br>')

	return string;
