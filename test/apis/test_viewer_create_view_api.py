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
import datetime
import os

from groupdocs_viewer_cloud import *
from test.test_context import TestContext
from test.test_file import TestFile

class TestViewerCreateViewApi(TestContext):
    """ViewerApi unit tests"""

    def test_create_view_returns_missing_file_info(self):
        view_options = ViewOptions()
        request = CreateViewRequest(view_options)
        with self.assertRaises(ApiException) as context:
            self.view_api.create_view(request)
        self.assertEqual("Parameter 'FileInfo' is not specified.", context.exception.message)
    
    def test_create_view_returns_file_not_found(self):
        view_options = ViewOptions()
        view_options.file_info = TestFile.not_exist().ToFileInfo()
        request = CreateViewRequest(view_options)
        with self.assertRaises(ApiException) as context:
            self.view_api.create_view(request)
        self.assertEqual("Can't find file located at 'somefolder\\not-exist.docx'.", context.exception.message)

    def test_create_view_with_minimal_view_options(self):
        view_options = ViewOptions()
        view_options.file_info = TestFile.password_protected_docx().ToFileInfo()
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(4, len(data.pages))
        self.assertEqual(0, len(data.attachments))

        request = DownloadFileRequest(data.pages[0].path)
        data = self.file_api.download_file(request)        
        self.assertGreater(os.path.getsize(data), 0)

    def test_create_view_with_default_view_format(self):
        view_options = ViewOptions()
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(1, len(data.pages))
        self.assertEqual(0, len(data.attachments))
        self.assertEqual(1, data.pages[0].number)

    def test_create_view_with_html_view_format(self):
        view_options = ViewOptions()
        view_options.view_format = "HTML"
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(1, len(data.pages))
        self.assertEqual(0, len(data.attachments))
        self.assertEqual(1, data.pages[0].number)

    def test_create_view_with_image_view_format(self):
        view_options = ViewOptions()
        view_options.view_format = "JPG"
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(1, len(data.pages))
        self.assertEqual(0, len(data.attachments))
        self.assertEqual(1, data.pages[0].number)        

    def test_create_view_with_render_hidden_pages(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.two_hidden_pages_vsd().ToFileInfo()
        render_options = RenderOptions()
        render_options.render_hidden_pages = True
        view_options.render_options = render_options
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(3, len(data.pages))

    def test_create_view_with_spreadsheet_paginate_sheets_option(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.with_hidden_rows_and_columns().ToFileInfo()
        sp_options = SpreadsheetOptions()
        sp_options.paginate_sheets = True
        sp_options.count_rows_per_page = 5
        render_options = RenderOptions()
        render_options.spreadsheet_options = sp_options
        view_options.render_options = render_options
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(2, len(data.pages))

    def test_create_view_with_spreadsheet_render_hidden_rows_option(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.with_hidden_rows_and_columns().ToFileInfo()
        sp_options = SpreadsheetOptions()
        sp_options.paginate_sheets = True
        sp_options.count_rows_per_page = 5
        sp_options.render_hidden_rows = True
        render_options = RenderOptions()
        render_options.spreadsheet_options = sp_options
        view_options.render_options = render_options
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(3, len(data.pages))

    def test_create_view_with_cad_options(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.three_layouts_dwf().ToFileInfo()
        cad_options = CadOptions()
        cad_options.scale_factor = 5.0
        render_options = RenderOptions()
        render_options.cad_options = cad_options
        view_options.render_options = render_options
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(3, len(data.pages))

    def test_create_view_with_project_options(self):
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
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(1, len(data.pages))

    def test_create_view_with_fonts_path_option(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.uses_custom_font_pptx().ToFileInfo()
        view_options.view_format = "PNG"
        view_options.fonts_path = "font/ttf"
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(1, len(data.pages))

    def test_create_view_with_start_and_count_pages(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.four_pages_docx().ToFileInfo()
        render_options = RenderOptions()
        render_options.start_page_number = 2
        render_options.count_pages_to_render = 2
        view_options.render_options = render_options
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(2, len(data.pages))
        self.assertEqual(2, data.pages[0].number)

    def test_create_view_with_html_view_options(self):
        view_options = ViewOptions()        
        view_options.file_info = TestFile.one_page_docx().ToFileInfo()        
        render_options = HtmlOptions()
        render_options.external_resources = True
        view_options.render_options = render_options
        request = CreateViewRequest(view_options)
        data = self.view_api.create_view(request)
        self.assertEqual(1, len(data.pages))
        self.assertGreater(len(data.pages[0].resources), 0)

if __name__ == '__main__':
    unittest.main()
