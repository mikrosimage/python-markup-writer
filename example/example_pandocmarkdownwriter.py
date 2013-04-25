#!/usr/bin/python
from pandocmarkdownwriter import *

### INPUT ###
outputfile = "pandocmarkdownTest.md"
file = open( outputfile, "w+" )

pmd = PandocMarkdownWriter()

### HEADER ###
pmd.addHeader( "PDF generated with MarkdownPandocWriter and Pandoc", 2)

## PARAGRAPH ###
pmd.addHeader( "Paragraph :", 3)
paragraph = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

pmd.addParagraph( paragraph, 0 )
pmd.addSimpleLineBreak()

### TABLE ###
pmd.addHeader( "Table :", 3)

array = []
for i in range(0,3):
	line = []
	row1 = []
	row2 = []
	row1.append("Row 1 of line " + str(i) )
	row2.append( "line 1 within row 2 of line " + str(i) )
	row2.append( "line 1 within row 2 of line " + str(i) )
	row2.append( "line 1 within row 2 of line " + str(i) )
	line.append( row1 )
	line.append( row2 )
	array.append( line )

# array = [
# 	['Numbers', 'Characters', 'Days'],
# 	['1', 'a', 'Monday'],
# 	['23', 'b', 'Tuesday'],
# 	['456', 'c', 'Wednesday']
# ]

t = PandocMarkdownTable()

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

pmd.addTable( t )

### IMAGE ###
# pmd.addHeader( "Image :", 3)
# pmd.addImage( "logo.png", "Markdown", "Markdown logo" )

### OUTPUT ###
file.write( pmd.getStream() )
file.close()
