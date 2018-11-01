# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="RowInfo.py">
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

class RowInfo(object):
    """
    The page text row information.
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
        'row_left': 'float',
        'row_top': 'float',
        'row_width': 'float',
        'row_height': 'float',
        'text_coordinates': 'list[float]',
        'character_coordinates': 'list[float]'
    }

    attribute_map = {
        'text': 'text',
        'row_left': 'rowLeft',
        'row_top': 'rowTop',
        'row_width': 'rowWidth',
        'row_height': 'rowHeight',
        'text_coordinates': 'textCoordinates',
        'character_coordinates': 'characterCoordinates'
    }

    def __init__(self, text=None, row_left=None, row_top=None, row_width=None, row_height=None, text_coordinates=None, character_coordinates=None, **kwargs):  # noqa: E501
        """Initializes new instance of RowInfo"""  # noqa: E501

        self._text = None
        self._row_left = None
        self._row_top = None
        self._row_width = None
        self._row_height = None
        self._text_coordinates = None
        self._character_coordinates = None

        if text is not None:
            self.text = text
        if row_left is not None:
            self.row_left = row_left
        if row_top is not None:
            self.row_top = row_top
        if row_width is not None:
            self.row_width = row_width
        if row_height is not None:
            self.row_height = row_height
        if text_coordinates is not None:
            self.text_coordinates = text_coordinates
        if character_coordinates is not None:
            self.character_coordinates = character_coordinates
    
    @property
    def text(self):
        """
        Gets the text.  # noqa: E501

        Row text.  # noqa: E501

        :return: The text.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text.

        Row text.  # noqa: E501

        :param text: The text.  # noqa: E501
        :type: str
        """
        self._text = text
    
    @property
    def row_left(self):
        """
        Gets the row_left.  # noqa: E501

        Row left coordinate.  # noqa: E501

        :return: The row_left.  # noqa: E501
        :rtype: float
        """
        return self._row_left

    @row_left.setter
    def row_left(self, row_left):
        """
        Sets the row_left.

        Row left coordinate.  # noqa: E501

        :param row_left: The row_left.  # noqa: E501
        :type: float
        """
        self._row_left = row_left
    
    @property
    def row_top(self):
        """
        Gets the row_top.  # noqa: E501

        Row top coordinate.  # noqa: E501

        :return: The row_top.  # noqa: E501
        :rtype: float
        """
        return self._row_top

    @row_top.setter
    def row_top(self, row_top):
        """
        Sets the row_top.

        Row top coordinate.  # noqa: E501

        :param row_top: The row_top.  # noqa: E501
        :type: float
        """
        self._row_top = row_top
    
    @property
    def row_width(self):
        """
        Gets the row_width.  # noqa: E501

        Row width.  # noqa: E501

        :return: The row_width.  # noqa: E501
        :rtype: float
        """
        return self._row_width

    @row_width.setter
    def row_width(self, row_width):
        """
        Sets the row_width.

        Row width.  # noqa: E501

        :param row_width: The row_width.  # noqa: E501
        :type: float
        """
        self._row_width = row_width
    
    @property
    def row_height(self):
        """
        Gets the row_height.  # noqa: E501

        Row height.  # noqa: E501

        :return: The row_height.  # noqa: E501
        :rtype: float
        """
        return self._row_height

    @row_height.setter
    def row_height(self, row_height):
        """
        Sets the row_height.

        Row height.  # noqa: E501

        :param row_height: The row_height.  # noqa: E501
        :type: float
        """
        self._row_height = row_height
    
    @property
    def text_coordinates(self):
        """
        Gets the text_coordinates.  # noqa: E501

        Text coordinates.  # noqa: E501

        :return: The text_coordinates.  # noqa: E501
        :rtype: list[float]
        """
        return self._text_coordinates

    @text_coordinates.setter
    def text_coordinates(self, text_coordinates):
        """
        Sets the text_coordinates.

        Text coordinates.  # noqa: E501

        :param text_coordinates: The text_coordinates.  # noqa: E501
        :type: list[float]
        """
        self._text_coordinates = text_coordinates
    
    @property
    def character_coordinates(self):
        """
        Gets the character_coordinates.  # noqa: E501

        Characters coordinates.  # noqa: E501

        :return: The character_coordinates.  # noqa: E501
        :rtype: list[float]
        """
        return self._character_coordinates

    @character_coordinates.setter
    def character_coordinates(self, character_coordinates):
        """
        Sets the character_coordinates.

        Characters coordinates.  # noqa: E501

        :param character_coordinates: The character_coordinates.  # noqa: E501
        :type: list[float]
        """
        self._character_coordinates = character_coordinates

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
        if not isinstance(other, RowInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
