import sys

class PandocMarkdownTable():
	def __init__( self ):
		self.data  = []
		self.size  = [0,0]
		self.title = ""

		self.alignementList = ['left','center','right']
		self.tableAlignement = "center"
		self.rowAlignement = []
		
		self.textStyles = ['normal','italic','bold']
		self.textColors = ['black','white','red','green','blue','cyan','magenta','yellow']
		
		self.borderStyles = ['none','out','frame','header','doubleheader']
		self.vLines = []
		self.hLines = []
		self.image  = False


	def setContent( self, array ):
		self.data = array
		width = []
		for line in self.data:
			width.append( len(line) )
		self.size = [ len( self.data ), max(width) ]
		for i in range(0, self.size[1]):
			self.rowAlignement.append('c')

	def setTitle( self, title ):
		self.title = title

	def setTableAlignement( self, alignement ):
		if alignement == self.alignementList[0] :
			self.tableAlignement = 'flushleft'
		elif alignement == self.alignementList[1] :
			self.tableAlignement = 'center'
		elif alignement == self.alignementList[2] :
			self.tableAlignement = 'flushright'
		else:
			raise ValueError("alignement not available, possible values are: " + ", ".join(self.alignementList) )


	def setBorders( self, borderStyle ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")

		if   borderStyle == self.borderStyles[1]: #out
			self.vLines.append('|')
			for i in range(0, self.size[1]):
				self.vLines.append('')			
			self.vLines[ self.size[1] ] = '|'

			self.hLines.append(' \hline ')
			for i in range(0, self.size[0]):
				self.hLines.append('')			
			self.hLines[ self.size[0] ] = ' \hline '

		elif borderStyle == self.borderStyles[2]: #frame
			for i in range(0, self.size[1]+1):
				self.vLines.append('|')
			for i in range(0, self.size[0]+1):
				self.hLines.append(' \hline ')

		elif borderStyle == self.borderStyles[3]: #header
			self.vLines.append('|')
			for i in range(0, self.size[1]):
				self.vLines.append('')			
			self.vLines[ self.size[1] ] = '|'

			self.hLines.append(' \hline ')
			self.hLines.append(' \hline ')
			for i in range(1, self.size[0]):
				self.hLines.append('')			
			self.hLines[ self.size[0] ] = ' \hline '

		elif borderStyle == self.borderStyles[4]: #doubleheader
			self.vLines.append('|')
			self.vLines.append('|')
			for i in range(1, self.size[1]):
				self.vLines.append('')			
			self.vLines[ self.size[1] ] = '|'

			self.hLines.append(' \hline ')
			self.hLines.append(' \hline ')
			for i in range(1, self.size[0]):
				self.hLines.append('')			
			self.hLines[ self.size[0] ] = ' \hline '

		elif borderStyle != self.borderStyles[0] :
				raise ValueError("cell style is not available, possible values are: " + ", ".join(self.borderStyles) )		


	def setCellStyle( self, line, row, textStyle ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if line > self.size[0] or line < 0 :
			raise ValueError("line value not valid")
		if row  > self.size[1] or row  < 0 :
			raise ValueError("row value not valid")

		if textStyle == self.textStyles[1]:
			self.data[line][row] = "\\"+"textit{"+ self.data[line][row] +"}"
		elif textStyle == self.textStyles[2]:
			self.data[line][row] = "\\"+"textbf{"+ self.data[line][row] +"}"
		elif textStyle != self.textStyles[0] :
			raise ValueError("cell style is not available, possible values are: " + ", ".join(self.textStyles) )

	def setTextColor( self, line, row, color ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if line > self.size[0] or line < 0 :
			raise ValueError("line value not valid")
		if row  > self.size[1] or row  < 0 :
			raise ValueError("row value not valid")

		if self.textColors.count(color) == 0:
			raise ValueError("cell style is not available, possible values are: " + ", ".join(self.textColors) )
		self.data[line][row] = "\\ "+"{"+"\\"+"color{"+color+"}"+self.data[line][row]+"}"

	def setRowAlignement( self, row, alignement ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if row > self.size[1] or row < 0 :
			raise ValueError("row value not valid")
		
		if alignement == self.alignementList[0] :
			self.rowAlignement[row] = 'l'
		elif alignement == self.alignementList[1] :
			self.rowAlignement[row] = 'c'
		elif alignement == self.alignementList[2] :
			self.rowAlignement[row] = 'r'
		else:
			raise ValueError("alignement not available, possible values are: " + ", ".join(self.alignementList) )


	def addImage( self, imagePath, line, row, scale=1 ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if line > self.size[0] or line < 0 :
			raise ValueError("line value not valid")
		if row  > self.size[1] or row  < 0 :
			raise ValueError("row value not valid")

		self.data[line][row] = " \\" + "includegraphics{" + imagePath + "} "


	def getTable( self ):
		string = ""
		if len( self.data ) == 0 :
			raise ValueError("setData() before getTable()")
		
		print self.image
		string += "\\" + "begin{table}[h]"
		string += "\\" + "begin{"+ self.tableAlignement+ "}"
		string += "\\" + "begin{tabular}{"

		for i in range(0, self.size[1]):
			string += self.vLines[i]
			string += self.rowAlignement[i]
		string += self.vLines[ self.size[1] ]
		string += "}"
		
		for i in range(0, self.size[0]) :
			string += self.hLines[i]
			j=0
			while j!=len(self.data[i])-1:

				string += self.data[i][j] + "&"
				j+=1
			string += self.data[i][j] + "\\" + "\\"
		string += self.hLines[ self.size[0] ]

		string += "\\" + "end{tabular}"
		string += "\\" + "caption{" + self.title + "}"
		string += "\\" + "end{"+ self.tableAlignement+ "}"
		string += "\\" + "end {table} "
		return string;