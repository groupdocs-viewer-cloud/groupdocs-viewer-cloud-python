# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WordProcessingOptions.py">
#   Copyright (c) 2003-2020 Aspose Pty Ltd
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
        'render_tracked_changes': 'bool'
    }

    attribute_map = {
        'render_tracked_changes': 'RenderTrackedChanges'
    }

    def __init__(self, render_tracked_changes=None, **kwargs):  # noqa: E501
        """Initializes new instance of WordProcessingOptions"""  # noqa: E501

        self._render_tracked_changes = None

        if render_tracked_changes is not None:
            self.render_tracked_changes = render_tracked_changes
    
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
