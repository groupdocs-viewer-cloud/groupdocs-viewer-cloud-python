# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="CellsOptions.py">
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

class CellsOptions(object):
    """
    The Spreadsheet documents rendering options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'render_grid_lines': 'bool',
        'paginate_sheets': 'bool',
        'count_rows_per_page': 'int',
        'ignore_empty_rows': 'bool',
        'encoding': 'str',
        'internal_hyperlink_prefix': 'str',
        'text_overflow_mode': 'str',
        'render_hidden_rows': 'bool',
        'render_hidden_columns': 'bool',
        'render_print_area_only': 'bool'
    }

    attribute_map = {
        'render_grid_lines': 'renderGridLines',
        'paginate_sheets': 'paginateSheets',
        'count_rows_per_page': 'countRowsPerPage',
        'ignore_empty_rows': 'ignoreEmptyRows',
        'encoding': 'encoding',
        'internal_hyperlink_prefix': 'internalHyperlinkPrefix',
        'text_overflow_mode': 'textOverflowMode',
        'render_hidden_rows': 'renderHiddenRows',
        'render_hidden_columns': 'renderHiddenColumns',
        'render_print_area_only': 'renderPrintAreaOnly'
    }

    def __init__(self, render_grid_lines=None, paginate_sheets=None, count_rows_per_page=None, ignore_empty_rows=None, encoding=None, internal_hyperlink_prefix=None, text_overflow_mode=None, render_hidden_rows=None, render_hidden_columns=None, render_print_area_only=None, **kwargs):  # noqa: E501
        """Initializes new instance of CellsOptions"""  # noqa: E501

        self._render_grid_lines = None
        self._paginate_sheets = None
        self._count_rows_per_page = None
        self._ignore_empty_rows = None
        self._encoding = None
        self._internal_hyperlink_prefix = None
        self._text_overflow_mode = None
        self._render_hidden_rows = None
        self._render_hidden_columns = None
        self._render_print_area_only = None

        if render_grid_lines is not None:
            self.render_grid_lines = render_grid_lines
        if paginate_sheets is not None:
            self.paginate_sheets = paginate_sheets
        if count_rows_per_page is not None:
            self.count_rows_per_page = count_rows_per_page
        if ignore_empty_rows is not None:
            self.ignore_empty_rows = ignore_empty_rows
        if encoding is not None:
            self.encoding = encoding
        if internal_hyperlink_prefix is not None:
            self.internal_hyperlink_prefix = internal_hyperlink_prefix
        if text_overflow_mode is not None:
            self.text_overflow_mode = text_overflow_mode
        if render_hidden_rows is not None:
            self.render_hidden_rows = render_hidden_rows
        if render_hidden_columns is not None:
            self.render_hidden_columns = render_hidden_columns
        if render_print_area_only is not None:
            self.render_print_area_only = render_print_area_only
    
    @property
    def render_grid_lines(self):
        """
        Gets the render_grid_lines.  # noqa: E501

        Indicates whether to render grid lines.  # noqa: E501

        :return: The render_grid_lines.  # noqa: E501
        :rtype: bool
        """
        return self._render_grid_lines

    @render_grid_lines.setter
    def render_grid_lines(self, render_grid_lines):
        """
        Sets the render_grid_lines.

        Indicates whether to render grid lines.  # noqa: E501

        :param render_grid_lines: The render_grid_lines.  # noqa: E501
        :type: bool
        """
        self._render_grid_lines = render_grid_lines
    
    @property
    def paginate_sheets(self):
        """
        Gets the paginate_sheets.  # noqa: E501

        Allows to enable worksheets pagination. By default one worksheet is rendered into one page.  # noqa: E501

        :return: The paginate_sheets.  # noqa: E501
        :rtype: bool
        """
        return self._paginate_sheets

    @paginate_sheets.setter
    def paginate_sheets(self, paginate_sheets):
        """
        Sets the paginate_sheets.

        Allows to enable worksheets pagination. By default one worksheet is rendered into one page.  # noqa: E501

        :param paginate_sheets: The paginate_sheets.  # noqa: E501
        :type: bool
        """
        self._paginate_sheets = paginate_sheets
    
    @property
    def count_rows_per_page(self):
        """
        Gets the count_rows_per_page.  # noqa: E501

        The number of rows rendered into one page when PaginateSheets = true. Default value is 50.  # noqa: E501

        :return: The count_rows_per_page.  # noqa: E501
        :rtype: int
        """
        return self._count_rows_per_page

    @count_rows_per_page.setter
    def count_rows_per_page(self, count_rows_per_page):
        """
        Sets the count_rows_per_page.

        The number of rows rendered into one page when PaginateSheets = true. Default value is 50.  # noqa: E501

        :param count_rows_per_page: The count_rows_per_page.  # noqa: E501
        :type: int
        """
        self._count_rows_per_page = count_rows_per_page
    
    @property
    def ignore_empty_rows(self):
        """
        Gets the ignore_empty_rows.  # noqa: E501

        Indicates whether empty rows should be ignored.  # noqa: E501

        :return: The ignore_empty_rows.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_empty_rows

    @ignore_empty_rows.setter
    def ignore_empty_rows(self, ignore_empty_rows):
        """
        Sets the ignore_empty_rows.

        Indicates whether empty rows should be ignored.  # noqa: E501

        :param ignore_empty_rows: The ignore_empty_rows.  # noqa: E501
        :type: bool
        """
        self._ignore_empty_rows = ignore_empty_rows
    
    @property
    def encoding(self):
        """
        Gets the encoding.  # noqa: E501

        The text (*.csv) document encoding.  # noqa: E501

        :return: The encoding.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding.

        The text (*.csv) document encoding.  # noqa: E501

        :param encoding: The encoding.  # noqa: E501
        :type: str
        """
        self._encoding = encoding
    
    @property
    def internal_hyperlink_prefix(self):
        """
        Gets the internal_hyperlink_prefix.  # noqa: E501

        Prefix for hyper-link that references worksheet inside the same document. For rendering document as HTML only.  # noqa: E501

        :return: The internal_hyperlink_prefix.  # noqa: E501
        :rtype: str
        """
        return self._internal_hyperlink_prefix

    @internal_hyperlink_prefix.setter
    def internal_hyperlink_prefix(self, internal_hyperlink_prefix):
        """
        Sets the internal_hyperlink_prefix.

        Prefix for hyper-link that references worksheet inside the same document. For rendering document as HTML only.  # noqa: E501

        :param internal_hyperlink_prefix: The internal_hyperlink_prefix.  # noqa: E501
        :type: str
        """
        self._internal_hyperlink_prefix = internal_hyperlink_prefix
    
    @property
    def text_overflow_mode(self):
        """
        Gets the text_overflow_mode.  # noqa: E501

        Text overflow mode applied when the text is too big to fit into the cell. Supported values {Overlay|OverlayIfNextIsEmpty|HideText|AutoFitColumn}: 1. Overlay - overlay next cells even they are not empty. 2. OverlayIfNextIsEmpty - overlay next cells only if they are not empty (default). 3. HideText - hide overflow text. 4. AutoFitColumn - expand cell width to fit overflowed text.  # noqa: E501

        :return: The text_overflow_mode.  # noqa: E501
        :rtype: str
        """
        return self._text_overflow_mode

    @text_overflow_mode.setter
    def text_overflow_mode(self, text_overflow_mode):
        """
        Sets the text_overflow_mode.

        Text overflow mode applied when the text is too big to fit into the cell. Supported values {Overlay|OverlayIfNextIsEmpty|HideText|AutoFitColumn}: 1. Overlay - overlay next cells even they are not empty. 2. OverlayIfNextIsEmpty - overlay next cells only if they are not empty (default). 3. HideText - hide overflow text. 4. AutoFitColumn - expand cell width to fit overflowed text.  # noqa: E501

        :param text_overflow_mode: The text_overflow_mode.  # noqa: E501
        :type: str
        """
        self._text_overflow_mode = text_overflow_mode
    
    @property
    def render_hidden_rows(self):
        """
        Gets the render_hidden_rows.  # noqa: E501

        Enables rendering of hidden rows.  # noqa: E501

        :return: The render_hidden_rows.  # noqa: E501
        :rtype: bool
        """
        return self._render_hidden_rows

    @render_hidden_rows.setter
    def render_hidden_rows(self, render_hidden_rows):
        """
        Sets the render_hidden_rows.

        Enables rendering of hidden rows.  # noqa: E501

        :param render_hidden_rows: The render_hidden_rows.  # noqa: E501
        :type: bool
        """
        self._render_hidden_rows = render_hidden_rows
    
    @property
    def render_hidden_columns(self):
        """
        Gets the render_hidden_columns.  # noqa: E501

        Enables rendering of hidden columns.  # noqa: E501

        :return: The render_hidden_columns.  # noqa: E501
        :rtype: bool
        """
        return self._render_hidden_columns

    @render_hidden_columns.setter
    def render_hidden_columns(self, render_hidden_columns):
        """
        Sets the render_hidden_columns.

        Enables rendering of hidden columns.  # noqa: E501

        :param render_hidden_columns: The render_hidden_columns.  # noqa: E501
        :type: bool
        """
        self._render_hidden_columns = render_hidden_columns
    
    @property
    def render_print_area_only(self):
        """
        Gets the render_print_area_only.  # noqa: E501

        Enables rendering worksheet(s) sections which is defined as print area. Renders each print area in a worksheet as a separate page.  # noqa: E501

        :return: The render_print_area_only.  # noqa: E501
        :rtype: bool
        """
        return self._render_print_area_only

    @render_print_area_only.setter
    def render_print_area_only(self, render_print_area_only):
        """
        Sets the render_print_area_only.

        Enables rendering worksheet(s) sections which is defined as print area. Renders each print area in a worksheet as a separate page.  # noqa: E501

        :param render_print_area_only: The render_print_area_only.  # noqa: E501
        :type: bool
        """
        self._render_print_area_only = render_print_area_only

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
        if not isinstance(other, CellsOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
