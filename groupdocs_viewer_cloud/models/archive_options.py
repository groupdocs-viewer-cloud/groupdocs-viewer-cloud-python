# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ArchiveOptions.py">
#   Copyright (c) 2003-2023 Aspose Pty Ltd
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

class ArchiveOptions(object):
    """
    Provides options for rendering archive files
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'folder': 'str',
        'file_name': 'str',
        'items_per_page': 'int'
    }

    attribute_map = {
        'folder': 'Folder',
        'file_name': 'FileName',
        'items_per_page': 'ItemsPerPage'
    }

    def __init__(self, folder=None, file_name=None, items_per_page=None, **kwargs):  # noqa: E501
        """Initializes new instance of ArchiveOptions"""  # noqa: E501

        self._folder = None
        self._file_name = None
        self._items_per_page = None

        if folder is not None:
            self.folder = folder
        if file_name is not None:
            self.file_name = file_name
        if items_per_page is not None:
            self.items_per_page = items_per_page
    
    @property
    def folder(self):
        """
        Gets the folder.  # noqa: E501

        The folder inside the archive to be rendered  # noqa: E501

        :return: The folder.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder.

        The folder inside the archive to be rendered  # noqa: E501

        :param folder: The folder.  # noqa: E501
        :type: str
        """
        self._folder = folder
    
    @property
    def file_name(self):
        """
        Gets the file_name.  # noqa: E501

        The filename to display in the header. By default the name of the source file is displayed.  # noqa: E501

        :return: The file_name.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name.

        The filename to display in the header. By default the name of the source file is displayed.  # noqa: E501

        :param file_name: The file_name.  # noqa: E501
        :type: str
        """
        self._file_name = file_name
    
    @property
    def items_per_page(self):
        """
        Gets the items_per_page.  # noqa: E501

        Number of records per page (for rendering to HTML only)               # noqa: E501

        :return: The items_per_page.  # noqa: E501
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """
        Sets the items_per_page.

        Number of records per page (for rendering to HTML only)               # noqa: E501

        :param items_per_page: The items_per_page.  # noqa: E501
        :type: int
        """
        if items_per_page is None:
            raise ValueError("Invalid value for `items_per_page`, must not be `None`")  # noqa: E501
        self._items_per_page = items_per_page

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
        if not isinstance(other, ArchiveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
