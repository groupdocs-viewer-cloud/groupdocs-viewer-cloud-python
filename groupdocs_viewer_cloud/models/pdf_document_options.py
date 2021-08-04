# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfDocumentOptions.py">
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

class PdfDocumentOptions(object):
    """
    Provides options for rendering PDF documents
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'disable_chars_grouping': 'bool',
        'enable_layered_rendering': 'bool',
        'enable_font_hinting': 'bool',
        'render_original_page_size': 'bool',
        'image_quality': 'str',
        'render_text_as_image': 'bool'
    }

    attribute_map = {
        'disable_chars_grouping': 'DisableCharsGrouping',
        'enable_layered_rendering': 'EnableLayeredRendering',
        'enable_font_hinting': 'EnableFontHinting',
        'render_original_page_size': 'RenderOriginalPageSize',
        'image_quality': 'ImageQuality',
        'render_text_as_image': 'RenderTextAsImage'
    }

    def __init__(self, disable_chars_grouping=None, enable_layered_rendering=None, enable_font_hinting=None, render_original_page_size=None, image_quality=None, render_text_as_image=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfDocumentOptions"""  # noqa: E501

        self._disable_chars_grouping = None
        self._enable_layered_rendering = None
        self._enable_font_hinting = None
        self._render_original_page_size = None
        self._image_quality = None
        self._render_text_as_image = None

        if disable_chars_grouping is not None:
            self.disable_chars_grouping = disable_chars_grouping
        if enable_layered_rendering is not None:
            self.enable_layered_rendering = enable_layered_rendering
        if enable_font_hinting is not None:
            self.enable_font_hinting = enable_font_hinting
        if render_original_page_size is not None:
            self.render_original_page_size = render_original_page_size
        if image_quality is not None:
            self.image_quality = image_quality
        if render_text_as_image is not None:
            self.render_text_as_image = render_text_as_image
    
    @property
    def disable_chars_grouping(self):
        """
        Gets the disable_chars_grouping.  # noqa: E501

        Disables chars grouping to keep maximum precision during chars positioning when rendering the page  # noqa: E501

        :return: The disable_chars_grouping.  # noqa: E501
        :rtype: bool
        """
        return self._disable_chars_grouping

    @disable_chars_grouping.setter
    def disable_chars_grouping(self, disable_chars_grouping):
        """
        Sets the disable_chars_grouping.

        Disables chars grouping to keep maximum precision during chars positioning when rendering the page  # noqa: E501

        :param disable_chars_grouping: The disable_chars_grouping.  # noqa: E501
        :type: bool
        """
        if disable_chars_grouping is None:
            raise ValueError("Invalid value for `disable_chars_grouping`, must not be `None`")  # noqa: E501
        self._disable_chars_grouping = disable_chars_grouping
    
    @property
    def enable_layered_rendering(self):
        """
        Gets the enable_layered_rendering.  # noqa: E501

        Enables rendering of text and graphics according to z-order in original PDF document  when rendering into HTML  # noqa: E501

        :return: The enable_layered_rendering.  # noqa: E501
        :rtype: bool
        """
        return self._enable_layered_rendering

    @enable_layered_rendering.setter
    def enable_layered_rendering(self, enable_layered_rendering):
        """
        Sets the enable_layered_rendering.

        Enables rendering of text and graphics according to z-order in original PDF document  when rendering into HTML  # noqa: E501

        :param enable_layered_rendering: The enable_layered_rendering.  # noqa: E501
        :type: bool
        """
        if enable_layered_rendering is None:
            raise ValueError("Invalid value for `enable_layered_rendering`, must not be `None`")  # noqa: E501
        self._enable_layered_rendering = enable_layered_rendering
    
    @property
    def enable_font_hinting(self):
        """
        Gets the enable_font_hinting.  # noqa: E501

        Enables font hinting. The font hinting adjusts the display of an outline font. Supported only for TTF fonts when these fonts are used in source document.  # noqa: E501

        :return: The enable_font_hinting.  # noqa: E501
        :rtype: bool
        """
        return self._enable_font_hinting

    @enable_font_hinting.setter
    def enable_font_hinting(self, enable_font_hinting):
        """
        Sets the enable_font_hinting.

        Enables font hinting. The font hinting adjusts the display of an outline font. Supported only for TTF fonts when these fonts are used in source document.  # noqa: E501

        :param enable_font_hinting: The enable_font_hinting.  # noqa: E501
        :type: bool
        """
        if enable_font_hinting is None:
            raise ValueError("Invalid value for `enable_font_hinting`, must not be `None`")  # noqa: E501
        self._enable_font_hinting = enable_font_hinting
    
    @property
    def render_original_page_size(self):
        """
        Gets the render_original_page_size.  # noqa: E501

        When this option enabled the output pages will have the same size in pixels as page size in a source PDF document. By default GroupDocs.Viewer calculates output image page size for better rendering quality. This option is supported when rendering into PNG or JPG formats.  # noqa: E501

        :return: The render_original_page_size.  # noqa: E501
        :rtype: bool
        """
        return self._render_original_page_size

    @render_original_page_size.setter
    def render_original_page_size(self, render_original_page_size):
        """
        Sets the render_original_page_size.

        When this option enabled the output pages will have the same size in pixels as page size in a source PDF document. By default GroupDocs.Viewer calculates output image page size for better rendering quality. This option is supported when rendering into PNG or JPG formats.  # noqa: E501

        :param render_original_page_size: The render_original_page_size.  # noqa: E501
        :type: bool
        """
        if render_original_page_size is None:
            raise ValueError("Invalid value for `render_original_page_size`, must not be `None`")  # noqa: E501
        self._render_original_page_size = render_original_page_size
    
    @property
    def image_quality(self):
        """
        Gets the image_quality.  # noqa: E501

        Specifies output image quality for image resources when rendering into HTML. The default value is Low  # noqa: E501

        :return: The image_quality.  # noqa: E501
        :rtype: str
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """
        Sets the image_quality.

        Specifies output image quality for image resources when rendering into HTML. The default value is Low  # noqa: E501

        :param image_quality: The image_quality.  # noqa: E501
        :type: str
        """
        if image_quality is None:
            raise ValueError("Invalid value for `image_quality`, must not be `None`")  # noqa: E501
        allowed_values = ["Low", "Medium", "High"]  # noqa: E501
        if not image_quality.isdigit():	
            if image_quality not in allowed_values:
                raise ValueError(
                    "Invalid value for `image_quality` ({0}), must be one of {1}"  # noqa: E501
                    .format(image_quality, allowed_values))
            self._image_quality = image_quality
        else:
            self._image_quality = allowed_values[int(image_quality) if six.PY3 else long(image_quality)]
    
    @property
    def render_text_as_image(self):
        """
        Gets the render_text_as_image.  # noqa: E501

        When this option is set to true, the text is rendered as an image in the output HTML. Enable this option to make text unselectable or to fix characters rendering and make HTML look like PDF. The default value is false. This option is supported when rendering into HTML.  # noqa: E501

        :return: The render_text_as_image.  # noqa: E501
        :rtype: bool
        """
        return self._render_text_as_image

    @render_text_as_image.setter
    def render_text_as_image(self, render_text_as_image):
        """
        Sets the render_text_as_image.

        When this option is set to true, the text is rendered as an image in the output HTML. Enable this option to make text unselectable or to fix characters rendering and make HTML look like PDF. The default value is false. This option is supported when rendering into HTML.  # noqa: E501

        :param render_text_as_image: The render_text_as_image.  # noqa: E501
        :type: bool
        """
        if render_text_as_image is None:
            raise ValueError("Invalid value for `render_text_as_image`, must not be `None`")  # noqa: E501
        self._render_text_as_image = render_text_as_image

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
        if not isinstance(other, PdfDocumentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
