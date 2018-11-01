# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_fonts_api.py">
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

from __future__ import absolute_import

import unittest
import threading

from groupdocs_viewer_cloud import ViewerApi, Configuration, ApiException
from test.test_context import TestContext
from test.test_settings import TestSettings

class TestFontsApi(TestContext):
    """ViewerApi unit tests"""

    def test_delete_fonts_cache(self):
        """
        Test case for delete_fonts_cache
    
        Removes fonts cache.  # noqa: E501
        """
        
        response = self.viewer_api.delete_fonts_cache()
    
        self.assertIsNone(response)

    def test_delete_fonts_cache_async(self):
        """
        Test case for delete_fonts_cache

        Removes fonts cache.  # noqa: E501
        """

        apply_result = self.viewer_api.delete_fonts_cache(is_async = True)
        response = apply_result.get()

        self.assertIsNone(response)

    def test_get_fonts(self):
        """
        Test case for get_fonts

        List installed fonts.  # noqa: E501
        """
        data = self.viewer_api.get_fonts()

        for font in data.families:
            self.assertFalse(font.name == "")

    def test_get_fonts_async(self):
        """
        Test case for get_fonts
    
        List installed fonts.  # noqa: E501
        """
        apply_result = self.viewer_api.get_fonts(is_async = True)
        data = apply_result.get()
    
        for font in data.families:
            self.assertFalse(font.name == "")

if __name__ == '__main__':
    unittest.main()