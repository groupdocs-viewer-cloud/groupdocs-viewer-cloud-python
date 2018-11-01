# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_html_attachments_api.py">
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

class TestHtmlAttachmentsApi(TestContext):
    """ViewerApi unit tests"""

    def test_html_get_attachment_from_msg(self):
        """
        Test case for html_get_attachment

        Downloads attachment.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()
      
        request = HtmlGetAttachmentRequest(file.file_name, file.attachment_name)
        request.folder = file.folder

        response = self.viewer_api.html_get_attachment(request)

        self.assertIsNotNone(response)

    def test_html_get_attachment_from_pdf(self):
        """
        Test case for html_get_attachment

        Downloads attachment.  # noqa: E501
        """
        file = TestFile.with_attachment_pdf()
      
        request = HtmlGetAttachmentRequest(file.file_name, file.attachment_name)
        request.folder = file.folder

        response = self.viewer_api.html_get_attachment(request)

        self.assertIsNotNone(response)

    def test_html_get_attachments_from_msg(self):
        """
        Test case for html_get_attachments

        Retrieves list of document attachments.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()
      
        request = HtmlGetAttachmentsRequest(file.file_name)
        request.folder = file.folder

        response = self.viewer_api.html_get_attachments(request)

        self.assertEqual(1, len(response.attachments))
        self.assertEqual("password-protected.docx", response.attachments[0].name)  

    def test_html_get_attachments_from_pdf(self):
        """
        Test case for html_get_attachments

        Retrieves list of document attachments.  # noqa: E501
        """
        file = TestFile.with_attachment_pdf()
      
        request = HtmlGetAttachmentsRequest(file.file_name)
        request.folder = file.folder

        response = self.viewer_api.html_get_attachments(request)

        self.assertEqual(1, len(response.attachments))
        self.assertEqual("password-protected.docx", response.attachments[0].name)

if __name__ == '__main__':
    unittest.main()
