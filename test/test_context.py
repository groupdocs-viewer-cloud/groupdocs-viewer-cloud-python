# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="test_context.py">
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

import glob
import json
import os
import tempfile
import unittest
import warnings
import threading

from test.test_settings import TestSettings

import asposestoragecloud
import six

from groupdocs_viewer_cloud import Configuration, ViewerApi

class TestContext(unittest.TestCase):

    viewer_api = None
    _storage_api = None
    _test_files_uploaded = False

    def setUp(self):
        if six.PY3:
            warnings.simplefilter("ignore", ResourceWarning)

        self._init_viewer_api()
        self._upload_test_files()

    def tearDown(self):
        self._remove_folder_in_storage("cache")
        self._remove_folder_in_storage("tests")
        self._close_viewer_api_thread_pool()
        self._close_storage_api_thread_pool()

    def get_test_file_path(self, file):
        test_files = "test\\test_files"
        test_file_path = os.path.join(test_files, file.folder, file.file_name) 

        return test_file_path

    def to_json_file(self, obj):
        obj_dict = { obj.attribute_map[attr]: getattr(obj, attr)
                     for attr, _ in six.iteritems(obj.swagger_types)
                     if hasattr(obj, attr) and getattr(obj, attr) is not None }

        json_str = json.dumps(obj_dict)

        temp_file = tempfile.NamedTemporaryFile("w", delete = False)

        json_file = temp_file.file
        json_file.write(json_str)
        json_file.close()

        return temp_file.name

    def _close_viewer_api_thread_pool(self):
        self.viewer_api.close()

    def _close_storage_api_thread_pool(self):
        thread_pool = self._storage_api.api_client.pool
        if thread_pool is not None:
            thread_pool.close()
            thread_pool.join()

    def _remove_folder_in_storage(self, folder):
        self._init_storage_api()
        self._storage_api.delete_folder(folder, recursive = True)

    def _upload_test_files(self):
        if TestContext._test_files_uploaded:
            return

        self._init_storage_api()
        test_files = "test\\test_files"

        for path, _, files in os.walk(test_files):
            for file_name in files:
                local_file_path = os.path.join(path, file_name)                
                remote_file_path = local_file_path.replace(test_files + "\\", "")
                file_contents = open(local_file_path, "rb") 
                self._storage_api.put_create(remote_file_path, file_contents)

        TestContext._test_files_uploaded = True

    def _init_viewer_api(self):
        if self.viewer_api is None:
            configuration = Configuration(TestSettings.APP_SID, TestSettings.APP_KEY)
            configuration.api_base_url = TestSettings.API_BASE_URL
            self.viewer_api = ViewerApi.from_config(configuration)

    def _init_storage_api(self):
        if self._storage_api is not None:
            return self._storage_api

        configuration = asposestoragecloud.Configuration()
        configuration.host = TestSettings.API_BASE_URL
        configuration.base_url = TestSettings.API_BASE_URL + "/v1"

        api_client = asposestoragecloud.ApiClient(
            TestSettings.APP_KEY, TestSettings.APP_SID, TestSettings.API_BASE_URL, configuration)
        
        self._storage_api = asposestoragecloud.StorageApi(api_client)
