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
array = [
	['Numbers', 'Characters', 'Days'],
	['1', 'a', 'Monday'],
	['23', 'b', 'Tuesday'],
	['456', 'c', 'Wednesday']
]

t = PandocMarkdownTable()

t.setTitle('This is an example')
t.setContent( array )
t.setCellStyle( 0, 0, 'bold')
t.setCellStyle( 0, 1, 'bold')
t.setCellStyle( 0, 2, 'bold')
t.setCellStyle( 2, 0, 'bold')
t.setCellStyle( 3, 2, 'bold')
t.setTextColor( 0, 0, 'red')
t.setTextColor( 2, 2, 'blue')
t.setTextColor( 2, 2, 'black')
t.setCellStyle( 1, 2, 'italic')
t.setTextColor( 3, 2, 'cyan')
t.setCellStyle( 3, 1, 'italic')
t.setCellStyle( 3, 2, 'italic')
t.setRowAlignment( 0, 'right')
t.setRowAlignment( 2, 'left')
t.setBorders('header')
# t.addImage( "little_logo.png", 1, 1 )
t.setTableAlignment('center')

pmd.addTable( t )

### IMAGE ###
pmd.addHeader( "Image :", 3)
pmd.addImage( "logo.png", "Markdown", "Markdown logo" )

### OUTPUT ###
file.write( pmd.getStream() )
file.close()
