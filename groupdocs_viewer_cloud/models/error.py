# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Error.py">
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

class Error(object):
    """
    Error
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'message': 'str',
        'description': 'str',
        'inner_error': 'ErrorDetails'
    }

    attribute_map = {
        'code': 'Code',
        'message': 'Message',
        'description': 'Description',
        'inner_error': 'InnerError'
    }

    def __init__(self, code=None, message=None, description=None, inner_error=None, **kwargs):  # noqa: E501
        """Initializes new instance of Error"""  # noqa: E501

        self._code = None
        self._message = None
        self._description = None
        self._inner_error = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if description is not None:
            self.description = description
        if inner_error is not None:
            self.inner_error = inner_error
    
    @property
    def code(self):
        """
        Gets the code.  # noqa: E501

        Code               # noqa: E501

        :return: The code.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code.

        Code               # noqa: E501

        :param code: The code.  # noqa: E501
        :type: str
        """
        self._code = code
    
    @property
    def message(self):
        """
        Gets the message.  # noqa: E501

        Message               # noqa: E501

        :return: The message.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message.

        Message               # noqa: E501

        :param message: The message.  # noqa: E501
        :type: str
        """
        self._message = message
    
    @property
    def description(self):
        """
        Gets the description.  # noqa: E501

        Description               # noqa: E501

        :return: The description.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description.

        Description               # noqa: E501

        :param description: The description.  # noqa: E501
        :type: str
        """
        self._description = description
    
    @property
    def inner_error(self):
        """
        Gets the inner_error.  # noqa: E501

        Inner Error               # noqa: E501

        :return: The inner_error.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._inner_error

    @inner_error.setter
    def inner_error(self, inner_error):
        """
        Sets the inner_error.

        Inner Error               # noqa: E501

        :param inner_error: The inner_error.  # noqa: E501
        :type: ErrorDetails
        """
        self._inner_error = inner_error

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
