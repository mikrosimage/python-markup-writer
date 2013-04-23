import sys

from markdownwriter import *
from PandocMarkdownTable import *

class PandocMarkdownWriter( MarkdownWriter ):
	def addTable( self, table):
		if not isinstance(table, PandocMarkdownTable):
			raise ValueError("request a 'PandocMarkdownTable' object")
		self.stream += table.getTable()
	

	def addImage( self, imageUrl, imageTitle="", imageLegend="" ):
		if imageLegend == "":
			imageLegend = imageTitle
		self.stream += "![" + imageLegend + "]"
		self.stream += "(" + imageUrl + " \"" + imageTitle + "\")"


	def addTitle( self, title ):
		self.stream += "%"+ title
		