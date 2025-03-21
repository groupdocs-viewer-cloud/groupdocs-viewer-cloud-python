# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WordProcessingOptions.py">
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
        'bottom_margin': 'float',
        'page_size': 'str',
        'enable_open_type_features': 'bool',
        'unlink_table_of_contents': 'bool',
        'update_fields': 'bool'
    }

    attribute_map = {
        'render_tracked_changes': 'RenderTrackedChanges',
        'left_margin': 'LeftMargin',
        'right_margin': 'RightMargin',
        'top_margin': 'TopMargin',
        'bottom_margin': 'BottomMargin',
        'page_size': 'PageSize',
        'enable_open_type_features': 'EnableOpenTypeFeatures',
        'unlink_table_of_contents': 'UnlinkTableOfContents',
        'update_fields': 'UpdateFields'
    }

    def __init__(self, render_tracked_changes=None, left_margin=None, right_margin=None, top_margin=None, bottom_margin=None, page_size=None, enable_open_type_features=None, unlink_table_of_contents=None, update_fields=None, **kwargs):  # noqa: E501
        """Initializes new instance of WordProcessingOptions"""  # noqa: E501

        self._render_tracked_changes = None
        self._left_margin = None
        self._right_margin = None
        self._top_margin = None
        self._bottom_margin = None
        self._page_size = None
        self._enable_open_type_features = None
        self._unlink_table_of_contents = None
        self._update_fields = None

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
        if page_size is not None:
            self.page_size = page_size
        if enable_open_type_features is not None:
            self.enable_open_type_features = enable_open_type_features
        if unlink_table_of_contents is not None:
            self.unlink_table_of_contents = unlink_table_of_contents
        if update_fields is not None:
            self.update_fields = update_fields
    
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
    
    @property
    def page_size(self):
        """
        Gets the page_size.  # noqa: E501

        The size of the page.  # noqa: E501

        :return: The page_size.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size.

        The size of the page.  # noqa: E501

        :param page_size: The page_size.  # noqa: E501
        :type: str
        """
        if page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501
        allowed_values = ["Unspecified", "Letter", "Ledger", "A0", "A1", "A2", "A3", "A4"]  # noqa: E501
        if not page_size.isdigit():	
            if page_size not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_size` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_size, allowed_values))
            self._page_size = page_size
        else:
            self._page_size = allowed_values[int(page_size) if six.PY3 else long(page_size)]
    
    @property
    def enable_open_type_features(self):
        """
        Gets the enable_open_type_features.  # noqa: E501

        This option enables kerning and other OpenType Features when rendering Arabic, Hebrew, Indian Latin-based, or Cyrillic-based scripts.  # noqa: E501

        :return: The enable_open_type_features.  # noqa: E501
        :rtype: bool
        """
        return self._enable_open_type_features

    @enable_open_type_features.setter
    def enable_open_type_features(self, enable_open_type_features):
        """
        Sets the enable_open_type_features.

        This option enables kerning and other OpenType Features when rendering Arabic, Hebrew, Indian Latin-based, or Cyrillic-based scripts.  # noqa: E501

        :param enable_open_type_features: The enable_open_type_features.  # noqa: E501
        :type: bool
        """
        if enable_open_type_features is None:
            raise ValueError("Invalid value for `enable_open_type_features`, must not be `None`")  # noqa: E501
        self._enable_open_type_features = enable_open_type_features
    
    @property
    def unlink_table_of_contents(self):
        """
        Gets the unlink_table_of_contents.  # noqa: E501

        When rendering to HTML or PDF, you can set this option to `true` to disable navigation from the table of contents. For HTML rendering, `a` tags with relative links will be replaced with `span` tags, removing functionality but preserving visual appearance. For PDF rendering, the table of contents will be rendered as plain text without links to document sections.               # noqa: E501

        :return: The unlink_table_of_contents.  # noqa: E501
        :rtype: bool
        """
        return self._unlink_table_of_contents

    @unlink_table_of_contents.setter
    def unlink_table_of_contents(self, unlink_table_of_contents):
        """
        Sets the unlink_table_of_contents.

        When rendering to HTML or PDF, you can set this option to `true` to disable navigation from the table of contents. For HTML rendering, `a` tags with relative links will be replaced with `span` tags, removing functionality but preserving visual appearance. For PDF rendering, the table of contents will be rendered as plain text without links to document sections.               # noqa: E501

        :param unlink_table_of_contents: The unlink_table_of_contents.  # noqa: E501
        :type: bool
        """
        if unlink_table_of_contents is None:
            raise ValueError("Invalid value for `unlink_table_of_contents`, must not be `None`")  # noqa: E501
        self._unlink_table_of_contents = unlink_table_of_contents
    
    @property
    def update_fields(self):
        """
        Gets the update_fields.  # noqa: E501

        Determines if fields of certain types should be updated before saving the input WordProcessing document to the HTML, PDF, PNG, or JPEG output formats. Default value for this property is true — fields will be updated before saving.               # noqa: E501

        :return: The update_fields.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """
        Sets the update_fields.

        Determines if fields of certain types should be updated before saving the input WordProcessing document to the HTML, PDF, PNG, or JPEG output formats. Default value for this property is true — fields will be updated before saving.               # noqa: E501

        :param update_fields: The update_fields.  # noqa: E501
        :type: bool
        """
        if update_fields is None:
            raise ValueError("Invalid value for `update_fields`, must not be `None`")  # noqa: E501
        self._update_fields = update_fields

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
