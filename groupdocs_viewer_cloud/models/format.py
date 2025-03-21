# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Format.py">
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

class Format(object):
    """
    File-format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'extension': 'str',
        'file_format': 'str'
    }

    attribute_map = {
        'extension': 'Extension',
        'file_format': 'FileFormat'
    }

    def __init__(self, extension=None, file_format=None, **kwargs):  # noqa: E501
        """Initializes new instance of Format"""  # noqa: E501

        self._extension = None
        self._file_format = None

        if extension is not None:
            self.extension = extension
        if file_format is not None:
            self.file_format = file_format
    
    @property
    def extension(self):
        """
        Gets the extension.  # noqa: E501

        File extension  # noqa: E501

        :return: The extension.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension.

        File extension  # noqa: E501

        :param extension: The extension.  # noqa: E501
        :type: str
        """
        self._extension = extension
    
    @property
    def file_format(self):
        """
        Gets the file_format.  # noqa: E501

        File format  # noqa: E501

        :return: The file_format.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """
        Sets the file_format.

        File format  # noqa: E501

        :param file_format: The file_format.  # noqa: E501
        :type: str
        """
        self._file_format = file_format

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
        if not isinstance(other, Format):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
