# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_file.py">
#   Copyright (c) 2003-2021 Aspose Pty Ltd
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

from __future__ import absolute_import

from groupdocs_comparison_cloud import FileInfo

class TestFile:
    """Test file"""

    def __init__(self, file_name, folder, password = None):
            self.file_name = file_name
            self.folder = folder
            self.password = password
            
    def ToFileInfo(self):
        f = FileInfo()
        f.file_path = self.folder + self.file_name
        if hasattr(self, 'password'):
            f.password = self.password
        return f

class TestFiles:
    """Test files"""

    SourceCell = TestFile("source.xlsx", "source_files\\cell\\")
    SourceDiagram = TestFile("source.vsdx", "source_files\\diagram\\")
    SourceEmail = TestFile("source.eml", "source_files\\email\\")
    SourceHtml = TestFile("source.html", "source_files\\html\\")
    SourceImage = TestFile("source.png", "source_files\\image\\")
    SourceNote = TestFile("source.one", "source_files\\note\\")
    SourcePdf = TestFile("source.pdf", "source_files\\pdf\\")
    SourceSlide = TestFile("source.pptx", "source_files\\slide\\")
    SourceText = TestFile("source.txt", "source_files\\text\\")
    SourceWord = TestFile("source.docx", "source_files\\word\\")
    SourceWithRevs = TestFile("source_with_revs.docx", "source_files\\word\\")

    SourceCellProtected = TestFile("source_protected.xlsx", "source_files\\cell\\", "1231")
    SourceNoteProtected = TestFile("source_protected.one", "source_files\\note\\", "123")
    SourcePdfProtected = TestFile("source_protected.pdf", "source_files\\pdf\\", "12345678")
    SourceSlideProtected = TestFile("source_protected.pptx", "source_files\\slide\\", "1231")
    SourceWordProtected = TestFile("source_protected.docx", "source_files\\word\\", "1231")


    TargetCell = TestFile("target.xlsx", "target_files\\cell\\")
    TargetDiagram = TestFile("target.vsdx", "target_files\\diagram\\")
    TargetEmail = TestFile("target.eml", "target_files\\email\\")
    TargetHtml = TestFile("target.html", "target_files\\html\\")
    TargetImage = TestFile("target.png", "target_files\\image\\")
    TargetNote = TestFile("target.one", "target_files\\note\\")
    TargetPdf = TestFile("target.pdf", "target_files\\pdf\\")
    TargetSlide = TestFile("target.pptx", "target_files\\slide\\")
    TargetText = TestFile("target.txt", "target_files\\text\\")
    TargetWord = TestFile("target.docx", "target_files\\word\\")

    TargetCellProtected = TestFile("target_protected.xlsx", "target_files\\cell\\", "1471")
    TargetNoteProtected = TestFile("target_protected.one", "target_files\\note\\", "123")
    TargetPdfProtected = TestFile("target_protected.pdf", "target_files\\pdf\\", "0987654")
    TargetSlideProtected = TestFile("target_protected.pptx", "target_files\\slide\\", "1471")
    TargetWordProtected = TestFile("target_protected.docx", "target_files\\word\\", "5784")

    TargetSlide1 = TestFile("target_1.pptx", "target_files\\slide\\")
    TargetSlide2 = TestFile("target_2.pptx", "target_files\\slide\\")
    TargetSlide1Protected = TestFile("target_1_protected.pptx", "target_files\\slide\\", "1471")
    TargetSlide2Protected = TestFile("target_2_protected.pptx", "target_files\\slide\\", "1471")
    TargetWord1 = TestFile("target_1.docx", "target_files\\word\\")
    TargetWord2 = TestFile("target_2.docx", "target_files\\word\\")
    TargetWord1Protected = TestFile("target_1_protected.docx", "target_files\\word\\", "5784")
    TargetWord2Protected = TestFile("target_2_protected.docx", "target_files\\word\\", "5784")

    NotExist = TestFile("not-exist.docx", "somefolder\\")

    @classmethod
    def get_test_files(cls):
        return [
                cls.SourceCell,
                cls.SourceDiagram,
                cls.SourceEmail,
                cls.SourceHtml,
                cls.SourceImage,
                cls.SourceNote,
                cls.SourcePdf,
                cls.SourceSlide,
                cls.SourceText,
                cls.SourceWord,
                cls.SourceWithRevs,
                cls.SourceCellProtected,
                cls.SourceNoteProtected,
                cls.SourcePdfProtected,
                cls.SourceSlideProtected,
                cls.SourceWordProtected,
                cls.TargetCell,
                cls.TargetDiagram,
                cls.TargetEmail,
                cls.TargetHtml,
                cls.TargetImage,
                cls.TargetNote,
                cls.TargetPdf,
                cls.TargetSlide,
                cls.TargetText,
                cls.TargetWord,
                cls.TargetCellProtected,
                cls.TargetNoteProtected,
                cls.TargetPdfProtected,
                cls.TargetSlideProtected,
                cls.TargetWordProtected,
                cls.TargetSlide1,
                cls.TargetSlide2,
                cls.TargetSlide1Protected,
                cls.TargetSlide2Protected,
                cls.TargetWord1,
                cls.TargetWord2,
                cls.TargetWord1Protected,
                cls.TargetWord2Protected
        ]

