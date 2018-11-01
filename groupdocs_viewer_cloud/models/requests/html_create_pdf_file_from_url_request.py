# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="html_create_pdf_file_from_url_request.py">
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
# --------------------------------------------------------------------------------

class HtmlCreatePdfFileFromUrlRequest(object):
    """
    Request model for html_create_pdf_file_from_url operation.
    :param url The URL to retrieve document.
    :param pdf_file_options The PDF file rendering.
    :param file_name The file name.
    :param fonts_folder The folder with custom fonts in storage.
    :param folder The folder which contains specified file in storage.
    :param storage The file storage which have to be used.
    """

    def __init__(self, url, pdf_file_options=None, file_name=None, fonts_folder=None, folder=None, storage=None):
        """Initializes new instance of HtmlCreatePdfFileFromUrlRequest."""  # noqa: E501
        self.url = url
        self.pdf_file_options = pdf_file_options
        self.file_name = file_name
        self.fonts_folder = fonts_folder
        self.folder = folder
        self.storage = storage
