# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Tile.py">
#   Copyright (c) 2003-2024 Aspose Pty Ltd
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

class Tile(object):
    """
    Represents drawing region
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_point_x': 'int',
        'start_point_y': 'int',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'start_point_x': 'StartPointX',
        'start_point_y': 'StartPointY',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, start_point_x=None, start_point_y=None, width=None, height=None, **kwargs):  # noqa: E501
        """Initializes new instance of Tile"""  # noqa: E501

        self._start_point_x = None
        self._start_point_y = None
        self._width = None
        self._height = None

        if start_point_x is not None:
            self.start_point_x = start_point_x
        if start_point_y is not None:
            self.start_point_y = start_point_y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
    
    @property
    def start_point_x(self):
        """
        Gets the start_point_x.  # noqa: E501

        The X coordinate of the lowest left point on the drawing where the tile begins  # noqa: E501

        :return: The start_point_x.  # noqa: E501
        :rtype: int
        """
        return self._start_point_x

    @start_point_x.setter
    def start_point_x(self, start_point_x):
        """
        Sets the start_point_x.

        The X coordinate of the lowest left point on the drawing where the tile begins  # noqa: E501

        :param start_point_x: The start_point_x.  # noqa: E501
        :type: int
        """
        if start_point_x is None:
            raise ValueError("Invalid value for `start_point_x`, must not be `None`")  # noqa: E501
        self._start_point_x = start_point_x
    
    @property
    def start_point_y(self):
        """
        Gets the start_point_y.  # noqa: E501

        The Y coordinate of the lowest left point on the drawing where the tile begins  # noqa: E501

        :return: The start_point_y.  # noqa: E501
        :rtype: int
        """
        return self._start_point_y

    @start_point_y.setter
    def start_point_y(self, start_point_y):
        """
        Sets the start_point_y.

        The Y coordinate of the lowest left point on the drawing where the tile begins  # noqa: E501

        :param start_point_y: The start_point_y.  # noqa: E501
        :type: int
        """
        if start_point_y is None:
            raise ValueError("Invalid value for `start_point_y`, must not be `None`")  # noqa: E501
        self._start_point_y = start_point_y
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        The width of the tile in pixels  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        The width of the tile in pixels  # noqa: E501

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

        The height of the tile in pixels  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        The height of the tile in pixels  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
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
        if not isinstance(other, Tile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
