# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="VisioRenderingOptions.py">
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

class VisioRenderingOptions(object):
    """
    The Visio files processing documents view options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'render_figures_only': 'bool',
        'figure_width': 'int'
    }

    attribute_map = {
        'render_figures_only': 'RenderFiguresOnly',
        'figure_width': 'FigureWidth'
    }

    def __init__(self, render_figures_only=None, figure_width=None, **kwargs):  # noqa: E501
        """Initializes new instance of VisioRenderingOptions"""  # noqa: E501

        self._render_figures_only = None
        self._figure_width = None

        if render_figures_only is not None:
            self.render_figures_only = render_figures_only
        if figure_width is not None:
            self.figure_width = figure_width
    
    @property
    def render_figures_only(self):
        """
        Gets the render_figures_only.  # noqa: E501

        Render only Visio figures, not a diagram.  # noqa: E501

        :return: The render_figures_only.  # noqa: E501
        :rtype: bool
        """
        return self._render_figures_only

    @render_figures_only.setter
    def render_figures_only(self, render_figures_only):
        """
        Sets the render_figures_only.

        Render only Visio figures, not a diagram.  # noqa: E501

        :param render_figures_only: The render_figures_only.  # noqa: E501
        :type: bool
        """
        if render_figures_only is None:
            raise ValueError("Invalid value for `render_figures_only`, must not be `None`")  # noqa: E501
        self._render_figures_only = render_figures_only
    
    @property
    def figure_width(self):
        """
        Gets the figure_width.  # noqa: E501

        Figure width, height will be calculated automatically. Default value is 100.  # noqa: E501

        :return: The figure_width.  # noqa: E501
        :rtype: int
        """
        return self._figure_width

    @figure_width.setter
    def figure_width(self, figure_width):
        """
        Sets the figure_width.

        Figure width, height will be calculated automatically. Default value is 100.  # noqa: E501

        :param figure_width: The figure_width.  # noqa: E501
        :type: int
        """
        if figure_width is None:
            raise ValueError("Invalid value for `figure_width`, must not be `None`")  # noqa: E501
        self._figure_width = figure_width

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
        if not isinstance(other, VisioRenderingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
