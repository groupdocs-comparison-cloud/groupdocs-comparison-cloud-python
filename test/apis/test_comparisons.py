# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd">
#   Copyright (c) 2003-2023 Aspose Pty Ltd
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

import unittest

from groupdocs_comparison_cloud import *
from test.test_context import TestContext
from test.test_file import TestFile, TestFiles

class TestComparisons(TestContext):
    """ComparisonApi unit tests"""

    def test_comparisons_cells(self):
        options = self.GetComparisonOptions(TestFiles.SourceCell, TestFiles.TargetCell)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_diagram(self):
        options = self.GetComparisonOptions(TestFiles.SourceDiagram, TestFiles.TargetDiagram)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_email(self):
        options = self.GetComparisonOptions(TestFiles.SourceEmail, TestFiles.TargetEmail)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_html(self):
        options = self.GetComparisonOptions(TestFiles.SourceHtml, TestFiles.TargetHtml)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_image(self):
        options = self.GetComparisonOptions(TestFiles.SourceImage, TestFiles.TargetImage)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_note(self):
        options = self.GetComparisonOptions(TestFiles.SourceNote, TestFiles.TargetNote)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_note_protected(self):
        options = self.GetComparisonOptions(TestFiles.SourceNoteProtected, TestFiles.TargetNoteProtected)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_pdf(self):
        options = self.GetComparisonOptions(TestFiles.SourcePdf, TestFiles.TargetPdf)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_pdf_protected(self):
        options = self.GetComparisonOptions(TestFiles.SourcePdfProtected, TestFiles.TargetPdfProtected)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_text(self):
        options = self.GetComparisonOptions(TestFiles.SourceText, TestFiles.TargetText)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_word(self):
        options = self.GetComparisonOptions(TestFiles.SourceWord, TestFiles.TargetWord)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_comparisons_word_protected(self):
        options = self.GetComparisonOptions(TestFiles.SourceWordProtected, TestFiles.TargetWordProtected)
        response = self.compare_api.comparisons(ComparisonsRequest(options))
        self.assertEqual(response.rel, options.output_path)   

    def GetComparisonOptions(self, source, target):
        options = ComparisonOptions()
        options.source_file = source.ToFileInfo()
        options.output_path = "/resultFilePath/" + source.file_name
        
        options.settings = Settings()
        options.settings.generate_summary_page = True
        options.settings.show_deleted_content = True
        options.settings.style_change_detection = True
        options.settings.use_frames_for_del_ins_elements = False
        options.settings.meta_data = None
        options.settings.details_level = "Low"
        options.settings.diagram_master_setting = None
        options.settings.calculate_component_coordinates = False
        options.settings.clone_metadata = "Default"
        options.settings.mark_deleted_inserted_content_deep = False
        options.settings.password = "1111"
        options.settings.password_save_option = "User"
        
        options.settings.deleted_items_style = ItemsStyle()        
        options.settings.deleted_items_style.begin_separator_string = ""
        options.settings.deleted_items_style.end_separator_string = ""
        options.settings.deleted_items_style.font_color = "16711680"
        options.settings.deleted_items_style.highlight_color = "16711680"
        options.settings.deleted_items_style.bold = False
        options.settings.deleted_items_style.italic = False
        options.settings.deleted_items_style.strike_through = False
        
        options.settings.inserted_items_style = ItemsStyle()        
        options.settings.inserted_items_style.begin_separator_string = ""
        options.settings.inserted_items_style.end_separator_string = ""
        options.settings.inserted_items_style.font_color = "255"
        options.settings.inserted_items_style.highlight_color = "255"
        options.settings.inserted_items_style.bold = False
        options.settings.inserted_items_style.italic = False
        options.settings.inserted_items_style.strike_through = False
        
        options.settings.changed_items_style = ItemsStyle()
        options.settings.changed_items_style.begin_separator_string = ""
        options.settings.changed_items_style.end_separator_string = ""
        options.settings.changed_items_style.font_color = "65280"
        options.settings.changed_items_style.highlight_color = "65280"
        options.settings.changed_items_style.bold = False
        options.settings.changed_items_style.italic = False
        options.settings.changed_items_style.strike_through = False
      
        options.target_files = [target.ToFileInfo()]

        return options

if __name__ == '__main__':
    unittest.main()
