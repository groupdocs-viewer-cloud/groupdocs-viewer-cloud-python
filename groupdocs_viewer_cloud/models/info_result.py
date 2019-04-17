# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="InfoResult.py">
#   Copyright (c) 2003-2019 Aspose Pty Ltd
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

class InfoResult(object):
    """
    View result information
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pages': 'list[PageInfo]',
        'attachments': 'list[AttachmentInfo]'
    }

    attribute_map = {
        'pages': 'Pages',
        'attachments': 'Attachments'
    }

    def __init__(self, pages=None, attachments=None, **kwargs):  # noqa: E501
        """Initializes new instance of InfoResult"""  # noqa: E501

        self._pages = None
        self._attachments = None

        if pages is not None:
            self.pages = pages
        if attachments is not None:
            self.attachments = attachments
    
    @property
    def pages(self):
        """
        Gets the pages.  # noqa: E501

        View result pages  # noqa: E501

        :return: The pages.  # noqa: E501
        :rtype: list[PageInfo]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages.

        View result pages  # noqa: E501

        :param pages: The pages.  # noqa: E501
        :type: list[PageInfo]
        """
        self._pages = pages
    
    @property
    def attachments(self):
        """
        Gets the attachments.  # noqa: E501

        Attachments  # noqa: E501

        :return: The attachments.  # noqa: E501
        :rtype: list[AttachmentInfo]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments.

        Attachments  # noqa: E501

        :param attachments: The attachments.  # noqa: E501
        :type: list[AttachmentInfo]
        """
        self._attachments = attachments

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
        if not isinstance(other, InfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other