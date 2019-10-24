try:
    from MarkdownTable import MarkdownTable
except ImportError:  # Python 3
    from .MarkdownTable import MarkdownTable

class MarkdownWriter():
	def __init__( self, stream="" ):
		self.stream = stream
		self.textStyles = ['normal','italic','bold']

	def getStream( self ):
		return self.stream;

	def getStylizedText( self, text, textStyle ):
		string = ""
		if textStyle != self.textStyles[0] :
			if textStyle == self.textStyles[1]:
				string += "_" + text + "_"
			elif textStyle == self.textStyles[2]:
				string += "__" + text + "__"
			else:
				raise ValueError("text style is not available, possible values are: " + ", ".join(self.textStyles) )
		else:
			string = text
		return string;

	def transformSpecialCharacters( self, text ):
		string = text
		string = string.replace('*', '\*')
		string = string.replace('`', '\`')
		string = string.replace('_', '\_')
		string = string.replace('{', '\{')
		string = string.replace('}', '\}')
		string = string.replace('[', '\[')
		string = string.replace(']', '\]')
		string = string.replace('(', '\(')
		string = string.replace(')', '\)')
		string = string.replace('#', '\#')
		string = string.replace('+', '\+')
		string = string.replace('-', '\-')
		string = string.replace('!', '\!')
		string = string.replace('&', '&amp;')
		string = string.replace('<', '&lt;')
		return string;


	def addSpace( self ):
		self.stream += " "

	def addSimpleLineBreak( self ):
		self.stream += "  \n"

	def addDoubleLineBreak( self ):
		self.stream += "\n \n"

	def addTabulation( self, tabNum ):
		self.stream += ">"*tabNum

	def addHorizontalRule( self ):
		self.addDoubleLineBreak()
		self.stream += "-----"
		self.addDoubleLineBreak()

	def addHeader( self, text, level=1 ):
		if level < 1 or level > 6 :
			raise ValueError("header level must be included in [1,6]")

		self.stream += "#"*level + " "
		self.stream += text + "\n"			

	def addParagraph( self, text, tabulation=0, textStyle='normal' ):	
		if tabulation < 0 :
			raise ValueError("tabulation number must be positive")

		self.stream += ">"*tabulation
		self.stream += self.getStylizedText( self.transformSpecialCharacters( text ), textStyle )
		self.addDoubleLineBreak() 


	def addText( self, text, textStyle='normal'):
		self.stream += self.getStylizedText( self.transformSpecialCharacters( text ), textStyle )

	def addList( self, text, numStyleList=False, tabulation=0, textStyle='normal' ):
		if type(text) is not list:
			raise ValueError("request a list of string")

		if tabulation < 0 :
			raise ValueError("tabulation number must be positive")

		for i in range(0,len(text)) :
			if numStyleList == False :
				self.stream += ">"*tabulation
				self.stream += "+ "
				self.stream += self.getStylizedText( text[i], textStyle )
				self.addSimpleLineBreak()
			else : 
				self.stream += ">"*tabulation
				self.stream += str(i+1)+". "
				self.stream += self.getStylizedText( text[i], textStyle )
				self.addSimpleLineBreak()

	def addCodeBlock( self, codeText ):
		codeLines = codeText.split('\n')
		self.addSimpleLineBreak()
		for line in codeLines:
			self.stream += "\t"
			self.stream += line
			self.addSimpleLineBreak()

	def addCodeWord( self, codeWord ):
			self.stream += "`"
			self.stream += codeWord
			self.stream += "`"

	def addLink( self, linkUrl, linkText, linkTitle="" ):
		self.stream += "[" + linkText + "]"
		self.stream += "(" + linkUrl
		if linkTitle != "":
			self.stream += " \"" + linkTitle + "\"" + ")"
		else:
			self.stream += ")"

	def addImage( self, imageUrl, imageTitle="", altText="Alt. text" ):
		self.stream += "![" + altText + "]"
		self.stream += "(" + imageUrl + " \"" + imageTitle + "\")"

	def addImageWithLink( self, imageUrl, linkUrl, imageTitle="", altText="Alt. text" ):
		self.stream += "[![" + altText + "]"
		self.stream += "(" + imageUrl + " \"" + imageTitle + "\")]"
		self.stream += "(" + linkUrl + ")"

	def addTable(self, table):
		if not isinstance(table, MarkdownTable):
			raise ValueError("request a 'MarkdownTable' object")
		self.stream += table.getTable()
