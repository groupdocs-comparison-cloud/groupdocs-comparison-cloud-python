# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd">
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

import unittest

from groupdocs_comparison_cloud import *
from test.test_context import TestContext
from test.test_file import TestFiles

class TestReviewApi(TestContext):
    """ReviewApi unit tests"""

    def test_get_revisions(self):        
        response = self.review_api.get_revisions(GetRevisionsRequest(TestFiles.SourceWithRevs.ToFileInfo()))
        self.assertEqual(len(response), 2)

    def test_apply_revisions(self):    
        options = ApplyRevisionsOptions()
        options.source_file = TestFiles.SourceWithRevs.ToFileInfo()
        options.output_path = "/resultFilePath/result.docx"
        rev1 = RevisionInfo()
        rev1.id = 0
        rev1.action = "Accept"
        rev2 = RevisionInfo()
        rev2.id = 1
        rev2.action = "Reject"    
        options.revisions = [rev1, rev2]

        response = self.review_api.apply_revisions(ApplyRevisionsRequest(options))
        self.assertEqual(response.rel, options.output_path)
            
    def test_accept_all_revisions(self):    
        options = ApplyRevisionsOptions()
        options.source_file = TestFiles.SourceWithRevs.ToFileInfo()
        options.output_path = "/resultFilePath/result.docx"
        options.accept_all = True

        response = self.review_api.apply_revisions(ApplyRevisionsRequest(options))
        self.assertEqual(response.rel, options.output_path)

    def test_reject_all_revisions(self):    
        options = ApplyRevisionsOptions()
        options.source_file = TestFiles.SourceWithRevs.ToFileInfo()
        options.output_path = "/resultFilePath/result.docx"
        options.reject_all = True

        response = self.review_api.apply_revisions(ApplyRevisionsRequest(options))
        self.assertEqual(response.rel, options.output_path)

if __name__ == '__main__':
    unittest.main()
