# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="image_get_attachment_page_request.py">
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

class ImageGetAttachmentPageRequest(object):
    """
    Request model for image_get_attachment_page operation.
    :param file_name The file name.
    :param attachment_name Name of the attachment.
    :param page_number The attachment page number.
    :param format The image format (jpg, png or bmp). Default value is png.
    :param width The image width.
    :param height The image height.
    :param quality The image quality for jpg format. Default value is 90.
    :param password The document password.
    :param attachment_password The attachment password.
    :param extract_text When this options is set to true text contained in document will be extracted and returned along with other information.
    :param render_comments Allows to render document comments.
    :param render_hidden_pages Enables rendering of document hidden pages, sheets or slides.
    :param default_font_name The name of the default font.
    :param fonts_folder The folder with custom fonts in storage.
    :param folder The folder which contains specified file in storage.
    :param storage The file storage which have to be used.
    """

    def __init__(self, file_name, attachment_name, page_number, format=None, width=None, height=None, quality=None, password=None, attachment_password=None, extract_text=None, render_comments=None, render_hidden_pages=None, default_font_name=None, fonts_folder=None, folder=None, storage=None):
        """Initializes new instance of ImageGetAttachmentPageRequest."""  # noqa: E501
        self.file_name = file_name
        self.attachment_name = attachment_name
        self.page_number = page_number
        self.format = format
        self.width = width
        self.height = height
        self.quality = quality
        self.password = password
        self.attachment_password = attachment_password
        self.extract_text = extract_text
        self.render_comments = render_comments
        self.render_hidden_pages = render_hidden_pages
        self.default_font_name = default_font_name
        self.fonts_folder = fonts_folder
        self.folder = folder
        self.storage = storage
