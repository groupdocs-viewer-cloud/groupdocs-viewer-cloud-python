# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_html_attachment_page_resource_api.py">
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

class TestHtmlAttachmentPageResourceApi(TestContext):
    """ViewerApi unit tests"""

    def test_html_get_attachment_page_resource(self):
        """
        Test case for html_get_attachment_page_resource

        Downloads HTML page resource (image, style, graphics or font).  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        pages = self.get_pages(file)
        first_page = pages[0] 

        for resource in first_page.resources:
            request = HtmlGetAttachmentPageResourceRequest(
                file.file_name,
                file.attachment_name,
                first_page.number,
                resource.name,
                file.folder)

            page_resource = self.viewer_api.html_get_attachment_page_resource(request)

            self.assertIsNotNone(page_resource)

    def get_pages(self, file):
        request = HtmlGetAttachmentPagesRequest(file.file_name, file.attachment_name)
        request.attachment_password = file.attachment_password
        request.folder = file.folder
        request.embed_resources = False
        request.start_page_number = 1
        request.count_pages = 1

        response = self.viewer_api.html_get_attachment_pages(request)

        return response.pages

if __name__ == '__main__':
    unittest.main()
