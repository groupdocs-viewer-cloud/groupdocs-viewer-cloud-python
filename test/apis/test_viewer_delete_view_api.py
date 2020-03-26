# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd">
#   Copyright (c) 2003-2020 Aspose Pty Ltd
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

from groupdocs_viewer_cloud import *
from test.test_context import TestContext
from test.test_file import TestFile

class TestViewerDeleteViewApi(TestContext):
    """ViewerApi unit tests"""

    def test_delete_view_with_default_view_format(self):
        # Create view
        view_options = ViewOptions()
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(1, len(data.pages))
        # Delete view
        view_options = DeleteViewOptions()
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = DeleteViewRequest(view_options)
        self.view_api.delete_view(request)

if __name__ == '__main__':
    unittest.main()
