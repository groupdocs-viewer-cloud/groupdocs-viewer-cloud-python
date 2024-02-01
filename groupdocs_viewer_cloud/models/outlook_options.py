# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="OutlookOptions.py">
#   Copyright (c) 2003-2024 Aspose Pty Ltd
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

class OutlookOptions(object):
    """
    Provides options for rendering Outlook data files
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
        'text_filter': 'str',
        'address_filter': 'str',
        'max_items_in_folder': 'int'
    }

    attribute_map = {
        'folder': 'Folder',
        'text_filter': 'TextFilter',
        'address_filter': 'AddressFilter',
        'max_items_in_folder': 'MaxItemsInFolder'
    }

    def __init__(self, folder=None, text_filter=None, address_filter=None, max_items_in_folder=None, **kwargs):  # noqa: E501
        """Initializes new instance of OutlookOptions"""  # noqa: E501

        self._folder = None
        self._text_filter = None
        self._address_filter = None
        self._max_items_in_folder = None

        if folder is not None:
            self.folder = folder
        if text_filter is not None:
            self.text_filter = text_filter
        if address_filter is not None:
            self.address_filter = address_filter
        if max_items_in_folder is not None:
            self.max_items_in_folder = max_items_in_folder
    
    @property
    def folder(self):
        """
        Gets the folder.  # noqa: E501

        The name of the folder (e.g. Inbox, Sent Item or Deleted Items) to render  # noqa: E501

        :return: The folder.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """
        Sets the folder.

        The name of the folder (e.g. Inbox, Sent Item or Deleted Items) to render  # noqa: E501

        :param folder: The folder.  # noqa: E501
        :type: str
        """
        self._folder = folder
    
    @property
    def text_filter(self):
        """
        Gets the text_filter.  # noqa: E501

        The keywords used to filter messages  # noqa: E501

        :return: The text_filter.  # noqa: E501
        :rtype: str
        """
        return self._text_filter

    @text_filter.setter
    def text_filter(self, text_filter):
        """
        Sets the text_filter.

        The keywords used to filter messages  # noqa: E501

        :param text_filter: The text_filter.  # noqa: E501
        :type: str
        """
        self._text_filter = text_filter
    
    @property
    def address_filter(self):
        """
        Gets the address_filter.  # noqa: E501

        The email-address used to filter messages by sender or recipient  # noqa: E501

        :return: The address_filter.  # noqa: E501
        :rtype: str
        """
        return self._address_filter

    @address_filter.setter
    def address_filter(self, address_filter):
        """
        Sets the address_filter.

        The email-address used to filter messages by sender or recipient  # noqa: E501

        :param address_filter: The address_filter.  # noqa: E501
        :type: str
        """
        self._address_filter = address_filter
    
    @property
    def max_items_in_folder(self):
        """
        Gets the max_items_in_folder.  # noqa: E501

        The maximum number of messages or items, that can be rendered from one folder  # noqa: E501

        :return: The max_items_in_folder.  # noqa: E501
        :rtype: int
        """
        return self._max_items_in_folder

    @max_items_in_folder.setter
    def max_items_in_folder(self, max_items_in_folder):
        """
        Sets the max_items_in_folder.

        The maximum number of messages or items, that can be rendered from one folder  # noqa: E501

        :param max_items_in_folder: The max_items_in_folder.  # noqa: E501
        :type: int
        """
        if max_items_in_folder is None:
            raise ValueError("Invalid value for `max_items_in_folder`, must not be `None`")  # noqa: E501
        self._max_items_in_folder = max_items_in_folder

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
        if not isinstance(other, OutlookOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
