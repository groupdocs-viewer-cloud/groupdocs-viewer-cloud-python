# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="WebDocumentOptions.py">
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

class WebDocumentOptions(object):
    """
    This rendering options enables you to customize the appearance of the output HTML/PDF/PNG/JPEG when rendering Web documents.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_size': 'str',
        'left_margin': 'float',
        'right_margin': 'float',
        'top_margin': 'float',
        'bottom_margin': 'float'
    }

    attribute_map = {
        'page_size': 'PageSize',
        'left_margin': 'LeftMargin',
        'right_margin': 'RightMargin',
        'top_margin': 'TopMargin',
        'bottom_margin': 'BottomMargin'
    }

    def __init__(self, page_size=None, left_margin=None, right_margin=None, top_margin=None, bottom_margin=None, **kwargs):  # noqa: E501
        """Initializes new instance of WebDocumentOptions"""  # noqa: E501

        self._page_size = None
        self._left_margin = None
        self._right_margin = None
        self._top_margin = None
        self._bottom_margin = None

        if page_size is not None:
            self.page_size = page_size
        if left_margin is not None:
            self.left_margin = left_margin
        if right_margin is not None:
            self.right_margin = right_margin
        if top_margin is not None:
            self.top_margin = top_margin
        if bottom_margin is not None:
            self.bottom_margin = bottom_margin
    
    @property
    def page_size(self):
        """
        Gets the page_size.  # noqa: E501

        The size of the output page. The default value is GroupDocs.Viewer.Options.PageSize.Letter 792 x 612 points. When contents does not fit set a larger page size e.g. GroupDocs.Viewer.Options.PageSize.A3.               # noqa: E501

        :return: The page_size.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size.

        The size of the output page. The default value is GroupDocs.Viewer.Options.PageSize.Letter 792 x 612 points. When contents does not fit set a larger page size e.g. GroupDocs.Viewer.Options.PageSize.A3.               # noqa: E501

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
    def left_margin(self):
        """
        Gets the left_margin.  # noqa: E501

        The distance (in points) between the left edge of the page and the left boundary  of the body text. The default value is 5 points.  # noqa: E501

        :return: The left_margin.  # noqa: E501
        :rtype: float
        """
        return self._left_margin

    @left_margin.setter
    def left_margin(self, left_margin):
        """
        Sets the left_margin.

        The distance (in points) between the left edge of the page and the left boundary  of the body text. The default value is 5 points.  # noqa: E501

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

        The distance (in points) between the right edge of the page and the right boundary of the body text. The default value is 5 points.  # noqa: E501

        :return: The right_margin.  # noqa: E501
        :rtype: float
        """
        return self._right_margin

    @right_margin.setter
    def right_margin(self, right_margin):
        """
        Sets the right_margin.

        The distance (in points) between the right edge of the page and the right boundary of the body text. The default value is 5 points.  # noqa: E501

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

        The distance (in points) between the top edge of the page and the top boundary of the body text. The default value is 72 points.  # noqa: E501

        :return: The top_margin.  # noqa: E501
        :rtype: float
        """
        return self._top_margin

    @top_margin.setter
    def top_margin(self, top_margin):
        """
        Sets the top_margin.

        The distance (in points) between the top edge of the page and the top boundary of the body text. The default value is 72 points.  # noqa: E501

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

        The distance (in points) between the bottom edge of the page and the bottom boundary of the body text. The default value is 72 points.  # noqa: E501

        :return: The bottom_margin.  # noqa: E501
        :rtype: float
        """
        return self._bottom_margin

    @bottom_margin.setter
    def bottom_margin(self, bottom_margin):
        """
        Sets the bottom_margin.

        The distance (in points) between the bottom edge of the page and the bottom boundary of the body text. The default value is 72 points.  # noqa: E501

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
        if not isinstance(other, WebDocumentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
