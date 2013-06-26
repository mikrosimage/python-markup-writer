#!/usr/bin/python
from latexwriter import *

### INPUT ###
outputfile = "latexTest.tex"
file = open( outputfile, "w+" )

lw = LatexWriter()

lw.setDocumentClass( "report" )
lw.beginDocument()

### HEADER ###
for i in range(1,8):
	lw.addHeader( "Header " + str(i), i)

### PARAGRAPH ###
paragraph = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

lw.addParagraph( paragraph, 0 )
lw.addSimpleLineBreak()
lw.addParagraph( paragraph, 1, False )
lw.addSimpleLineBreak()
lw.addParagraph( paragraph, 2, True )
lw.addSimpleLineBreak()

specialString = "* ` _ {} [] () # + - . ! & <"
# lw.addParagraph( specialString, 0 )

### TABLE ###
lw.addHeader( "Table :", 3)

# array = [
# 	['File bloc id', 'RIFF'],
# 	['File size', '221018'],
# 	['Riff type id', 'WAVE'],
# 	['Specific WAVE Chunks', 
# 		[
# 			['Format sub-chunk (valid) :',
# 			'gsrlsergjhrfgh rdgsrfv :'],
# 			['~ ~ Sub-chunk size : 16', 
# 			'~ ~ Compression code : 1', 
# 			'~ ~ Number of channels : 1', 
# 			'~ ~ Sample rate : 8000', 
# 			'~ ~ Bytes per second : 16000', 
# 			'~ ~ Byte per block : 2', 
# 			'~ ~ Bits per sample : 16'], 
# 		],
# 		[
# 			['Data sub-chunk (valid) :'], 
# 			['~ ~ Sub-chunk size : 220982']
# 		]
# 	]
# ]
array = [
	['Numbers', 'Characters', 'Days'],
	['1', 'a', 'Monday'],
	['23', 'b', 'Tuesday'],
	['456', 'c', 'Wednesday']
]

t = LatexTable()

t.setTitle('This is an example')
t.setContent( array )

t.setCellStyle( 0, 0, 'bold')
t.setCellStyle( 0, 1, 'bold')
t.setCellStyle( 2, 0, 'bold')
t.setTextColor( 0, 0, 'red')
t.setTextColor( 1, 1, 'blue')
t.setRowAlignment( 1, 'right')
t.setRowAlignment( 0, 'left')
t.setBorders('frame')
# t.addImage( "little_logo.png", 1, 0 )
t.setTableAlignment('left')

lw.addTable( t )

### TEXT ###
lw.addSimpleLineBreak()
lw.addText( "Texte normal" )
lw.addSpace()
lw.addText( "Texte italic", 'italic' )
lw.addSpace()
lw.addText( "Texte gras", 'bold' )
lw.addDoubleLineBreak()
lw.addText( paragraph )
lw.addDoubleLineBreak()

### LIST ###
liste = ['mot 1','mot 2','mot 3','mot 4']
lw.addList( liste, True, 1 )

### LINK ###
lw.addText( "Here is the link : " )
lw.addLink( "http://www.google.fr", "Google" )
lw.addSimpleLineBreak()

lw.addHorizontalRule()

### IMAGE ###
lw.addImage( "logo.png", 0.5 )

lw.addSimpleLineBreak()


lw.endDocument()

### OUTPUT ###
file.write( lw.getStream() )
file.close()
