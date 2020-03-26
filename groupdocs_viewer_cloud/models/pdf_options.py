# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfOptions.py">
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

from groupdocs_viewer_cloud.models import RenderOptions

class PdfOptions(RenderOptions):
    """
    Options for rendering document into PDF
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'jpg_quality': 'int',
        'document_open_password': 'str',
        'permissions_password': 'str',
        'permissions': 'str'
    }

    attribute_map = {
        'jpg_quality': 'JpgQuality',
        'document_open_password': 'DocumentOpenPassword',
        'permissions_password': 'PermissionsPassword',
        'permissions': 'Permissions'
    }

    def __init__(self, jpg_quality=None, document_open_password=None, permissions_password=None, permissions=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfOptions"""  # noqa: E501

        self._jpg_quality = None
        self._document_open_password = None
        self._permissions_password = None
        self._permissions = None

        if jpg_quality is not None:
            self.jpg_quality = jpg_quality
        if document_open_password is not None:
            self.document_open_password = document_open_password
        if permissions_password is not None:
            self.permissions_password = permissions_password
        if permissions is not None:
            self.permissions = permissions

        base = super(PdfOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def jpg_quality(self):
        """
        Gets the jpg_quality.  # noqa: E501

        The quality of the JPG images contained by output PDF document; Valid values are between 1 and 100; Default value is 90  # noqa: E501

        :return: The jpg_quality.  # noqa: E501
        :rtype: int
        """
        return self._jpg_quality

    @jpg_quality.setter
    def jpg_quality(self, jpg_quality):
        """
        Sets the jpg_quality.

        The quality of the JPG images contained by output PDF document; Valid values are between 1 and 100; Default value is 90  # noqa: E501

        :param jpg_quality: The jpg_quality.  # noqa: E501
        :type: int
        """
        if jpg_quality is None:
            raise ValueError("Invalid value for `jpg_quality`, must not be `None`")  # noqa: E501
        self._jpg_quality = jpg_quality
    
    @property
    def document_open_password(self):
        """
        Gets the document_open_password.  # noqa: E501

        The password required to open the PDF document  # noqa: E501

        :return: The document_open_password.  # noqa: E501
        :rtype: str
        """
        return self._document_open_password

    @document_open_password.setter
    def document_open_password(self, document_open_password):
        """
        Sets the document_open_password.

        The password required to open the PDF document  # noqa: E501

        :param document_open_password: The document_open_password.  # noqa: E501
        :type: str
        """
        self._document_open_password = document_open_password
    
    @property
    def permissions_password(self):
        """
        Gets the permissions_password.  # noqa: E501

        The password required to change permission settings; Using a permissions password  you can restrict printing, modification and data extraction  # noqa: E501

        :return: The permissions_password.  # noqa: E501
        :rtype: str
        """
        return self._permissions_password

    @permissions_password.setter
    def permissions_password(self, permissions_password):
        """
        Sets the permissions_password.

        The password required to change permission settings; Using a permissions password  you can restrict printing, modification and data extraction  # noqa: E501

        :param permissions_password: The permissions_password.  # noqa: E501
        :type: str
        """
        self._permissions_password = permissions_password
    
    @property
    def permissions(self):
        """
        Gets the permissions.  # noqa: E501

        The PDF document permissions such as printing, modification and data extraction  # noqa: E501

        :return: The permissions.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions.

        The PDF document permissions such as printing, modification and data extraction  # noqa: E501

        :param permissions: The permissions.  # noqa: E501
        :type: str
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501
        allowed_values = ["AllowAll", "DenyPrinting", "DenyModification", "DenyDataExtraction", "DenyAll"]  # noqa: E501
        if not permissions.isdigit():	
            if permissions not in allowed_values:
                raise ValueError(
                    "Invalid value for `permissions` ({0}), must be one of {1}"  # noqa: E501
                    .format(permissions, allowed_values))
            self._permissions = permissions
        else:
            self._permissions = allowed_values[int(permissions) if six.PY3 else long(permissions)]

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
        if not isinstance(other, PdfOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
