
# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_html_attachment_pages_api.py">
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
from test.test_context import TestContext
from test.test_file import TestFile

from groupdocs_viewer_cloud import ApiException
from groupdocs_viewer_cloud.models import *
from groupdocs_viewer_cloud.models.requests import *

class TestHtmlAttachmentPagesApi(TestContext):
    """ViewerApi unit tests"""

    def test_html_get_attachment_page(self):
        """
        Test case for html_get_attachment_page

        Downloads attachment page as HTML.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        request = HtmlGetAttachmentPageRequest(file.file_name, file.attachment_name, 1)
        request.attachment_password = file.attachment_password
        request.folder = file.folder

        response = self.viewer_api.html_get_attachment_page(request)

        self.assertIsNotNone(response)

    def test_html_get_attachment_pages(self):
        """
        Test case for html_get_attachment_pages

        Retrieves attachment pages as HTML.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        request = HtmlGetAttachmentPagesRequest(file.file_name, file.attachment_name)
        request.attachment_password = file.attachment_password
        request.folder = file.folder

        response = self.viewer_api.html_get_attachment_pages(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual("with-attachment.msg", response.file_name)
        self.assertEqual("password-protected.docx", response.attachment_name)
        self.assertEqual("email\\msg", response.folder)

    def test_html_get_zip_with_attachment_pages(self):
        """
        Test case for html_get_zip_with_attachment_pages

        Retrieves attachment pages as HTML.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        request = HtmlGetZipWithAttachmentPagesRequest(file.file_name, file.attachment_name)
        request.attachment_password = file.attachment_password
        request.resource_path = "./r{page-number}/{resource-name}"
        request.folder = file.folder

        response = self.viewer_api.html_get_zip_with_attachment_pages(request)

        self.assertIsNotNone(response)

    def test_html_create_attachment_pages_cache(self):
        """
        Test case for html_create_attachment_pages_cache

        Creates attachment cache.   # noqa: E501
        """
        file = TestFile.with_attachment_pdf()

        html_options = HtmlOptions()
        html_options.attachment_password = file.attachment_password

        request = HtmlCreateAttachmentPagesCacheRequest(file.file_name, file.attachment_name)
        request.html_options = html_options
        request.folder = file.folder

        response = self.viewer_api.html_create_attachment_pages_cache(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual("with-attachment.pdf", response.file_name)
        self.assertEqual("password-protected.docx", response.attachment_name)
        self.assertEqual("pdf\\pdf", response.folder)

    def test_html_delete_attachment_pages_cache(self):
        """
        Test case for html_delete_attachment_pages_cache

        Removes attachment cache.  # noqa: E501
        """
        file = TestFile.with_attachment_pdf()

        request = HtmlDeleteAttachmentPagesCacheRequest(file.file_name, file.attachment_name)
        request.folder = file.folder

        response = self.viewer_api.html_delete_attachment_pages_cache(request)

        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
