#!/usr/bin/python
from markdownwriter import *

### INPUT ###
outputfile = "markdownTest.md"
file = open( outputfile, "w+" )

md = MarkdownWriter()

### HEADER ###
for i in range(1,7):
	md.addHeader( "Header " + str(i), i)

### PARAGRAPH ###
paragraph = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

md.addParagraph( paragraph, 0 )
md.addParagraph( paragraph, 1, 'italic' )
md.addParagraph( paragraph, 2, 'bold' )

specialString = "* ` _ {} [] () # + - . ! & <"
md.addParagraph( specialString, 0 )

### TEXT ###
md.addSimpleLineBreak()
md.addText( "Texte normal" )
md.addSpace()
md.addText( "Texte italic", 'italic' )
md.addSpace()
md.addText( "Texte gras", 'bold' )
md.addDoubleLineBreak()
md.addText( paragraph )
md.addDoubleLineBreak()

### LIST ###
liste = ['mot 1','mot 2','mot 3','mot 4']
md.addListElement( liste, True, 1 )


### CODE ###
code = "a = 1\nprint a"
md.addCodeBlock( code )

md.addText( "Use the " )
md.addCodeWord( "print" )
md.addText( " function" )
md.addHorizontalRule()

### LINK ###
md.addText( "Here is the link : " )
md.addLink( "http://www.google.fr", "Google", "Clic !")

md.addHorizontalRule()

### IMAGE ###
md.addImage( "logo.png", "Markdown" )

md.addSimpleLineBreak()

### OUTPUT ###
file.write( md.getStream() )
file.close()
