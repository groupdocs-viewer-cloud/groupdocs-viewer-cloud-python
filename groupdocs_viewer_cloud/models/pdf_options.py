# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfOptions.py">
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

class PdfOptions(object):
    """
    The PDF documents rendering options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enable_precise_rendering': 'bool',
        'enable_initial_content_ordering': 'bool',
        'render_layers_separately': 'bool',
        'image_quality': 'str'
    }

    attribute_map = {
        'enable_precise_rendering': 'enablePreciseRendering',
        'enable_initial_content_ordering': 'enableInitialContentOrdering',
        'render_layers_separately': 'renderLayersSeparately',
        'image_quality': 'imageQuality'
    }

    def __init__(self, enable_precise_rendering=None, enable_initial_content_ordering=None, render_layers_separately=None, image_quality=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfOptions"""  # noqa: E501

        self._enable_precise_rendering = None
        self._enable_initial_content_ordering = None
        self._render_layers_separately = None
        self._image_quality = None

        if enable_precise_rendering is not None:
            self.enable_precise_rendering = enable_precise_rendering
        if enable_initial_content_ordering is not None:
            self.enable_initial_content_ordering = enable_initial_content_ordering
        if render_layers_separately is not None:
            self.render_layers_separately = render_layers_separately
        if image_quality is not None:
            self.image_quality = image_quality
    
    @property
    def enable_precise_rendering(self):
        """
        Gets the enable_precise_rendering.  # noqa: E501

        Indicates whether the PDF document is rendered in a precise mode or not. It is recommended to enable this option when rendering documents with complex content e.g. documents which contains hieroglyphs or any kind o glyphs which should be rendered separately from each other.  # noqa: E501

        :return: The enable_precise_rendering.  # noqa: E501
        :rtype: bool
        """
        return self._enable_precise_rendering

    @enable_precise_rendering.setter
    def enable_precise_rendering(self, enable_precise_rendering):
        """
        Sets the enable_precise_rendering.

        Indicates whether the PDF document is rendered in a precise mode or not. It is recommended to enable this option when rendering documents with complex content e.g. documents which contains hieroglyphs or any kind o glyphs which should be rendered separately from each other.  # noqa: E501

        :param enable_precise_rendering: The enable_precise_rendering.  # noqa: E501
        :type: bool
        """
        self._enable_precise_rendering = enable_precise_rendering
    
    @property
    def enable_initial_content_ordering(self):
        """
        Gets the enable_initial_content_ordering.  # noqa: E501

        When this option is enabled content (graphics and text) will be added to HTML document accordingly Z-order in original PDF document. When this option is disabled content (graphics and text) will be added to a single layer.  # noqa: E501

        :return: The enable_initial_content_ordering.  # noqa: E501
        :rtype: bool
        """
        return self._enable_initial_content_ordering

    @enable_initial_content_ordering.setter
    def enable_initial_content_ordering(self, enable_initial_content_ordering):
        """
        Sets the enable_initial_content_ordering.

        When this option is enabled content (graphics and text) will be added to HTML document accordingly Z-order in original PDF document. When this option is disabled content (graphics and text) will be added to a single layer.  # noqa: E501

        :param enable_initial_content_ordering: The enable_initial_content_ordering.  # noqa: E501
        :type: bool
        """
        self._enable_initial_content_ordering = enable_initial_content_ordering
    
    @property
    def render_layers_separately(self):
        """
        Gets the render_layers_separately.  # noqa: E501

        When this option is enabled layers will be separated from each other in the HTML document.  # noqa: E501

        :return: The render_layers_separately.  # noqa: E501
        :rtype: bool
        """
        return self._render_layers_separately

    @render_layers_separately.setter
    def render_layers_separately(self, render_layers_separately):
        """
        Sets the render_layers_separately.

        When this option is enabled layers will be separated from each other in the HTML document.  # noqa: E501

        :param render_layers_separately: The render_layers_separately.  # noqa: E501
        :type: bool
        """
        self._render_layers_separately = render_layers_separately
    
    @property
    def image_quality(self):
        """
        Gets the image_quality.  # noqa: E501

        Specifies output image quality for image resources when rendering as HTML. The default value is Low. Supported values {Low|Medium|High}: 1. Low - satisfying image quality and smallest image size. 2. Medium - better image quality and larger image size. 3. High - best image quality with largest image size.  # noqa: E501

        :return: The image_quality.  # noqa: E501
        :rtype: str
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """
        Sets the image_quality.

        Specifies output image quality for image resources when rendering as HTML. The default value is Low. Supported values {Low|Medium|High}: 1. Low - satisfying image quality and smallest image size. 2. Medium - better image quality and larger image size. 3. High - best image quality with largest image size.  # noqa: E501

        :param image_quality: The image_quality.  # noqa: E501
        :type: str
        """
        self._image_quality = image_quality

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
