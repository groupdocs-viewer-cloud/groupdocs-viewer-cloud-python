# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="RenderOptions.py">
#   Copyright (c) 2003-2021 Aspose Pty Ltd
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

class RenderOptions(object):
    """
    Rendering options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_page_number': 'int',
        'count_pages_to_render': 'int',
        'pages_to_render': 'list[int]',
        'page_rotations': 'list[PageRotation]',
        'default_font_name': 'str',
        'default_encoding': 'str',
        'render_comments': 'bool',
        'render_notes': 'bool',
        'render_hidden_pages': 'bool',
        'spreadsheet_options': 'SpreadsheetOptions',
        'cad_options': 'CadOptions',
        'email_options': 'EmailOptions',
        'project_management_options': 'ProjectManagementOptions',
        'pdf_document_options': 'PdfDocumentOptions',
        'word_processing_options': 'WordProcessingOptions',
        'outlook_options': 'OutlookOptions',
        'archive_options': 'ArchiveOptions'
    }

    attribute_map = {
        'start_page_number': 'StartPageNumber',
        'count_pages_to_render': 'CountPagesToRender',
        'pages_to_render': 'PagesToRender',
        'page_rotations': 'PageRotations',
        'default_font_name': 'DefaultFontName',
        'default_encoding': 'DefaultEncoding',
        'render_comments': 'RenderComments',
        'render_notes': 'RenderNotes',
        'render_hidden_pages': 'RenderHiddenPages',
        'spreadsheet_options': 'SpreadsheetOptions',
        'cad_options': 'CadOptions',
        'email_options': 'EmailOptions',
        'project_management_options': 'ProjectManagementOptions',
        'pdf_document_options': 'PdfDocumentOptions',
        'word_processing_options': 'WordProcessingOptions',
        'outlook_options': 'OutlookOptions',
        'archive_options': 'ArchiveOptions'
    }

    def __init__(self, start_page_number=None, count_pages_to_render=None, pages_to_render=None, page_rotations=None, default_font_name=None, default_encoding=None, render_comments=None, render_notes=None, render_hidden_pages=None, spreadsheet_options=None, cad_options=None, email_options=None, project_management_options=None, pdf_document_options=None, word_processing_options=None, outlook_options=None, archive_options=None, **kwargs):  # noqa: E501
        """Initializes new instance of RenderOptions"""  # noqa: E501

        self._start_page_number = None
        self._count_pages_to_render = None
        self._pages_to_render = None
        self._page_rotations = None
        self._default_font_name = None
        self._default_encoding = None
        self._render_comments = None
        self._render_notes = None
        self._render_hidden_pages = None
        self._spreadsheet_options = None
        self._cad_options = None
        self._email_options = None
        self._project_management_options = None
        self._pdf_document_options = None
        self._word_processing_options = None
        self._outlook_options = None
        self._archive_options = None

        if start_page_number is not None:
            self.start_page_number = start_page_number
        if count_pages_to_render is not None:
            self.count_pages_to_render = count_pages_to_render
        if pages_to_render is not None:
            self.pages_to_render = pages_to_render
        if page_rotations is not None:
            self.page_rotations = page_rotations
        if default_font_name is not None:
            self.default_font_name = default_font_name
        if default_encoding is not None:
            self.default_encoding = default_encoding
        if render_comments is not None:
            self.render_comments = render_comments
        if render_notes is not None:
            self.render_notes = render_notes
        if render_hidden_pages is not None:
            self.render_hidden_pages = render_hidden_pages
        if spreadsheet_options is not None:
            self.spreadsheet_options = spreadsheet_options
        if cad_options is not None:
            self.cad_options = cad_options
        if email_options is not None:
            self.email_options = email_options
        if project_management_options is not None:
            self.project_management_options = project_management_options
        if pdf_document_options is not None:
            self.pdf_document_options = pdf_document_options
        if word_processing_options is not None:
            self.word_processing_options = word_processing_options
        if outlook_options is not None:
            self.outlook_options = outlook_options
        if archive_options is not None:
            self.archive_options = archive_options
    
    @property
    def start_page_number(self):
        """
        Gets the start_page_number.  # noqa: E501

        Page number from which rendering should be started  # noqa: E501

        :return: The start_page_number.  # noqa: E501
        :rtype: int
        """
        return self._start_page_number

    @start_page_number.setter
    def start_page_number(self, start_page_number):
        """
        Sets the start_page_number.

        Page number from which rendering should be started  # noqa: E501

        :param start_page_number: The start_page_number.  # noqa: E501
        :type: int
        """
        if start_page_number is None:
            raise ValueError("Invalid value for `start_page_number`, must not be `None`")  # noqa: E501
        self._start_page_number = start_page_number
    
    @property
    def count_pages_to_render(self):
        """
        Gets the count_pages_to_render.  # noqa: E501

        Count pages which should be rendered  # noqa: E501

        :return: The count_pages_to_render.  # noqa: E501
        :rtype: int
        """
        return self._count_pages_to_render

    @count_pages_to_render.setter
    def count_pages_to_render(self, count_pages_to_render):
        """
        Sets the count_pages_to_render.

        Count pages which should be rendered  # noqa: E501

        :param count_pages_to_render: The count_pages_to_render.  # noqa: E501
        :type: int
        """
        if count_pages_to_render is None:
            raise ValueError("Invalid value for `count_pages_to_render`, must not be `None`")  # noqa: E501
        self._count_pages_to_render = count_pages_to_render
    
    @property
    def pages_to_render(self):
        """
        Gets the pages_to_render.  # noqa: E501

        Pages list to render. Ignored, if StartPageNumber and CountPagesToRender are provided  # noqa: E501

        :return: The pages_to_render.  # noqa: E501
        :rtype: list[int]
        """
        return self._pages_to_render

    @pages_to_render.setter
    def pages_to_render(self, pages_to_render):
        """
        Sets the pages_to_render.

        Pages list to render. Ignored, if StartPageNumber and CountPagesToRender are provided  # noqa: E501

        :param pages_to_render: The pages_to_render.  # noqa: E501
        :type: list[int]
        """
        self._pages_to_render = pages_to_render
    
    @property
    def page_rotations(self):
        """
        Gets the page_rotations.  # noqa: E501

        Page rotations  # noqa: E501

        :return: The page_rotations.  # noqa: E501
        :rtype: list[PageRotation]
        """
        return self._page_rotations

    @page_rotations.setter
    def page_rotations(self, page_rotations):
        """
        Sets the page_rotations.

        Page rotations  # noqa: E501

        :param page_rotations: The page_rotations.  # noqa: E501
        :type: list[PageRotation]
        """
        self._page_rotations = page_rotations
    
    @property
    def default_font_name(self):
        """
        Gets the default_font_name.  # noqa: E501

        Default font name may be specified in following cases: - You want to generally specify the default font to fall back on, if particular font   in the document cannot be found during rendering. - Your document uses fonts, that contain non-English characters and you want to make sure   any missing font is replaced with one that has the same character set available.  # noqa: E501

        :return: The default_font_name.  # noqa: E501
        :rtype: str
        """
        return self._default_font_name

    @default_font_name.setter
    def default_font_name(self, default_font_name):
        """
        Sets the default_font_name.

        Default font name may be specified in following cases: - You want to generally specify the default font to fall back on, if particular font   in the document cannot be found during rendering. - Your document uses fonts, that contain non-English characters and you want to make sure   any missing font is replaced with one that has the same character set available.  # noqa: E501

        :param default_font_name: The default_font_name.  # noqa: E501
        :type: str
        """
        self._default_font_name = default_font_name
    
    @property
    def default_encoding(self):
        """
        Gets the default_encoding.  # noqa: E501

        Default encoding for the plain text files such as .csv, .txt and .eml files when encoding is not specified in header  # noqa: E501

        :return: The default_encoding.  # noqa: E501
        :rtype: str
        """
        return self._default_encoding

    @default_encoding.setter
    def default_encoding(self, default_encoding):
        """
        Sets the default_encoding.

        Default encoding for the plain text files such as .csv, .txt and .eml files when encoding is not specified in header  # noqa: E501

        :param default_encoding: The default_encoding.  # noqa: E501
        :type: str
        """
        self._default_encoding = default_encoding
    
    @property
    def render_comments(self):
        """
        Gets the render_comments.  # noqa: E501

        When enabled comments will be rendered to the output  # noqa: E501

        :return: The render_comments.  # noqa: E501
        :rtype: bool
        """
        return self._render_comments

    @render_comments.setter
    def render_comments(self, render_comments):
        """
        Sets the render_comments.

        When enabled comments will be rendered to the output  # noqa: E501

        :param render_comments: The render_comments.  # noqa: E501
        :type: bool
        """
        if render_comments is None:
            raise ValueError("Invalid value for `render_comments`, must not be `None`")  # noqa: E501
        self._render_comments = render_comments
    
    @property
    def render_notes(self):
        """
        Gets the render_notes.  # noqa: E501

        When enabled notes will be rendered to the output  # noqa: E501

        :return: The render_notes.  # noqa: E501
        :rtype: bool
        """
        return self._render_notes

    @render_notes.setter
    def render_notes(self, render_notes):
        """
        Sets the render_notes.

        When enabled notes will be rendered to the output  # noqa: E501

        :param render_notes: The render_notes.  # noqa: E501
        :type: bool
        """
        if render_notes is None:
            raise ValueError("Invalid value for `render_notes`, must not be `None`")  # noqa: E501
        self._render_notes = render_notes
    
    @property
    def render_hidden_pages(self):
        """
        Gets the render_hidden_pages.  # noqa: E501

        When enabled hidden pages, sheets or slides will be rendered to the output  # noqa: E501

        :return: The render_hidden_pages.  # noqa: E501
        :rtype: bool
        """
        return self._render_hidden_pages

    @render_hidden_pages.setter
    def render_hidden_pages(self, render_hidden_pages):
        """
        Sets the render_hidden_pages.

        When enabled hidden pages, sheets or slides will be rendered to the output  # noqa: E501

        :param render_hidden_pages: The render_hidden_pages.  # noqa: E501
        :type: bool
        """
        if render_hidden_pages is None:
            raise ValueError("Invalid value for `render_hidden_pages`, must not be `None`")  # noqa: E501
        self._render_hidden_pages = render_hidden_pages
    
    @property
    def spreadsheet_options(self):
        """
        Gets the spreadsheet_options.  # noqa: E501

        Rendering options for Spreadsheet source file formats Spreadsheet file formats include files with extensions: .xls, .xlsx, .xlsm, .xlsb, .csv, .ods, .ots, .xltx, .xltm, .tsv   # noqa: E501

        :return: The spreadsheet_options.  # noqa: E501
        :rtype: SpreadsheetOptions
        """
        return self._spreadsheet_options

    @spreadsheet_options.setter
    def spreadsheet_options(self, spreadsheet_options):
        """
        Sets the spreadsheet_options.

        Rendering options for Spreadsheet source file formats Spreadsheet file formats include files with extensions: .xls, .xlsx, .xlsm, .xlsb, .csv, .ods, .ots, .xltx, .xltm, .tsv   # noqa: E501

        :param spreadsheet_options: The spreadsheet_options.  # noqa: E501
        :type: SpreadsheetOptions
        """
        self._spreadsheet_options = spreadsheet_options
    
    @property
    def cad_options(self):
        """
        Gets the cad_options.  # noqa: E501

        Rendering options for CAD source file formats CAD file formats include files with extensions: .dwg, .dxf, .dgn, .ifc, .stl  # noqa: E501

        :return: The cad_options.  # noqa: E501
        :rtype: CadOptions
        """
        return self._cad_options

    @cad_options.setter
    def cad_options(self, cad_options):
        """
        Sets the cad_options.

        Rendering options for CAD source file formats CAD file formats include files with extensions: .dwg, .dxf, .dgn, .ifc, .stl  # noqa: E501

        :param cad_options: The cad_options.  # noqa: E501
        :type: CadOptions
        """
        self._cad_options = cad_options
    
    @property
    def email_options(self):
        """
        Gets the email_options.  # noqa: E501

        Rendering options for Email source file formats Email file formats include files with extensions: .msg, .eml, .emlx, .ifc, .stl  # noqa: E501

        :return: The email_options.  # noqa: E501
        :rtype: EmailOptions
        """
        return self._email_options

    @email_options.setter
    def email_options(self, email_options):
        """
        Sets the email_options.

        Rendering options for Email source file formats Email file formats include files with extensions: .msg, .eml, .emlx, .ifc, .stl  # noqa: E501

        :param email_options: The email_options.  # noqa: E501
        :type: EmailOptions
        """
        self._email_options = email_options
    
    @property
    def project_management_options(self):
        """
        Gets the project_management_options.  # noqa: E501

        Rendering options for MS Project source file formats Project file formats include files with extensions: .mpt, .mpp  # noqa: E501

        :return: The project_management_options.  # noqa: E501
        :rtype: ProjectManagementOptions
        """
        return self._project_management_options

    @project_management_options.setter
    def project_management_options(self, project_management_options):
        """
        Sets the project_management_options.

        Rendering options for MS Project source file formats Project file formats include files with extensions: .mpt, .mpp  # noqa: E501

        :param project_management_options: The project_management_options.  # noqa: E501
        :type: ProjectManagementOptions
        """
        self._project_management_options = project_management_options
    
    @property
    def pdf_document_options(self):
        """
        Gets the pdf_document_options.  # noqa: E501

        Rendering options for PDF source file formats  # noqa: E501

        :return: The pdf_document_options.  # noqa: E501
        :rtype: PdfDocumentOptions
        """
        return self._pdf_document_options

    @pdf_document_options.setter
    def pdf_document_options(self, pdf_document_options):
        """
        Sets the pdf_document_options.

        Rendering options for PDF source file formats  # noqa: E501

        :param pdf_document_options: The pdf_document_options.  # noqa: E501
        :type: PdfDocumentOptions
        """
        self._pdf_document_options = pdf_document_options
    
    @property
    def word_processing_options(self):
        """
        Gets the word_processing_options.  # noqa: E501

        Rendering options for WordProcessing source file formats  # noqa: E501

        :return: The word_processing_options.  # noqa: E501
        :rtype: WordProcessingOptions
        """
        return self._word_processing_options

    @word_processing_options.setter
    def word_processing_options(self, word_processing_options):
        """
        Sets the word_processing_options.

        Rendering options for WordProcessing source file formats  # noqa: E501

        :param word_processing_options: The word_processing_options.  # noqa: E501
        :type: WordProcessingOptions
        """
        self._word_processing_options = word_processing_options
    
    @property
    def outlook_options(self):
        """
        Gets the outlook_options.  # noqa: E501

        Rendering options for Outlook source file formats  # noqa: E501

        :return: The outlook_options.  # noqa: E501
        :rtype: OutlookOptions
        """
        return self._outlook_options

    @outlook_options.setter
    def outlook_options(self, outlook_options):
        """
        Sets the outlook_options.

        Rendering options for Outlook source file formats  # noqa: E501

        :param outlook_options: The outlook_options.  # noqa: E501
        :type: OutlookOptions
        """
        self._outlook_options = outlook_options
    
    @property
    def archive_options(self):
        """
        Gets the archive_options.  # noqa: E501

        Rendering options for Archive source file formats  # noqa: E501

        :return: The archive_options.  # noqa: E501
        :rtype: ArchiveOptions
        """
        return self._archive_options

    @archive_options.setter
    def archive_options(self, archive_options):
        """
        Sets the archive_options.

        Rendering options for Archive source file formats  # noqa: E501

        :param archive_options: The archive_options.  # noqa: E501
        :type: ArchiveOptions
        """
        self._archive_options = archive_options

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
        if not isinstance(other, RenderOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
