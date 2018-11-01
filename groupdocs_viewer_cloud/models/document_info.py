# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="DocumentInfo.py">
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

class DocumentInfo(object):
    """
    Describes document information.
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
        'extension': 'str',
        'file_format': 'str',
        'size': 'int',
        'date_modified': 'datetime',
        'pages': 'list[PageInfo]',
        'attachments': 'list[AttachmentInfo]',
        'layers': 'list[str]'
    }

    attribute_map = {
        'file_name': 'fileName',
        'extension': 'extension',
        'file_format': 'fileFormat',
        'size': 'size',
        'date_modified': 'dateModified',
        'pages': 'pages',
        'attachments': 'attachments',
        'layers': 'layers'
    }

    def __init__(self, file_name=None, extension=None, file_format=None, size=None, date_modified=None, pages=None, attachments=None, layers=None, **kwargs):  # noqa: E501
        """Initializes new instance of DocumentInfo"""  # noqa: E501

        self._file_name = None
        self._extension = None
        self._file_format = None
        self._size = None
        self._date_modified = None
        self._pages = None
        self._attachments = None
        self._layers = None

        if file_name is not None:
            self.file_name = file_name
        if extension is not None:
            self.extension = extension
        if file_format is not None:
            self.file_format = file_format
        if size is not None:
            self.size = size
        if date_modified is not None:
            self.date_modified = date_modified
        if pages is not None:
            self.pages = pages
        if attachments is not None:
            self.attachments = attachments
        if layers is not None:
            self.layers = layers
    
    @property
    def file_name(self):
        """
        Gets the file_name.  # noqa: E501

        File name.  # noqa: E501

        :return: The file_name.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name.

        File name.  # noqa: E501

        :param file_name: The file_name.  # noqa: E501
        :type: str
        """
        self._file_name = file_name
    
    @property
    def extension(self):
        """
        Gets the extension.  # noqa: E501

        Extension  # noqa: E501

        :return: The extension.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension.

        Extension  # noqa: E501

        :param extension: The extension.  # noqa: E501
        :type: str
        """
        self._extension = extension
    
    @property
    def file_format(self):
        """
        Gets the file_format.  # noqa: E501

        File format.  # noqa: E501

        :return: The file_format.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """
        Sets the file_format.

        File format.  # noqa: E501

        :param file_format: The file_format.  # noqa: E501
        :type: str
        """
        self._file_format = file_format
    
    @property
    def size(self):
        """
        Gets the size.  # noqa: E501

        Size in bytes.  # noqa: E501

        :return: The size.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size.

        Size in bytes.  # noqa: E501

        :param size: The size.  # noqa: E501
        :type: int
        """
        self._size = size
    
    @property
    def date_modified(self):
        """
        Gets the date_modified.  # noqa: E501

        Modification date.  # noqa: E501

        :return: The date_modified.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified.

        Modification date.  # noqa: E501

        :param date_modified: The date_modified.  # noqa: E501
        :type: datetime
        """
        self._date_modified = date_modified
    
    @property
    def pages(self):
        """
        Gets the pages.  # noqa: E501

        Pages information.  # noqa: E501

        :return: The pages.  # noqa: E501
        :rtype: list[PageInfo]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages.

        Pages information.  # noqa: E501

        :param pages: The pages.  # noqa: E501
        :type: list[PageInfo]
        """
        self._pages = pages
    
    @property
    def attachments(self):
        """
        Gets the attachments.  # noqa: E501

        List of attachments.  # noqa: E501

        :return: The attachments.  # noqa: E501
        :rtype: list[AttachmentInfo]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments.

        List of attachments.  # noqa: E501

        :param attachments: The attachments.  # noqa: E501
        :type: list[AttachmentInfo]
        """
        self._attachments = attachments
    
    @property
    def layers(self):
        """
        Gets the layers.  # noqa: E501

        The list of layers contained in a CAD document.  # noqa: E501

        :return: The layers.  # noqa: E501
        :rtype: list[str]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """
        Sets the layers.

        The list of layers contained in a CAD document.  # noqa: E501

        :param layers: The layers.  # noqa: E501
        :type: list[str]
        """
        self._layers = layers

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
        if not isinstance(other, DocumentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
