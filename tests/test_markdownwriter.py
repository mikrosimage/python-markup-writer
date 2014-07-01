# -*- coding: utf-8 -*-

from markdownwriter import MarkdownWriter
import unittest


style = 'bold'


class TestMarkdownWriter(unittest.TestCase):

    def setUp(self):
        self.md = MarkdownWriter()

    def test_addSpace(self):
        self.md.addSpace()
        self.assertEquals(self.md.stream, ' ')

    def test_addSimpleLineBreak(self):
        self.md.addSimpleLineBreak()
        self.assertEquals(self.md.stream, '  \n')

    def test_addDoubleLineBreak(self):
        self.md.addDoubleLineBreak()
        self.assertEquals(self.md.stream, '\n \n')

    def test_addTabulation(self):
        self.md.addTabulation(9)
        self.assertEquals(self.md.stream, '>>>>>>>>>')

    def test_addHorizontalRule(self):
        self.md.addHorizontalRule()
        self.assertEquals(self.md.stream, '\n \n-----\n \n')

    def test_addHeader(self):
        self.md.addHeader('text', 6)
        self.assertEquals(self.md.stream, '###### text\n')

    def test_addHeader0(self):
        self.assertRaises(ValueError, self.md.addHeader, 'text', 0)

    def test_addHeader7(self):
        self.assertRaises(ValueError, self.md.addHeader, 'text', 7)

    def test_addParagraph(self):
        self.md.addParagraph('text', 6, style)
        self.assertEquals(self.md.stream, '>>>>>>__text__\n \n')

    def test_addParagraphNegTab(self):
        self.assertRaises(ValueError, self.md.addParagraph, 'text', -3, style)

    def test_addText(self):
        self.md.addText('text', style)
        self.assertEquals(self.md.stream, '__text__')

    def test_addList(self):
        self.md.addList(['text1', 'text2'], True, 1, style)
        self.assertEquals(self.md.stream, '>1. __text1__  \n>2. __text2__  \n')

    def test_addStringToList(self):
        self.assertRaises(ValueError, self.md.addList, 'text1', True, 1, style)

    def test_addListNegTab(self):
        self.assertRaises(
            ValueError, self.md.addList, 'text1', True, -4, style
        )

    def test_addCodeBlock1(self):
        self.md.addCodeBlock("string = \"Hello World\"")
        self.assertEquals(self.md.stream, '  \n\tstring = \"Hello World\"  \n')

    def test_addCodeBlock2(self):
        self.md.addCodeBlock(
            "string = \"Hello World\"\nprint string\nfile.open()"
        )
        self.assertEquals(
            self.md.stream,
            '  \n'
            '\tstring = \"Hello World\"  \n'
            '\tprint string  \n'
            '\tfile.open()  \n'
        )

    def test_addCodeWord(self):
        self.md.addCodeWord("string = \"Hello World\"")
        self.assertEquals(self.md.stream, '`string = \"Hello World\"`')

    def test_addLink1(self):
        self.md.addLink("URL", "TEXT")
        self.assertEquals(self.md.stream, '[TEXT](URL)')

    def test_addLink2(self):
        self.md.addLink("URL", "TEXT", "TITLE")
        self.assertEquals(self.md.stream, '[TEXT](URL \"TITLE\")')

    def test_addImage(self):
        self.md.addImage("URL", "TITLE", "TEXT")
        self.assertEquals(self.md.stream, '![Alt TEXT](URL \"TITLE\")')

    def test_getStream(self):
        self.md.addText('text', style)
        self.assertEquals(self.md.getStream(), '__text__')

    def test_getStylizedText(self):
        self.assertEquals(self.md.getStylizedText('text', style), '__text__')

    def test_transformSpecialCharacters(self):
        self.assertEquals(
            self.md.transformSpecialCharacters("* ` _ {} ! & <"),
            '\* \` \_ \{\} \! &amp; &lt;'
        )
