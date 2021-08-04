# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WordProcessingOptions.py">
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

class WordProcessingOptions(object):
    """
    Provides options for rendering word processing documents
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'render_tracked_changes': 'bool',
        'left_margin': 'float',
        'right_margin': 'float',
        'top_margin': 'float',
        'bottom_margin': 'float'
    }

    attribute_map = {
        'render_tracked_changes': 'RenderTrackedChanges',
        'left_margin': 'LeftMargin',
        'right_margin': 'RightMargin',
        'top_margin': 'TopMargin',
        'bottom_margin': 'BottomMargin'
    }

    def __init__(self, render_tracked_changes=None, left_margin=None, right_margin=None, top_margin=None, bottom_margin=None, **kwargs):  # noqa: E501
        """Initializes new instance of WordProcessingOptions"""  # noqa: E501

        self._render_tracked_changes = None
        self._left_margin = None
        self._right_margin = None
        self._top_margin = None
        self._bottom_margin = None

        if render_tracked_changes is not None:
            self.render_tracked_changes = render_tracked_changes
        if left_margin is not None:
            self.left_margin = left_margin
        if right_margin is not None:
            self.right_margin = right_margin
        if top_margin is not None:
            self.top_margin = top_margin
        if bottom_margin is not None:
            self.bottom_margin = bottom_margin
    
    @property
    def render_tracked_changes(self):
        """
        Gets the render_tracked_changes.  # noqa: E501

        Enables tracked changes (revisions) rendering  # noqa: E501

        :return: The render_tracked_changes.  # noqa: E501
        :rtype: bool
        """
        return self._render_tracked_changes

    @render_tracked_changes.setter
    def render_tracked_changes(self, render_tracked_changes):
        """
        Sets the render_tracked_changes.

        Enables tracked changes (revisions) rendering  # noqa: E501

        :param render_tracked_changes: The render_tracked_changes.  # noqa: E501
        :type: bool
        """
        if render_tracked_changes is None:
            raise ValueError("Invalid value for `render_tracked_changes`, must not be `None`")  # noqa: E501
        self._render_tracked_changes = render_tracked_changes
    
    @property
    def left_margin(self):
        """
        Gets the left_margin.  # noqa: E501

        Left page margin (for HTML rendering only)  # noqa: E501

        :return: The left_margin.  # noqa: E501
        :rtype: float
        """
        return self._left_margin

    @left_margin.setter
    def left_margin(self, left_margin):
        """
        Sets the left_margin.

        Left page margin (for HTML rendering only)  # noqa: E501

        :param left_margin: The left_margin.  # noqa: E501
        :type: float
        """
        if left_margin is None:
            raise ValueError("Invalid value for `left_margin`, must not be `None`")  # noqa: E501
        self._left_margin = left_margin
    
    @property
    def right_margin(self):
        """
        Gets the right_margin.  # noqa: E501

        Right page margin (for HTML rendering only)  # noqa: E501

        :return: The right_margin.  # noqa: E501
        :rtype: float
        """
        return self._right_margin

    @right_margin.setter
    def right_margin(self, right_margin):
        """
        Sets the right_margin.

        Right page margin (for HTML rendering only)  # noqa: E501

        :param right_margin: The right_margin.  # noqa: E501
        :type: float
        """
        if right_margin is None:
            raise ValueError("Invalid value for `right_margin`, must not be `None`")  # noqa: E501
        self._right_margin = right_margin
    
    @property
    def top_margin(self):
        """
        Gets the top_margin.  # noqa: E501

        Top page margin (for HTML rendering only)  # noqa: E501

        :return: The top_margin.  # noqa: E501
        :rtype: float
        """
        return self._top_margin

    @top_margin.setter
    def top_margin(self, top_margin):
        """
        Sets the top_margin.

        Top page margin (for HTML rendering only)  # noqa: E501

        :param top_margin: The top_margin.  # noqa: E501
        :type: float
        """
        if top_margin is None:
            raise ValueError("Invalid value for `top_margin`, must not be `None`")  # noqa: E501
        self._top_margin = top_margin
    
    @property
    def bottom_margin(self):
        """
        Gets the bottom_margin.  # noqa: E501

        Bottom page margin (for HTML rendering only)  # noqa: E501

        :return: The bottom_margin.  # noqa: E501
        :rtype: float
        """
        return self._bottom_margin

    @bottom_margin.setter
    def bottom_margin(self, bottom_margin):
        """
        Sets the bottom_margin.

        Bottom page margin (for HTML rendering only)  # noqa: E501

        :param bottom_margin: The bottom_margin.  # noqa: E501
        :type: float
        """
        if bottom_margin is None:
            raise ValueError("Invalid value for `bottom_margin`, must not be `None`")  # noqa: E501
        self._bottom_margin = bottom_margin

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
        if not isinstance(other, WordProcessingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
