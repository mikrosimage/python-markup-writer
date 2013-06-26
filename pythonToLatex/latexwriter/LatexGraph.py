from LatexPlot import *

class LatexGraph():
	def __init__( self, title="" ):
		self.curves         = []
		self.title          = title
		self.maxCurveLength = 0

	def addCurve( self, curve ):
		# if type( curves ) is not list :
		# 	raise ValueError( "list of LatexPlot expected" )
		# for curve in curves
		if not isinstance( curve, LatexPlot ):
			raise ValueError( "LatexPlot expected" )
		else :
			self.curves.append( curve )
			if len( curve.coordinates ) > self.maxCurveLength :
				self.maxCurveLength = len( curve.coordinates )

	def setTitle( self, title ):		
		self.title = title

	def getGraph( self, rawWidth="", xLabel="", yLabel="", xUnit="", yUnit="", xScale=1, yScale=0.4, yMax=0, yMin=-70, xMin=0 ):
		latexString = ""
		if len( self.curves ) == 0 :
			raise ValueError("addCurve() before getGraph()")

		latexString += "\\begin{tikzpicture}[x=" + str(xScale) + "cm,y=" + str(yScale) + "cm]\n"

		if len( rawWidth ) > 0 :
			latexString += "\\pgfplotsset{width=" + rawWidth + "}\n"

		latexString += "\\begin{axis}[\n"
		latexString += "\ttitle=" + self.title + ",\n"

		if len( xUnit ) > 0 or len( yUnit ) > 0 :
			latexString += "\tuse units,\n"
			if len( xUnit ) > 0 :
				latexString += "\tx unit=" + xUnit + ",\n"
			if len( yUnit ) > 0 :
				latexString += "\ty unit=" + yUnit + ",\n"
		
		latexString += "\tymin=" + str(yMin) + ",\n"
		latexString += "\tymax=" + str(yMax) + ",\n"
		latexString += "\txmin=" + str(xMin) + ",\n"
		latexString += "\txmax=" + str( self.maxCurveLength ) + ",\n"
		latexString += "\txlabel=" + xLabel + ",\n"
		latexString += "\tylabel=" + yLabel + ",\n"
		latexString += "\tlegend style={cells={anchor=west}, legend pos=south east}\n"
		latexString += "]\n"

		for curve in self.curves :
			latexString += curve.getPlot()

		latexString += "\end{axis}\n"
		latexString += "\end{tikzpicture}\n"

		return latexString;