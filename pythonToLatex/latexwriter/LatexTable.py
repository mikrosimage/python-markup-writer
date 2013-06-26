class LatexTable():
	def __init__( self ):
		self.data  = []
		self.size  = [0,0]
		self.title = ""

		self.alignmentList = ['left','center','right']
		self.tableAlignment = "center"
		self.rowAlignment = []
		
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

			self.hLines[0] = ' \hline \n\t'
			for i in range(1, self.size[0]):
				self.hLines[i] = ''			
			self.hLines[ self.size[0] ] = ' \hline \n\t'

		elif borderStyle == self.borderStyles[2]: #frame
			for i in range(0, self.size[1]+1):
				self.vLines[i] = '|'
			for i in range(0, self.size[0]+1):
				self.hLines[i] = ' \hline \n\t'

		elif borderStyle == self.borderStyles[3]: #header
			# self.vLines[0] = '|'
			# for i in range(1, self.size[1]):
			# 	self.vLines[i] = ''		
			# self.vLines[ self.size[1] ] = '|'

			# self.hLines[0] = ' \hline \n\t'
			self.hLines[1] = ' \hline \n\t'
			# for i in range(2, self.size[0]):
			# 	self.hLines[i] = ''			
			# self.hLines[ self.size[0] ] = ' \hline \n\t'

		elif borderStyle == self.borderStyles[4]: #closedHeader
			self.vLines[0] = '|'
			for i in range(1, self.size[1]):
				self.vLines[i] = ''		
			self.vLines[ self.size[1] ] = '|'

			self.hLines[0] = ' \hline \n\t'
			self.hLines[1] = ' \hline \n\t'
			for i in range(2, self.size[0]):
				self.hLines[i] = ''			
			self.hLines[ self.size[0] ] = ' \hline \n\t'

		elif borderStyle == self.borderStyles[5]: #doubleHeader
			self.vLines[0] = '|'
			self.vLines[1] = '|'
			for i in range(2, self.size[1]):
				self.vLines[i] = ''			
			self.vLines[ self.size[1] ] = '|'

			self.hLines[0] = ' \hline \n\t'
			self.hLines[1] = ' \hline \n\t'
			for i in range(2, self.size[0]):
				self.hLines[i] = ''			
			self.hLines[ self.size[0] ] = ' \hline \n\t'

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
			if type( self.data[line][row] ) is not list :
				self.data[line][row] = "\\"+"textit{"+ self.data[line][row] +"}"
			else:
				for k in range( 0, len( self.data[line][row] ) ):
					self.data[line][row][k] = "\\"+"textit{"+ self.data[line][row][k] +"}"
		elif textStyle == self.textStyles[2]:
			if type( self.data[line][row] ) is not list :
				self.data[line][row] = "\\"+"textbf{"+ self.data[line][row] +"}"
			else:
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

		if type( self.data[line][row] ) is not list :
			if self.data[line][row].count( '{\color{') :
				for textColor in self.textColors :
					if self.data[line][row].count( textColor ) :
						self.data[line][row] = self.data[line][row].replace( textColor, color )
			else:
				self.data[line][row] = "{"+"\\"+"color{"+color+"}"+self.data[line][row]+"}"
		else:
			for k in range( 0, len( self.data[line][row] ) ):
				if self.data[line][row][k].count( '{\color{') :
					for textColor in self.textColors :
						if self.data[line][row][k].count( textColor ) :
							self.data[line][row][k] = self.data[line][row][k].replace( textColor, color )
				else:
					self.data[line][row][k] = "{"+"\\"+"color{"+color+"}"+self.data[line][row][k]+"}"

	def setRowAlignment( self, row, alignment, fill=False ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if row > self.size[1]-1 or row < 0 :
			raise ValueError("row value not valid")
		
		self.rowAlignment[row] = ""

		if fill :
			self.rowAlignment[row] += "@{\\extracolsep{\\fill}}"

		if alignment == self.alignmentList[0] :
			self.rowAlignment[row] += 'l'
		elif alignment == self.alignmentList[1] :
			self.rowAlignment[row] += 'c'
		elif alignment == self.alignmentList[2] :
			self.rowAlignment[row] += 'r'
		elif alignment[0] == 'p' or alignment[0] == 'm' or alignment[0] == 'b' :
			self.rowAlignment[row] += alignment + " "
		else :
			raise ValueError("alignment not available, possible values are: " + ", ".join(self.alignmentList) )


	def addImage( self, imagePath, line, row ):
		if self.size == [0,0]:
			raise ValueError("setContent() before")
		if line > self.size[0]-1 or line < 0 :
			raise ValueError("line value not valid")
		if row  > self.size[1]-1 or row  < 0 :
			raise ValueError("row value not valid")

		if type( self.data[line][row] ) is not list :
			self.data[line][row] = " \\" + "includegraphics{" + imagePath + "} "
		else:
			self.data[line][row][0] = " \\" + "includegraphics{" + imagePath + "} "

	def getTable( self, longTable=False, width="", title=False ):
		string = ""
		if len( self.data ) == 0 :
			raise ValueError("setContent() before getTable()")
		
		if title :
			string += "\\" + "begin{table}[h]\n"
			string += "\\" + "caption{" + self.title + "}\n"

		string += "\\" + "begin{"+ self.tableAlignment+ "}\n"

		if width == "" :
			if longTable == False :
				string += "\t\\" + "begin{tabular}{"
			else :
				string += "\t\\" + "begin{longtable}{"
		else :
			if longTable == False :
				string += "\t\\" + "begin{tabular*}{" + width + "}{"
			else :
				string += "\t\\" + "begin{longtabu} to " + width + " {"

		for i in range(0, self.size[1]) :	# columns
			string += self.vLines[i]
			string += self.rowAlignment[i]
		string += self.vLines[ self.size[1] ]
		string += "}\n\t"
		
		for i in range(0, self.size[0]) :	# lines
			string += self.hLines[i]
			for j in range( 0, len(self.data[i]) ):
				if type( self.data[i][j] ) is not list:		# data is not a list (string)
					if self.data[i][j] == "[...]" :
						string += "\\textit{ " + self.data[i][j] + "}"
					else :
						string += self.data[i][j]
					if j != len(self.data[i])-1 :
						string += " & "

				elif len(self.data[i][j]) == 0 :			# data is an empty list
					string += "\\textit{ - DATA - }"
					if j != len(self.data[i])-1 :
						string += " & "

				elif len(self.data[i][j]) == 1 :			# data is a list of one element
					string += self.data[i][j][0]
					if j != len(self.data[i])-1 :
						string += " & "
				else:										# data is a list of several elements
					kHeight = len(self.data[i][j])
					kWidth  = []

					for k in range( 0, len(self.data[i][j]) ):
						kWidth.append( len(self.data[i][j][k]) )
					if len( kWidth ) > 0 :
						kWidthMax = max( kWidth )

					string += "\\" + "begin{tabular}{"
					string += "l"*kWidthMax + "}\n"
					# string += self.rowAlignment[j] + "}"

					for k in range( 0, kHeight ):
						if type( self.data[i][j][k] ) is str or type( self.data[i][j][k] ) is unicode :
							string += self.data[i][j][k]

						elif type( self.data[i][j][k] ) is list :
							for l in range( 0, kWidthMax ):
								string += self.data[i][j][k][l]
								if l != kWidthMax-1 :
									string += " & "

						if k != kHeight-1 :
							string += "\\" + "\\\n"
					
					string += "\n\\" + "end{tabular}"
					if j != len(self.data[i])-1 :
						string += " & "

			string += " \\" + "\\" + "\n\t"

		string += self.hLines[ self.size[0] ]

		if width == "" :
			if longTable == False :
				string += "\\" + "end{tabular}\n"
			else :
				string += "\\" + "end{longtable}\n"
		else :
			if longTable == False :
				string += "\\" + "end{tabular*}\n"
			else :
				string += "\\" + "end{longtabu}\n"

		string += "\\" + "end{"+ self.tableAlignment+ "}\n"

		if title :
			string += "\\" + "end{table}\n"

		return string;