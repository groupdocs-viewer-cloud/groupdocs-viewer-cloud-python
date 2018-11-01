# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="html_get_page_resource_request.py">
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

class HtmlGetPageResourceRequest(object):
    """
    Request model for html_get_page_resource operation.
    :param file_name The file name.
    :param page_number The page number.
    :param resource_name Name of the resource.
    :param folder The folder which contains specified file in storage.
    :param storage The file storage which have to be used.
    """

    def __init__(self, file_name, page_number, resource_name, folder=None, storage=None):
        """Initializes new instance of HtmlGetPageResourceRequest."""  # noqa: E501
        self.file_name = file_name
        self.page_number = page_number
        self.resource_name = resource_name
        self.folder = folder
        self.storage = storage
