from HtmlTable import *

class HtmlWriter():
	def __init__( self, stream="" ):
		self.stream = stream
		self.textStyles = ['normal','italic','bold']

	def getStream( self ):
		return self.stream;

	def getStylizedText( self, text, textStyle ):
		string = ""
		if textStyle != self.textStyles[0] :
			if textStyle == self.textStyles[1]:
				string += "<i>" + text + "</i>"
			elif textStyle == self.textStyles[2]:
				string += "<strong>" + text + "</strong>"
			else:
				raise ValueError("text style is not available, possible values are: " + ", ".join(self.textStyles) )
		else:
			string = text
		return string;

	def addDocumentHeader( self ):
		self.stream += "<!DOCTYPE html>\n"

	def addTitle( self, title ):
		if type( title ) is not str :
			raise ValueError("request a 'str' object for tagName")
		self.stream += "<title>"
		self.stream += title
		self.stream += "</title>"

	def addScriptHeader( self, src, type="" ):
		self.stream += "<script"
		if type != "" :
			self.stream += " type=\"" + type +"\""
		self.stream += " src=\"" + src + "\"></script>\n"

	def addScript( self, script, type="" ):
		# if type( script ) is not str :
		# 	raise ValueError( "request a 'str' object for script" )
		self.stream += "<script"
		if type != "" :
			self.stream += " type=\"" + type +"\""
		self.stream += ">\n"
		self.stream += script
		self.stream += "\n</script>\n"

	def addLinkHeader( self, rel, href ):
		self.stream += "<link"
		self.stream += " rel=\"" + rel +"\""
		self.stream += " href=\"" + href + "\"/>\n"

	def addOpeningTag( self, tagName, htmlAttr="", empty=False ):
		if type( tagName ) is not str :
			raise ValueError("request a 'str' object for tagName")
		# if tagName != transformSpecialCharacters( tagName ) :
		# 	raise ValueError("request a string without special characters for tagName")
		self.stream += "<" + tagName 
		if htmlAttr != "" :
			self.stream += " " + htmlAttr + " " 
		if empty :
			self.stream += "/" 
		self.stream += ">\n"

	def addClosingTag( self, tagName ):
		if type( tagName ) is not str :
			raise ValueError("request a 'str' object for tagName")
		# if tagName != transformSpecialCharacters( tagName ) :
		# 	raise ValueError("request a string without special characters for tagName")
		self.stream += "</" + tagName + ">\n"

	def addRawHtml( self, rawHtml ):
		if not isinstance(rawHtml, str) :
			raise ValueError("request a 'str' object for rawHtml")
		self.stream += rawHtml + "\n"

	def addHeader( self, text, level ):
		self.stream += "<h" + str(level) + ">" + text + "</h" + str(level) + ">\n"

	def addParagraph( self, text, textStyle='normal' ):	
		self.stream += "<p>"
		self.stream += self.getStylizedText( transformSpecialCharacters( text ), textStyle )
		self.stream += "</p>\n"

	def addText( self, text, textStyle='normal'):
		self.stream += "<a>"
		self.stream += self.getStylizedText( transformSpecialCharacters( text ), textStyle )
		self.stream += "</a>"

	def addList( self, text, textStyle='normal' ):
		if type(text) is not list:
			raise ValueError("request a list of string")
		self.stream += "<ul>\n"
		for line in text :
			self.stream += "<li>"
			self.addText( line, textStyle )
			self.stream += "</li>\n"
		self.stream += "</ul>\n"

	def addLink( self, linkUrl, linkText="" ):
		self.stream += "<a href=\"" + linkUrl + "\">"
		if linkText != "" :
			self.stream += transformSpecialCharacters( linkText )
		else :
			self.stream += linkUrl
		self.stream += "</a>"

	def addTable( self, table, id="", border="" ):
		if not isinstance(table, HtmlTable):
			raise ValueError("request a 'HtmlTable' object")
		self.stream += table.getTable( id, border )

	def addImage( self, src, htmlAttr="" ):
		if type( src ) is not str :
			raise ValueError("request a 'str' object for src")
		self.stream += "<image "
		if htmlAttr != "" :
			self.stream += htmlAttr + " " 
		self.stream += "src=\"" + src + "\"></image>"