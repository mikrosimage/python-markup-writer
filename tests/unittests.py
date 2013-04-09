from markdownwriter import *
from nose.tools import *

def test_addSpace():
	md = MarkdownWriter()
	md.addSpace()
	assert md.stream == ' '

def test_addSimpleLineBreak():
	md = MarkdownWriter()
	md.addSimpleLineBreak()
	assert md.stream == '  \n'

def test_addDoubleLineBreak():
	md = MarkdownWriter()
	md.addDoubleLineBreak()
	assert md.stream == '\n \n'

def test_addTabulation():
	md = MarkdownWriter()
	md.addTabulation(9)
	assert md.stream == '>>>>>>>>>'

def test_addHorizontalRule():
	md = MarkdownWriter()
	md.addHorizontalRule()
	assert md.stream == '\n \n-----\n \n'


def test_addHeader():
	md = MarkdownWriter()
	md.addHeader('text', 6)
	assert md.stream == '###### text\n'

@raises(Exception)
def test_addHeader0():
	md = MarkdownWriter()
	md.addHeader('text', 0)
	assert md.stream == '###### text\n'

@raises(Exception)
def test_addHeader7():
	md = MarkdownWriter()
	md.addHeader('text', 7)
	assert md.stream == '###### text\n'


style = 'bold'


def test_addParagraph():
	md = MarkdownWriter()
	md.addParagraph('text', 6, style)
	assert md.stream == '>>>>>>__text__\n \n'

@raises(Exception)
def test_addParagraphNegTab():
	md = MarkdownWriter()
	md.addParagraph('text', -3, style)
	assert md.stream == '>>>>>>__text__\n \n'


def test_addText():
	md = MarkdownWriter()
	md.addText('text', style)
	assert md.stream == '__text__'


def test_addList():
	md = MarkdownWriter()
	md.addList(['text1', 'text2'], True, 1, style)
	assert md.stream == '>1. __text1__  \n>2. __text2__  \n'

@raises(Exception)
def test_addStringToList():
	md = MarkdownWriter()
	md.addList('text1', True, 1, style)
	assert md.stream == '>1. __text1__  \n>2. __text2__  \n'

@raises(Exception)
def test_addListNegTab():
	md = MarkdownWriter()
	md.addList('text1', True, -4, style)
	assert md.stream == '>1. __text1__  \n>2. __text2__  \n'


def test_addCodeBlock():
	md = MarkdownWriter()
	# md.addCodeBlock("string = \"Hello World\"")
	# assert md.stream == '  \n\tstring = \"Hello World\"  \n'
	md.addCodeBlock("string = \"Hello World\"\nprint string\nfile.open()")
	assert md.stream == '  \n\tstring = \"Hello World\"  \n\tprint string  \n\tfile.open()  \n'

def test_addCodeWord():
	md = MarkdownWriter()
	md.addCodeWord("string = \"Hello World\"")
	assert md.stream == '`string = \"Hello World\"`'

def test_addLink():
	md = MarkdownWriter()
	md.addLink("URL","TEXT")
	assert md.stream == '[TEXT](URL)'
	# md.addLink("URL","TEXT", "TITLE")
	# assert md.stream == '[TEXT](URL \"TITLE\")'

def test_addImage():
	md = MarkdownWriter()
	md.addImage("URL","TITLE", "TEXT")
	assert md.stream == '![Alt TEXT](URL \"TITLE\")'

def test_getStream():
	md = MarkdownWriter()
	md.addText('text', style)
	assert md.getStream() == '__text__'

def test_getStylizedText():
	md = MarkdownWriter()
	assert md.getStylizedText( 'text', style) == '__text__'

def test_transformSpecialCharacters():
	md = MarkdownWriter()
	assert md.transformSpecialCharacters( "* ` _ {} ! & <" ) == '\* \` \_ \{\} \! &amp; &lt;'