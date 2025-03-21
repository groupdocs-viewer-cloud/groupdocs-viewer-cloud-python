# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="InfoResult.py">
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

class InfoResult(object):
    """
    View result information
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'format_extension': 'str',
        'format': 'str',
        'pages': 'list[PageInfo]',
        'attachments': 'list[AttachmentInfo]',
        'archive_view_info': 'ArchiveViewInfo',
        'cad_view_info': 'CadViewInfo',
        'project_management_view_info': 'ProjectManagementViewInfo',
        'outlook_view_info': 'OutlookViewInfo',
        'pdf_view_info': 'PdfViewInfo'
    }

    attribute_map = {
        'format_extension': 'FormatExtension',
        'format': 'Format',
        'pages': 'Pages',
        'attachments': 'Attachments',
        'archive_view_info': 'ArchiveViewInfo',
        'cad_view_info': 'CadViewInfo',
        'project_management_view_info': 'ProjectManagementViewInfo',
        'outlook_view_info': 'OutlookViewInfo',
        'pdf_view_info': 'PdfViewInfo'
    }

    def __init__(self, format_extension=None, format=None, pages=None, attachments=None, archive_view_info=None, cad_view_info=None, project_management_view_info=None, outlook_view_info=None, pdf_view_info=None, **kwargs):  # noqa: E501
        """Initializes new instance of InfoResult"""  # noqa: E501

        self._format_extension = None
        self._format = None
        self._pages = None
        self._attachments = None
        self._archive_view_info = None
        self._cad_view_info = None
        self._project_management_view_info = None
        self._outlook_view_info = None
        self._pdf_view_info = None

        if format_extension is not None:
            self.format_extension = format_extension
        if format is not None:
            self.format = format
        if pages is not None:
            self.pages = pages
        if attachments is not None:
            self.attachments = attachments
        if archive_view_info is not None:
            self.archive_view_info = archive_view_info
        if cad_view_info is not None:
            self.cad_view_info = cad_view_info
        if project_management_view_info is not None:
            self.project_management_view_info = project_management_view_info
        if outlook_view_info is not None:
            self.outlook_view_info = outlook_view_info
        if pdf_view_info is not None:
            self.pdf_view_info = pdf_view_info
    
    @property
    def format_extension(self):
        """
        Gets the format_extension.  # noqa: E501

        File format extension  # noqa: E501

        :return: The format_extension.  # noqa: E501
        :rtype: str
        """
        return self._format_extension

    @format_extension.setter
    def format_extension(self, format_extension):
        """
        Sets the format_extension.

        File format extension  # noqa: E501

        :param format_extension: The format_extension.  # noqa: E501
        :type: str
        """
        self._format_extension = format_extension
    
    @property
    def format(self):
        """
        Gets the format.  # noqa: E501

        File format  # noqa: E501

        :return: The format.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format.

        File format  # noqa: E501

        :param format: The format.  # noqa: E501
        :type: str
        """
        self._format = format
    
    @property
    def pages(self):
        """
        Gets the pages.  # noqa: E501

        View result pages  # noqa: E501

        :return: The pages.  # noqa: E501
        :rtype: list[PageInfo]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages.

        View result pages  # noqa: E501

        :param pages: The pages.  # noqa: E501
        :type: list[PageInfo]
        """
        self._pages = pages
    
    @property
    def attachments(self):
        """
        Gets the attachments.  # noqa: E501

        Attachments  # noqa: E501

        :return: The attachments.  # noqa: E501
        :rtype: list[AttachmentInfo]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments.

        Attachments  # noqa: E501

        :param attachments: The attachments.  # noqa: E501
        :type: list[AttachmentInfo]
        """
        self._attachments = attachments
    
    @property
    def archive_view_info(self):
        """
        Gets the archive_view_info.  # noqa: E501

        Represents view information for archive file  # noqa: E501

        :return: The archive_view_info.  # noqa: E501
        :rtype: ArchiveViewInfo
        """
        return self._archive_view_info

    @archive_view_info.setter
    def archive_view_info(self, archive_view_info):
        """
        Sets the archive_view_info.

        Represents view information for archive file  # noqa: E501

        :param archive_view_info: The archive_view_info.  # noqa: E501
        :type: ArchiveViewInfo
        """
        self._archive_view_info = archive_view_info
    
    @property
    def cad_view_info(self):
        """
        Gets the cad_view_info.  # noqa: E501

        Represents view information for CAD drawing  # noqa: E501

        :return: The cad_view_info.  # noqa: E501
        :rtype: CadViewInfo
        """
        return self._cad_view_info

    @cad_view_info.setter
    def cad_view_info(self, cad_view_info):
        """
        Sets the cad_view_info.

        Represents view information for CAD drawing  # noqa: E501

        :param cad_view_info: The cad_view_info.  # noqa: E501
        :type: CadViewInfo
        """
        self._cad_view_info = cad_view_info
    
    @property
    def project_management_view_info(self):
        """
        Gets the project_management_view_info.  # noqa: E501

        Represents view information for MS Project document  # noqa: E501

        :return: The project_management_view_info.  # noqa: E501
        :rtype: ProjectManagementViewInfo
        """
        return self._project_management_view_info

    @project_management_view_info.setter
    def project_management_view_info(self, project_management_view_info):
        """
        Sets the project_management_view_info.

        Represents view information for MS Project document  # noqa: E501

        :param project_management_view_info: The project_management_view_info.  # noqa: E501
        :type: ProjectManagementViewInfo
        """
        self._project_management_view_info = project_management_view_info
    
    @property
    def outlook_view_info(self):
        """
        Gets the outlook_view_info.  # noqa: E501

        Represents view information for Outlook Data file  # noqa: E501

        :return: The outlook_view_info.  # noqa: E501
        :rtype: OutlookViewInfo
        """
        return self._outlook_view_info

    @outlook_view_info.setter
    def outlook_view_info(self, outlook_view_info):
        """
        Sets the outlook_view_info.

        Represents view information for Outlook Data file  # noqa: E501

        :param outlook_view_info: The outlook_view_info.  # noqa: E501
        :type: OutlookViewInfo
        """
        self._outlook_view_info = outlook_view_info
    
    @property
    def pdf_view_info(self):
        """
        Gets the pdf_view_info.  # noqa: E501

        Represents view information for PDF document  # noqa: E501

        :return: The pdf_view_info.  # noqa: E501
        :rtype: PdfViewInfo
        """
        return self._pdf_view_info

    @pdf_view_info.setter
    def pdf_view_info(self, pdf_view_info):
        """
        Sets the pdf_view_info.

        Represents view information for PDF document  # noqa: E501

        :param pdf_view_info: The pdf_view_info.  # noqa: E501
        :type: PdfViewInfo
        """
        self._pdf_view_info = pdf_view_info

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
        if not isinstance(other, InfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
