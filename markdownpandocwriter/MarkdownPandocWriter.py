import sys

from markdownwriter import *

class Table():
	def __init__( self ):
		self.data = []
		self.size = [0,0]

	def setData( self, array ):
		self.data = array
		self.size[0] = len( self.data )
		tmpSize = []
		for line in self.data:
			tmpSize.append( len(line) )
		self.size[1] = max(tmpSize)

	def getTable( self ):
		if len( self.data ) == 0 :
			raise ValueError("setData() before getTable()")
		string = "\\"+"begin{table}[h]" + "\\" + "centering"
		string += "\\"+"begin{tabular}{"
		string += "|c" * self.size[1]
		string += "|} \hline "
		for i in range(0, self.size[0]) :
			if i==0:
				j=0
				while j!=len(self.data[i])-1:
					string += self.data[i][j] + "&"
					j+=1
				string += self.data[i][j] + "\\" + "\\ \hline "   
			else:
				j=0
				while j!=len(self.data[i])-1:
					string += self.data[i][j] + "&"
					j+=1
				string += self.data[i][j] + "\\" + "\\" 
		string += " \hline "
		string += "\end{tabular}\end{table}"
		return string;

class MarkdownPandocWriter( MarkdownWriter ):
	def addTable( self, array ):
		if type( array ) is not list:
			raise ValueError("request a list (of lists) of strings")

		table = Table()
		table.setData( array )
		self.stream += table.getTable()
	
	def addImage( self, imageUrl, imageTitle="", imageLegend="" ):
		if imageLegend == "":
			imageLegend = imageTitle
		self.stream += "![" + imageLegend + "]"
		self.stream += "(" + imageUrl + " \"" + imageTitle + "\")"