# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="HtmlOptions.py">
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

from groupdocs_viewer_cloud.models import RenderOptions

class HtmlOptions(RenderOptions):
    """
    Options for rendering document into HTML
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_resources': 'bool',
        'resource_path': 'str',
        'is_responsive': 'bool',
        'minify': 'bool',
        'exclude_fonts': 'bool',
        'fonts_to_exclude': 'list[str]'
    }

    attribute_map = {
        'external_resources': 'ExternalResources',
        'resource_path': 'ResourcePath',
        'is_responsive': 'IsResponsive',
        'minify': 'Minify',
        'exclude_fonts': 'ExcludeFonts',
        'fonts_to_exclude': 'FontsToExclude'
    }

    def __init__(self, external_resources=None, resource_path=None, is_responsive=None, minify=None, exclude_fonts=None, fonts_to_exclude=None, **kwargs):  # noqa: E501
        """Initializes new instance of HtmlOptions"""  # noqa: E501

        self._external_resources = None
        self.__resource_path = None
        self._is_responsive = None
        self._minify = None
        self._exclude_fonts = None
        self._fonts_to_exclude = None

        if external_resources is not None:
            self.external_resources = external_resources
        if resource_path is not None:
            self.resource_path = resource_path
        if is_responsive is not None:
            self.is_responsive = is_responsive
        if minify is not None:
            self.minify = minify
        if exclude_fonts is not None:
            self.exclude_fonts = exclude_fonts
        if fonts_to_exclude is not None:
            self.fonts_to_exclude = fonts_to_exclude

        base = super(HtmlOptions, self)
        base.__init__(**kwargs)

        self.swagger_types.update(base.swagger_types)
        self.attribute_map.update(base.attribute_map)
    
    @property
    def external_resources(self):
        """
        Gets the external_resources.  # noqa: E501

        Controls output HTML document resources (styles, images and fonts) linking. By default this option is disabled and all the resources are embedded into HTML document.  # noqa: E501

        :return: The external_resources.  # noqa: E501
        :rtype: bool
        """
        return self._external_resources

    @external_resources.setter
    def external_resources(self, external_resources):
        """
        Sets the external_resources.

        Controls output HTML document resources (styles, images and fonts) linking. By default this option is disabled and all the resources are embedded into HTML document.  # noqa: E501

        :param external_resources: The external_resources.  # noqa: E501
        :type: bool
        """
        if external_resources is None:
            raise ValueError("Invalid value for `external_resources`, must not be `None`")  # noqa: E501
        self._external_resources = external_resources
    
    @property
    def resource_path(self):
        """
        Gets the resource_path.  # noqa: E501

        Path for the HTML resources (styles, images and fonts). For example when resource path is http://example.com/api/pages/{page-number}/resources/{resource-name} the {page-number} and {resource-name} templates will be replaced with page number and resource name accordingly. This option is ignored when ExternalResources option is disabled.  # noqa: E501

        :return: The resource_path.  # noqa: E501
        :rtype: str
        """
        return self.__resource_path

    @resource_path.setter
    def resource_path(self, resource_path):
        """
        Sets the resource_path.

        Path for the HTML resources (styles, images and fonts). For example when resource path is http://example.com/api/pages/{page-number}/resources/{resource-name} the {page-number} and {resource-name} templates will be replaced with page number and resource name accordingly. This option is ignored when ExternalResources option is disabled.  # noqa: E501

        :param resource_path: The resource_path.  # noqa: E501
        :type: str
        """
        self.__resource_path = resource_path
    
    @property
    def is_responsive(self):
        """
        Gets the is_responsive.  # noqa: E501

        Indicates whether rendering will provide responsive web pages, that look well on different device types. Default value is false.  # noqa: E501

        :return: The is_responsive.  # noqa: E501
        :rtype: bool
        """
        return self._is_responsive

    @is_responsive.setter
    def is_responsive(self, is_responsive):
        """
        Sets the is_responsive.

        Indicates whether rendering will provide responsive web pages, that look well on different device types. Default value is false.  # noqa: E501

        :param is_responsive: The is_responsive.  # noqa: E501
        :type: bool
        """
        if is_responsive is None:
            raise ValueError("Invalid value for `is_responsive`, must not be `None`")  # noqa: E501
        self._is_responsive = is_responsive
    
    @property
    def minify(self):
        """
        Gets the minify.  # noqa: E501

        Enables HTML content and HTML resources minification  # noqa: E501

        :return: The minify.  # noqa: E501
        :rtype: bool
        """
        return self._minify

    @minify.setter
    def minify(self, minify):
        """
        Sets the minify.

        Enables HTML content and HTML resources minification  # noqa: E501

        :param minify: The minify.  # noqa: E501
        :type: bool
        """
        if minify is None:
            raise ValueError("Invalid value for `minify`, must not be `None`")  # noqa: E501
        self._minify = minify
    
    @property
    def exclude_fonts(self):
        """
        Gets the exclude_fonts.  # noqa: E501

        When enabled prevents adding any fonts into HTML document               # noqa: E501

        :return: The exclude_fonts.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_fonts

    @exclude_fonts.setter
    def exclude_fonts(self, exclude_fonts):
        """
        Sets the exclude_fonts.

        When enabled prevents adding any fonts into HTML document               # noqa: E501

        :param exclude_fonts: The exclude_fonts.  # noqa: E501
        :type: bool
        """
        if exclude_fonts is None:
            raise ValueError("Invalid value for `exclude_fonts`, must not be `None`")  # noqa: E501
        self._exclude_fonts = exclude_fonts
    
    @property
    def fonts_to_exclude(self):
        """
        Gets the fonts_to_exclude.  # noqa: E501

        This option is supported for presentations only. The list of font names, to exclude from HTML document               # noqa: E501

        :return: The fonts_to_exclude.  # noqa: E501
        :rtype: list[str]
        """
        return self._fonts_to_exclude

    @fonts_to_exclude.setter
    def fonts_to_exclude(self, fonts_to_exclude):
        """
        Sets the fonts_to_exclude.

        This option is supported for presentations only. The list of font names, to exclude from HTML document               # noqa: E501

        :param fonts_to_exclude: The fonts_to_exclude.  # noqa: E501
        :type: list[str]
        """
        self._fonts_to_exclude = fonts_to_exclude

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
