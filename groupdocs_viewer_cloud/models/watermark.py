# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Watermark.py">
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

class Watermark(object):
    """
    Text watermark
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text': 'str',
        'color': 'str',
        'position': 'str',
        'size': 'int'
    }

    attribute_map = {
        'text': 'Text',
        'color': 'Color',
        'position': 'Position',
        'size': 'Size'
    }

    def __init__(self, text=None, color=None, position=None, size=None, **kwargs):  # noqa: E501
        """Initializes new instance of Watermark"""  # noqa: E501

        self._text = None
        self._color = None
        self._position = None
        self._size = None

        if text is not None:
            self.text = text
        if color is not None:
            self.color = color
        if position is not None:
            self.position = position
        if size is not None:
            self.size = size
    
    @property
    def text(self):
        """
        Gets the text.  # noqa: E501

        Watermark text.  # noqa: E501

        :return: The text.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text.

        Watermark text.  # noqa: E501

        :param text: The text.  # noqa: E501
        :type: str
        """
        self._text = text
    
    @property
    def color(self):
        """
        Gets the color.  # noqa: E501

        Watermark color. Supported formats {Magenta|(112,222,11)|(50,112,222,11)}. Default value is \"Red\".  # noqa: E501

        :return: The color.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color.

        Watermark color. Supported formats {Magenta|(112,222,11)|(50,112,222,11)}. Default value is \"Red\".  # noqa: E501

        :param color: The color.  # noqa: E501
        :type: str
        """
        self._color = color
    
    @property
    def position(self):
        """
        Gets the position.  # noqa: E501

        Watermark position. Default value is \"Diagonal\".  # noqa: E501

        :return: The position.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position.

        Watermark position. Default value is \"Diagonal\".  # noqa: E501

        :param position: The position.  # noqa: E501
        :type: str
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501
        allowed_values = ["Diagonal", "TopLeft", "TopCenter", "TopRight", "BottomLeft", "BottomCenter", "BottomRight"]  # noqa: E501
        if not position.isdigit():	
            if position not in allowed_values:
                raise ValueError(
                    "Invalid value for `position` ({0}), must be one of {1}"  # noqa: E501
                    .format(position, allowed_values))
            self._position = position
        else:
            self._position = allowed_values[int(position) if six.PY3 else long(position)]
    
    @property
    def size(self):
        """
        Gets the size.  # noqa: E501

        Watermark size in percents. Default value is 100.  # noqa: E501

        :return: The size.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size.

        Watermark size in percents. Default value is 100.  # noqa: E501

        :param size: The size.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        self._size = size

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
        if not isinstance(other, Watermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
