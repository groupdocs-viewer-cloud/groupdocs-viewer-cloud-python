# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_image_document_pdf_api.py">
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

class TestImageDocumentPdfApi(TestContext):
    """ViewerApi unit tests"""

    def test_image_get_pdf_file(self):
        """
        Test case for image_get_pdf_file

        Downloads document as PDF.  # noqa: E501
        """
        file = TestFile.four_pages_docx()

        request = ImageGetPdfFileRequest(file.file_name)
        request.folder = file.folder

        response = self.viewer_api.image_get_pdf_file(request)

        self.assertTrue(response is not None)
    
    def test_image_get_pdf_file_from_url(self):
        """
        Test case for image_get_pdf_file_from_url

        Downloads document at provided URL as PDF.  Document will be retrieved from the passed URL and added to Storage.  # noqa: E501
        """
        file = TestFile.from_url_one_page_docx()

        request = ImageGetPdfFileFromUrlRequest(file.url)
        request.folder = "tests\\from_url"

        response = self.viewer_api.image_get_pdf_file_from_url(request)

        self.assertTrue(response is not None)

    def test_image_create_pdf_file(self):
        """
        Test case for image_create_pdf_file

        Creates PDF document.  Removes PDF document if it was created before.  # noqa: E501
        """
        file = TestFile.password_protected_docx()

        pdf_file_options = PdfFileOptions()
        pdf_file_options.password = file.password

        request = ImageCreatePdfFileRequest(file.file_name)
        request.folder = file.folder
        request.pdf_file_options = pdf_file_options

        response = self.viewer_api.image_create_pdf_file(request)

        self.assertTrue(response.file_name != "")
        self.assertTrue(response.folder != "")
        self.assertTrue(response.pdf_file_name != "")

    def test_image_create_pdf_file_from_content(self):
        """
        Test case for image_create_pdf_file_from_content

        Creates PDF document from document passed in request body and saves it in cache. Content with document or multipart content is expected where first part is document and second is PdfFileOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501
        """
        file = TestFile.password_protected_docx()

        pdf_file_options = PdfFileOptions()
        pdf_file_options.password = file.password

        file_content = self.get_test_file_path(file)
        options_json = self.to_json_file(pdf_file_options)

        request = ImageCreatePdfFileFromContentRequest(file_content, options_json)
        request.folder = "tests\\from_content"

        response = self.viewer_api.image_create_pdf_file_from_content(request)

        self.assertTrue(response.file_name != "")
        self.assertTrue(response.folder != "")
        self.assertTrue(response.pdf_file_name != "")

    def test_image_create_pdf_file_from_url(self):
        """
        Test case for image_create_pdf_file_from_url

        Creates PDF document for document at provided URL and saves it in cache.  Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file. Expects PdfFileOptions object data in request body.  # noqa: E501
        """
        file = TestFile.from_url_with_notes_pptx()

        pdf_file_options = PdfFileOptions()
        pdf_file_options.slides_options = SlidesOptions()
        pdf_file_options.slides_options.render_notes = True

        request = ImageCreatePdfFileFromUrlRequest(file.url)
        request.pdf_file_options = pdf_file_options
        request.folder = "tests\\from_url"

        response = self.viewer_api.image_create_pdf_file_from_url(request)

        self.assertTrue(response.file_name != "")
        self.assertTrue(response.folder != "")
        self.assertTrue(response.pdf_file_name != "")

if __name__ == '__main__':
    unittest.main()
