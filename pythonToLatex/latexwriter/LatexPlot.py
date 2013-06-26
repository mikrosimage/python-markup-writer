class LatexPlot():
	def __init__( self, title="", data=[] ):
		self.title       = title
		self.data        = data
		self.coordinates = []
		self.color       = ""
		self.mode        = "sharp plot"
		self.fill        = False
		self.opacity     = 0.5

	def setColor( self, color ):
		self.color = color

	def setMode( self, mode ):	# 'sharp plot', or 'smooth'
		self.mode = mode

	def setFill( self, fill ):	# boolean
		self.fill = fill

	def setOpacity( self, opacity ):
		if opacity < 0 or opacity > 1 :
			raise ValueError( "the opacity value must be between 0 and 1" )
		self.opacity = opacity

	def setTitle( self, title ):		
		self.title = title

	def setData( self, data ):
		if type( data ) is not list :
			raise ValueError( "list expected" )
		else :
			self.data = data

	def setCoordinates( self ):
		if len( self.data ) == 0 :
			raise ValueError("setData() before setCoordinates()")
		self.coordinates.append( "( 0, -70 )" )
		for i in range( 0, len( self.data ) ) :
			self.coordinates.append( "( " + str(i) + ", " + self.data[i] + " )" )
		self.coordinates.append( "( " + str( len( self.data )-1 ) + ", -70 )" )

	def getPlot( self ):
		latexString = ""

		latexString += "\\addplot["
		latexString += self.mode
		latexString += ", color=" + self.color
		if self.fill :
			latexString += ", fill, fill opacity=" + str( self.opacity )
		latexString += "]\n"

		latexString += "\tcoordinates {\n"
		for point in self.coordinates :
			latexString += "\t\t" + point + "\n"
		if self.fill :
			# latexString += "} \closedcycle;\n"
			latexString += "} --cycle;\n"
		else:
			latexString += "};\n"
		latexString += "\\addlegendentry{" + self.title + "}\n"

		return latexString;