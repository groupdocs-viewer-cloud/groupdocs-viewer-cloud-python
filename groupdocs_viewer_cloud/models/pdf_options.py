# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfOptions.py">
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
        'permissions': 'list[str]',
        'image_max_width': 'int',
        'image_max_height': 'int',
        'image_width': 'int',
        'image_height': 'int'
    }

    attribute_map = {
        'jpg_quality': 'JpgQuality',
        'document_open_password': 'DocumentOpenPassword',
        'permissions_password': 'PermissionsPassword',
        'permissions': 'Permissions',
        'image_max_width': 'ImageMaxWidth',
        'image_max_height': 'ImageMaxHeight',
        'image_width': 'ImageWidth',
        'image_height': 'ImageHeight'
    }

    def __init__(self, jpg_quality=None, document_open_password=None, permissions_password=None, permissions=None, image_max_width=None, image_max_height=None, image_width=None, image_height=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfOptions"""  # noqa: E501

        self._jpg_quality = None
        self._document_open_password = None
        self._permissions_password = None
        self._permissions = None
        self._image_max_width = None
        self._image_max_height = None
        self._image_width = None
        self._image_height = None

        if jpg_quality is not None:
            self.jpg_quality = jpg_quality
        if document_open_password is not None:
            self.document_open_password = document_open_password
        if permissions_password is not None:
            self.permissions_password = permissions_password
        if permissions is not None:
            self.permissions = permissions
        if image_max_width is not None:
            self.image_max_width = image_max_width
        if image_max_height is not None:
            self.image_max_height = image_max_height
        if image_width is not None:
            self.image_width = image_width
        if image_height is not None:
            self.image_height = image_height

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

        The array of PDF document permissions. Allowed values are: AllowAll, DenyPrinting, DenyModification, DenyDataExtraction, DenyAll Default value is AllowAll, if now permissions are set.  # noqa: E501

        :return: The permissions.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions.

        The array of PDF document permissions. Allowed values are: AllowAll, DenyPrinting, DenyModification, DenyDataExtraction, DenyAll Default value is AllowAll, if now permissions are set.  # noqa: E501

        :param permissions: The permissions.  # noqa: E501
        :type: list[str]
        """
        self._permissions = permissions
    
    @property
    def image_max_width(self):
        """
        Gets the image_max_width.  # noqa: E501

        Max width of an output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :return: The image_max_width.  # noqa: E501
        :rtype: int
        """
        return self._image_max_width

    @image_max_width.setter
    def image_max_width(self, image_max_width):
        """
        Sets the image_max_width.

        Max width of an output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :param image_max_width: The image_max_width.  # noqa: E501
        :type: int
        """
        if image_max_width is None:
            raise ValueError("Invalid value for `image_max_width`, must not be `None`")  # noqa: E501
        self._image_max_width = image_max_width
    
    @property
    def image_max_height(self):
        """
        Gets the image_max_height.  # noqa: E501

        Max height of an output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :return: The image_max_height.  # noqa: E501
        :rtype: int
        """
        return self._image_max_height

    @image_max_height.setter
    def image_max_height(self, image_max_height):
        """
        Sets the image_max_height.

        Max height of an output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :param image_max_height: The image_max_height.  # noqa: E501
        :type: int
        """
        if image_max_height is None:
            raise ValueError("Invalid value for `image_max_height`, must not be `None`")  # noqa: E501
        self._image_max_height = image_max_height
    
    @property
    def image_width(self):
        """
        Gets the image_width.  # noqa: E501

        The width of the output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :return: The image_width.  # noqa: E501
        :rtype: int
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """
        Sets the image_width.

        The width of the output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :param image_width: The image_width.  # noqa: E501
        :type: int
        """
        if image_width is None:
            raise ValueError("Invalid value for `image_width`, must not be `None`")  # noqa: E501
        self._image_width = image_width
    
    @property
    def image_height(self):
        """
        Gets the image_height.  # noqa: E501

        The height of an output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :return: The image_height.  # noqa: E501
        :rtype: int
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """
        Sets the image_height.

        The height of an output image in pixels. (When converting single image to HTML only)  # noqa: E501

        :param image_height: The image_height.  # noqa: E501
        :type: int
        """
        if image_height is None:
            raise ValueError("Invalid value for `image_height`, must not be `None`")  # noqa: E501
        self._image_height = image_height

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
