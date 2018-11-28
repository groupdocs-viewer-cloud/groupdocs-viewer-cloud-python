# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="HtmlOptions.py">
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

class HtmlOptions(RenderOptions):
    """
    Provides options for rendering document pages as HTML.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resource_path': 'str',
        'ignore_resource_path_in_resources': 'bool',
        'embed_resources': 'bool',
        'enable_minification': 'bool',
        'enable_responsive_rendering': 'bool',
        'exclude_fonts': 'bool',
        'exclude_fonts_list': 'list[str]'
    }

    attribute_map = {
        'resource_path': 'resourcePath',
        'ignore_resource_path_in_resources': 'ignoreResourcePathInResources',
        'embed_resources': 'embedResources',
        'enable_minification': 'enableMinification',
        'enable_responsive_rendering': 'enableResponsiveRendering',
        'exclude_fonts': 'excludeFonts',
        'exclude_fonts_list': 'excludeFontsList'
    }

    def __init__(self, resource_path=None, ignore_resource_path_in_resources=None, embed_resources=None, enable_minification=None, enable_responsive_rendering=None, exclude_fonts=None, exclude_fonts_list=None, **kwargs):  # noqa: E501
        """Initializes new instance of HtmlOptions"""  # noqa: E501

        self.__resource_path = None
        self._ignore_resource_path_in_resources = None
        self._embed_resources = None
        self._enable_minification = None
        self._enable_responsive_rendering = None
        self._exclude_fonts = None
        self._exclude_fonts_list = None

        if resource_path is not None:
            self.resource_path = resource_path
        if ignore_resource_path_in_resources is not None:
            self.ignore_resource_path_in_resources = ignore_resource_path_in_resources
        if embed_resources is not None:
            self.embed_resources = embed_resources
        if enable_minification is not None:
            self.enable_minification = enable_minification
        if enable_responsive_rendering is not None:
            self.enable_responsive_rendering = enable_responsive_rendering
        if exclude_fonts is not None:
            self.exclude_fonts = exclude_fonts
        if exclude_fonts_list is not None:
            self.exclude_fonts_list = exclude_fonts_list

        base = super(HtmlOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def resource_path(self):
        """
        Gets the resource_path.  # noqa: E501

        Allows to specify HTML resources (styles, images and fonts) path. For example when resource path is http://example.com/api/pages/{page-number}/resources/{resource-name} the {page-number} and {resource-name} templates will be replaced with page number and resource name accordingly. Ignored when EmbedResources option is set to true.  # noqa: E501

        :return: The resource_path.  # noqa: E501
        :rtype: str
        """
        return self.__resource_path

    @resource_path.setter
    def resource_path(self, resource_path):
        """
        Sets the resource_path.

        Allows to specify HTML resources (styles, images and fonts) path. For example when resource path is http://example.com/api/pages/{page-number}/resources/{resource-name} the {page-number} and {resource-name} templates will be replaced with page number and resource name accordingly. Ignored when EmbedResources option is set to true.  # noqa: E501

        :param resource_path: The resource_path.  # noqa: E501
        :type: str
        """
        self.__resource_path = resource_path
    
    @property
    def ignore_resource_path_in_resources(self):
        """
        Gets the ignore_resource_path_in_resources.  # noqa: E501

        Allows to ignore ResourcePath when processing *.css files.  When this options is enabled ResourcePath won't be added to resource references in *.css file.  # noqa: E501

        :return: The ignore_resource_path_in_resources.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_resource_path_in_resources

    @ignore_resource_path_in_resources.setter
    def ignore_resource_path_in_resources(self, ignore_resource_path_in_resources):
        """
        Sets the ignore_resource_path_in_resources.

        Allows to ignore ResourcePath when processing *.css files.  When this options is enabled ResourcePath won't be added to resource references in *.css file.  # noqa: E501

        :param ignore_resource_path_in_resources: The ignore_resource_path_in_resources.  # noqa: E501
        :type: bool
        """
        self._ignore_resource_path_in_resources = ignore_resource_path_in_resources
    
    @property
    def embed_resources(self):
        """
        Gets the embed_resources.  # noqa: E501

        Controls output HTML document resources (styles, images and fonts) saving. When this options set to true all resources will be embedded into HTML document and ResourcePath option value will be ignored.  # noqa: E501

        :return: The embed_resources.  # noqa: E501
        :rtype: bool
        """
        return self._embed_resources

    @embed_resources.setter
    def embed_resources(self, embed_resources):
        """
        Sets the embed_resources.

        Controls output HTML document resources (styles, images and fonts) saving. When this options set to true all resources will be embedded into HTML document and ResourcePath option value will be ignored.  # noqa: E501

        :param embed_resources: The embed_resources.  # noqa: E501
        :type: bool
        """
        self._embed_resources = embed_resources
    
    @property
    def enable_minification(self):
        """
        Gets the enable_minification.  # noqa: E501

        Enables content (HTML, CSS and SVG) minification.  # noqa: E501

        :return: The enable_minification.  # noqa: E501
        :rtype: bool
        """
        return self._enable_minification

    @enable_minification.setter
    def enable_minification(self, enable_minification):
        """
        Sets the enable_minification.

        Enables content (HTML, CSS and SVG) minification.  # noqa: E501

        :param enable_minification: The enable_minification.  # noqa: E501
        :type: bool
        """
        self._enable_minification = enable_minification
    
    @property
    def enable_responsive_rendering(self):
        """
        Gets the enable_responsive_rendering.  # noqa: E501

        Indicates whether rendering will provide responsive web pages, that look well on different device types.  # noqa: E501

        :return: The enable_responsive_rendering.  # noqa: E501
        :rtype: bool
        """
        return self._enable_responsive_rendering

    @enable_responsive_rendering.setter
    def enable_responsive_rendering(self, enable_responsive_rendering):
        """
        Sets the enable_responsive_rendering.

        Indicates whether rendering will provide responsive web pages, that look well on different device types.  # noqa: E501

        :param enable_responsive_rendering: The enable_responsive_rendering.  # noqa: E501
        :type: bool
        """
        self._enable_responsive_rendering = enable_responsive_rendering
    
    @property
    def exclude_fonts(self):
        """
        Gets the exclude_fonts.  # noqa: E501

        Prevents adding fonts to the output HTML document.    # noqa: E501

        :return: The exclude_fonts.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_fonts

    @exclude_fonts.setter
    def exclude_fonts(self, exclude_fonts):
        """
        Sets the exclude_fonts.

        Prevents adding fonts to the output HTML document.    # noqa: E501

        :param exclude_fonts: The exclude_fonts.  # noqa: E501
        :type: bool
        """
        self._exclude_fonts = exclude_fonts
    
    @property
    def exclude_fonts_list(self):
        """
        Gets the exclude_fonts_list.  # noqa: E501

        The list of font names, that will be excluded from HTML.  # noqa: E501

        :return: The exclude_fonts_list.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_fonts_list

    @exclude_fonts_list.setter
    def exclude_fonts_list(self, exclude_fonts_list):
        """
        Sets the exclude_fonts_list.

        The list of font names, that will be excluded from HTML.  # noqa: E501

        :param exclude_fonts_list: The exclude_fonts_list.  # noqa: E501
        :type: list[str]
        """
        self._exclude_fonts_list = exclude_fonts_list

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
        if not isinstance(other, HtmlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
