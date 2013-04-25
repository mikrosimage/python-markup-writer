import sys

class PandocMarkdownTable():
	def __init__( self ):
		self.data  = []
		self.size  = [0,0]
		self.title = ""

		self.alignmentList = ['left','center','right']
		self.tableAlignment = "center"
		self.rowAlignment = []
		
		self.textStyles = ['normal','italic','bold']
		self.textColors = ['black','white','red','green','blue','cyan','magenta','yellow']
		
		self.borderStyles = ['none','out','frame','header','doubleheader']
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
		self.size = [ len( self.data ), max(width) ]

		for i in range(0, self.size[1]):
			self.rowAlignment.append('c')

		for i in range(0, self.size[1]+1):
			self.vLines.append('')

		for i in range(0, self.size[0]+1):
			self.hLines.append('')	

	def setTitle( self, title ):		
		self.title = title

	def setTableAlignment( self, alignment ):
		if alignment == self.alignmentList[0] :
			self.tableAlignment = 'flushleft'
		elif alignment == self.alignmentList[1] :
			self.tableAlignment = 'center'
		elif alignment == self.alignmentList[2] :
			self.tableAlignment = 'flushright'
		else:
			raise ValueError("alignment not available, possible values are: " + ", ".join(self.alignmentList) )


	def setBorders( self, borderStyle ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")

		if   borderStyle == self.borderStyles[1]: #out
			self.vLines[0] = '|'
			for i in range(1, self.size[1]):
				self.vLines[i] = ''		
			self.vLines[ self.size[1] ] = '|'

			self.hLines[0] = ' \hline '
			for i in range(1, self.size[0]):
				self.hLines[i] = ''			
			self.hLines[ self.size[0] ] = ' \hline '

		elif borderStyle == self.borderStyles[2]: #frame
			for i in range(0, self.size[1]+1):
				self.vLines[i] = '|'
			for i in range(0, self.size[0]+1):
				self.hLines[i] = ' \hline '

		elif borderStyle == self.borderStyles[3]: #header
			self.vLines[0] = '|'
			for i in range(1, self.size[1]):
				self.vLines[i] = ''		
			self.vLines[ self.size[1] ] = '|'

			self.hLines[0] = ' \hline '
			self.hLines[1] = ' \hline '
			for i in range(2, self.size[0]):
				self.hLines[i] = ''			
			self.hLines[ self.size[0] ] = ' \hline '

		elif borderStyle == self.borderStyles[4]: #doubleheader
			self.vLines[0] = '|'
			self.vLines[1] = '|'
			for i in range(2, self.size[1]):
				self.vLines[i] = ''			
			self.vLines[ self.size[1] ] = '|'

			self.hLines[0] = ' \hline '
			self.hLines[1] = ' \hline '
			for i in range(2, self.size[0]):
				self.hLines[i] = ''			
			self.hLines[ self.size[0] ] = ' \hline '

		elif borderStyle != self.borderStyles[0] :
				raise ValueError("cell style is not available, possible values are: " + ", ".join(self.borderStyles) )


	def setCellStyle( self, line, row, textStyle ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if line > self.size[0]-1 or line < 0 :
			raise ValueError("line value not valid")
		if row  > self.size[1]-1 or row  < 0 :
			raise ValueError("row value not valid")

		if textStyle == self.textStyles[1]:
			for k in range( 0, len( self.data[line][row] ) ):
				self.data[line][row][k] = "\\"+"textit{"+ self.data[line][row][k] +"}"
		elif textStyle == self.textStyles[2]:
			for k in range( 0, len( self.data[line][row] ) ):
				self.data[line][row][k] = "\\"+"textbf{"+ self.data[line][row][k] +"}"
		elif textStyle != self.textStyles[0] :
			raise ValueError("cell style is not available, possible values are: " + ", ".join(self.textStyles) )

	def setTextColor( self, line, row, color ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if line > self.size[0]-1 or line < 0 :
			raise ValueError("line value not valid")
		if row  > self.size[1]-1 or row  < 0 :
			raise ValueError("row value not valid")

		if self.textColors.count( color ) == 0:
			raise ValueError("cell style is not available, possible values are: " + ", ".join(self.textColors) )

		for k in range( 0, len( self.data[line][row] ) ):
			if self.data[line][row][k].count( '\ {\color{') :
				for textColor in self.textColors :
					if self.data[line][row][k].count( textColor ) :
						self.data[line][row][k] = self.data[line][row][k].replace( textColor, color )
			else:
				self.data[line][row][k] = "{"+"\\"+"color{"+color+"}"+self.data[line][row][k]+"}"

	def setRowAlignment( self, row, alignment ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if row > self.size[1]-1 or row < 0 :
			raise ValueError("row value not valid")
		
		if alignment == self.alignmentList[0] :
			self.rowAlignment[row] = 'l'
		elif alignment == self.alignmentList[1] :
			self.rowAlignment[row] = 'c'
		elif alignment == self.alignmentList[2] :
			self.rowAlignment[row] = 'r'
		else:
			raise ValueError("alignment not available, possible values are: " + ", ".join(self.alignmentList) )


	def addImage( self, imagePath, line, row ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if line > self.size[0]-1 or line < 0 :
			raise ValueError("line value not valid")
		if row  > self.size[1]-1 or row  < 0 :
			raise ValueError("row value not valid")

		self.data[line][row][0] = " \\" + "includegraphics{" + imagePath + "} "


	def getTable( self ):
		string = ""
		if len( self.data ) == 0 :
			raise ValueError("setData() before getTable()")
		
		string += "\\" + "begin{table}[h]"
		string += "\\" + "begin{"+ self.tableAlignment+ "}"
		string += "\\" + "begin{tabular}{"

		for i in range(0, self.size[1]):
			string += self.vLines[i]
			string += self.rowAlignment[i]
		string += self.vLines[ self.size[1] ]
		string += "}"
		
		for i in range(0, self.size[0]) :
			string += self.hLines[i]
			for j in range( 0, len(self.data[i]) ):
				if len(self.data[i][j]) == 1:
					string += self.data[i][j][0] + "&"
				else:
					kHeight = len(self.data[i][j])
					kWidth  = []
					for k in range( 0, len(self.data[i][j]) ):
						kWidth.append( len(self.data[i][j][k]) )
					kWidthMax = max( kWidth )

					string += "\\" + "begin{tabular}{"
					string += self.rowAlignment[j] + "}"

					for k in range( 0, kHeight ):
						string += self.data[i][j][k]
						if( k != kHeight-1 ):
							string += "\\" + "\\"
					
					string += "\\" + "end{tabular}"
					string += "\\" + "\\"

		string += self.hLines[ self.size[0] ]

		string += "\\" + "end{tabular}"
		string += "\\" + "caption{" + self.title + "}"
		string += "\\" + "end{"+ self.tableAlignment+ "}"
		string += "\\" + "end{table}"

		return string;