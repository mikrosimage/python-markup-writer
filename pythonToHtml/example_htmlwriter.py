#!/usr/bin/python
from htmlwriter import *

### INPUT ###
outputfile = "htmlTest.html"
file = open( outputfile, "w+" )

hw = HtmlWriter()

hw.addDocumentHeader()

hw.addOpeningTag( "html", "lang=\"fr\"" )

hw.addOpeningTag( "head" )
hw.addOpeningTag( "meta", "charset=\"utf-8\"", True )
hw.addTitle( "HTML WRITER")

hw.addLinkHeader( "stylesheet", "style.css" )

hw.addClosingTag( "head" )

hw.addOpeningTag( "body" )
hw.addOpeningTag( "div", "id=\"main\"" )

hw.addOpeningTag( "div", "id=\"header\"" )
hw.addHeader( "HTML Writer", 2 )
hw.addImage( "http://www.w3.org/html/logo/downloads/HTML5_Logo_512.png", "id=\"img\"" )
hw.addClosingTag( "div" )

hw.addOpeningTag( "div", "id=\"container\"" )
hw.addHeader( "Text :", 3 )
text = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
hw.addParagraph( text )
hw.addHeader( "Table :", 3 )
table = [
	["Name", "John"],
	["City", "NYC"],
	["Country", "USA"],
	["Planet", "Earth"]
]
ht = HtmlTable()
ht.setContent( table )
ht.setTitle( "Human" )
hw.addTable( ht, "table", 1 )

hw.addHeader( "List :", 3 )
stringList = [ "line1", "line2", "line3", "line4", "line5", "line6" ]
hw.addList( stringList )

hw.addClosingTag( "div" )

hw.addClosingTag( "div" )
hw.addClosingTag( "body" )


hw.addClosingTag( "html" )



### OUTPUT ###
file.write( hw.getStream() )
file.close()