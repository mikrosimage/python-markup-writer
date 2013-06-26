from utils import *

class HtmlTable():
	def __init__( self ):
		self.data  = []
		self.size  = [0,0]
		self.title = ""

		self.alignmentList = ['left','center','right']
		self.tableAlignment = "center"
		self.columnAlignment = []
		self.columnWidth = []
		
		self.textStyles = ['normal','italic','bold']
		self.textColors = ['black','white','red','green','blue','cyan','magenta','yellow']
		
		self.borderStyles = ['none','out','frame','header','closedHeader','doubleHeader']
		self.vLines = []
		self.hLines = []

	def setContent( self, array ):
		if type(array) is not list :
			raise ValueError( "list of lists expected" )
		if type(array[0]) is not list :
			raise ValueError( "list of lists expected" )

		self.data = array
		width = []
		for line in self.data:
			width.append( len(line) )
		self.size = [ len( self.data ), max( width ) ]


	def setTitle( self, title ):
		self.title = title

	def setColumnWidth( self, width ):
		self.columnWidth.append( width )

	def setColumnAlignment( self, alignment ):
		for align in self.alignmentList :
			if align == alignment :
				self.columnAlignment.append( alignment )

	def getTable( self, id="", border="" ):
		string = ""
		if len( self.data ) == 0 :
			raise ValueError("setContent() before getTable()")
		
		string += "<table"
		if id != "" :
			string += " id=\""+ id +"\"" 
		if border != "" :
			string += " border=\""+ str(border) +"\""
		string += ">\n"

		if self.title != "" :
			string += "<caption>"
			string += transformSpecialCharacters( self.title )
			string += "<caption>\n"
	
		if len(self.columnWidth) != 0 :
			string += "<colgroup>\n"
			for width in self.columnWidth :	# column width
				string += "<col style='width: " + width + ";'/>\n"
			string += "</colgroup>\n"

		for i in range(0, self.size[0]) :	# lines
			string += "<tr>\n"
			for j in range( 0, len(self.data[i]) ):
				string += "\t<td"
				if len(self.columnAlignment) == len(self.data[i]) :
					string += " align='" + self.columnAlignment[j] + "'"
				elif len(self.columnAlignment) != 0 :
					raise RuntimeError( "Column aligment must be specified for all or none column." )
				string += ">"

				if type( self.data[i][j] ) is not list:		# data is not a list (string)
					if self.data[i][j] == "[...]" :
						string += "<i>" + self.data[i][j] + "</i>"
					else :
						string += self.data[i][j]

				elif len(self.data[i][j]) == 0 :			# data is an empty list
					string += "<i> - DATA - </i>"

				elif len(self.data[i][j]) == 1 :			# data is a list of one element
					string += self.data[i][j][0]

				else:										# data is a list of several elements
					kHeight = len(self.data[i][j])
					kWidth  = []

					for k in range( 0, len(self.data[i][j]) ):
						kWidth.append( len(self.data[i][j][k]) )
					if len( kWidth ) > 0 :
						kWidthMax = max( kWidth )

					string += "\n<table>\n"
					for k in range( 0, kHeight ):
						string += "<tr>\n"
						if type( self.data[i][j][k] ) is str or type( self.data[i][j][k] ) is unicode :
							string += "\t<td>"
							string += self.data[i][j][k]
							string += "</td>\n"

						elif type( self.data[i][j][k] ) is list :
							for l in range( 0, kWidthMax ):
								string += "\t<td>"
								string += self.data[i][j][k][l]
								string += "</td>\n"
						string += "</tr>\n"
					string += "</table>\n"

				string += "</td>\n"
			string += "</tr>\n"
		string += "</table>\n"

		return string;