# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PageRotation.py">
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

class PageRotation(object):
    """
    Clockwise page rotation 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_number': 'int',
        'rotation_angle': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'rotation_angle': 'RotationAngle'
    }

    def __init__(self, page_number=None, rotation_angle=None, **kwargs):  # noqa: E501
        """Initializes new instance of PageRotation"""  # noqa: E501

        self._page_number = None
        self._rotation_angle = None

        if page_number is not None:
            self.page_number = page_number
        if rotation_angle is not None:
            self.rotation_angle = rotation_angle
    
    @property
    def page_number(self):
        """
        Gets the page_number.  # noqa: E501

        Page number to rotate  # noqa: E501

        :return: The page_number.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number.

        Page number to rotate  # noqa: E501

        :param page_number: The page_number.  # noqa: E501
        :type: int
        """
        if page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501
        self._page_number = page_number
    
    @property
    def rotation_angle(self):
        """
        Gets the rotation_angle.  # noqa: E501

        Rotation angle  # noqa: E501

        :return: The rotation_angle.  # noqa: E501
        :rtype: str
        """
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """
        Sets the rotation_angle.

        Rotation angle  # noqa: E501

        :param rotation_angle: The rotation_angle.  # noqa: E501
        :type: str
        """
        if rotation_angle is None:
            raise ValueError("Invalid value for `rotation_angle`, must not be `None`")  # noqa: E501
        allowed_values = ["On90Degree", "On180Degree", "On270Degree"]  # noqa: E501
        if not rotation_angle.isdigit():	
            if rotation_angle not in allowed_values:
                raise ValueError(
                    "Invalid value for `rotation_angle` ({0}), must be one of {1}"  # noqa: E501
                    .format(rotation_angle, allowed_values))
            self._rotation_angle = rotation_angle
        else:
            self._rotation_angle = allowed_values[int(rotation_angle) if six.PY3 else long(rotation_angle)]

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
        if not isinstance(other, PageRotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
