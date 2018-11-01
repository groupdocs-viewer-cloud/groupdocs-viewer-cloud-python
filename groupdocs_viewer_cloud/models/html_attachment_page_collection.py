# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="HtmlAttachmentPageCollection.py">
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

class HtmlAttachmentPageCollection(object):
    """
    Describes attachment pages.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_name': 'str',
        'folder': 'str',
        'attachment_name': 'str',
        'pages': 'list[HtmlPage]'
    }

    attribute_map = {
        'file_name': 'fileName',
        'folder': 'folder',
        'attachment_name': 'attachmentName',
        'pages': 'pages'
    }

    def __init__(self, file_name=None, folder=None, attachment_name=None, pages=None, **kwargs):  # noqa: E501
        """Initializes new instance of HtmlAttachmentPageCollection"""  # noqa: E501

        self._file_name = None
        self._folder = None
        self._attachment_name = None
        self._pages = None

        if file_name is not None:
            self.file_name = file_name
        if folder is not None:
            self.folder = folder
        if attachment_name is not None:
            self.attachment_name = attachment_name
        if pages is not None:
            self.pages = pages
    
    @property
    def file_name(self):
        """
        Gets the file_name.  # noqa: E501

        The file name.  # noqa: E501

        :return: The file_name.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name.

        The file name.  # noqa: E501

        :param file_name: The file_name.  # noqa: E501
        :type: str
        """
        self._file_name = file_name
    
    @property
    def folder(self):
        """
        Gets the folder.  # noqa: E501

        File folder.  # noqa: E501

        :return: The folder.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder.

        File folder.  # noqa: E501

        :param folder: The folder.  # noqa: E501
        :type: str
        """
        self._folder = folder
    
    @property
    def attachment_name(self):
        """
        Gets the attachment_name.  # noqa: E501

        Attachment name.  # noqa: E501

        :return: The attachment_name.  # noqa: E501
        :rtype: str
        """
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, attachment_name):
        """
        Sets the attachment_name.

        Attachment name.  # noqa: E501

        :param attachment_name: The attachment_name.  # noqa: E501
        :type: str
        """
        self._attachment_name = attachment_name
    
    @property
    def pages(self):
        """
        Gets the pages.  # noqa: E501

        Pages list.  # noqa: E501

        :return: The pages.  # noqa: E501
        :rtype: list[HtmlPage]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages.

        Pages list.  # noqa: E501

        :param pages: The pages.  # noqa: E501
        :type: list[HtmlPage]
        """
        self._pages = pages

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
        if not isinstance(other, HtmlAttachmentPageCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
