# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="html_get_attachment_page_request.py">
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

class HtmlGetAttachmentPageRequest(object):
    """
    Request model for html_get_attachment_page operation.
    :param file_name The document name.
    :param attachment_name Name of the attachment.
    :param page_number The attachment page number.
    :param resource_path The attachment page HTML resource path.
    :param ignore_resource_path_in_resources When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
    :param embed_resources Whether to embed HTML resources or save them separate.
    :param enable_minification Enables content (HTML, CSS and SVG) minification.
    :param enable_responsive_rendering Indicates whether rendering will provide responsive web pages, that look well on different device types.
    :param exclude_fonts Prevents adding fonts to the output HTML document.
    :param render_comments Allows to render document comments.
    :param render_hidden_pages Enables rendering of document hidden pages, sheets or slides.
    :param password The document password.
    :param attachment_password The attachment password.
    :param default_font_name The name of the default font.
    :param fonts_folder The folder with custom fonts in storage.
    :param folder The folder which contains specified file in storage.
    :param storage The file storage which have to be used.
    """

    def __init__(self, file_name, attachment_name, page_number, resource_path=None, ignore_resource_path_in_resources=None, embed_resources=None, enable_minification=None, enable_responsive_rendering=None, exclude_fonts=None, render_comments=None, render_hidden_pages=None, password=None, attachment_password=None, default_font_name=None, fonts_folder=None, folder=None, storage=None):
        """Initializes new instance of HtmlGetAttachmentPageRequest."""  # noqa: E501
        self.file_name = file_name
        self.attachment_name = attachment_name
        self.page_number = page_number
        self.resource_path = resource_path
        self.ignore_resource_path_in_resources = ignore_resource_path_in_resources
        self.embed_resources = embed_resources
        self.enable_minification = enable_minification
        self.enable_responsive_rendering = enable_responsive_rendering
        self.exclude_fonts = exclude_fonts
        self.render_comments = render_comments
        self.render_hidden_pages = render_hidden_pages
        self.password = password
        self.attachment_password = attachment_password
        self.default_font_name = default_font_name
        self.fonts_folder = fonts_folder
        self.folder = folder
        self.storage = storage
