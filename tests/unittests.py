from markdownwriter import *
from pandocmarkdownwriter import *
from nose.tools import *

### MARKDOWNWRITER TESTS ###
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

@raises(Exception)
def test_addHeader7():
	md = MarkdownWriter()
	md.addHeader('text', 7)


style = 'bold'


def test_addParagraph():
	md = MarkdownWriter()
	md.addParagraph('text', 6, style)
	assert md.stream == '>>>>>>__text__\n \n'

@raises(Exception)
def test_addParagraphNegTab():
	md = MarkdownWriter()
	md.addParagraph('text', -3, style)


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

@raises(Exception)
def test_addListNegTab():
	md = MarkdownWriter()
	md.addList('text1', True, -4, style)


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


### PANDOCMARKDOWNTABLE TESTS ###

def test_setContentData():
	table = PandocMarkdownTable()
	array = [['test']]
	table.setContent(array)
	assert table.data == [['test']]


def test_setContentSize():
	table = PandocMarkdownTable()
	array = [['test']]
	table.setContent(array)
	assert table.size == [1,1]

def test_setContentAlignment():
	table = PandocMarkdownTable()
	array = [['test']]
	table.setContent(array)
	assert table.rowAlignment == ['c']

@raises(Exception)
def test_setContentArrayType1():
	table = PandocMarkdownTable()
	array = ['test']
	table.setContent(array)

@raises(Exception)
def test_setContentArrayType2():
	table = PandocMarkdownTable()
	array = 'test'
	table.setContent(array)


def test_setTitle():
	table = PandocMarkdownTable()
	table.setTitle('title test')
	assert table.title == 'title test'


def test_setTableAlignment():
	table = PandocMarkdownTable()
	table.setTableAlignment('left')
	assert table.tableAlignment == 'flushleft'
	table.setTableAlignment('center')
	assert table.tableAlignment == 'center'
	table.setTableAlignment('right')
	assert table.tableAlignment == 'flushright'

@raises(Exception)
def test_setTableAlignmentOther():
	table = PandocMarkdownTable()
	table.setTableAlignment('other')



def initPancodeMarkdownTable():
	table = PandocMarkdownTable()
	array = [['test','test','test'],
			 ['test','test','test'],
			 ['test','test','test']]
	table.setContent(array)
	return table;

def test_setBorders():
	table = initPancodeMarkdownTable()
	table.setBorders('none')
	assert_equal(table.vLines, ['','','',''])
	assert_equal(table.hLines, ['','','',''])

	table.setBorders('out')
	assert_equal(table.vLines, ['|','','','|'])
	assert_equal(table.hLines, [' \hline ','','',' \hline '])

	table.setBorders('frame')
	assert_equal(table.vLines, ['|','|','|','|'])
	assert_equal(table.hLines, [' \hline ',' \hline ',' \hline ', ' \hline '])

	table.setBorders('header')
	assert_equal(table.vLines, ['|','','','|'])
	assert_equal(table.hLines, [' \hline ',' \hline ','',' \hline '])
	
	table.setBorders('doubleheader')
	assert_equal(table.vLines, ['|','|','','|'])
	assert_equal(table.hLines, [' \hline ',' \hline ','',' \hline '])

@raises(Exception)
def test_setBordersOther():
	table = initPancodeMarkdownTable()
	table.setBorders('other')

@raises(Exception)
def test_setBordersNoContent():
	table = PandocMarkdownTable()
	array = [['test','test','test'],
			 ['test','test','test'],
			 ['test','test','test']]
	table.setBorders('none')


def test_setCellStyleNormal():
	table = initPancodeMarkdownTable()
	table.setCellStyle(1,1,'normal')
	assert table.data[1][1] == 'test'

def test_setCellStyleItalic():
	table = initPancodeMarkdownTable()
	table.setCellStyle(1,1,'italic')
	assert table.data[1][1] == '\\textit{test}'

def test_setCellStyleBold():
	table = initPancodeMarkdownTable()
	table.setCellStyle(1,1,'bold')
	assert table.data[1][1] == '\\textbf{test}'

def test_setCellStyleItalicBold():
	table = initPancodeMarkdownTable()
	table.setCellStyle(1,1,'italic')
	table.setCellStyle(1,1,'bold')
	assert table.data[1][1] == '\\textbf{\\textit{test}}'

def test_setCellStyleBoldItalic():
	table = initPancodeMarkdownTable()
	table.setCellStyle(1,1,'bold')
	table.setCellStyle(1,1,'italic')
	assert table.data[1][1] == '\\textit{\\textbf{test}}'	

@raises(Exception)
def test_setCellStyleOther():
	table = initPancodeMarkdownTable()
	table.setCellStyle(1,1,'other')

@raises(Exception)
def test_setCellStyleOutRange1():
	table = initPancodeMarkdownTable()
	table.setCellStyle(3,3,'normal')

@raises(Exception)
def test_setCellStyleOutRange2():
	table = initPancodeMarkdownTable()
	table.setCellStyle(-1,-1,'normal')

@raises(Exception)
def test_setCellStyleNoContent():
	table = PandocMarkdownTable()
	array = [['test','test','test'],
			 ['test','test','test'],
			 ['test','test','test']]
	table.setCellStyle(1,1,'normal')


def test_setTextColorBlack():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'black')
	assert_equal(table.data[1][1], '\\ {\\color{black}test}') 

def test_setTextColorWhite():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'white')
	assert_equal(table.data[1][1], '\\ {\\color{white}test}')

def test_setTextColorRed():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'red')
	assert_equal(table.data[1][1], '\\ {\\color{red}test}')

def test_setTextColorGreen():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'green')
	assert_equal(table.data[1][1], '\\ {\\color{green}test}')

def test_setTextColorBlue():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'blue')
	assert_equal(table.data[1][1], '\\ {\\color{blue}test}')

def test_setTextColorCyan():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'cyan')
	assert_equal(table.data[1][1], '\\ {\\color{cyan}test}')

def test_setTextColorMagenta():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'magenta')
	assert_equal(table.data[1][1], '\\ {\\color{magenta}test}')

def test_setTextColorYellow():
	table = initPancodeMarkdownTable()
	table.setTextColor(1,1,'yellow')
	assert_equal(table.data[1][1], '\\ {\\color{yellow}test}')

def test_setTextColorOtherAndOutRange():
	table = initPancodeMarkdownTable()
	assert_raises( Exception, table.setTextColor,  1,  1, 'other' )
	assert_raises( Exception, table.setTextColor,  3,  3, 'normal' )
	assert_raises( Exception, table.setTextColor, -1, -1, 'normal')

def test_setTextColorNoContent():	
	table = PandocMarkdownTable()
	assert_raises( Exception, table.setTextColor, 1, 1, 'normal' )