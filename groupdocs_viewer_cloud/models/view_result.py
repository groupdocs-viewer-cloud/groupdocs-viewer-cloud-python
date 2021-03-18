# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ViewResult.py">
#   Copyright (c) 2003-2021 Aspose Pty Ltd
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

class ViewResult(object):
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
        'pages': 'list[PageView]',
        'attachments': 'list[AttachmentView]',
        'file': 'Resource'
    }

    attribute_map = {
        'pages': 'Pages',
        'attachments': 'Attachments',
        'file': 'File'
    }

    def __init__(self, pages=None, attachments=None, file=None, **kwargs):  # noqa: E501
        """Initializes new instance of ViewResult"""  # noqa: E501

        self._pages = None
        self._attachments = None
        self._file = None

        if pages is not None:
            self.pages = pages
        if attachments is not None:
            self.attachments = attachments
        if file is not None:
            self.file = file
    
    @property
    def pages(self):
        """
        Gets the pages.  # noqa: E501

        View result pages  # noqa: E501

        :return: The pages.  # noqa: E501
        :rtype: list[PageView]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages.

        View result pages  # noqa: E501

        :param pages: The pages.  # noqa: E501
        :type: list[PageView]
        """
        self._pages = pages
    
    @property
    def attachments(self):
        """
        Gets the attachments.  # noqa: E501

        Attachments  # noqa: E501

        :return: The attachments.  # noqa: E501
        :rtype: list[AttachmentView]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments.

        Attachments  # noqa: E501

        :param attachments: The attachments.  # noqa: E501
        :type: list[AttachmentView]
        """
        self._attachments = attachments
    
    @property
    def file(self):
        """
        Gets the file.  # noqa: E501

        ULR to retrieve file.  # noqa: E501

        :return: The file.  # noqa: E501
        :rtype: Resource
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file.

        ULR to retrieve file.  # noqa: E501

        :param file: The file.  # noqa: E501
        :type: Resource
        """
        self._file = file

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
        if not isinstance(other, ViewResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
