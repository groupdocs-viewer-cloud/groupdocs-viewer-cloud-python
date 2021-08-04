# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="TextOptions.py">
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

class TextOptions(object):
    """
    Provides options for rendering text documents
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'max_chars_per_row': 'int',
        'max_rows_per_page': 'int'
    }

    attribute_map = {
        'max_chars_per_row': 'MaxCharsPerRow',
        'max_rows_per_page': 'MaxRowsPerPage'
    }

    def __init__(self, max_chars_per_row=None, max_rows_per_page=None, **kwargs):  # noqa: E501
        """Initializes new instance of TextOptions"""  # noqa: E501

        self._max_chars_per_row = None
        self._max_rows_per_page = None

        if max_chars_per_row is not None:
            self.max_chars_per_row = max_chars_per_row
        if max_rows_per_page is not None:
            self.max_rows_per_page = max_rows_per_page
    
    @property
    def max_chars_per_row(self):
        """
        Gets the max_chars_per_row.  # noqa: E501

        Max chars per row on page. Default value is 85.  # noqa: E501

        :return: The max_chars_per_row.  # noqa: E501
        :rtype: int
        """
        return self._max_chars_per_row

    @max_chars_per_row.setter
    def max_chars_per_row(self, max_chars_per_row):
        """
        Sets the max_chars_per_row.

        Max chars per row on page. Default value is 85.  # noqa: E501

        :param max_chars_per_row: The max_chars_per_row.  # noqa: E501
        :type: int
        """
        if max_chars_per_row is None:
            raise ValueError("Invalid value for `max_chars_per_row`, must not be `None`")  # noqa: E501
        self._max_chars_per_row = max_chars_per_row
    
    @property
    def max_rows_per_page(self):
        """
        Gets the max_rows_per_page.  # noqa: E501

        Max rows per page. Default value is 55.  # noqa: E501

        :return: The max_rows_per_page.  # noqa: E501
        :rtype: int
        """
        return self._max_rows_per_page

    @max_rows_per_page.setter
    def max_rows_per_page(self, max_rows_per_page):
        """
        Sets the max_rows_per_page.

        Max rows per page. Default value is 55.  # noqa: E501

        :param max_rows_per_page: The max_rows_per_page.  # noqa: E501
        :type: int
        """
        if max_rows_per_page is None:
            raise ValueError("Invalid value for `max_rows_per_page`, must not be `None`")  # noqa: E501
        self._max_rows_per_page = max_rows_per_page

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
        if not isinstance(other, TextOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
