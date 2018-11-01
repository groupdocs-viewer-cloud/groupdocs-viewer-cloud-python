# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="EmailOptions.py">
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

class EmailOptions(object):
    """
    The Email documents rendering options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'encoding': 'str',
        'page_size': 'str',
        'field_labels': 'list[FieldLabel]'
    }

    attribute_map = {
        'encoding': 'encoding',
        'page_size': 'pageSize',
        'field_labels': 'fieldLabels'
    }

    def __init__(self, encoding=None, page_size=None, field_labels=None, **kwargs):  # noqa: E501
        """Initializes new instance of EmailOptions"""  # noqa: E501

        self._encoding = None
        self._page_size = None
        self._field_labels = None

        if encoding is not None:
            self.encoding = encoding
        if page_size is not None:
            self.page_size = page_size
        if field_labels is not None:
            self.field_labels = field_labels
    
    @property
    def encoding(self):
        """
        Gets the encoding.  # noqa: E501

        The document encoding e.g. \"utf-8\".  # noqa: E501

        :return: The encoding.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding.

        The document encoding e.g. \"utf-8\".  # noqa: E501

        :param encoding: The encoding.  # noqa: E501
        :type: str
        """
        self._encoding = encoding
    
    @property
    def page_size(self):
        """
        Gets the page_size.  # noqa: E501

        The size of the output page when rendering as PDF or image. Supported values {Unknown|Letter|Ledger|A0|A1|A2|A3}: 1. Unknown - the default, unspecified page size. 2. Letter - the size of the Letter page in points is 792x612. 3. Ledger - the size of the Letter page in points is 1224x792. 4. A0 - the size of the A0 page in points is 3371x2384. 5. A1 - the size of the A1 page in points is 2384x1685. 6. A2 - the size of the A2 page in points is 1684x1190. 7. A3 - the size of the A3 page in points is 1190x842. 8. A4 - the size of the A4 page in points is 842x595.  # noqa: E501

        :return: The page_size.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size.

        The size of the output page when rendering as PDF or image. Supported values {Unknown|Letter|Ledger|A0|A1|A2|A3}: 1. Unknown - the default, unspecified page size. 2. Letter - the size of the Letter page in points is 792x612. 3. Ledger - the size of the Letter page in points is 1224x792. 4. A0 - the size of the A0 page in points is 3371x2384. 5. A1 - the size of the A1 page in points is 2384x1685. 6. A2 - the size of the A2 page in points is 1684x1190. 7. A3 - the size of the A3 page in points is 1190x842. 8. A4 - the size of the A4 page in points is 842x595.  # noqa: E501

        :param page_size: The page_size.  # noqa: E501
        :type: str
        """
        self._page_size = page_size
    
    @property
    def field_labels(self):
        """
        Gets the field_labels.  # noqa: E501

        The list of supported email message field labels: 1. Field: \"Anniversary\" - default value is \"Anniversary\". 2. Field: \"Attachments\" - default value is \"Attachments\". 3. Field: \"Bcc\" - default value is \"Bcc\". 4. Field: \"Birthday\" - default value is \"Birthday\". 5. Field: \"Business\" - default value is \"Business\". 6. Field: \"BusinessAddress\" - default value is \"Business Address\". 7. Field: \"BusinessFax\" - default value is \"Business Fax\". 8. Field: \"BusinessHomepage\" - default value is \"BusinessHomePage\". 9. Field: \"Cc\" - default value is \"Cc\". 10. Field: \"Company\" - default value is \"Company\". 11. Field: \"Department\" - default value is \"Department\". 12. Field: \"Email\" - default value is \"Email\". 13. Field: \"EmailDisplayAs\" - default value is \"Email Display As\". 14. Field: \"Email2\" - default value is \"Email2\". 15. Field: \"Email2DisplayAs\" - default value is \"Email2 Display As\". 16. Field: \"Email3\" - default value is \"Email3\". 17. Field: \"Email3DisplayAs\" - default value is \"Email3 Display As\". 18. Field: \"End\" - default value is \"End\". 19. Field: \"FirstName\" - default value is \"First Name\". 20. Field: \"From\" - default value is \"From\". 21. Field: \"FullName\" - default value is \"Full Name\". 22. Field: \"Gender\" - default value is \"Gender\". 23. Field: \"Hobbies\" - default value is \"Hobbies\". 24. Field: \"Home\" - default value is \"Home\". 25. Field: \"HomeAddress\" - default value is \"Home Address\". 26. Field: \"Importance\" - default value is \"Importance\". 27. Field: \"JobTitle\" - default value is \"Job Title\". 28. Field: \"LastName\" - default value is \"Last Name\". 29. Field: \"Location\" - default value is \"Location\". 30. Field: \"MiddleName\" - default value is \"Middle Name\". 31. Field: \"Mobile\" - default value is \"Mobile\". 32. Field: \"Organizer\" - default value is \"Organizer\". 33. Field: \"OtherAddress\" - default value is \"Other Address\". 34. Field: \"PersonalHomepage\" - default value is \"PersonalHomePage\". 35. Field: \"Profession\" - default value is \"Profession\". 36. Field: \"Recurrence\" - default value is \"Recurrence\". 37. Field: \"RecurrencePattern\" - default value is \"Recurrence Pattern\". 38. Field: \"RequiredAttendees\" - default value is \"Required Attendees\". 39. Field: \"Sent\" - default value is \"Sent\". 40. Field: \"ShowTimeAs\" - default value is \"Show Time As\". 41. Field: \"SpousePartner\" - default value is \"Spouse/Partner\". 42. Field: \"Start\" - default value is \"Start\". 43. Field: \"Subject\" - default value is \"Subject\". 44. Field: \"To\" - default value is \"To\". 45. Field: \"UserField1\" - default value is \"User Field 1\". 46. Field: \"UserField2\" - default value is \"User Field 2\". 47. Field: \"UserField3\" - default value is \"User Field 3\". 48. Field: \"UserField4\" - default value is \"User Field 4\".  # noqa: E501

        :return: The field_labels.  # noqa: E501
        :rtype: list[FieldLabel]
        """
        return self._field_labels

    @field_labels.setter
    def field_labels(self, field_labels):
        """
        Sets the field_labels.

        The list of supported email message field labels: 1. Field: \"Anniversary\" - default value is \"Anniversary\". 2. Field: \"Attachments\" - default value is \"Attachments\". 3. Field: \"Bcc\" - default value is \"Bcc\". 4. Field: \"Birthday\" - default value is \"Birthday\". 5. Field: \"Business\" - default value is \"Business\". 6. Field: \"BusinessAddress\" - default value is \"Business Address\". 7. Field: \"BusinessFax\" - default value is \"Business Fax\". 8. Field: \"BusinessHomepage\" - default value is \"BusinessHomePage\". 9. Field: \"Cc\" - default value is \"Cc\". 10. Field: \"Company\" - default value is \"Company\". 11. Field: \"Department\" - default value is \"Department\". 12. Field: \"Email\" - default value is \"Email\". 13. Field: \"EmailDisplayAs\" - default value is \"Email Display As\". 14. Field: \"Email2\" - default value is \"Email2\". 15. Field: \"Email2DisplayAs\" - default value is \"Email2 Display As\". 16. Field: \"Email3\" - default value is \"Email3\". 17. Field: \"Email3DisplayAs\" - default value is \"Email3 Display As\". 18. Field: \"End\" - default value is \"End\". 19. Field: \"FirstName\" - default value is \"First Name\". 20. Field: \"From\" - default value is \"From\". 21. Field: \"FullName\" - default value is \"Full Name\". 22. Field: \"Gender\" - default value is \"Gender\". 23. Field: \"Hobbies\" - default value is \"Hobbies\". 24. Field: \"Home\" - default value is \"Home\". 25. Field: \"HomeAddress\" - default value is \"Home Address\". 26. Field: \"Importance\" - default value is \"Importance\". 27. Field: \"JobTitle\" - default value is \"Job Title\". 28. Field: \"LastName\" - default value is \"Last Name\". 29. Field: \"Location\" - default value is \"Location\". 30. Field: \"MiddleName\" - default value is \"Middle Name\". 31. Field: \"Mobile\" - default value is \"Mobile\". 32. Field: \"Organizer\" - default value is \"Organizer\". 33. Field: \"OtherAddress\" - default value is \"Other Address\". 34. Field: \"PersonalHomepage\" - default value is \"PersonalHomePage\". 35. Field: \"Profession\" - default value is \"Profession\". 36. Field: \"Recurrence\" - default value is \"Recurrence\". 37. Field: \"RecurrencePattern\" - default value is \"Recurrence Pattern\". 38. Field: \"RequiredAttendees\" - default value is \"Required Attendees\". 39. Field: \"Sent\" - default value is \"Sent\". 40. Field: \"ShowTimeAs\" - default value is \"Show Time As\". 41. Field: \"SpousePartner\" - default value is \"Spouse/Partner\". 42. Field: \"Start\" - default value is \"Start\". 43. Field: \"Subject\" - default value is \"Subject\". 44. Field: \"To\" - default value is \"To\". 45. Field: \"UserField1\" - default value is \"User Field 1\". 46. Field: \"UserField2\" - default value is \"User Field 2\". 47. Field: \"UserField3\" - default value is \"User Field 3\". 48. Field: \"UserField4\" - default value is \"User Field 4\".  # noqa: E501

        :param field_labels: The field_labels.  # noqa: E501
        :type: list[FieldLabel]
        """
        self._field_labels = field_labels

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
        if not isinstance(other, EmailOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
