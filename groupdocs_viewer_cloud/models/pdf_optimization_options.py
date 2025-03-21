# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PdfOptimizationOptions.py">
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

class PdfOptimizationOptions(object):
    """
    Contains the PDF optimization options to apply to the output PDF file.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'lineriaze': 'bool',
        'remove_annotations': 'bool',
        'remove_form_fields': 'bool',
        'convert_to_gray_scale': 'bool',
        'subset_fonts': 'bool',
        'compress_images': 'bool',
        'image_quality': 'int',
        'resize_images': 'bool',
        'max_resolution': 'int',
        'optimize_spreadsheets': 'bool'
    }

    attribute_map = {
        'lineriaze': 'Lineriaze',
        'remove_annotations': 'RemoveAnnotations',
        'remove_form_fields': 'RemoveFormFields',
        'convert_to_gray_scale': 'ConvertToGrayScale',
        'subset_fonts': 'SubsetFonts',
        'compress_images': 'CompressImages',
        'image_quality': 'ImageQuality',
        'resize_images': 'ResizeImages',
        'max_resolution': 'MaxResolution',
        'optimize_spreadsheets': 'OptimizeSpreadsheets'
    }

    def __init__(self, lineriaze=None, remove_annotations=None, remove_form_fields=None, convert_to_gray_scale=None, subset_fonts=None, compress_images=None, image_quality=None, resize_images=None, max_resolution=None, optimize_spreadsheets=None, **kwargs):  # noqa: E501
        """Initializes new instance of PdfOptimizationOptions"""  # noqa: E501

        self._lineriaze = None
        self._remove_annotations = None
        self._remove_form_fields = None
        self._convert_to_gray_scale = None
        self._subset_fonts = None
        self._compress_images = None
        self._image_quality = None
        self._resize_images = None
        self._max_resolution = None
        self._optimize_spreadsheets = None

        if lineriaze is not None:
            self.lineriaze = lineriaze
        if remove_annotations is not None:
            self.remove_annotations = remove_annotations
        if remove_form_fields is not None:
            self.remove_form_fields = remove_form_fields
        if convert_to_gray_scale is not None:
            self.convert_to_gray_scale = convert_to_gray_scale
        if subset_fonts is not None:
            self.subset_fonts = subset_fonts
        if compress_images is not None:
            self.compress_images = compress_images
        if image_quality is not None:
            self.image_quality = image_quality
        if resize_images is not None:
            self.resize_images = resize_images
        if max_resolution is not None:
            self.max_resolution = max_resolution
        if optimize_spreadsheets is not None:
            self.optimize_spreadsheets = optimize_spreadsheets
    
    @property
    def lineriaze(self):
        """
        Gets the lineriaze.  # noqa: E501

        Enables optimization the output PDF file for viewing online with a web browser. This optimization allows a browser to display the first pages of a PDF file when     you open the document, instead of waiting for the entire file to download.  # noqa: E501

        :return: The lineriaze.  # noqa: E501
        :rtype: bool
        """
        return self._lineriaze

    @lineriaze.setter
    def lineriaze(self, lineriaze):
        """
        Sets the lineriaze.

        Enables optimization the output PDF file for viewing online with a web browser. This optimization allows a browser to display the first pages of a PDF file when     you open the document, instead of waiting for the entire file to download.  # noqa: E501

        :param lineriaze: The lineriaze.  # noqa: E501
        :type: bool
        """
        if lineriaze is None:
            raise ValueError("Invalid value for `lineriaze`, must not be `None`")  # noqa: E501
        self._lineriaze = lineriaze
    
    @property
    def remove_annotations(self):
        """
        Gets the remove_annotations.  # noqa: E501

        Enables removing annotation from the output PDF file.  # noqa: E501

        :return: The remove_annotations.  # noqa: E501
        :rtype: bool
        """
        return self._remove_annotations

    @remove_annotations.setter
    def remove_annotations(self, remove_annotations):
        """
        Sets the remove_annotations.

        Enables removing annotation from the output PDF file.  # noqa: E501

        :param remove_annotations: The remove_annotations.  # noqa: E501
        :type: bool
        """
        if remove_annotations is None:
            raise ValueError("Invalid value for `remove_annotations`, must not be `None`")  # noqa: E501
        self._remove_annotations = remove_annotations
    
    @property
    def remove_form_fields(self):
        """
        Gets the remove_form_fields.  # noqa: E501

        Enables removing form fields from a PDF file.  # noqa: E501

        :return: The remove_form_fields.  # noqa: E501
        :rtype: bool
        """
        return self._remove_form_fields

    @remove_form_fields.setter
    def remove_form_fields(self, remove_form_fields):
        """
        Sets the remove_form_fields.

        Enables removing form fields from a PDF file.  # noqa: E501

        :param remove_form_fields: The remove_form_fields.  # noqa: E501
        :type: bool
        """
        if remove_form_fields is None:
            raise ValueError("Invalid value for `remove_form_fields`, must not be `None`")  # noqa: E501
        self._remove_form_fields = remove_form_fields
    
    @property
    def convert_to_gray_scale(self):
        """
        Gets the convert_to_gray_scale.  # noqa: E501

        Enables converting the output PDF file to a grayscale.  # noqa: E501

        :return: The convert_to_gray_scale.  # noqa: E501
        :rtype: bool
        """
        return self._convert_to_gray_scale

    @convert_to_gray_scale.setter
    def convert_to_gray_scale(self, convert_to_gray_scale):
        """
        Sets the convert_to_gray_scale.

        Enables converting the output PDF file to a grayscale.  # noqa: E501

        :param convert_to_gray_scale: The convert_to_gray_scale.  # noqa: E501
        :type: bool
        """
        if convert_to_gray_scale is None:
            raise ValueError("Invalid value for `convert_to_gray_scale`, must not be `None`")  # noqa: E501
        self._convert_to_gray_scale = convert_to_gray_scale
    
    @property
    def subset_fonts(self):
        """
        Gets the subset_fonts.  # noqa: E501

        Subsets fonts in the output PDF file. If the file uses embedded fonts, it contains all font data. GroupDocs.Viewer can subset embedded fonts to reduce the file size.  # noqa: E501

        :return: The subset_fonts.  # noqa: E501
        :rtype: bool
        """
        return self._subset_fonts

    @subset_fonts.setter
    def subset_fonts(self, subset_fonts):
        """
        Sets the subset_fonts.

        Subsets fonts in the output PDF file. If the file uses embedded fonts, it contains all font data. GroupDocs.Viewer can subset embedded fonts to reduce the file size.  # noqa: E501

        :param subset_fonts: The subset_fonts.  # noqa: E501
        :type: bool
        """
        if subset_fonts is None:
            raise ValueError("Invalid value for `subset_fonts`, must not be `None`")  # noqa: E501
        self._subset_fonts = subset_fonts
    
    @property
    def compress_images(self):
        """
        Gets the compress_images.  # noqa: E501

        Enables compressing images in the output PDF file. Use this option to allow other compressing options: PdfOptimizationOptions.ImageQuality and PdfOptimizationOptions.MaxResolution.  # noqa: E501

        :return: The compress_images.  # noqa: E501
        :rtype: bool
        """
        return self._compress_images

    @compress_images.setter
    def compress_images(self, compress_images):
        """
        Sets the compress_images.

        Enables compressing images in the output PDF file. Use this option to allow other compressing options: PdfOptimizationOptions.ImageQuality and PdfOptimizationOptions.MaxResolution.  # noqa: E501

        :param compress_images: The compress_images.  # noqa: E501
        :type: bool
        """
        if compress_images is None:
            raise ValueError("Invalid value for `compress_images`, must not be `None`")  # noqa: E501
        self._compress_images = compress_images
    
    @property
    def image_quality(self):
        """
        Gets the image_quality.  # noqa: E501

        Sets the image quality in the output PDF file (in percent). To change the image quality, first set the PdfOptimizationOptions.CompressImages property to true.  # noqa: E501

        :return: The image_quality.  # noqa: E501
        :rtype: int
        """
        return self._image_quality

    @image_quality.setter
    def image_quality(self, image_quality):
        """
        Sets the image_quality.

        Sets the image quality in the output PDF file (in percent). To change the image quality, first set the PdfOptimizationOptions.CompressImages property to true.  # noqa: E501

        :param image_quality: The image_quality.  # noqa: E501
        :type: int
        """
        if image_quality is None:
            raise ValueError("Invalid value for `image_quality`, must not be `None`")  # noqa: E501
        self._image_quality = image_quality
    
    @property
    def resize_images(self):
        """
        Gets the resize_images.  # noqa: E501

        Enables setting the maximum resolution in the output PDF file. To allow this option, set the GroupDocs.Viewer.Options.PdfOptimizationOptions.CompressImages property to true. This option allows setting the GroupDocs.Viewer.Options.PdfOptimizationOptions.MaxResolution property.  # noqa: E501

        :return: The resize_images.  # noqa: E501
        :rtype: bool
        """
        return self._resize_images

    @resize_images.setter
    def resize_images(self, resize_images):
        """
        Sets the resize_images.

        Enables setting the maximum resolution in the output PDF file. To allow this option, set the GroupDocs.Viewer.Options.PdfOptimizationOptions.CompressImages property to true. This option allows setting the GroupDocs.Viewer.Options.PdfOptimizationOptions.MaxResolution property.  # noqa: E501

        :param resize_images: The resize_images.  # noqa: E501
        :type: bool
        """
        if resize_images is None:
            raise ValueError("Invalid value for `resize_images`, must not be `None`")  # noqa: E501
        self._resize_images = resize_images
    
    @property
    def max_resolution(self):
        """
        Gets the max_resolution.  # noqa: E501

        Sets the maximum resolution in the output PDF file. To allow this option, set the GroupDocs.Viewer.Options.PdfOptimizationOptions.CompressImages and GroupDocs.Viewer.Options.PdfOptimizationOptions.MaxResolution properties to true. The default value is 300.  # noqa: E501

        :return: The max_resolution.  # noqa: E501
        :rtype: int
        """
        return self._max_resolution

    @max_resolution.setter
    def max_resolution(self, max_resolution):
        """
        Sets the max_resolution.

        Sets the maximum resolution in the output PDF file. To allow this option, set the GroupDocs.Viewer.Options.PdfOptimizationOptions.CompressImages and GroupDocs.Viewer.Options.PdfOptimizationOptions.MaxResolution properties to true. The default value is 300.  # noqa: E501

        :param max_resolution: The max_resolution.  # noqa: E501
        :type: int
        """
        if max_resolution is None:
            raise ValueError("Invalid value for `max_resolution`, must not be `None`")  # noqa: E501
        self._max_resolution = max_resolution
    
    @property
    def optimize_spreadsheets(self):
        """
        Gets the optimize_spreadsheets.  # noqa: E501

        Enables optimization of spreadsheets in the PDF files. This optimization allows to reduce the output file size by setting up border lines. Besides that, it removes the Arial and Times New Roman characters of 32-127 codes.  # noqa: E501

        :return: The optimize_spreadsheets.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_spreadsheets

    @optimize_spreadsheets.setter
    def optimize_spreadsheets(self, optimize_spreadsheets):
        """
        Sets the optimize_spreadsheets.

        Enables optimization of spreadsheets in the PDF files. This optimization allows to reduce the output file size by setting up border lines. Besides that, it removes the Arial and Times New Roman characters of 32-127 codes.  # noqa: E501

        :param optimize_spreadsheets: The optimize_spreadsheets.  # noqa: E501
        :type: bool
        """
        if optimize_spreadsheets is None:
            raise ValueError("Invalid value for `optimize_spreadsheets`, must not be `None`")  # noqa: E501
        self._optimize_spreadsheets = optimize_spreadsheets

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
        if not isinstance(other, PdfOptimizationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
