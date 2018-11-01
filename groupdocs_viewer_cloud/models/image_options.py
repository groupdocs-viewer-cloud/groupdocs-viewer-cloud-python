# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ImageOptions.py">
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

from groupdocs_viewer_cloud.models import RenderOptions

class ImageOptions(RenderOptions):
    """
    Provides options for rendering document as image.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'format': 'str',
        'quality': 'int',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'format': 'format',
        'quality': 'quality',
        'width': 'width',
        'height': 'height'
    }

    def __init__(self, format=None, quality=None, width=None, height=None, **kwargs):  # noqa: E501
        """Initializes new instance of ImageOptions"""  # noqa: E501

        self._format = None
        self._quality = None
        self._width = None
        self._height = None

        if format is not None:
            self.format = format
        if quality is not None:
            self.quality = quality
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

        base = super(ImageOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def format(self):
        """
        Gets the format.  # noqa: E501

        Allows to set image format (png, jpg, bmp). Default value is png.  # noqa: E501

        :return: The format.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format.

        Allows to set image format (png, jpg, bmp). Default value is png.  # noqa: E501

        :param format: The format.  # noqa: E501
        :type: str
        """
        self._format = format
    
    @property
    def quality(self):
        """
        Gets the quality.  # noqa: E501

        Allows to specify quality when rendering as JPG. Valid values are between 1 and 100.  Default value is 90.  # noqa: E501

        :return: The quality.  # noqa: E501
        :rtype: int
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality.

        Allows to specify quality when rendering as JPG. Valid values are between 1 and 100.  Default value is 90.  # noqa: E501

        :param quality: The quality.  # noqa: E501
        :type: int
        """
        self._quality = quality
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Allows to specify output image width.  Specify image width in case when you want to change output image dimensions. When Width has value and Height value is 0 then Height value will be calculated  to save image proportions.   # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Allows to specify output image width.  Specify image width in case when you want to change output image dimensions. When Width has value and Height value is 0 then Height value will be calculated  to save image proportions.   # noqa: E501

        :param width: The width.  # noqa: E501
        :type: int
        """
        self._width = width
    
    @property
    def height(self):
        """
        Gets the height.  # noqa: E501

        Allows to specify output image height.  Specify image height in case when you want to change output image dimensions. When Height has value and Width value is 0 then Width value will be calculated  to save image proportions.  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Allows to specify output image height.  Specify image height in case when you want to change output image dimensions. When Height has value and Width value is 0 then Width value will be calculated  to save image proportions.  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        self._height = height

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
        if not isinstance(other, ImageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
