# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PageInfo.py">
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

class PageInfo(object):
    """
    Page information.
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
        'name': 'str',
        'width': 'int',
        'height': 'int',
        'angle': 'int',
        'visible': 'bool',
        'rows': 'list[RowInfo]'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name',
        'width': 'width',
        'height': 'height',
        'angle': 'angle',
        'visible': 'visible',
        'rows': 'rows'
    }

    def __init__(self, number=None, name=None, width=None, height=None, angle=None, visible=None, rows=None, **kwargs):  # noqa: E501
        """Initializes new instance of PageInfo"""  # noqa: E501

        self._number = None
        self._name = None
        self._width = None
        self._height = None
        self._angle = None
        self._visible = None
        self._rows = None

        if number is not None:
            self.number = number
        if name is not None:
            self.name = name
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if angle is not None:
            self.angle = angle
        if visible is not None:
            self.visible = visible
        if rows is not None:
            self.rows = rows
    
    @property
    def number(self):
        """
        Gets the number.  # noqa: E501

        Page number.  # noqa: E501

        :return: The number.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number.

        Page number.  # noqa: E501

        :param number: The number.  # noqa: E501
        :type: int
        """
        self._number = number
    
    @property
    def name(self):
        """
        Gets the name.  # noqa: E501

        Page name.  # noqa: E501

        :return: The name.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name.

        Page name.  # noqa: E501

        :param name: The name.  # noqa: E501
        :type: str
        """
        self._name = name
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Page width.  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Page width.  # noqa: E501

        :param width: The width.  # noqa: E501
        :type: int
        """
        self._width = width
    
    @property
    def height(self):
        """
        Gets the height.  # noqa: E501

        Page height.  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Page height.  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        self._height = height
    
    @property
    def angle(self):
        """
        Gets the angle.  # noqa: E501

        Page angle.  # noqa: E501

        :return: The angle.  # noqa: E501
        :rtype: int
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """
        Sets the angle.

        Page angle.  # noqa: E501

        :param angle: The angle.  # noqa: E501
        :type: int
        """
        self._angle = angle
    
    @property
    def visible(self):
        """
        Gets the visible.  # noqa: E501

        Page visibility.  # noqa: E501

        :return: The visible.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible.

        Page visibility.  # noqa: E501

        :param visible: The visible.  # noqa: E501
        :type: bool
        """
        self._visible = visible
    
    @property
    def rows(self):
        """
        Gets the rows.  # noqa: E501

        Page rows.  # noqa: E501

        :return: The rows.  # noqa: E501
        :rtype: list[RowInfo]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows.

        Page rows.  # noqa: E501

        :param rows: The rows.  # noqa: E501
        :type: list[RowInfo]
        """
        self._rows = rows

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
