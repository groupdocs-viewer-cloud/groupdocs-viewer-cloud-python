# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_image_attachment_info_api.py">
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

class TestImageAttachmentInfoApi(TestContext):
    """ViewerApi unit tests"""

    def test_image_get_attachment_info(self):
        """
        Test case for image_get_attachment_info

        Retrieves attachment information.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        request = ImageGetAttachmentInfoRequest(file.file_name, file.attachment_name)
        request.attachment_password = file.attachment_password
        request.folder = file.folder
    
        data = self.viewer_api.image_get_attachment_info(request)
    
        self.assertEqual(1, len(data.pages))
        self.assertEqual(".docx", data.extension)
        self.assertEqual("password-protected.docx", data.file_name)

    def test_image_get_attachment_info_attachment_not_found(self):
        """
        Test case for image_get_attachment_info

        Retrieves attachment information.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        request = ImageGetAttachmentInfoRequest(file.file_name, "not-found.pdf")
        request.folder = file.folder
    
        with self.assertRaises(ApiException) as context:
            self.viewer_api.image_get_attachment_info(request)

        self.assertEqual("Can't find attachment with given name 'not-found.pdf'.", context.exception.message)

    def test_image_get_attachment_info_password_not_provided(self):
        """
        Test case for image_get_attachment_info

        Retrieves attachment information.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        request = ImageGetAttachmentInfoRequest(file.file_name, file.attachment_name)
        request.folder = file.folder
    
        with self.assertRaises(ApiException) as context:
            self.viewer_api.image_get_attachment_info(request)

        self.assertEqual("The password was not provided. The specified file 'password-protected.docx' is password-protected.", context.exception.message)

    def test_image_get_attachment_info_invalid_password(self):
        """
        Test case for image_get_attachment_info

        Retrieves attachment information.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()

        request = ImageGetAttachmentInfoRequest(file.file_name, file.attachment_name)
        request.attachment_password = "not a password"
        request.folder = file.folder
    
        with self.assertRaises(ApiException) as context:
            self.viewer_api.image_get_attachment_info(request)

        self.assertEqual("Password provided for file with name 'password-protected.docx' is incorrect.", context.exception.message)

    def test_image_get_attachment_info_with_options(self):
        """
        Test case for image_get_attachment_info_with_options

        Retrieves attachment information with specified DocumentInfoOptions. 
        Expects DocumentInfoOptions object data in request body.  # noqa: E501
        """
        file = TestFile.with_attachment_msg()
      
        document_info_options = DocumentInfoOptions()
        document_info_options.attachment_password = file.attachment_password 

        request = ImageGetAttachmentInfoWithOptionsRequest(
          file.file_name,
          file.attachment_name,
          document_info_options,
          file.folder)

        response = self.viewer_api.image_get_attachment_info_with_options(request)

        self.assertEqual(1, len(response.pages))
        self.assertEqual(".docx", response.extension)
        self.assertEqual("password-protected.docx", response.file_name)

if __name__ == '__main__':
    unittest.main()
