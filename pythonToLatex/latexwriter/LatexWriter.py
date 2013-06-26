import sys
from LatexTable import *
from LatexGraph import *
from utils import *

class LatexWriter():
	def __init__( self, stream="" ):
		self.stream = stream
		self.textStyles = ['normal','italic','bold']

	def getStream( self ):
		return self.stream;

	def getStylizedText( self, text, textStyle ):
		string = ""
		if textStyle != self.textStyles[0] :
			if textStyle == self.textStyles[1]:
				string += "\\"+"textit{" + text + "}"
			elif textStyle == self.textStyles[2]:
				string += "\\"+"textbf{" + text + "}"
			else:
				raise ValueError("text style is not available, possible values are: " + ", ".join(self.textStyles) )
		else:
			string = text
		return string;

	def setDocumentClass( self, documentClass="article", options="11pt, a4paper" ):
		self.stream += "\\documentclass[" + options + "]{" + documentClass + "} \n"

	def beginDocument( self ):
		self.stream += "\\begin{document} \n"

	def endDocument( self ):
		self.stream += "\\end{document} \n"

	def addPackage( self, package, options="" ):
		# if not isinstance(options, List):
		# 	raise ValueError("request a 'List' object for options")
		self.stream += "\\usepackage"
		if options != "" :
			self.stream += "[" + options + "]"
			# self.stream += "[" + ", ".join( options ) + "]"
		self.stream += "{" + package + "} \n"

	def addMacroSetting( self, name, value, unit ):
		if name == "" or unit == "" :
			raise ValueError("request name, value and unit")
		self.stream += "\\" + name + " = " + str(value) + " " + unit + " \n"

	def addMacro( self, name ):
		if not isinstance(name, str) :
			raise ValueError("request a 'str' object for name")
		self.stream += "\\" + name + " \n"

	def addSimpleCommand( self, command, value="" ):
		if not isinstance(command, str) :
			raise ValueError("request a 'str' object for command")
		self.stream += "\\" + command + "{" + value + "} \n"

	def addNewCommand( self, newcommand, value ):
		if not isinstance(newcommand, str) :
			raise ValueError("request a 'str' object for newcommand")
		if not isinstance(value, str) :
			raise ValueError("request a 'str' object for value")
		if newcommand == "" or value == "" :
			raise ValueError("request a command name and its value")
		self.stream += "\\newcommand{\\" + newcommand + "}{" + value + "}\n"

	def addRawLatex( self, rawLatex ):
		if not isinstance(rawLatex, str) :
			raise ValueError("request a 'str' object for rawLatex")
		self.stream += rawLatex + " \n"

	def addSpace( self ):
		self.stream += " "

	def addSimpleLineBreak( self ):
		self.stream += "  \n"

	def addDoubleLineBreak( self ):
		self.stream += "\n \n"

	def addHorizontalRule( self ):
		self.stream += "\\rule{\\linewidth}{0.5pt}"

	def addHeader( self, text, level=1, number=False ):
		if level < 1 or level > 7 :
			raise ValueError("header level must be included in [1,6]")
		num = "*"
		if number :
			num = ""

		if level == 1 :
			self.stream += "\\part"          + num + "{" + text + "}"
		if level == 2 :
			self.stream += "\\chapter"       + num + "{" + text + "}"
		if level == 3 :
			self.stream += "\\section"       + num + "{" + text + "}"
		if level == 4 :
			self.stream += "\\subsection"    + num + "{" + text + "}"
		if level == 5 :
			self.stream += "\\subsubsection" + num + "{" + text + "}"
		if level == 6 :
			self.stream += "\\paragraph"     + num + "{" + text + "}"
		if level == 7 :
			self.stream += "\\subparagraph"  + num + "{" + text + "}"
		
		self.stream += "\n"


	def addParagraph( self, text, tabulation=0, indent=False, textStyle='normal' ):	
		if tabulation < 0 :
			raise ValueError("tabulation number must be positive")
		if indent :
			self.stream += "\\parindent \n"

		self.stream += self.getStylizedText( transformSpecialCharacters( text ), textStyle )


	def addText( self, text, textStyle='normal'):
		self.stream += self.getStylizedText( transformSpecialCharacters( text ), textStyle )

	def addList( self, text, numStyleList=False, tabulation=0, textStyle='normal' ):
		if type(text) is not list:
			raise ValueError("request a list of string")

		if tabulation < 0 :
			raise ValueError("tabulation number must be positive")

		if numStyleList == False :
				listType = "itemize"
		else :
			listType = "enumerate"

		self.stream += "\\begin{" + listType + "}\n"
		for i in range(0,len(text)) :
			self.stream += "\\item "
			self.stream += self.getStylizedText( text[i], textStyle )
			self.addSimpleLineBreak()
		self.stream += "\\end{" + listType + "}\n"

	def addLink( self, linkUrl, linkText="" ):
		if linkText != "":
			self.stream += "\\href{" + linkUrl + "}{" + linkText + "}"
		else:
			self.stream += "\\url{" + linkUrl + "}"

	def addImage( self, imageUrl, imageScale=1 ):
		self.stream += "\includegraphics[scale=" + str( imageScale ) + "]{" + imageUrl + "}"

	def addTable( self, table, longTable=False, width="", title=False ):
		if not isinstance(table, LatexTable):
			raise ValueError("request a 'LatexTable' object")
		self.stream += table.getTable( longTable, width, title )

	def addGraph( self, graph, rawWidth="", xLabel="", yLabel="", xUnit="", yUnit="", xScale=1, yScale=0.4, yMax=0, yMin=-70, xMin=0 ):
		if not isinstance(graph, LatexGraph):
			raise ValueError("request a 'LatexGraph' object")
		self.stream += graph.getGraph( rawWidth, xLabel, yLabel, xUnit, yUnit, xScale, yScale, yMax, yMin, xMin )
