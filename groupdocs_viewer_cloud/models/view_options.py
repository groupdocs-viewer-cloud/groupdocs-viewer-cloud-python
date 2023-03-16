# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ViewOptions.py">
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

class ViewOptions(object):
    """
    View options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_info': 'FileInfo',
        'view_format': 'str',
        'output_path': 'str',
        'fonts_path': 'str',
        'watermark': 'Watermark',
        'render_options': 'RenderOptions'
    }

    attribute_map = {
        'file_info': 'FileInfo',
        'view_format': 'ViewFormat',
        'output_path': 'OutputPath',
        'fonts_path': 'FontsPath',
        'watermark': 'Watermark',
        'render_options': 'RenderOptions'
    }

    def __init__(self, file_info=None, view_format=None, output_path=None, fonts_path=None, watermark=None, render_options=None, **kwargs):  # noqa: E501
        """Initializes new instance of ViewOptions"""  # noqa: E501

        self._file_info = None
        self._view_format = None
        self._output_path = None
        self._fonts_path = None
        self._watermark = None
        self._render_options = None

        if file_info is not None:
            self.file_info = file_info
        if view_format is not None:
            self.view_format = view_format
        if output_path is not None:
            self.output_path = output_path
        if fonts_path is not None:
            self.fonts_path = fonts_path
        if watermark is not None:
            self.watermark = watermark
        if render_options is not None:
            self.render_options = render_options
    
    @property
    def file_info(self):
        """
        Gets the file_info.  # noqa: E501

        File info  # noqa: E501

        :return: The file_info.  # noqa: E501
        :rtype: FileInfo
        """
        return self._file_info

    @file_info.setter
    def file_info(self, file_info):
        """
        Sets the file_info.

        File info  # noqa: E501

        :param file_info: The file_info.  # noqa: E501
        :type: FileInfo
        """
        self._file_info = file_info
    
    @property
    def view_format(self):
        """
        Gets the view_format.  # noqa: E501

        View format (HTML, PNG, JPG, or PDF) Default value is HTML.  # noqa: E501

        :return: The view_format.  # noqa: E501
        :rtype: str
        """
        return self._view_format

    @view_format.setter
    def view_format(self, view_format):
        """
        Sets the view_format.

        View format (HTML, PNG, JPG, or PDF) Default value is HTML.  # noqa: E501

        :param view_format: The view_format.  # noqa: E501
        :type: str
        """
        if view_format is None:
            raise ValueError("Invalid value for `view_format`, must not be `None`")  # noqa: E501
        allowed_values = ["HTML", "PNG", "JPG", "PDF"]  # noqa: E501
        if not view_format.isdigit():	
            if view_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `view_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(view_format, allowed_values))
            self._view_format = view_format
        else:
            self._view_format = allowed_values[int(view_format) if six.PY3 else long(view_format)]
    
    @property
    def output_path(self):
        """
        Gets the output_path.  # noqa: E501

        The output path Default value is 'viewer\\{input file path}_{file extension}\\'  # noqa: E501

        :return: The output_path.  # noqa: E501
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """
        Sets the output_path.

        The output path Default value is 'viewer\\{input file path}_{file extension}\\'  # noqa: E501

        :param output_path: The output_path.  # noqa: E501
        :type: str
        """
        self._output_path = output_path
    
    @property
    def fonts_path(self):
        """
        Gets the fonts_path.  # noqa: E501

        The path to directory containing custom fonts in storage  # noqa: E501

        :return: The fonts_path.  # noqa: E501
        :rtype: str
        """
        return self._fonts_path

    @fonts_path.setter
    def fonts_path(self, fonts_path):
        """
        Sets the fonts_path.

        The path to directory containing custom fonts in storage  # noqa: E501

        :param fonts_path: The fonts_path.  # noqa: E501
        :type: str
        """
        self._fonts_path = fonts_path
    
    @property
    def watermark(self):
        """
        Gets the watermark.  # noqa: E501

        Text watermark  # noqa: E501

        :return: The watermark.  # noqa: E501
        :rtype: Watermark
        """
        return self._watermark

    @watermark.setter
    def watermark(self, watermark):
        """
        Sets the watermark.

        Text watermark  # noqa: E501

        :param watermark: The watermark.  # noqa: E501
        :type: Watermark
        """
        self._watermark = watermark
    
    @property
    def render_options(self):
        """
        Gets the render_options.  # noqa: E501

        Rendering options  # noqa: E501

        :return: The render_options.  # noqa: E501
        :rtype: RenderOptions
        """
        return self._render_options

    @render_options.setter
    def render_options(self, render_options):
        """
        Sets the render_options.

        Rendering options  # noqa: E501

        :param render_options: The render_options.  # noqa: E501
        :type: RenderOptions
        """
        self._render_options = render_options

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
        if not isinstance(other, ViewOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
