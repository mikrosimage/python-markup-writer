#!/usr/bin/python
from markdownpandocwriter import *

### INPUT ###
outputfile = "markdownpandocTest.md"
file = open( outputfile, "w+" )

mpd = MarkdownPandocWriter()

### HEADER ###
mpd.addHeader( "PDF generated with MarkdownPandocWriter and Pandoc", 2)

## PARAGRAPH ###
mpd.addHeader( "Paragraph :", 3)
paragraph = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

mpd.addParagraph( paragraph, 0 )
mpd.addSimpleLineBreak()

### TABLE ###
mpd.addHeader( "Table :", 3)
array = [
	['Numbers', 'Characters', 'Days'],
	['1', 'a', 'Monday'],
	['2', 'b', 'Tuesday'],
	['3', 'c', 'Wednesday']
]

mpd.addTable( array )
mpd.addSimpleLineBreak()

### IMAGE ###
mpd.addHeader( "Image :", 3)
mpd.addImage( "logo.png", "Markdown", "Markdown logo" )

### OUTPUT ###
file.write( mpd.getStream() )
file.close()
