from pandocmarkdownwriter import PandocMarkdownTable, PandocMarkdownWriter
import unittest


class TestPandocMarkdownTableNoContent(unittest.TestCase):

    def setUp(self):
        self.table = PandocMarkdownTable()

    def test_setContent(self):
        array = [['test']]
        self.table.setContent(array)
        self.assertEquals(self.table.data, [['test']])
        self.assertEquals(self.table.size, [1, 1])
        self.assertEquals(self.table.rowAlignment, ['c'])

        self.assertRaises(Exception, self.table.setContent, ['test'])
        self.assertRaises(Exception, self.table.setContent, 'test')

    def test_setTitle(self):
        self.table.setTitle('title test')
        self.assertEquals(self.table.title, 'title test')

    def test_setTableAlignment(self):
        self.table.setTableAlignment('left')
        self.assertEquals(self.table.tableAlignment, 'flushleft')

        self.table.setTableAlignment('center')
        self.assertEquals(self.table.tableAlignment, 'center')

        self.table.setTableAlignment('right')
        self.assertEquals(self.table.tableAlignment, 'flushright')

        self.assertRaises(ValueError, self.table.setTableAlignment, 'other')

    def test_setBordersNoContent(self):
        self.assertRaises(ValueError, self.table.setBorders, 'none')

    def test_setCellStyleNoContent(self):
        self.assertRaises(ValueError, self.table.setCellStyle, 1, 1, 'normal')

    def test_setTextColorNoContent(self):
        self.assertRaises(ValueError, self.table.setTextColor, 1, 1, 'normal')

    def test_setRowAlignmentNoContent(self):
        self.assertRaises(ValueError, self.table.setRowAlignment, 1, 'center')

    def test_getTableNoContent(self):
        self.assertRaises(ValueError, self.table.getTable)

    def test_addImageNoContent(self):
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH", 1, 1)

    def test_setBordersNoContentArrayTable(self):
        self.assertRaises(ValueError, self.table.setBorders, 'none')

    def test_getTableNoContentArrayTable(self):
        self.assertRaises(ValueError, self.table.getTable)

    def test_addImageNoContentArrayTable(self):
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH", 1, 1)

    def test_setRowAlignmentNoContentArrayTable(self):
        self.assertRaises(ValueError, self.table.setRowAlignment, 1, 'center')

    def test_setCellStyleNoContentArrayTable(self):
        self.assertRaises(ValueError, self.table.setCellStyle, 1, 1, 'normal')

    def test_setTextColorNoContentArrayTable(self):
        self.assertRaises(ValueError, self.table.setTextColor, 1, 1, 'normal')


class TestPandocMarkdownableInitialized(unittest.TestCase):

    def setUp(self):
        self.table = PandocMarkdownTable()
        array = [
            ['test', 'test', 'test'],
            ['test', 'test', 'test'],
            ['test', 'test', 'test']
        ]
        self.table.setContent(array)

    def test_setBorders(self):
        self.table.setBorders('none')
        self.assertEquals(self.table.vLines, ['', '', '', ''])
        self.assertEquals(self.table.hLines, ['', '', '', ''])

        self.table.setBorders('out')
        self.assertEquals(self.table.vLines, ['|', '', '', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', '', '', r' \hline ']
        )

        self.table.setBorders('frame')
        self.assertEquals(self.table.vLines, ['|', '|', '|', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', r' \hline ', r' \hline ', r' \hline ']
        )

        self.table.setBorders('header')
        self.assertEquals(self.table.vLines, ['|', '', '', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', r' \hline ', '', r' \hline ']
        )

        self.table.setBorders('doubleheader')
        self.assertEquals(self.table.vLines, ['|', '|', '', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', r' \hline ', '', r' \hline ']
        )

    def test_setBordersOther(self):
        self.assertRaises(ValueError, self.table.setBorders, 'other')

    def test_setCellStyle1(self):
        self.table.setCellStyle(1, 1, 'normal')
        self.assertEquals(self.table.data[1][1], 'test')

    def test_setCellStyle2(self):
        self.table.setCellStyle(1, 1, 'italic')
        self.assertEquals(self.table.data[1][1], r'\textit{test}')

    def test_setCellStyle3(self):
        self.table.setCellStyle(1, 1, 'bold')
        self.assertEquals(self.table.data[1][1], r'\textbf{test}')

    def test_setCellStyle4(self):
        self.table.setCellStyle(1, 1, 'italic')
        self.table.setCellStyle(1, 1, 'bold')
        self.assertEquals(self.table.data[1][1], r'\textbf{\textit{test}}')

    def test_setCellStyle5(self):
        self.table.setCellStyle(1, 1, 'bold')
        self.table.setCellStyle(1, 1, 'italic')
        self.assertEquals(self.table.data[1][1], r'\textit{\textbf{test}}')

    def test_setCellStyle6(self):
        self.assertRaises(
            ValueError,
            self.table.setCellStyle,  1,  1, 'other'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle,  3,  3, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, -1, -1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, -1,  1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle,  1, -1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle,  3,  1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle,  1,  3, 'normal'
        )

    def test_setTextColorBlack(self):
        self.table.setTextColor(1, 1, 'black')
        self.assertEquals(self.table.data[1][1], r'{\color{black}test}')

    def test_setTextColorWhite(self):
        self.table.setTextColor(1, 1, 'white')
        self.assertEquals(self.table.data[1][1], r'{\color{white}test}')

    def test_setTextColorRed(self):
        self.table.setTextColor(1, 1, 'red')
        self.assertEquals(self.table.data[1][1], r'{\color{red}test}')

    def test_setTextColorGreen(self):
        self.table.setTextColor(1, 1, 'green')
        self.assertEquals(self.table.data[1][1], r'{\color{green}test}')

    def test_setTextColorBlue(self):
        self.table.setTextColor(1, 1, 'blue')
        self.assertEquals(self.table.data[1][1], r'{\color{blue}test}')

    def test_setTextColorCyan(self):
        self.table.setTextColor(1, 1, 'cyan')
        self.assertEquals(self.table.data[1][1], r'{\color{cyan}test}')

    def test_setTextColorMagenta(self):
        self.table.setTextColor(1, 1, 'magenta')
        self.assertEquals(self.table.data[1][1], r'{\color{magenta}test}')

    def test_setTextColorYellow(self):
        self.table.setTextColor(1, 1, 'yellow')
        self.assertEquals(self.table.data[1][1], r'{\color{yellow}test}')

    def test_setTextColorMultiple(self):
        self.table.setTextColor(1, 1, 'yellow')
        self.table.setTextColor(1, 1, 'red')
        self.assertEquals(self.table.data[1][1], r'{\color{red}test}')

    def test_setTextColorOtherAndOutRange(self):
        self.assertRaises(
            ValueError,
            self.table.setTextColor,  1,  1, 'other'
        )
        self.assertRaises(
            ValueError,
            self.table.setTextColor,  3,  3, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setTextColor, -1, -1, 'normal'
        )

    def test_setRowAlignment(self):
        self.table.setRowAlignment(0, 'left')
        self.assertEquals(self.table.rowAlignment, ['l', 'c', 'c'])

        self.table.setRowAlignment(2, 'right')
        self.assertEquals(self.table.rowAlignment, ['l', 'c', 'r'])

        self.table.setRowAlignment(0, 'center')
        self.table.setRowAlignment(1, 'right')
        self.table.setRowAlignment(2, 'left')
        self.assertEquals(self.table.rowAlignment, ['c', 'r', 'l'])

        self.assertRaises(ValueError, self.table.setRowAlignment,  1, 'other')
        self.assertRaises(ValueError, self.table.setRowAlignment, -1, 'center')
        self.assertRaises(ValueError, self.table.setRowAlignment,  3, 'center')

    def test_addImage(self):
        self.table.addImage("IMAGEPATH", 1, 1)
        self.assertEquals(
            self.table.data[1][1],
            r' \includegraphics{IMAGEPATH} '
        )

        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH", -1,  1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  1, -1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  3,  1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  3, -1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  3,  3)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH", -1, -1)

    def test_getTable(self):
        stream = self.table.getTable()
        self.assertEquals(
            stream,
            r"\begin{table}[h]\begin{center}\begin{tabular}"
            r"{ccc}test&test&test\\test&test&test\\test&test&test\\"
            r"\end{tabular}\caption{}\end{center}\end{table}"
        )


class TestPandocMarkdownArrayTable(unittest.TestCase):

    def setUp(self):
        self.table = PandocMarkdownTable()
        array = [
            [
                ['test'],
                ['test', 'test'],
                ['test']
            ],
            [
                'test',
                'test',
                'test'
            ],
            [
                'test',
                ['test', 'test'],
                ['test']
            ]
        ]
        self.table.setContent(array)

    def test_setBordersArrayTable(self):
        self.table.setBorders('none')
        self.assertEquals(self.table.vLines, ['', '', '', ''])
        self.assertEquals(
            self.table.hLines,
            ['', '', '', '']
        )

        self.table.setBorders('out')
        self.assertEquals(self.table.vLines, ['|', '', '', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', '', '', r' \hline ']
        )

        self.table.setBorders('frame')
        self.assertEquals(self.table.vLines, ['|', '|', '|', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', r' \hline ', r' \hline ', r' \hline ']
        )

        self.table.setBorders('header')
        self.assertEquals(self.table.vLines, ['|', '', '', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', r' \hline ', '', r' \hline ']
        )

        self.table.setBorders('doubleheader')
        self.assertEquals(self.table.vLines, ['|', '|', '', '|'])
        self.assertEquals(
            self.table.hLines,
            [r' \hline ', r' \hline ', '', r' \hline ']
        )

    def test_setBordersOtherArrayTable(self):
        self.assertRaises(ValueError, self.table.setBorders, 'other')

    def test_setCellStyleArrayTable(self):
        self.table.setCellStyle(0, 0, 'normal')
        self.assertEquals(self.table.data[0][0][0], 'test')
        self.table.setCellStyle(0, 1, 'normal')
        self.assertEquals(self.table.data[0][1][0], 'test')
        self.table.setCellStyle(2, 1, 'normal')
        self.assertEquals(self.table.data[2][1][1], 'test')
        self.table.setCellStyle(1, 1, 'normal')
        self.assertEquals(self.table.data[1][1], 'test')

    def test_setCellStyleArrayTableItalic(self):
        self.table.setCellStyle(0, 0, 'italic')
        self.assertEquals(self.table.data[0][0][0], r'\textit{test}')
        self.table.setCellStyle(0, 1, 'italic')
        self.assertEquals(self.table.data[0][1][0], r'\textit{test}')
        self.table.setCellStyle(2, 1, 'italic')
        self.assertEquals(self.table.data[2][1][1], r'\textit{test}')
        self.table.setCellStyle(1, 1, 'italic')
        self.assertEquals(self.table.data[1][1], r'\textit{test}')

    def test_setCellStyleArrayTableBold(self):
        self.table.setCellStyle(0, 0, 'bold')
        self.assertEquals(self.table.data[0][0][0], r'\textbf{test}')
        self.table.setCellStyle(0, 1, 'bold')
        self.assertEquals(self.table.data[0][1][0], r'\textbf{test}')
        self.table.setCellStyle(2, 1, 'bold')
        self.assertEquals(self.table.data[2][1][1], r'\textbf{test}')
        self.table.setCellStyle(1, 1, 'bold')
        self.assertEquals(self.table.data[1][1], r'\textbf{test}')

    def test_setCellStyleArrayTableItalicBold(self):
        self.table.setCellStyle(0, 0, 'italic')
        self.table.setCellStyle(0, 0, 'bold')
        self.assertEquals(self.table.data[0][0][0], r'\textbf{\textit{test}}')
        self.table.setCellStyle(0, 1, 'italic')
        self.table.setCellStyle(0, 1, 'bold')
        self.assertEquals(self.table.data[0][1][0], r'\textbf{\textit{test}}')
        self.table.setCellStyle(2, 1, 'italic')
        self.table.setCellStyle(2, 1, 'bold')
        self.assertEquals(self.table.data[2][1][1], r'\textbf{\textit{test}}')
        self.table.setCellStyle(1, 1, 'italic')
        self.table.setCellStyle(1, 1, 'bold')
        self.assertEquals(self.table.data[1][1],    r'\textbf{\textit{test}}')

    def test_setCellStyleArrayTableBoldItalic(self):
        self.table.setCellStyle(0, 0, 'bold')
        self.table.setCellStyle(0, 0, 'italic')
        self.assertEquals(self.table.data[0][0][0], r'\textit{\textbf{test}}')
        self.table.setCellStyle(0, 1, 'bold')
        self.table.setCellStyle(0, 1, 'italic')
        self.assertEquals(self.table.data[0][1][0], r'\textit{\textbf{test}}')
        self.table.setCellStyle(2, 1, 'bold')
        self.table.setCellStyle(2, 1, 'italic')
        self.assertEquals(self.table.data[2][1][1], r'\textit{\textbf{test}}')
        self.table.setCellStyle(1, 1, 'bold')
        self.table.setCellStyle(1, 1, 'italic')
        self.assertEquals(self.table.data[1][1],    r'\textit{\textbf{test}}')

    def test_setCellStyleArrayTableOther(self):
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, 1, 1, 'other'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, 3, 3, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, -1, -1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, -1, 1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, 1, -1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, 3, 1, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setCellStyle, 1, 3, 'normal'
        )

    def test_setTextColorBlackArrayTable(self):
        self.table.setTextColor(0, 0, 'black')
        self.assertEquals(self.table.data[0][0][0], r'{\color{black}test}')
        self.table.setTextColor(0, 1, 'black')
        self.assertEquals(self.table.data[0][1][0], r'{\color{black}test}')
        self.table.setTextColor(2, 1, 'black')
        self.assertEquals(self.table.data[2][1][1], r'{\color{black}test}')
        self.table.setTextColor(1, 1, 'black')
        self.assertEquals(self.table.data[1][1], r'{\color{black}test}')

    def test_setTextColorWhiteArrayTable(self):
        self.table.setTextColor(0, 0, 'white')
        self.assertEquals(self.table.data[0][0][0], r'{\color{white}test}')
        self.table.setTextColor(0, 1, 'white')
        self.assertEquals(self.table.data[0][1][0], r'{\color{white}test}')
        self.table.setTextColor(2, 1, 'white')
        self.assertEquals(self.table.data[2][1][1], r'{\color{white}test}')
        self.table.setTextColor(1, 1, 'white')
        self.assertEquals(self.table.data[1][1], r'{\color{white}test}')

    def test_setTextColorRedArrayTable(self):
        self.table.setTextColor(0, 0, 'red')
        self.assertEquals(self.table.data[0][0][0], r'{\color{red}test}')
        self.table.setTextColor(0, 1, 'red')
        self.assertEquals(self.table.data[0][1][0], r'{\color{red}test}')
        self.table.setTextColor(2, 1, 'red')
        self.assertEquals(self.table.data[2][1][1], r'{\color{red}test}')
        self.table.setTextColor(1, 1, 'red')
        self.assertEquals(self.table.data[1][1], r'{\color{red}test}')

    def test_setTextColorGreenArrayTable(self):
        self.table.setTextColor(0, 0, 'green')
        self.assertEquals(self.table.data[0][0][0], r'{\color{green}test}')
        self.table.setTextColor(0, 1, 'green')
        self.assertEquals(self.table.data[0][1][0], r'{\color{green}test}')
        self.table.setTextColor(2, 1, 'green')
        self.assertEquals(self.table.data[2][1][1], r'{\color{green}test}')
        self.table.setTextColor(1, 1, 'green')
        self.assertEquals(self.table.data[1][1], r'{\color{green}test}')

    def test_setTextColorBlueArrayTable(self):
        self.table.setTextColor(0, 0, 'blue')
        self.assertEquals(self.table.data[0][0][0], r'{\color{blue}test}')
        self.table.setTextColor(0, 1, 'blue')
        self.assertEquals(self.table.data[0][1][0], r'{\color{blue}test}')
        self.table.setTextColor(2, 1, 'blue')
        self.assertEquals(self.table.data[2][1][1], r'{\color{blue}test}')
        self.table.setTextColor(1, 1, 'blue')
        self.assertEquals(self.table.data[1][1], r'{\color{blue}test}')

    def test_setTextColorCyanArrayTable(self):
        self.table.setTextColor(0, 0, 'cyan')
        self.assertEquals(self.table.data[0][0][0], r'{\color{cyan}test}')
        self.table.setTextColor(0, 1, 'cyan')
        self.assertEquals(self.table.data[0][1][0], r'{\color{cyan}test}')
        self.table.setTextColor(2, 1, 'cyan')
        self.assertEquals(self.table.data[2][1][1], r'{\color{cyan}test}')
        self.table.setTextColor(1, 1, 'cyan')
        self.assertEquals(self.table.data[1][1], r'{\color{cyan}test}')

    def test_setTextColorMagentaArrayTable(self):
        self.table.setTextColor(0, 0, 'magenta')
        self.assertEquals(self.table.data[0][0][0], r'{\color{magenta}test}')
        self.table.setTextColor(0, 1, 'magenta')
        self.assertEquals(self.table.data[0][1][0], r'{\color{magenta}test}')
        self.table.setTextColor(2, 1, 'magenta')
        self.assertEquals(self.table.data[2][1][1], r'{\color{magenta}test}')
        self.table.setTextColor(1, 1, 'magenta')
        self.assertEquals(self.table.data[1][1], r'{\color{magenta}test}')

    def test_setTextColorYellowArrayTable(self):
        self.table.setTextColor(0, 0, 'yellow')
        self.assertEquals(self.table.data[0][0][0], r'{\color{yellow}test}')
        self.table.setTextColor(0, 1, 'yellow')
        self.assertEquals(self.table.data[0][1][0], r'{\color{yellow}test}')
        self.table.setTextColor(2, 1, 'yellow')
        self.assertEquals(self.table.data[2][1][1], r'{\color{yellow}test}')
        self.table.setTextColor(1, 1, 'yellow')
        self.assertEquals(self.table.data[1][1], r'{\color{yellow}test}')

    def test_setTextColorMultipleArrayTable(self):
        self.table.setTextColor(0, 0, 'yellow')
        self.table.setTextColor(0, 0, 'red')
        self.assertEquals(self.table.data[0][0][0], r'{\color{red}test}')
        self.table.setTextColor(0, 1, 'yellow')
        self.table.setTextColor(0, 1, 'red')
        self.assertEquals(self.table.data[0][1][0], r'{\color{red}test}')
        self.table.setTextColor(2, 1, 'yellow')
        self.table.setTextColor(2, 1, 'red')
        self.assertEquals(self.table.data[2][1][1], r'{\color{red}test}')
        self.table.setTextColor(1, 1, 'yellow')
        self.table.setTextColor(1, 1, 'red')
        self.assertEquals(self.table.data[1][1], r'{\color{red}test}')

    def test_setTextColorOtherAndOutRangeArrayTable(self):
        self.assertRaises(
            ValueError,
            self.table.setTextColor,  1,  1, 'other'
        )
        self.assertRaises(
            ValueError,
            self.table.setTextColor,  3,  3, 'normal'
        )
        self.assertRaises(
            ValueError,
            self.table.setTextColor, -1, -1, 'normal'
        )

    def test_setRowAlignmentArrayTable(self):
        self.table.setRowAlignment(0, 'left')
        self.assertEquals(self.table.rowAlignment, ['l', 'c', 'c'])

        self.table.setRowAlignment(2, 'right')
        self.assertEquals(self.table.rowAlignment, ['l', 'c', 'r'])

        self.table.setRowAlignment(0, 'center')
        self.table.setRowAlignment(1, 'right')
        self.table.setRowAlignment(2, 'left')
        self.assertEquals(self.table.rowAlignment, ['c', 'r', 'l'])

        self.assertRaises(ValueError, self.table.setRowAlignment, 1, 'other')
        self.assertRaises(ValueError, self.table.setRowAlignment, -1, 'center')
        self.assertRaises(ValueError, self.table.setRowAlignment, 3, 'center')

    def test_addImageArrayTable(self):
        self.table.addImage("IMAGEPATH", 1, 1)
        self.assertEquals(
            self.table.data[1][1],
            r' \includegraphics{IMAGEPATH} '
        )

        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH", -1,  1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  1, -1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  3,  1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  3, -1)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH",  3,  3)
        self.assertRaises(ValueError, self.table.addImage, "IMAGEPATH", -1, -1)

    def test_getTableArrayTable(self):
        stream = self.table.getTable()
        self.assertEquals(
            stream,
            r"\begin{table}[h]\begin{center}\begin{tabular}"
            r"{ccc}test&\begin{tabular}{c}test\\test"
            r"\end{tabular}&test\\test&test&test\\test&\begin{tabular}"
            r"{c}test\\test\end{tabular}&test\\"
            r"\end{tabular}\caption{}\end{center}\end{table}"
        )


class TestPandocMarkdownWriter(unittest.TestCase):

    def setUp(self):
        self.pmw = PandocMarkdownWriter()

    def test_addTable(self):
        table = PandocMarkdownTable()
        array = [
            ['test', 'test', 'test'],
            ['test', 'test', 'test'],
            ['test', 'test', 'test']
        ]
        table.setContent(array)
        self.pmw.addTable(table)
        self.assertEquals(
            self.pmw.stream,
            r"\begin{table}[h]\begin{center}\begin{tabular}"
            r"{ccc}test&test&test\\test&test&test\\test&test&test\\"
            r"\end{tabular}\caption{}\end{center}\end{table}"
        )
        table = ""
        self.assertRaises(ValueError, self.pmw.addTable, table)

    def test_addImage1(self):
        self.pmw.addImage("URL", "TITLE", "LEGEND")
        self.assertEquals(self.pmw.stream, '![LEGEND](URL "TITLE")')

    def test_addImage2(self):
        self.pmw.addImage("URL", "TITLE")
        self.assertEquals(self.pmw.stream, '![TITLE](URL "TITLE")')

    def test_addImage3(self):
        self.pmw.addImage("URL")
        self.assertEquals(self.pmw.stream, '![](URL "")')
