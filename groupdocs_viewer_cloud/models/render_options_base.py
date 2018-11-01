# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="RenderOptionsBase.py">
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

import pprint
import re  # noqa: F401

import six

class RenderOptionsBase(object):
    """
    Base render options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'password': 'str',
        'attachment_password': 'str',
        'extract_text': 'bool',
        'render_comments': 'bool',
        'render_hidden_pages': 'bool',
        'transforms': 'list[str]',
        'default_font_name': 'str',
        'watermark': 'Watermark',
        'cells_options': 'CellsOptions',
        'cad_options': 'CadOptions',
        'email_options': 'EmailOptions',
        'words_options': 'WordsOptions',
        'pdf_options': 'PdfOptions',
        'slides_options': 'SlidesOptions',
        'project_options': 'ProjectOptions'
    }

    attribute_map = {
        'password': 'password',
        'attachment_password': 'attachmentPassword',
        'extract_text': 'extractText',
        'render_comments': 'renderComments',
        'render_hidden_pages': 'renderHiddenPages',
        'transforms': 'transforms',
        'default_font_name': 'defaultFontName',
        'watermark': 'watermark',
        'cells_options': 'cellsOptions',
        'cad_options': 'cadOptions',
        'email_options': 'emailOptions',
        'words_options': 'wordsOptions',
        'pdf_options': 'pdfOptions',
        'slides_options': 'slidesOptions',
        'project_options': 'projectOptions'
    }

    def __init__(self, password=None, attachment_password=None, extract_text=None, render_comments=None, render_hidden_pages=None, transforms=None, default_font_name=None, watermark=None, cells_options=None, cad_options=None, email_options=None, words_options=None, pdf_options=None, slides_options=None, project_options=None, **kwargs):  # noqa: E501
        """Initializes new instance of RenderOptionsBase"""  # noqa: E501

        self._password = None
        self._attachment_password = None
        self._extract_text = None
        self._render_comments = None
        self._render_hidden_pages = None
        self._transforms = None
        self._default_font_name = None
        self._watermark = None
        self._cells_options = None
        self._cad_options = None
        self._email_options = None
        self._words_options = None
        self._pdf_options = None
        self._slides_options = None
        self._project_options = None

        if password is not None:
            self.password = password
        if attachment_password is not None:
            self.attachment_password = attachment_password
        if extract_text is not None:
            self.extract_text = extract_text
        if render_comments is not None:
            self.render_comments = render_comments
        if render_hidden_pages is not None:
            self.render_hidden_pages = render_hidden_pages
        if transforms is not None:
            self.transforms = transforms
        if default_font_name is not None:
            self.default_font_name = default_font_name
        if watermark is not None:
            self.watermark = watermark
        if cells_options is not None:
            self.cells_options = cells_options
        if cad_options is not None:
            self.cad_options = cad_options
        if email_options is not None:
            self.email_options = email_options
        if words_options is not None:
            self.words_options = words_options
        if pdf_options is not None:
            self.pdf_options = pdf_options
        if slides_options is not None:
            self.slides_options = slides_options
        if project_options is not None:
            self.project_options = project_options
    
    @property
    def password(self):
        """
        Gets the password.  # noqa: E501

        Allows to specify document password in case when document is password-protected.  # noqa: E501

        :return: The password.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password.

        Allows to specify document password in case when document is password-protected.  # noqa: E501

        :param password: The password.  # noqa: E501
        :type: str
        """
        self._password = password
    
    @property
    def attachment_password(self):
        """
        Gets the attachment_password.  # noqa: E501

        Allows to specify attachment password in case when attachment is password-protected.  # noqa: E501

        :return: The attachment_password.  # noqa: E501
        :rtype: str
        """
        return self._attachment_password

    @attachment_password.setter
    def attachment_password(self, attachment_password):
        """
        Sets the attachment_password.

        Allows to specify attachment password in case when attachment is password-protected.  # noqa: E501

        :param attachment_password: The attachment_password.  # noqa: E501
        :type: str
        """
        self._attachment_password = attachment_password
    
    @property
    def extract_text(self):
        """
        Gets the extract_text.  # noqa: E501

        Enables document text extraction. For rendering document as image only.  # noqa: E501

        :return: The extract_text.  # noqa: E501
        :rtype: bool
        """
        return self._extract_text

    @extract_text.setter
    def extract_text(self, extract_text):
        """
        Sets the extract_text.

        Enables document text extraction. For rendering document as image only.  # noqa: E501

        :param extract_text: The extract_text.  # noqa: E501
        :type: bool
        """
        self._extract_text = extract_text
    
    @property
    def render_comments(self):
        """
        Gets the render_comments.  # noqa: E501

        Enables document comments rendering.  # noqa: E501

        :return: The render_comments.  # noqa: E501
        :rtype: bool
        """
        return self._render_comments

    @render_comments.setter
    def render_comments(self, render_comments):
        """
        Sets the render_comments.

        Enables document comments rendering.  # noqa: E501

        :param render_comments: The render_comments.  # noqa: E501
        :type: bool
        """
        self._render_comments = render_comments
    
    @property
    def render_hidden_pages(self):
        """
        Gets the render_hidden_pages.  # noqa: E501

        Enables rendering of document hidden pages, sheets or slides.  # noqa: E501

        :return: The render_hidden_pages.  # noqa: E501
        :rtype: bool
        """
        return self._render_hidden_pages

    @render_hidden_pages.setter
    def render_hidden_pages(self, render_hidden_pages):
        """
        Sets the render_hidden_pages.

        Enables rendering of document hidden pages, sheets or slides.  # noqa: E501

        :param render_hidden_pages: The render_hidden_pages.  # noqa: E501
        :type: bool
        """
        self._render_hidden_pages = render_hidden_pages
    
    @property
    def transforms(self):
        """
        Gets the transforms.  # noqa: E501

        Transforms to apply. Available transforms [\"Rotate\",\"Reorder\",\"AddPrintAction\"]. 1. Rotate - pages will be rotated on angle if angle was set before. 2. Reorder - for rendering document as PDF only. Pages will be ordered according to rearrangements made before. 3. AddPrintAction - for rendering document as PDF only. An JavaScript action will be added which opens print dialog when PDF document is opened.     # noqa: E501

        :return: The transforms.  # noqa: E501
        :rtype: list[str]
        """
        return self._transforms

    @transforms.setter
    def transforms(self, transforms):
        """
        Sets the transforms.

        Transforms to apply. Available transforms [\"Rotate\",\"Reorder\",\"AddPrintAction\"]. 1. Rotate - pages will be rotated on angle if angle was set before. 2. Reorder - for rendering document as PDF only. Pages will be ordered according to rearrangements made before. 3. AddPrintAction - for rendering document as PDF only. An JavaScript action will be added which opens print dialog when PDF document is opened.     # noqa: E501

        :param transforms: The transforms.  # noqa: E501
        :type: list[str]
        """
        self._transforms = transforms
    
    @property
    def default_font_name(self):
        """
        Gets the default_font_name.  # noqa: E501

        The name of the default font. Default font name may be specified in following cases: - You want to generally specify the default font to fall back on, if particular font   in the document cannot be found during rendering. - Your document uses fonts, that contain non-English characters and you want to make sure   any missing font is replaced with one that has the same character set available.  # noqa: E501

        :return: The default_font_name.  # noqa: E501
        :rtype: str
        """
        return self._default_font_name

    @default_font_name.setter
    def default_font_name(self, default_font_name):
        """
        Sets the default_font_name.

        The name of the default font. Default font name may be specified in following cases: - You want to generally specify the default font to fall back on, if particular font   in the document cannot be found during rendering. - Your document uses fonts, that contain non-English characters and you want to make sure   any missing font is replaced with one that has the same character set available.  # noqa: E501

        :param default_font_name: The default_font_name.  # noqa: E501
        :type: str
        """
        self._default_font_name = default_font_name
    
    @property
    def watermark(self):
        """
        Gets the watermark.  # noqa: E501

        Allows to specify watermark.  # noqa: E501

        :return: The watermark.  # noqa: E501
        :rtype: Watermark
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """
        Sets the watermark.

        Allows to specify watermark.  # noqa: E501

        :param watermark: The watermark.  # noqa: E501
        :type: Watermark
        """
        self._watermark = watermark
    
    @property
    def cells_options(self):
        """
        Gets the cells_options.  # noqa: E501

        The Spreadsheet documents rendering options.  # noqa: E501

        :return: The cells_options.  # noqa: E501
        :rtype: CellsOptions
        """
        return self._cells_options

    @cells_options.setter
    def cells_options(self, cells_options):
        """
        Sets the cells_options.

        The Spreadsheet documents rendering options.  # noqa: E501

        :param cells_options: The cells_options.  # noqa: E501
        :type: CellsOptions
        """
        self._cells_options = cells_options
    
    @property
    def cad_options(self):
        """
        Gets the cad_options.  # noqa: E501

        The CAD documents rendering options.  # noqa: E501

        :return: The cad_options.  # noqa: E501
        :rtype: CadOptions
        """
        return self._cad_options

    @cad_options.setter
    def cad_options(self, cad_options):
        """
        Sets the cad_options.

        The CAD documents rendering options.  # noqa: E501

        :param cad_options: The cad_options.  # noqa: E501
        :type: CadOptions
        """
        self._cad_options = cad_options
    
    @property
    def email_options(self):
        """
        Gets the email_options.  # noqa: E501

        The Email documents rendering options.  # noqa: E501

        :return: The email_options.  # noqa: E501
        :rtype: EmailOptions
        """
        return self._email_options

    @email_options.setter
    def email_options(self, email_options):
        """
        Sets the email_options.

        The Email documents rendering options.  # noqa: E501

        :param email_options: The email_options.  # noqa: E501
        :type: EmailOptions
        """
        self._email_options = email_options
    
    @property
    def words_options(self):
        """
        Gets the words_options.  # noqa: E501

        The Text documents rendering options.  # noqa: E501

        :return: The words_options.  # noqa: E501
        :rtype: WordsOptions
        """
        return self._words_options

    @words_options.setter
    def words_options(self, words_options):
        """
        Sets the words_options.

        The Text documents rendering options.  # noqa: E501

        :param words_options: The words_options.  # noqa: E501
        :type: WordsOptions
        """
        self._words_options = words_options
    
    @property
    def pdf_options(self):
        """
        Gets the pdf_options.  # noqa: E501

        The PDF documents rendering options.  # noqa: E501

        :return: The pdf_options.  # noqa: E501
        :rtype: PdfOptions
        """
        return self._pdf_options

    @pdf_options.setter
    def pdf_options(self, pdf_options):
        """
        Sets the pdf_options.

        The PDF documents rendering options.  # noqa: E501

        :param pdf_options: The pdf_options.  # noqa: E501
        :type: PdfOptions
        """
        self._pdf_options = pdf_options
    
    @property
    def slides_options(self):
        """
        Gets the slides_options.  # noqa: E501

        The Presentation documents rendering options.  # noqa: E501

        :return: The slides_options.  # noqa: E501
        :rtype: SlidesOptions
        """
        return self._slides_options

    @slides_options.setter
    def slides_options(self, slides_options):
        """
        Sets the slides_options.

        The Presentation documents rendering options.  # noqa: E501

        :param slides_options: The slides_options.  # noqa: E501
        :type: SlidesOptions
        """
        self._slides_options = slides_options
    
    @property
    def project_options(self):
        """
        Gets the project_options.  # noqa: E501

        The Microsoft Project documents rendering options.  # noqa: E501

        :return: The project_options.  # noqa: E501
        :rtype: ProjectOptions
        """
        return self._project_options

    @project_options.setter
    def project_options(self, project_options):
        """
        Sets the project_options.

        The Microsoft Project documents rendering options.  # noqa: E501

        :param project_options: The project_options.  # noqa: E501
        :type: ProjectOptions
        """
        self._project_options = project_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RenderOptionsBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
