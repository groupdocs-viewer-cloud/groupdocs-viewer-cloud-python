# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="TextElement.py">
#   Copyright (c) Aspose Pty Ltd
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

class TextElement(object):
    """
    Text element
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'x': 'float',
        'y': 'float',
        'width': 'float',
        'height': 'float',
        'value': 'str'
    }

    attribute_map = {
        'x': 'X',
        'y': 'Y',
        'width': 'Width',
        'height': 'Height',
        'value': 'Value'
    }

    def __init__(self, x=None, y=None, width=None, height=None, value=None, **kwargs):  # noqa: E501
        """Initializes new instance of TextElement"""  # noqa: E501

        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self._value = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if value is not None:
            self.value = value
    
    @property
    def x(self):
        """
        Gets the x.  # noqa: E501

        The X coordinate of the highest left point on the page layout where the rectangle that contains element begins.               # noqa: E501

        :return: The x.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x.

        The X coordinate of the highest left point on the page layout where the rectangle that contains element begins.               # noqa: E501

        :param x: The x.  # noqa: E501
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501
        self._x = x
    
    @property
    def y(self):
        """
        Gets the y.  # noqa: E501

        The Y coordinate of the highest left point on the page layout where the rectangle that contains element begins.               # noqa: E501

        :return: The y.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y.

        The Y coordinate of the highest left point on the page layout where the rectangle that contains element begins.               # noqa: E501

        :param y: The y.  # noqa: E501
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501
        self._y = y
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        The width of the rectangle which contains the element (in pixels).                # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        The width of the rectangle which contains the element (in pixels).                # noqa: E501

        :param width: The width.  # noqa: E501
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
        self._width = width
    
    @property
    def height(self):
        """
        Gets the height.  # noqa: E501

        The height of the rectangle which contains the element (in pixels).                # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        The height of the rectangle which contains the element (in pixels).                # noqa: E501

        :param height: The height.  # noqa: E501
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def value(self):
        """
        Gets the value.  # noqa: E501

        The element value  # noqa: E501

        :return: The value.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value.

        The element value  # noqa: E501

        :param value: The value.  # noqa: E501
        :type: str
        """
        self._value = value

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
        if not isinstance(other, TextElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
