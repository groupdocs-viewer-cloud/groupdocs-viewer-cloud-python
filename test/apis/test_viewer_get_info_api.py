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
import datetime
from groupdocs_viewer_cloud import *
from test.test_context import TestContext
from test.test_file import TestFile

class TestViewerGetInfoApi(TestContext):
    """ViewerApi unit tests"""

    def test_get_info_returns_missing_file_info(self):
        view_options = ViewOptions()
        request = GetInfoRequest(view_options)
        with self.assertRaises(ApiException) as context:
            self.info_api.get_info(request)
        self.assertEqual("Parameter 'FileInfo' is not specified.", context.exception.message)
    
    def test_get_info_returns_file_not_found(self):
        view_options = ViewOptions()
        view_options.file_info = TestFile.not_exist().ToFileInfo()
        request = GetInfoRequest(view_options)
        with self.assertRaises(ApiException) as context:
            self.info_api.get_info(request)
        self.assertEqual("Can't find file located at 'somefolder\\not-exist.docx'.", context.exception.message)

    def test_get_info_password_protected(self):
        view_options = ViewOptions()
        view_options.file_info = TestFile.password_protected_docx().ToFileInfo()
        view_options.file_info.password = None
        request = GetInfoRequest(view_options)
        with self.assertRaises(ApiException) as context:
            self.info_api.get_info(request)
        self.assertEqual("Please specify password to load the document.", context.exception.message)

    def test_get_info_with_minimal_view_options(self):
        view_options = ViewOptions()
        view_options.file_info = TestFile.password_protected_docx().ToFileInfo()
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(4, len(data.pages))
        self.assertEqual(0, len(data.attachments))

    def test_get_info_with_default_view_format(self):
        view_options = ViewOptions()
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(1, len(data.pages))
        self.assertEqual(0, len(data.attachments))
        self.assertEqual(1, data.pages[0].number)

    def test_get_info_with_html_view_format(self):
        view_options = ViewOptions()
        view_options.view_format = "HTML"
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(1, len(data.pages))
        self.assertEqual(0, len(data.attachments))
        self.assertEqual(1, data.pages[0].number)

    def test_get_info_with_image_view_format(self):
        view_options = ViewOptions()
        view_options.view_format = "JPG"
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(1, len(data.pages))
        self.assertEqual(0, len(data.attachments))
        self.assertEqual(1, data.pages[0].number)
        self.assertGreater(data.pages[0].width, 0)

    def test_get_info_with_render_hidden_pages(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.two_hidden_pages_vsd().ToFileInfo()
        render_options = RenderOptions()
        render_options.render_hidden_pages = True
        view_options.render_options = render_options
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(3, len(data.pages))

    def test_get_info_with_spreadsheet_paginate_sheets_option(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.with_hidden_rows_and_columns().ToFileInfo()
        sp_options = SpreadsheetOptions()
        sp_options.paginate_sheets = True
        sp_options.count_rows_per_page = 5
        render_options = RenderOptions()
        render_options.spreadsheet_options = sp_options
        view_options.render_options = render_options
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(3, len(data.pages))

    def test_get_info_with_spreadsheet_render_hidden_rows_option(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.with_hidden_rows_and_columns().ToFileInfo()
        sp_options = SpreadsheetOptions()
        sp_options.paginate_sheets = True
        sp_options.count_rows_per_page = 5
        sp_options.render_hidden_rows = True
        render_options = RenderOptions()
        render_options.spreadsheet_options = sp_options
        view_options.render_options = render_options
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(3, len(data.pages))

    def test_get_info_with_cad_options(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.three_layouts_dwf().ToFileInfo()
        cad_options = CadOptions()
        cad_options.scale_factor = 5.0
        render_options = RenderOptions()
        render_options.cad_options = cad_options
        view_options.render_options = render_options
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(3, len(data.pages))

    def test_get_info_with_project_options(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.project_mpp().ToFileInfo()
        project_options = ProjectManagementOptions()
        project_options.page_size = "A4"
        project_options.time_unit = "Months"
        project_options.start_date = datetime.datetime(2008, 7, 1, 0, 0)
        project_options.end_date = datetime.datetime(2008, 7, 31, 0, 0)
        render_options = RenderOptions()
        render_options.project_management_options = project_options
        view_options.render_options = render_options
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertGreater(len(data.pages), 0)

    def test_get_info_with_image_view_options(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        view_options.view_format = "PNG"
        render_options = ImageOptions()
        render_options.extract_text = True
        view_options.render_options = render_options
        request = GetInfoRequest(view_options)
        data = self.info_api.get_info(request)
        self.assertEqual(1, len(data.pages))
        self.assertGreater(len(data.pages[0].lines), 0)

if __name__ == '__main__':
    unittest.main()
