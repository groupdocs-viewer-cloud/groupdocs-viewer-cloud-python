# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_viewer_api.py">
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
import warnings
import threading

import six

from groupdocs_viewer_cloud import ViewerApi, Configuration
from test.test_settings import TestSettings

class TestViewerApi(unittest.TestCase):
    """ViewerApi unit tests"""

    def setUp(self):
        if six.PY3:
            warnings.simplefilter("ignore", ResourceWarning)

    def test_initialize_from_keys(self):
        """Test for factory method from_keys"""
        
        viewer_api = ViewerApi.from_keys(TestSettings.APP_SID, TestSettings.APP_KEY)

        self.assertIsNotNone(viewer_api)
    
    def test_initialize_from_config(self):
        """Test for factory method from_config"""
        
        config = Configuration(TestSettings.APP_SID, TestSettings.APP_KEY)
        viewer_api = ViewerApi.from_config(config)

        self.assertIsNotNone(viewer_api)

    def test_close_app_pool(self):
        """
        Test for method which closes thread pool
        This methods should be safe to call multiple times
        """
        
        config = Configuration(TestSettings.APP_SID, TestSettings.APP_KEY)
        config.api_base_url = TestSettings.API_BASE_URL
        viewer_api = ViewerApi.from_config(config)

        viewer_api.get_supported_file_formats(is_async = True).get()
        viewer_api.close()

        viewer_api.get_supported_file_formats(is_async = True).get()
        viewer_api.close()

        self.assertEqual(1, threading.active_count())

if __name__ == '__main__':
    unittest.main()
