# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="EmailOptions.py">
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

class EmailOptions(object):
    """
    Rendering options for Email file formats. Email file formats include files with extensions: .msg, .eml, .emlx, .ifc, .stl
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
        'field_labels': 'list[FieldLabel]'
    }

    attribute_map = {
        'page_size': 'PageSize',
        'field_labels': 'FieldLabels'
    }

    def __init__(self, page_size=None, field_labels=None, **kwargs):  # noqa: E501
        """Initializes new instance of EmailOptions"""  # noqa: E501

        self._page_size = None
        self._field_labels = None

        if page_size is not None:
            self.page_size = page_size
        if field_labels is not None:
            self.field_labels = field_labels
    
    @property
    def page_size(self):
        """
        Gets the page_size.  # noqa: E501

        The size of the output page when rendering as PDF or image.  # noqa: E501

        :return: The page_size.  # noqa: E501
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size.

        The size of the output page when rendering as PDF or image.  # noqa: E501

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
    def field_labels(self):
        """
        Gets the field_labels.  # noqa: E501

        The list of supported email message field labels: 1. Field: \"Anniversary\" - default label is \"Anniversary\". 2. Field: \"Attachments\" - default label is \"Attachments\". 3. Field: \"Bcc\" - default label is \"Bcc\". 4. Field: \"Birthday\" - default label is \"Birthday\". 5. Field: \"Business\" - default label is \"Business\". 6. Field: \"BusinessAddress\" - default label is \"Business Address\". 7. Field: \"BusinessFax\" - default label is \"Business Fax\". 8. Field: \"BusinessHomepage\" - default label is \"BusinessHomePage\". 9. Field: \"Cc\" - default label is \"Cc\". 10. Field: \"Company\" - default label is \"Company\". 11. Field: \"Department\" - default label is \"Department\". 12. Field: \"Email\" - default label is \"Email\". 13. Field: \"EmailDisplayAs\" - default label is \"Email Display As\". 14. Field: \"Email2\" - default label is \"Email2\". 15. Field: \"Email2DisplayAs\" - default label is \"Email2 Display As\". 16. Field: \"Email3\" - default label is \"Email3\". 17. Field: \"Email3DisplayAs\" - default label is \"Email3 Display As\". 18. Field: \"End\" - default label is \"End\". 19. Field: \"FirstName\" - default label is \"First Name\". 20. Field: \"From\" - default label is \"From\". 21. Field: \"FullName\" - default label is \"Full Name\". 22. Field: \"Gender\" - default label is \"Gender\". 23. Field: \"Hobbies\" - default label is \"Hobbies\". 24. Field: \"Home\" - default label is \"Home\". 25. Field: \"HomeAddress\" - default label is \"Home Address\". 26. Field: \"Importance\" - default label is \"Importance\". 27. Field: \"JobTitle\" - default label is \"Job Title\". 28. Field: \"LastName\" - default label is \"Last Name\". 29. Field: \"Location\" - default label is \"Location\". 30. Field: \"MiddleName\" - default label is \"Middle Name\". 31. Field: \"Mobile\" - default label is \"Mobile\". 32. Field: \"Organizer\" - default label is \"Organizer\". 33. Field: \"OtherAddress\" - default label is \"Other Address\". 34. Field: \"PersonalHomepage\" - default label is \"PersonalHomePage\". 35. Field: \"Profession\" - default label is \"Profession\". 36. Field: \"Recurrence\" - default label is \"Recurrence\". 37. Field: \"RecurrencePattern\" - default label is \"Recurrence Pattern\". 38. Field: \"RequiredAttendees\" - default label is \"Required Attendees\". 39. Field: \"Sent\" - default label is \"Sent\". 40. Field: \"ShowTimeAs\" - default label is \"Show Time As\". 41. Field: \"SpousePartner\" - default label is \"Spouse/Partner\". 42. Field: \"Start\" - default label is \"Start\". 43. Field: \"Subject\" - default label is \"Subject\". 44. Field: \"To\" - default label is \"To\". 45. Field: \"UserField1\" - default label is \"User Field 1\". 46. Field: \"UserField2\" - default label is \"User Field 2\". 47. Field: \"UserField3\" - default label is \"User Field 3\". 48. Field: \"UserField4\" - default label is \"User Field 4\".  # noqa: E501

        :return: The field_labels.  # noqa: E501
        :rtype: list[FieldLabel]
        """
        return self._field_labels

    @field_labels.setter
    def field_labels(self, field_labels):
        """
        Sets the field_labels.

        The list of supported email message field labels: 1. Field: \"Anniversary\" - default label is \"Anniversary\". 2. Field: \"Attachments\" - default label is \"Attachments\". 3. Field: \"Bcc\" - default label is \"Bcc\". 4. Field: \"Birthday\" - default label is \"Birthday\". 5. Field: \"Business\" - default label is \"Business\". 6. Field: \"BusinessAddress\" - default label is \"Business Address\". 7. Field: \"BusinessFax\" - default label is \"Business Fax\". 8. Field: \"BusinessHomepage\" - default label is \"BusinessHomePage\". 9. Field: \"Cc\" - default label is \"Cc\". 10. Field: \"Company\" - default label is \"Company\". 11. Field: \"Department\" - default label is \"Department\". 12. Field: \"Email\" - default label is \"Email\". 13. Field: \"EmailDisplayAs\" - default label is \"Email Display As\". 14. Field: \"Email2\" - default label is \"Email2\". 15. Field: \"Email2DisplayAs\" - default label is \"Email2 Display As\". 16. Field: \"Email3\" - default label is \"Email3\". 17. Field: \"Email3DisplayAs\" - default label is \"Email3 Display As\". 18. Field: \"End\" - default label is \"End\". 19. Field: \"FirstName\" - default label is \"First Name\". 20. Field: \"From\" - default label is \"From\". 21. Field: \"FullName\" - default label is \"Full Name\". 22. Field: \"Gender\" - default label is \"Gender\". 23. Field: \"Hobbies\" - default label is \"Hobbies\". 24. Field: \"Home\" - default label is \"Home\". 25. Field: \"HomeAddress\" - default label is \"Home Address\". 26. Field: \"Importance\" - default label is \"Importance\". 27. Field: \"JobTitle\" - default label is \"Job Title\". 28. Field: \"LastName\" - default label is \"Last Name\". 29. Field: \"Location\" - default label is \"Location\". 30. Field: \"MiddleName\" - default label is \"Middle Name\". 31. Field: \"Mobile\" - default label is \"Mobile\". 32. Field: \"Organizer\" - default label is \"Organizer\". 33. Field: \"OtherAddress\" - default label is \"Other Address\". 34. Field: \"PersonalHomepage\" - default label is \"PersonalHomePage\". 35. Field: \"Profession\" - default label is \"Profession\". 36. Field: \"Recurrence\" - default label is \"Recurrence\". 37. Field: \"RecurrencePattern\" - default label is \"Recurrence Pattern\". 38. Field: \"RequiredAttendees\" - default label is \"Required Attendees\". 39. Field: \"Sent\" - default label is \"Sent\". 40. Field: \"ShowTimeAs\" - default label is \"Show Time As\". 41. Field: \"SpousePartner\" - default label is \"Spouse/Partner\". 42. Field: \"Start\" - default label is \"Start\". 43. Field: \"Subject\" - default label is \"Subject\". 44. Field: \"To\" - default label is \"To\". 45. Field: \"UserField1\" - default label is \"User Field 1\". 46. Field: \"UserField2\" - default label is \"User Field 2\". 47. Field: \"UserField3\" - default label is \"User Field 3\". 48. Field: \"UserField4\" - default label is \"User Field 4\".  # noqa: E501

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
