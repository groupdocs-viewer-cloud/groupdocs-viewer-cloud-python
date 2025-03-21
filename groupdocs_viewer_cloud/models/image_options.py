# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ImageOptions.py">
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

from groupdocs_viewer_cloud.models import RenderOptions

class ImageOptions(RenderOptions):
    """
    Options for rendering document into image
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'width': 'int',
        'height': 'int',
        'extract_text': 'bool',
        'jpeg_quality': 'int',
        'max_width': 'int',
        'max_height': 'int'
    }

    attribute_map = {
        'width': 'Width',
        'height': 'Height',
        'extract_text': 'ExtractText',
        'jpeg_quality': 'JpegQuality',
        'max_width': 'MaxWidth',
        'max_height': 'MaxHeight'
    }

    def __init__(self, width=None, height=None, extract_text=None, jpeg_quality=None, max_width=None, max_height=None, **kwargs):  # noqa: E501
        """Initializes new instance of ImageOptions"""  # noqa: E501

        self._width = None
        self._height = None
        self._extract_text = None
        self._jpeg_quality = None
        self._max_width = None
        self._max_height = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if extract_text is not None:
            self.extract_text = extract_text
        if jpeg_quality is not None:
            self.jpeg_quality = jpeg_quality
        if max_width is not None:
            self.max_width = max_width
        if max_height is not None:
            self.max_height = max_height

        base = super(ImageOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
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
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
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
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def extract_text(self):
        """
        Gets the extract_text.  # noqa: E501

        When enabled Viewer will extract text when it's possible (e.g. raster formats don't have text layer) and return it in the viewing result. This option might be useful when you want to add selectable text layer over the image.   # noqa: E501

        :return: The extract_text.  # noqa: E501
        :rtype: bool
        """
        return self._extract_text

    @extract_text.setter
    def extract_text(self, extract_text):
        """
        Sets the extract_text.

        When enabled Viewer will extract text when it's possible (e.g. raster formats don't have text layer) and return it in the viewing result. This option might be useful when you want to add selectable text layer over the image.   # noqa: E501

        :param extract_text: The extract_text.  # noqa: E501
        :type: bool
        """
        if extract_text is None:
            raise ValueError("Invalid value for `extract_text`, must not be `None`")  # noqa: E501
        self._extract_text = extract_text
    
    @property
    def jpeg_quality(self):
        """
        Gets the jpeg_quality.  # noqa: E501

        Allows to specify quality when rendering as JPG. Valid values are between 1 and 100.  Default value is 90.  # noqa: E501

        :return: The jpeg_quality.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """
        Sets the jpeg_quality.

        Allows to specify quality when rendering as JPG. Valid values are between 1 and 100.  Default value is 90.  # noqa: E501

        :param jpeg_quality: The jpeg_quality.  # noqa: E501
        :type: int
        """
        if jpeg_quality is None:
            raise ValueError("Invalid value for `jpeg_quality`, must not be `None`")  # noqa: E501
        self._jpeg_quality = jpeg_quality
    
    @property
    def max_width(self):
        """
        Gets the max_width.  # noqa: E501

        Max width of an output image in pixels  # noqa: E501

        :return: The max_width.  # noqa: E501
        :rtype: int
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """
        Sets the max_width.

        Max width of an output image in pixels  # noqa: E501

        :param max_width: The max_width.  # noqa: E501
        :type: int
        """
        if max_width is None:
            raise ValueError("Invalid value for `max_width`, must not be `None`")  # noqa: E501
        self._max_width = max_width
    
    @property
    def max_height(self):
        """
        Gets the max_height.  # noqa: E501

        Max height of an output image in pixels  # noqa: E501

        :return: The max_height.  # noqa: E501
        :rtype: int
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """
        Sets the max_height.

        Max height of an output image in pixels  # noqa: E501

        :param max_height: The max_height.  # noqa: E501
        :type: int
        """
        if max_height is None:
            raise ValueError("Invalid value for `max_height`, must not be `None`")  # noqa: E501
        self._max_height = max_height

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
