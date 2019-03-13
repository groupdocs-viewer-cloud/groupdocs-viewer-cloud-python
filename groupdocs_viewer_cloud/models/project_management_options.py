# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ProjectManagementOptions.py">
#   Copyright (c) 2003-2019 Aspose Pty Ltd
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

class ProjectManagementOptions(object):
    """
    Rendering options for Project file formats. Project file formats include files with extensions: .mpt, .mpp
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
        'time_unit': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'page_size': 'PageSize',
        'time_unit': 'TimeUnit',
        'start_date': 'StartDate',
        'end_date': 'EndDate'
    }

    def __init__(self, page_size=None, time_unit=None, start_date=None, end_date=None, **kwargs):  # noqa: E501
        """Initializes new instance of ProjectManagementOptions"""  # noqa: E501

        self._page_size = None
        self._time_unit = None
        self._start_date = None
        self._end_date = None

        if page_size is not None:
            self.page_size = page_size
        if time_unit is not None:
            self.time_unit = time_unit
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
    
    @property
    def page_size(self):
        """
        Gets the page_size.  # noqa: E501

        The size of the page. Supported values {Unknown|Letter|Ledger|A0|A1|A2|A3}: 1. Unknown - the default, unspecified page size. 2. Letter - the size of the Letter page in points is 792x612. 3. Ledger - the size of the Letter page in points is 1224x792. 4. A0 - the size of the A0 page in points is 3371x2384. 5. A1 - the size of the A1 page in points is 2384x1685. 6. A2 - the size of the A2 page in points is 1684x1190. 7. A3 - the size of the A3 page in points is 1190x842. 8. A4 - the size of the A4 page in points is 842x595.  # noqa: E501

        :return: The page_size.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size.

        The size of the page. Supported values {Unknown|Letter|Ledger|A0|A1|A2|A3}: 1. Unknown - the default, unspecified page size. 2. Letter - the size of the Letter page in points is 792x612. 3. Ledger - the size of the Letter page in points is 1224x792. 4. A0 - the size of the A0 page in points is 3371x2384. 5. A1 - the size of the A1 page in points is 2384x1685. 6. A2 - the size of the A2 page in points is 1684x1190. 7. A3 - the size of the A3 page in points is 1190x842. 8. A4 - the size of the A4 page in points is 842x595.  # noqa: E501

        :param page_size: The page_size.  # noqa: E501
        :type: str
        """
        self._page_size = page_size
    
    @property
    def time_unit(self):
        """
        Gets the time_unit.  # noqa: E501

        The time unit to use as minimal point. Supported values {Unknown|Days|ThirdsOfMonths|Months}: 1. Unknown - unknown, unspecified time scale. 2. Days - one day interval. 3. ThirdsOfMonths - one third of the month. 4. Months - one month interval.  # noqa: E501

        :return: The time_unit.  # noqa: E501
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """
        Sets the time_unit.

        The time unit to use as minimal point. Supported values {Unknown|Days|ThirdsOfMonths|Months}: 1. Unknown - unknown, unspecified time scale. 2. Days - one day interval. 3. ThirdsOfMonths - one third of the month. 4. Months - one month interval.  # noqa: E501

        :param time_unit: The time_unit.  # noqa: E501
        :type: str
        """
        self._time_unit = time_unit
    
    @property
    def start_date(self):
        """
        Gets the start_date.  # noqa: E501

        The start date of a Gantt Chart View to render.          # noqa: E501

        :return: The start_date.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date.

        The start date of a Gantt Chart View to render.          # noqa: E501

        :param start_date: The start_date.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501
        self._start_date = start_date
    
    @property
    def end_date(self):
        """
        Gets the end_date.  # noqa: E501

        The end date of a Gantt Chart View to render.  # noqa: E501

        :return: The end_date.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date.

        The end date of a Gantt Chart View to render.  # noqa: E501

        :param end_date: The end_date.  # noqa: E501
        :type: datetime
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501
        self._end_date = end_date

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
        if not isinstance(other, ProjectManagementOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
