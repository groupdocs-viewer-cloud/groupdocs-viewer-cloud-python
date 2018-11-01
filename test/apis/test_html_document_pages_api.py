# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_html_document_pages_api.py">
#   Copyright (c) 2003-2018 Aspose Pty Ltd
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

from groupdocs_viewer_cloud.models import *
from groupdocs_viewer_cloud.models.requests import *
from test.test_context import TestContext
from test.test_file import TestFile

class TestHtmlDocumentPagesApi(TestContext):
    """ViewerApi unit tests"""

    def test_html_get_page(self):
        """
        Test case for html_get_page

        Downloads document page as HTML.  # noqa: E501
        """
        file = TestFile.one_page_docx()

        request = HtmlGetPageRequest(file.file_name, 1)
        request.folder = file.folder

        response = self.viewer_api.html_get_page(request)

        self.assertIsNotNone(response)

    def test_html_get_page_with_custom_font(self):
        """
        Test case for html_get_page

        Downloads document page as HTML.  # noqa: E501
        """
        file = TestFile.uses_custom_font_pptx()

        request = HtmlGetPageRequest(file.file_name, 1)
        request.folder = file.folder
        request.fonts_folder = "fonts"

        response = self.viewer_api.html_get_page(request)

        self.assertIsNotNone(response)

    def test_html_get_pages(self):
        """
        Test case for html_get_pages

        Retrieves list of document pages as HTML.  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        request = HtmlGetPagesRequest(file.file_name)
        request.folder = file.folder

        response = self.viewer_api.html_get_pages(request)

        self.assertEqual(4, len(response.pages))
        self.assertEqual("four-pages.docx", response.file_name)
        self.assertEqual("words\\docx", response.folder)

    def test_html_get_pages_from_url(self):
        """
        Test case for html_get_pages_from_url

        Retrieves list of document pages as HTML.  # noqa: E501
        """
        file = TestFile.from_url_with_notes_pptx()

        request = HtmlGetPagesFromUrlRequest(file.url)
        request.folder = "tests\\from_url"

        response = self.viewer_api.html_get_pages_from_url(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual("with-notes.pptx", response.file_name)

    def test_html_get_zip_with_pages(self):
        """
        Test case for html_get_zip_with_pages

        Retrieves list of document pages as HTML.  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        request = HtmlGetZipWithPagesRequest(file.file_name)
        request.resource_path = "./r/{resource-name}"
        request.folder = file.folder

        response = self.viewer_api.html_get_zip_with_pages(request)

        self.assertIsNotNone(response)

    def test_html_create_pages_cache(self):
        """
        Test case for html_create_pages_cache

        Creates document pages as HTML and saves them in cache. Pages created before will be removed from cache.  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        html_options = HtmlOptions()
        html_options.embed_resources = True

        request = HtmlCreatePagesCacheRequest(file.file_name)
        request.html_options = html_options
        request.folder = file.folder

        response = self.viewer_api.html_create_pages_cache(request)

        self.assertEqual(4, len(response.pages))
        self.assertEqual("four-pages.docx", response.file_name)
        self.assertEqual("words\\docx", response.folder)

    def test_html_create_pages_cache_from_content(self):
        """
        Test case for html_create_pages_cache_from_content

        Creates posted document pages as HTML and saves them in cache. Content with document or multipart content is expected where first part is document and second is HtmlOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501
        """
        file = TestFile.password_protected_docx()

        html_options = HtmlOptions()
        html_options.password = file.password
        html_options.embed_resources = True

        file_content = self.get_test_file_path(file)
        options_json = self.to_json_file(html_options)

        request = HtmlCreatePagesCacheFromContentRequest(file_content, options_json)
        request.folder = "tests\\from_content"

        response = self.viewer_api.html_create_pages_cache_from_content(request)

        self.assertTrue(response.file_name.endswith(".docx"))
        self.assertEqual(1, len(response.pages))

    def test_html_create_pages_cache_from_url(self):
        """
        Test case for html_create_pages_cache_from_url

        Creates pages as HTML and saves them in cache for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501
        """
        file = TestFile.from_url_with_notes_pptx()

        html_options = HtmlOptions()
        html_options.embed_resources = True

        request = HtmlCreatePagesCacheFromUrlRequest(file.url)
        request.html_options = html_options
        request.file_name =  file.file_name
        request.folder = "tests\\from_url"

        response = self.viewer_api.html_create_pages_cache_from_url(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual("with-notes.pptx", response.file_name)

    def test_html_rotate_pages(self):
        """
        Test case for html_transform_pages

        Rotates or reorders document page(s).  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        transform_options = RotateOptions()
        transform_options.page_number = 1
        transform_options.angle = 90

        request = HtmlTransformPagesRequest(file.file_name)
        request.transform_options = transform_options
        request.folder = file.folder

        response = self.viewer_api.html_transform_pages(request)

        self.assertEqual(90, response.pages[0].angle)

    def test_html_reorder_pages(self):
        """
        Test case for html_transform_pages

        Rotates or reorders document page(s).  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        transform_options = ReorderOptions()
        transform_options.page_number = 1
        transform_options.new_position = 2

        request = HtmlTransformPagesRequest(file.file_name)
        request.transform_options = transform_options
        request.folder = file.folder

        response = self.viewer_api.html_transform_pages(request)

        self.assertEqual(1, response.pages[1].number)
        self.assertEqual(2, response.pages[0].number)

    def test_html_delete_pages_cache(self):
        """
        Test case for html_delete_pages_cache

        Removes document cache.  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        request = HtmlDeletePagesCacheRequest(file.file_name)
        request.folder = file.folder

        response = self.viewer_api.html_delete_pages_cache(request)

        self.assertIsNone(response)
    
if __name__ == '__main__':
    unittest.main()
