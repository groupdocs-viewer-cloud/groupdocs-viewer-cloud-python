# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PageInfo.py">
#   Copyright (c) 2003-2020 Aspose Pty Ltd
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

class PageInfo(object):
    """
    Page information
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'number': 'int',
        'width': 'int',
        'height': 'int',
        'visible': 'bool',
        'lines': 'list[Line]'
    }

    attribute_map = {
        'number': 'Number',
        'width': 'Width',
        'height': 'Height',
        'visible': 'Visible',
        'lines': 'Lines'
    }

    def __init__(self, number=None, width=None, height=None, visible=None, lines=None, **kwargs):  # noqa: E501
        """Initializes new instance of PageInfo"""  # noqa: E501

        self._number = None
        self._width = None
        self._height = None
        self._visible = None
        self._lines = None

        if number is not None:
            self.number = number
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if visible is not None:
            self.visible = visible
        if lines is not None:
            self.lines = lines
    
    @property
    def number(self):
        """
        Gets the number.  # noqa: E501

        The page number  # noqa: E501

        :return: The number.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number.

        The page number  # noqa: E501

        :param number: The number.  # noqa: E501
        :type: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        self._number = number
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        The width of the page in pixels when viewing as JPG or PNG  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        The width of the page in pixels when viewing as JPG or PNG  # noqa: E501

        :param width: The width.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
        self._width = width
    
    @property
    def height(self):
        """
        Gets the height.  # noqa: E501

        The height of the page in pixels when viewing as JPG or PNG  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        The height of the page in pixels when viewing as JPG or PNG  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def visible(self):
        """
        Gets the visible.  # noqa: E501

        The page visibility indicator  # noqa: E501

        :return: The visible.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible.

        The page visibility indicator  # noqa: E501

        :param visible: The visible.  # noqa: E501
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")  # noqa: E501
        self._visible = visible
    
    @property
    def lines(self):
        """
        Gets the lines.  # noqa: E501

        The lines contained by the page when viewing as JPG or PNG with enabled Text Extraction  # noqa: E501

        :return: The lines.  # noqa: E501
        :rtype: list[Line]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines.

        The lines contained by the page when viewing as JPG or PNG with enabled Text Extraction  # noqa: E501

        :param lines: The lines.  # noqa: E501
        :type: list[Line]
        """
        self._lines = lines

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
        if not isinstance(other, PageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
