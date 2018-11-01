# coding: utf-8

# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="html_get_pages_from_url_request.py">
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

class HtmlGetPagesFromUrlRequest(object):
    """
    Request model for html_get_pages_from_url operation.
    :param url The URL to retrieve document.
    :param file_name The file name.
    :param resource_path The HTML resource path.
    :param ignore_resource_path_in_resources When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
    :param embed_resources Whether to embed HTML resources or save them separate.
    :param enable_minification Enables content (HTML, CSS and SVG) minification.
    :param enable_responsive_rendering Indicates whether rendering will provide responsive web pages, that look well on different device types.
    :param exclude_fonts Prevents adding fonts to the output HTML document.
    :param start_page_number The starting document page number to render.
    :param count_pages The count of document pages to render.
    :param password The document password.
    :param render_comments Allows to render document comments.
    :param render_hidden_pages Enables rendering of document hidden pages, sheets or slides.
    :param default_font_name The name of the default font.
    :param fonts_folder The folder with custom fonts in storage.
    :param folder The folder which contains specified file in storage.
    :param storage The file storage which have to be used.
    """

    def __init__(self, url, file_name=None, resource_path=None, ignore_resource_path_in_resources=None, embed_resources=None, enable_minification=None, enable_responsive_rendering=None, exclude_fonts=None, start_page_number=None, count_pages=None, password=None, render_comments=None, render_hidden_pages=None, default_font_name=None, fonts_folder=None, folder=None, storage=None):
        """Initializes new instance of HtmlGetPagesFromUrlRequest."""  # noqa: E501
        self.url = url
        self.file_name = file_name
        self.resource_path = resource_path
        self.ignore_resource_path_in_resources = ignore_resource_path_in_resources
        self.embed_resources = embed_resources
        self.enable_minification = enable_minification
        self.enable_responsive_rendering = enable_responsive_rendering
        self.exclude_fonts = exclude_fonts
        self.start_page_number = start_page_number
        self.count_pages = count_pages
        self.password = password
        self.render_comments = render_comments
        self.render_hidden_pages = render_hidden_pages
        self.default_font_name = default_font_name
        self.fonts_folder = fonts_folder
        self.folder = folder
        self.storage = storage
