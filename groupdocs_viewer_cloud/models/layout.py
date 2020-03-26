# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Layout.py">
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

class Layout(object):
    """
    Represents layout contained by the CAD drawing
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'width': 'float',
        'height': 'float'
    }

    attribute_map = {
        'name': 'Name',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, name=None, width=None, height=None, **kwargs):  # noqa: E501
        """Initializes new instance of Layout"""  # noqa: E501

        self._name = None
        self._width = None
        self._height = None

        if name is not None:
            self.name = name
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
    
    @property
    def name(self):
        """
        Gets the name.  # noqa: E501

        The name of the layout  # noqa: E501

        :return: The name.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name.

        The name of the layout  # noqa: E501

        :param name: The name.  # noqa: E501
        :type: str
        """
        self._name = name
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        The width of the layout  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        The width of the layout  # noqa: E501

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

        The height of the layout  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        The height of the layout  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height

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
        if not isinstance(other, Layout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
