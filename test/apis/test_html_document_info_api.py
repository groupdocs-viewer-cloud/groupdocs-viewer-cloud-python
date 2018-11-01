# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_html_document_info_api.py">
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
import json

from test.test_context import TestContext
from test.test_file import TestFile

from groupdocs_viewer_cloud import ApiException
from groupdocs_viewer_cloud.models import *
from groupdocs_viewer_cloud.models.requests import *

class TestHtmlDocumentInfoApi(TestContext):
    """ViewerApi unit tests"""

    def test_html_get_document_info(self):
        """
        Test case for html_get_document_info

        Retrieves document information.  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        request = HtmlGetDocumentInfoRequest(file.file_name)
        request.folder = file.folder

        response = self.viewer_api.html_get_document_info(request)

        self.assertEqual(4, len(response.pages))
        self.assertEqual(".docx", response.extension)
        self.assertEqual("four-pages.docx", response.file_name)

    def test_html_get_document_info_with_render_hidden_pages(self):
        """
        Test case for html_get_document_info

        Retrieves document information.  # noqa: E501
        """
        file = TestFile.two_hidden_pages_vsd()

        request = HtmlGetDocumentInfoRequest(file.file_name)
        request.folder = file.folder
        request.render_hidden_pages = True

        response = self.viewer_api.html_get_document_info(request)

        self.assertEqual(3, len(response.pages))
        self.assertEqual(".vsd", response.extension)
        self.assertEqual("two-hidden-pages.vsd", response.file_name)

    def test_html_get_document_info_file_not_found(self):
        """
        Test case for html_get_document_info

        Retrieves document information.  # noqa: E501
        """
        request = HtmlGetDocumentInfoRequest("file-not-found.docx")

        with self.assertRaises(ApiException) as context:
            self.viewer_api.html_get_document_info(request)

        self.assertEqual("Can't find file with given name 'file-not-found.docx' and folder ''.", context.exception.message)

    def test_html_get_document_info_password_not_provided(self):
        """
        Test case for html_get_document_info

        Retrieves document information.  # noqa: E501
        """
        file = TestFile.password_protected_docx()

        request = HtmlGetDocumentInfoRequest(file.file_name)
        request.folder = file.folder

        with self.assertRaises(ApiException) as context:
            self.viewer_api.html_get_document_info(request)

        self.assertEqual("The password was not provided. The specified file 'password-protected.docx' is password-protected.", context.exception.message)

    def test_html_get_document_info_invalid_password(self):
        """
        Test case for html_get_document_info

        Retrieves document information.  # noqa: E501
        """
        file = TestFile.password_protected_docx()

        request = HtmlGetDocumentInfoRequest(file.file_name)
        request.folder = file.folder
        request.password = "not-a-password"

        with self.assertRaises(ApiException) as context:
            self.viewer_api.html_get_document_info(request)

        self.assertEqual("Password provided for file with name 'password-protected.docx' is incorrect.", context.exception.message)

    def test_html_get_document_info_corrupted_file(self):
        """
        Test case for html_get_document_info

        Retrieves document information.  # noqa: E501
        """
        file = TestFile.corrupted_pdf()

        request = HtmlGetDocumentInfoRequest(file.file_name)
        request.folder = file.folder

        with self.assertRaises(ApiException) as context:
            self.viewer_api.html_get_document_info(request)

        self.assertEqual("Failed to read specified file 'corrupted.pdf'. File can be corrupted or damaged.", context.exception.message)
   
    def test_html_get_document_info_from_url(self):
        """
        Test case for html_get_document_info_from_url

        Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501
        """
        file = TestFile.from_url_one_page_docx()

        request = HtmlGetDocumentInfoFromUrlRequest(file.url)
        request.file_name = file.file_name
        request.folder = "tests\\from_url"

        response = self.viewer_api.html_get_document_info_from_url(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual(".docx", response.extension)
        self.assertEqual("one-page.docx", response.file_name)

    def test_html_get_document_info_from_url_invalid_url(self):
        """
        Test case for html_get_document_info_from_url

        Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501
        """
        request = HtmlGetDocumentInfoFromUrlRequest("invalid-url")

        with self.assertRaises(ApiException) as context:
            self.viewer_api.html_get_document_info_from_url(request)

        self.assertEqual("Can't parse specified URL 'invalid-url'.", context.exception.message)

    def test_html_get_document_info_with_options(self):
        """
        Test case for html_get_document_info_with_options

        Retrieves document information with specified DocumentInfoOptions. Expects DocumentInfoOptions object data in request body.  # noqa: E501
        """
        file = TestFile.password_protected_docx()

        document_info_options = DocumentInfoOptions()
        document_info_options.password = file.password

        request = HtmlGetDocumentInfoWithOptionsRequest(file.file_name)
        request.file_name = file.file_name
        request.folder = file.folder
        request.document_info_options = document_info_options

        response = self.viewer_api.html_get_document_info_with_options(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual(".docx", response.extension)
        self.assertEqual("password-protected.docx", response.file_name)

    def test_html_get_document_info_from_content(self):
        """
        Test case for html_get_document_info_from_content

        Retrieves document information for posted document. Content with document or multipart content is expected where first part is document and second is DocumentInfoOptions. Saves file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501
        """
        file = TestFile.password_protected_docx()

        document_info_options = DocumentInfoOptions()
        document_info_options.password = file.password
        
        file_content = self.get_test_file_path(file)
        options_json = self.to_json_file(document_info_options)

        request = HtmlGetDocumentInfoFromContentRequest(file_content, options_json)
        request.file_name = file.file_name
        request.folder = "tests\\from_content"

        response = self.viewer_api.html_get_document_info_from_content(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual(".docx", response.extension)
        self.assertEqual("password-protected.docx", response.file_name)

    def test_html_get_document_info_from_url_with_options(self):
        """
        Test case for html_get_document_info_from_url_with_options

        Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501
        """
        file = TestFile.from_url_with_notes_pptx()

        document_info_options = DocumentInfoOptions()
        document_info_options.slides_options = SlidesOptions()
        document_info_options.slides_options.render = True 

        request = HtmlGetDocumentInfoFromUrlWithOptionsRequest(file.url)
        request.file_name = file.file_name
        request.document_info_options = document_info_options
        request.folder = "tests\\from_url"

        response = self.viewer_api.html_get_document_info_from_url_with_options(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual(".pptx", response.extension)
        self.assertEqual("with-notes.pptx", response.file_name)

if __name__ == '__main__':
    unittest.main()
