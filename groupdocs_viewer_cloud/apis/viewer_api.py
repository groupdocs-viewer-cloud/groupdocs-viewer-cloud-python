# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="viewer_api.py">
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

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from groupdocs_viewer_cloud.auth import Auth
from groupdocs_viewer_cloud.api_client import ApiClient
from groupdocs_viewer_cloud.api_exception import ApiException
from groupdocs_viewer_cloud.configuration import Configuration

class ViewerApi(object):
    """
    GroupDocs.Viewer Cloud API

    :param configuration: API configuration
    """

    def __init__(self, configuration):
        api_client = ApiClient(configuration)

        self.auth = Auth(configuration, api_client)
        self.api_client = api_client
        self.configuration = configuration

    def close(self):  # noqa: E501
        """
        Closes thread pool. This method should be called when 
        methods are executed asynchronously (is_async=True is passed as parameter)
        and this instance of ViewerApi is not going to be used any more.
        """
        if self.api_client is not None:
            if(self.api_client.pool is not None):
                self.api_client.pool.close()
                self.api_client.pool.join()
                self.api_client.pool = None

    @classmethod
    def from_keys(cls, app_sid, app_key):
        """
        Initializes new instance of ViewerApi with API keys

        :param app_sid Application identifier (App SID)
        :param app_key Application private key (App Key)
        """
        configuration = Configuration(app_sid, app_key)
        return ViewerApi(configuration)

    @classmethod
    def from_config(cls, configuration):
        """
        Initializes new instance of ViewerApi with configuration options

        :param configuration API configuration
        """
        return ViewerApi(configuration)

    def delete_fonts_cache(self, **kwargs):  # noqa: E501
        """Removes fonts cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._delete_fonts_cache_with_http_info(**kwargs)  # noqa: E501
        
        self._delete_fonts_cache_with_http_info(**kwargs)  # noqa: E501
        

    def _delete_fonts_cache_with_http_info(self, **kwargs):  # noqa: E501
        """Removes fonts cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fonts_cache" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/viewer/fonts/cache'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'DELETE',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':None,  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def get_fonts(self, **kwargs):  # noqa: E501
        """List installed fonts.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :return: FontCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._get_fonts_with_http_info(**kwargs)  # noqa: E501
        
        (data) = self._get_fonts_with_http_info(**kwargs)  # noqa: E501
        return data

    def _get_fonts_with_http_info(self, **kwargs):  # noqa: E501
        """List installed fonts.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        
        :return: FontCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fonts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/viewer/fonts'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'FontCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def get_supported_file_formats(self, **kwargs):  # noqa: E501
        """Retrieves list of supported file formats.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :return: FormatCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._get_supported_file_formats_with_http_info(**kwargs)  # noqa: E501
        
        (data) = self._get_supported_file_formats_with_http_info(**kwargs)  # noqa: E501
        return data

    def _get_supported_file_formats_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves list of supported file formats.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        
        :return: FormatCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_supported_file_formats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/viewer/formats'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'FormatCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_create_attachment_pages_cache(self, request,**kwargs):  # noqa: E501
        """Creates attachment cache.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param HtmlOptions html_options: The HTML rendering options.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: HtmlAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_create_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_create_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_create_attachment_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates attachment cache.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlCreateAttachmentPagesCacheRequest request object with parameters
        :return: HtmlAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_create_attachment_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_create_attachment_pages_cache`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_create_attachment_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.html_options is not None:
            body_params = request.html_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'HtmlAttachmentPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_create_pages_cache(self, request,**kwargs):  # noqa: E501
        """Creates document pages as HTML and saves them in cache. Pages created before will be removed from cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param HtmlOptions html_options: The HTML rendering options.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_create_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_create_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_create_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates document pages as HTML and saves them in cache. Pages created before will be removed from cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlCreatePagesCacheRequest request object with parameters
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_create_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_create_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.html_options is not None:
            body_params = request.html_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'HtmlPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_create_pages_cache_from_content(self, request,**kwargs):  # noqa: E501
        """Creates posted document pages as HTML and saves them in cache. Content with document or multipart content is expected where first part is document and second is HtmlOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param file file: File contents. (required)
        :param file html_options: HTML rendering options 'HtmlOptions' as JSON or XML. (required)
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_create_pages_cache_from_content_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_create_pages_cache_from_content_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_create_pages_cache_from_content_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates posted document pages as HTML and saves them in cache. Content with document or multipart content is expected where first part is document and second is HtmlOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlCreatePagesCacheFromContentRequest request object with parameters
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_create_pages_cache_from_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `html_create_pages_cache_from_content`")  # noqa: E501
        # verify the required parameter 'html_options' is set
        if request.html_options is None:
            raise ValueError("Missing the required parameter `html_options` when calling `html_create_pages_cache_from_content`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/pages'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501
        if request.html_options is not None:
            local_var_files.append((self.__downcase_first_letter('HtmlOptions'), request.html_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'HtmlPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_create_pages_cache_from_url(self, request,**kwargs):  # noqa: E501
        """Creates pages as HTML and saves them in cache for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param HtmlOptions html_options: The HTML rendering options.
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_create_pages_cache_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_create_pages_cache_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_create_pages_cache_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates pages as HTML and saves them in cache for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlCreatePagesCacheFromUrlRequest request object with parameters
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_create_pages_cache_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `html_create_pages_cache_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/pages'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.html_options is not None:
            body_params = request.html_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'HtmlPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_create_pdf_file(self, request,**kwargs):  # noqa: E501
        """Creates PDF document.  Removes PDF document if it was created before.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The document name. (required)
        :param PdfFileOptions pdf_file_options: The PDF file rendering options.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_create_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_create_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_create_pdf_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates PDF document.  Removes PDF document if it was created before.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlCreatePdfFileRequest request object with parameters
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_create_pdf_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_create_pdf_file`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pdf'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.pdf_file_options is not None:
            body_params = request.pdf_file_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PdfFileInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_create_pdf_file_from_content(self, request,**kwargs):  # noqa: E501
        """Creates PDF document from document passed in request body and saves it in cache. Content with document or multipart content is expected where first part is document and second is PdfFileOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param file file: File contents. (required)
        :param file pdf_file_options: PDF rendering options 'PdfFileOptions' as JSON or XML. (required)
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_create_pdf_file_from_content_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_create_pdf_file_from_content_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_create_pdf_file_from_content_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates PDF document from document passed in request body and saves it in cache. Content with document or multipart content is expected where first part is document and second is PdfFileOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlCreatePdfFileFromContentRequest request object with parameters
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_create_pdf_file_from_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `html_create_pdf_file_from_content`")  # noqa: E501
        # verify the required parameter 'pdf_file_options' is set
        if request.pdf_file_options is None:
            raise ValueError("Missing the required parameter `pdf_file_options` when calling `html_create_pdf_file_from_content`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/pdf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501
        if request.pdf_file_options is not None:
            local_var_files.append((self.__downcase_first_letter('PdfFileOptions'), request.pdf_file_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PdfFileInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_create_pdf_file_from_url(self, request,**kwargs):  # noqa: E501
        """Creates PDF document for document at provided URL and saves it in cache.  Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file. Expects PdfFileOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param PdfFileOptions pdf_file_options: The PDF file rendering.
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_create_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_create_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_create_pdf_file_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates PDF document for document at provided URL and saves it in cache.  Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file. Expects PdfFileOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlCreatePdfFileFromUrlRequest request object with parameters
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_create_pdf_file_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `html_create_pdf_file_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/pdf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.pdf_file_options is not None:
            body_params = request.pdf_file_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PdfFileInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_delete_attachment_pages_cache(self, request,**kwargs):  # noqa: E501
        """Removes attachment cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: Name of the attachment. (required)
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_delete_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        self._html_delete_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        

    def _html_delete_attachment_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes attachment cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlDeleteAttachmentPagesCacheRequest request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_delete_attachment_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_delete_attachment_pages_cache`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_delete_attachment_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/pages/cache'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'DELETE',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':None,  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_delete_pages_cache(self, request,**kwargs):  # noqa: E501
        """Removes document cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_delete_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        self._html_delete_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        

    def _html_delete_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes document cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlDeletePagesCacheRequest request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_delete_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_delete_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pages/cache'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'DELETE',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':None,  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_attachment(self, request,**kwargs):  # noqa: E501
        """Downloads attachment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: Name of the attachment. (required)
        :param str password: The document password.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_attachment_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_attachment_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_attachment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads attachment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetAttachmentRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_attachment`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_get_attachment`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_attachment_info(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_attachment_info_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_attachment_info_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_attachment_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetAttachmentInfoRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_attachment_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_attachment_info`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_get_attachment_info`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_attachment_info_with_options(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment information with specified DocumentInfoOptions. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param DocumentInfoOptions document_info_options: The rendering options.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_attachment_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_attachment_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_attachment_info_with_options_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment information with specified DocumentInfoOptions. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetAttachmentInfoWithOptionsRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_attachment_info_with_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_attachment_info_with_options`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_get_attachment_info_with_options`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.document_info_options is not None:
            body_params = request.document_info_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_attachment_page(self, request,**kwargs):  # noqa: E501
        """Downloads attachment page as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The document name. (required)
        :param str attachment_name: Name of the attachment. (required)
        :param int page_number: The attachment page number. (required)
        :param str resource_path: The attachment page HTML resource path.
        :param bool ignore_resource_path_in_resources: When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
        :param bool embed_resources: Whether to embed HTML resources or save them separate.
        :param bool enable_minification: Enables content (HTML, CSS and SVG) minification.
        :param bool enable_responsive_rendering: Indicates whether rendering will provide responsive web pages, that look well on different device types.
        :param bool exclude_fonts: Prevents adding fonts to the output HTML document.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_attachment_page_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_attachment_page_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_attachment_page_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads attachment page as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetAttachmentPageRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_attachment_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_attachment_page`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_get_attachment_page`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if request.page_number is None:
            raise ValueError("Missing the required parameter `page_number` when calling `html_get_attachment_page`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/pages/{pageNumber}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501
        if request.page_number is not None:
            path_params[self.__downcase_first_letter('PageNumber')] = request.page_number  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('ResourcePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResourcePath' + '}'), request.resource_path if request.resource_path is not None else '')
        else:
            if request.resource_path is not None:
                query_params.append((self.__downcase_first_letter('ResourcePath'), request.resource_path))  # noqa: E501
        if self.__downcase_first_letter('IgnoreResourcePathInResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('IgnoreResourcePathInResources' + '}'), request.ignore_resource_path_in_resources if request.ignore_resource_path_in_resources is not None else '')
        else:
            if request.ignore_resource_path_in_resources is not None:
                query_params.append((self.__downcase_first_letter('IgnoreResourcePathInResources'), request.ignore_resource_path_in_resources))  # noqa: E501
        if self.__downcase_first_letter('EmbedResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('EmbedResources' + '}'), request.embed_resources if request.embed_resources is not None else '')
        else:
            if request.embed_resources is not None:
                query_params.append((self.__downcase_first_letter('EmbedResources'), request.embed_resources))  # noqa: E501
        if self.__downcase_first_letter('EnableMinification') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableMinification' + '}'), request.enable_minification if request.enable_minification is not None else '')
        else:
            if request.enable_minification is not None:
                query_params.append((self.__downcase_first_letter('EnableMinification'), request.enable_minification))  # noqa: E501
        if self.__downcase_first_letter('EnableResponsiveRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableResponsiveRendering' + '}'), request.enable_responsive_rendering if request.enable_responsive_rendering is not None else '')
        else:
            if request.enable_responsive_rendering is not None:
                query_params.append((self.__downcase_first_letter('EnableResponsiveRendering'), request.enable_responsive_rendering))  # noqa: E501
        if self.__downcase_first_letter('ExcludeFonts') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExcludeFonts' + '}'), request.exclude_fonts if request.exclude_fonts is not None else '')
        else:
            if request.exclude_fonts is not None:
                query_params.append((self.__downcase_first_letter('ExcludeFonts'), request.exclude_fonts))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_attachment_page_resource(self, request,**kwargs):  # noqa: E501
        """Downloads HTML page resource (image, style, graphics or font).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param int page_number: The page number. (required)
        :param str resource_name: Name of the resource. (required)
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_attachment_page_resource_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_attachment_page_resource_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_attachment_page_resource_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads HTML page resource (image, style, graphics or font).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetAttachmentPageResourceRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_attachment_page_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_attachment_page_resource`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_get_attachment_page_resource`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if request.page_number is None:
            raise ValueError("Missing the required parameter `page_number` when calling `html_get_attachment_page_resource`")  # noqa: E501
        # verify the required parameter 'resource_name' is set
        if request.resource_name is None:
            raise ValueError("Missing the required parameter `resource_name` when calling `html_get_attachment_page_resource`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/pages/{pageNumber}/resources/{resourceName}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501
        if request.page_number is not None:
            path_params[self.__downcase_first_letter('PageNumber')] = request.page_number  # noqa: E501
        if request.resource_name is not None:
            path_params[self.__downcase_first_letter('ResourceName')] = request.resource_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_attachment_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param str resource_path: The attachment page HTML resource path.
        :param bool ignore_resource_path_in_resources: When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
        :param bool embed_resources: Whether to embed HTML resources or save them separate.
        :param bool enable_minification: Enables content (HTML, CSS and SVG) minification.
        :param bool enable_responsive_rendering: Indicates whether rendering will provide responsive web pages, that look well on different device types.
        :param bool exclude_fonts: Prevents adding fonts to the output HTML document.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: HtmlAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_attachment_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetAttachmentPagesRequest request object with parameters
        :return: HtmlAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_attachment_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_attachment_pages`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_get_attachment_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('ResourcePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResourcePath' + '}'), request.resource_path if request.resource_path is not None else '')
        else:
            if request.resource_path is not None:
                query_params.append((self.__downcase_first_letter('ResourcePath'), request.resource_path))  # noqa: E501
        if self.__downcase_first_letter('IgnoreResourcePathInResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('IgnoreResourcePathInResources' + '}'), request.ignore_resource_path_in_resources if request.ignore_resource_path_in_resources is not None else '')
        else:
            if request.ignore_resource_path_in_resources is not None:
                query_params.append((self.__downcase_first_letter('IgnoreResourcePathInResources'), request.ignore_resource_path_in_resources))  # noqa: E501
        if self.__downcase_first_letter('EmbedResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('EmbedResources' + '}'), request.embed_resources if request.embed_resources is not None else '')
        else:
            if request.embed_resources is not None:
                query_params.append((self.__downcase_first_letter('EmbedResources'), request.embed_resources))  # noqa: E501
        if self.__downcase_first_letter('EnableMinification') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableMinification' + '}'), request.enable_minification if request.enable_minification is not None else '')
        else:
            if request.enable_minification is not None:
                query_params.append((self.__downcase_first_letter('EnableMinification'), request.enable_minification))  # noqa: E501
        if self.__downcase_first_letter('EnableResponsiveRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableResponsiveRendering' + '}'), request.enable_responsive_rendering if request.enable_responsive_rendering is not None else '')
        else:
            if request.enable_responsive_rendering is not None:
                query_params.append((self.__downcase_first_letter('EnableResponsiveRendering'), request.enable_responsive_rendering))  # noqa: E501
        if self.__downcase_first_letter('ExcludeFonts') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExcludeFonts' + '}'), request.exclude_fonts if request.exclude_fonts is not None else '')
        else:
            if request.exclude_fonts is not None:
                query_params.append((self.__downcase_first_letter('ExcludeFonts'), request.exclude_fonts))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'HtmlAttachmentPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_attachments(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document attachments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str password: The document password.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: AttachmentCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_attachments_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_attachments_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_attachments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document attachments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetAttachmentsRequest request object with parameters
        :return: AttachmentCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_attachments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_attachments`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'AttachmentCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_document_info(self, request,**kwargs):  # noqa: E501
        """Retrieves document information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str password: The document password.
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_document_info_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_document_info_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_document_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetDocumentInfoRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_document_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_document_info`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_document_info_from_content(self, request,**kwargs):  # noqa: E501
        """Retrieves document information for posted document. Content with document or multipart content is expected where first part is document and second is DocumentInfoOptions. Saves file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param file file: File contents. (required)
        :param file document_info_options: Document info options 'DocumentInfoOptions' as JSON or XML. (required)
        :param str file_name: The file name.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_document_info_from_content_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_document_info_from_content_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_document_info_from_content_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information for posted document. Content with document or multipart content is expected where first part is document and second is DocumentInfoOptions. Saves file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetDocumentInfoFromContentRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_document_info_from_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `html_get_document_info_from_content`")  # noqa: E501
        # verify the required parameter 'document_info_options' is set
        if request.document_info_options is None:
            raise ValueError("Missing the required parameter `document_info_options` when calling `html_get_document_info_from_content`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/info'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501
        if request.document_info_options is not None:
            local_var_files.append((self.__downcase_first_letter('DocumentInfoOptions'), request.document_info_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_document_info_from_url(self, request,**kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param str file_name: The file name.
        :param str password: The document password.
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_document_info_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_document_info_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_document_info_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetDocumentInfoFromUrlRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_document_info_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `html_get_document_info_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/info'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_document_info_from_url_with_options(self, request,**kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param DocumentInfoOptions document_info_options: The rendering options.
        :param str file_name: The document name.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_document_info_from_url_with_options_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_document_info_from_url_with_options_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_document_info_from_url_with_options_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetDocumentInfoFromUrlWithOptionsRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_document_info_from_url_with_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `html_get_document_info_from_url_with_options`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/info'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.document_info_options is not None:
            body_params = request.document_info_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_document_info_with_options(self, request,**kwargs):  # noqa: E501
        """Retrieves document information with specified DocumentInfoOptions. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param DocumentInfoOptions document_info_options: The rendering options.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_document_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_document_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_document_info_with_options_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information with specified DocumentInfoOptions. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetDocumentInfoWithOptionsRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_document_info_with_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_document_info_with_options`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.document_info_options is not None:
            body_params = request.document_info_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_page(self, request,**kwargs):  # noqa: E501
        """Downloads document page as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param int page_number: The page number. (required)
        :param str resource_path: The HTML resource path.
        :param bool ignore_resource_path_in_resources: When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
        :param bool embed_resources: Whether to embed HTML resources or save them separate.
        :param bool enable_minification: Enables content (HTML, CSS and SVG) minification.
        :param bool enable_responsive_rendering: Indicates whether rendering will provide responsive web pages, that look well on different device types.
        :param bool exclude_fonts: Prevents adding fonts to the output HTML document.
        :param str password: The document password.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_page_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_page_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_page_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads document page as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetPageRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_page`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if request.page_number is None:
            raise ValueError("Missing the required parameter `page_number` when calling `html_get_page`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pages/{pageNumber}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.page_number is not None:
            path_params[self.__downcase_first_letter('PageNumber')] = request.page_number  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('ResourcePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResourcePath' + '}'), request.resource_path if request.resource_path is not None else '')
        else:
            if request.resource_path is not None:
                query_params.append((self.__downcase_first_letter('ResourcePath'), request.resource_path))  # noqa: E501
        if self.__downcase_first_letter('IgnoreResourcePathInResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('IgnoreResourcePathInResources' + '}'), request.ignore_resource_path_in_resources if request.ignore_resource_path_in_resources is not None else '')
        else:
            if request.ignore_resource_path_in_resources is not None:
                query_params.append((self.__downcase_first_letter('IgnoreResourcePathInResources'), request.ignore_resource_path_in_resources))  # noqa: E501
        if self.__downcase_first_letter('EmbedResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('EmbedResources' + '}'), request.embed_resources if request.embed_resources is not None else '')
        else:
            if request.embed_resources is not None:
                query_params.append((self.__downcase_first_letter('EmbedResources'), request.embed_resources))  # noqa: E501
        if self.__downcase_first_letter('EnableMinification') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableMinification' + '}'), request.enable_minification if request.enable_minification is not None else '')
        else:
            if request.enable_minification is not None:
                query_params.append((self.__downcase_first_letter('EnableMinification'), request.enable_minification))  # noqa: E501
        if self.__downcase_first_letter('EnableResponsiveRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableResponsiveRendering' + '}'), request.enable_responsive_rendering if request.enable_responsive_rendering is not None else '')
        else:
            if request.enable_responsive_rendering is not None:
                query_params.append((self.__downcase_first_letter('EnableResponsiveRendering'), request.enable_responsive_rendering))  # noqa: E501
        if self.__downcase_first_letter('ExcludeFonts') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExcludeFonts' + '}'), request.exclude_fonts if request.exclude_fonts is not None else '')
        else:
            if request.exclude_fonts is not None:
                query_params.append((self.__downcase_first_letter('ExcludeFonts'), request.exclude_fonts))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_page_resource(self, request,**kwargs):  # noqa: E501
        """Downloads HTML page resource (image, style, graphics or font).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param int page_number: The page number. (required)
        :param str resource_name: Name of the resource. (required)
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_page_resource_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_page_resource_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_page_resource_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads HTML page resource (image, style, graphics or font).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetPageResourceRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_page_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_page_resource`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if request.page_number is None:
            raise ValueError("Missing the required parameter `page_number` when calling `html_get_page_resource`")  # noqa: E501
        # verify the required parameter 'resource_name' is set
        if request.resource_name is None:
            raise ValueError("Missing the required parameter `resource_name` when calling `html_get_page_resource`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pages/{pageNumber}/resources/{resourceName}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.page_number is not None:
            path_params[self.__downcase_first_letter('PageNumber')] = request.page_number  # noqa: E501
        if request.resource_name is not None:
            path_params[self.__downcase_first_letter('ResourceName')] = request.resource_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str resource_path: The HTML resource path.
        :param bool ignore_resource_path_in_resources: When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
        :param bool embed_resources: Whether to embed HTML resources or save them separate.
        :param bool enable_minification: Enables content (HTML, CSS and SVG) minification.
        :param bool enable_responsive_rendering: Indicates whether rendering will provide responsive web pages, that look well on different device types.
        :param bool exclude_fonts: Prevents adding fonts to the output HTML document.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param str password: The document password.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetPagesRequest request object with parameters
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('ResourcePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResourcePath' + '}'), request.resource_path if request.resource_path is not None else '')
        else:
            if request.resource_path is not None:
                query_params.append((self.__downcase_first_letter('ResourcePath'), request.resource_path))  # noqa: E501
        if self.__downcase_first_letter('IgnoreResourcePathInResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('IgnoreResourcePathInResources' + '}'), request.ignore_resource_path_in_resources if request.ignore_resource_path_in_resources is not None else '')
        else:
            if request.ignore_resource_path_in_resources is not None:
                query_params.append((self.__downcase_first_letter('IgnoreResourcePathInResources'), request.ignore_resource_path_in_resources))  # noqa: E501
        if self.__downcase_first_letter('EmbedResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('EmbedResources' + '}'), request.embed_resources if request.embed_resources is not None else '')
        else:
            if request.embed_resources is not None:
                query_params.append((self.__downcase_first_letter('EmbedResources'), request.embed_resources))  # noqa: E501
        if self.__downcase_first_letter('EnableMinification') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableMinification' + '}'), request.enable_minification if request.enable_minification is not None else '')
        else:
            if request.enable_minification is not None:
                query_params.append((self.__downcase_first_letter('EnableMinification'), request.enable_minification))  # noqa: E501
        if self.__downcase_first_letter('EnableResponsiveRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableResponsiveRendering' + '}'), request.enable_responsive_rendering if request.enable_responsive_rendering is not None else '')
        else:
            if request.enable_responsive_rendering is not None:
                query_params.append((self.__downcase_first_letter('EnableResponsiveRendering'), request.enable_responsive_rendering))  # noqa: E501
        if self.__downcase_first_letter('ExcludeFonts') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExcludeFonts' + '}'), request.exclude_fonts if request.exclude_fonts is not None else '')
        else:
            if request.exclude_fonts is not None:
                query_params.append((self.__downcase_first_letter('ExcludeFonts'), request.exclude_fonts))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'HtmlPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_pages_from_url(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param str file_name: The file name.
        :param str resource_path: The HTML resource path.
        :param bool ignore_resource_path_in_resources: When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
        :param bool embed_resources: Whether to embed HTML resources or save them separate.
        :param bool enable_minification: Enables content (HTML, CSS and SVG) minification.
        :param bool enable_responsive_rendering: Indicates whether rendering will provide responsive web pages, that look well on different device types.
        :param bool exclude_fonts: Prevents adding fonts to the output HTML document.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param str password: The document password.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_pages_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_pages_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_pages_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetPagesFromUrlRequest request object with parameters
        :return: HtmlPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_pages_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `html_get_pages_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/pages'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('ResourcePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResourcePath' + '}'), request.resource_path if request.resource_path is not None else '')
        else:
            if request.resource_path is not None:
                query_params.append((self.__downcase_first_letter('ResourcePath'), request.resource_path))  # noqa: E501
        if self.__downcase_first_letter('IgnoreResourcePathInResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('IgnoreResourcePathInResources' + '}'), request.ignore_resource_path_in_resources if request.ignore_resource_path_in_resources is not None else '')
        else:
            if request.ignore_resource_path_in_resources is not None:
                query_params.append((self.__downcase_first_letter('IgnoreResourcePathInResources'), request.ignore_resource_path_in_resources))  # noqa: E501
        if self.__downcase_first_letter('EmbedResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('EmbedResources' + '}'), request.embed_resources if request.embed_resources is not None else '')
        else:
            if request.embed_resources is not None:
                query_params.append((self.__downcase_first_letter('EmbedResources'), request.embed_resources))  # noqa: E501
        if self.__downcase_first_letter('EnableMinification') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableMinification' + '}'), request.enable_minification if request.enable_minification is not None else '')
        else:
            if request.enable_minification is not None:
                query_params.append((self.__downcase_first_letter('EnableMinification'), request.enable_minification))  # noqa: E501
        if self.__downcase_first_letter('EnableResponsiveRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableResponsiveRendering' + '}'), request.enable_responsive_rendering if request.enable_responsive_rendering is not None else '')
        else:
            if request.enable_responsive_rendering is not None:
                query_params.append((self.__downcase_first_letter('EnableResponsiveRendering'), request.enable_responsive_rendering))  # noqa: E501
        if self.__downcase_first_letter('ExcludeFonts') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExcludeFonts' + '}'), request.exclude_fonts if request.exclude_fonts is not None else '')
        else:
            if request.exclude_fonts is not None:
                query_params.append((self.__downcase_first_letter('ExcludeFonts'), request.exclude_fonts))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'HtmlPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_pdf_file(self, request,**kwargs):  # noqa: E501
        """Downloads document as PDF.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str password: The document password. Not required if PDF document was created before.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_pdf_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads document as PDF.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetPdfFileRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_pdf_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_pdf_file`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pdf'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_pdf_file_from_url(self, request,**kwargs):  # noqa: E501
        """Downloads document at provided URL as PDF.  Document will be retrieved from the passed URL and added to Storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param str file_name: The file name.
        :param str password: The document password. Not required if PDF document was created before.
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_pdf_file_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads document at provided URL as PDF.  Document will be retrieved from the passed URL and added to Storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetPdfFileFromUrlRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_pdf_file_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `html_get_pdf_file_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/html/pdf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_zip_with_attachment_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param str resource_path: The attachment page HTML resource path.
        :param bool ignore_resource_path_in_resources: When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
        :param bool embed_resources: Whether to embed HTML resources or save them separate.
        :param bool enable_minification: Enables content (HTML, CSS and SVG) minification.
        :param bool enable_responsive_rendering: Indicates whether rendering will provide responsive web pages, that look well on different device types.
        :param bool exclude_fonts: Prevents adding fonts to the output HTML document.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_zip_with_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_zip_with_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_zip_with_attachment_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetZipWithAttachmentPagesRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_zip_with_attachment_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_zip_with_attachment_pages`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `html_get_zip_with_attachment_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/attachments/{attachmentName}/pages/zip'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('ResourcePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResourcePath' + '}'), request.resource_path if request.resource_path is not None else '')
        else:
            if request.resource_path is not None:
                query_params.append((self.__downcase_first_letter('ResourcePath'), request.resource_path))  # noqa: E501
        if self.__downcase_first_letter('IgnoreResourcePathInResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('IgnoreResourcePathInResources' + '}'), request.ignore_resource_path_in_resources if request.ignore_resource_path_in_resources is not None else '')
        else:
            if request.ignore_resource_path_in_resources is not None:
                query_params.append((self.__downcase_first_letter('IgnoreResourcePathInResources'), request.ignore_resource_path_in_resources))  # noqa: E501
        if self.__downcase_first_letter('EmbedResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('EmbedResources' + '}'), request.embed_resources if request.embed_resources is not None else '')
        else:
            if request.embed_resources is not None:
                query_params.append((self.__downcase_first_letter('EmbedResources'), request.embed_resources))  # noqa: E501
        if self.__downcase_first_letter('EnableMinification') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableMinification' + '}'), request.enable_minification if request.enable_minification is not None else '')
        else:
            if request.enable_minification is not None:
                query_params.append((self.__downcase_first_letter('EnableMinification'), request.enable_minification))  # noqa: E501
        if self.__downcase_first_letter('EnableResponsiveRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableResponsiveRendering' + '}'), request.enable_responsive_rendering if request.enable_responsive_rendering is not None else '')
        else:
            if request.enable_responsive_rendering is not None:
                query_params.append((self.__downcase_first_letter('EnableResponsiveRendering'), request.enable_responsive_rendering))  # noqa: E501
        if self.__downcase_first_letter('ExcludeFonts') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExcludeFonts' + '}'), request.exclude_fonts if request.exclude_fonts is not None else '')
        else:
            if request.exclude_fonts is not None:
                query_params.append((self.__downcase_first_letter('ExcludeFonts'), request.exclude_fonts))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/zip'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_get_zip_with_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str resource_path: The HTML resource path.
        :param bool ignore_resource_path_in_resources: When this option enabled ResourcePath won't be added to resource reference in *.css and *.svg files.
        :param bool embed_resources: Whether to embed HTML resources or save them separate.
        :param bool enable_minification: Enables content (HTML, CSS and SVG) minification.
        :param bool enable_responsive_rendering: Indicates whether rendering will provide responsive web pages, that look well on different device types.
        :param bool exclude_fonts: Prevents adding fonts to the output HTML document.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param str password: The document password.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_get_zip_with_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_get_zip_with_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_get_zip_with_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document pages as HTML.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlGetZipWithPagesRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_get_zip_with_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_get_zip_with_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pages/zip'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('ResourcePath') in path:
            path = path.replace('{' + self.__downcase_first_letter('ResourcePath' + '}'), request.resource_path if request.resource_path is not None else '')
        else:
            if request.resource_path is not None:
                query_params.append((self.__downcase_first_letter('ResourcePath'), request.resource_path))  # noqa: E501
        if self.__downcase_first_letter('IgnoreResourcePathInResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('IgnoreResourcePathInResources' + '}'), request.ignore_resource_path_in_resources if request.ignore_resource_path_in_resources is not None else '')
        else:
            if request.ignore_resource_path_in_resources is not None:
                query_params.append((self.__downcase_first_letter('IgnoreResourcePathInResources'), request.ignore_resource_path_in_resources))  # noqa: E501
        if self.__downcase_first_letter('EmbedResources') in path:
            path = path.replace('{' + self.__downcase_first_letter('EmbedResources' + '}'), request.embed_resources if request.embed_resources is not None else '')
        else:
            if request.embed_resources is not None:
                query_params.append((self.__downcase_first_letter('EmbedResources'), request.embed_resources))  # noqa: E501
        if self.__downcase_first_letter('EnableMinification') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableMinification' + '}'), request.enable_minification if request.enable_minification is not None else '')
        else:
            if request.enable_minification is not None:
                query_params.append((self.__downcase_first_letter('EnableMinification'), request.enable_minification))  # noqa: E501
        if self.__downcase_first_letter('EnableResponsiveRendering') in path:
            path = path.replace('{' + self.__downcase_first_letter('EnableResponsiveRendering' + '}'), request.enable_responsive_rendering if request.enable_responsive_rendering is not None else '')
        else:
            if request.enable_responsive_rendering is not None:
                query_params.append((self.__downcase_first_letter('EnableResponsiveRendering'), request.enable_responsive_rendering))  # noqa: E501
        if self.__downcase_first_letter('ExcludeFonts') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExcludeFonts' + '}'), request.exclude_fonts if request.exclude_fonts is not None else '')
        else:
            if request.exclude_fonts is not None:
                query_params.append((self.__downcase_first_letter('ExcludeFonts'), request.exclude_fonts))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/zip'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def html_transform_pages(self, request,**kwargs):  # noqa: E501
        """Rotates or reorders document page(s).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param TransformOptionsBase transform_options: The transformation options.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PageInfoCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._html_transform_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._html_transform_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _html_transform_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Rotates or reorders document page(s).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param HtmlTransformPagesRequest request object with parameters
        :return: PageInfoCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method html_transform_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `html_transform_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/html/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.transform_options is not None:
            body_params = request.transform_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PageInfoCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_create_attachment_pages_cache(self, request,**kwargs):  # noqa: E501
        """Creates attachment cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param ImageOptions image_options: The image rendering options.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: ImageAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_create_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_create_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_create_attachment_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates attachment cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageCreateAttachmentPagesCacheRequest request object with parameters
        :return: ImageAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_create_attachment_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_create_attachment_pages_cache`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_create_attachment_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.image_options is not None:
            body_params = request.image_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'ImageAttachmentPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_create_pages_cache(self, request,**kwargs):  # noqa: E501
        """Creates document pages as image and saves them in cache.  Pages created before will be removed from cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param ImageOptions image_options: The image render options.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_create_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_create_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_create_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates document pages as image and saves them in cache.  Pages created before will be removed from cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageCreatePagesCacheRequest request object with parameters
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_create_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_create_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.image_options is not None:
            body_params = request.image_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'ImagePageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_create_pages_cache_from_content(self, request,**kwargs):  # noqa: E501
        """Creates posted document pages as image and saves them in cache. Content with document or multipart content is expected where first part is document and second is HtmlOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param file file: File contents. (required)
        :param file image_options: Image rendering options 'ImageOptions' as JSON or XML. (required)
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_create_pages_cache_from_content_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_create_pages_cache_from_content_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_create_pages_cache_from_content_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates posted document pages as image and saves them in cache. Content with document or multipart content is expected where first part is document and second is HtmlOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageCreatePagesCacheFromContentRequest request object with parameters
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_create_pages_cache_from_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `image_create_pages_cache_from_content`")  # noqa: E501
        # verify the required parameter 'image_options' is set
        if request.image_options is None:
            raise ValueError("Missing the required parameter `image_options` when calling `image_create_pages_cache_from_content`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/pages'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501
        if request.image_options is not None:
            local_var_files.append((self.__downcase_first_letter('ImageOptions'), request.image_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'ImagePageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_create_pages_cache_from_url(self, request,**kwargs):  # noqa: E501
        """Creates pages as image and saves them in cache for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param ImageOptions image_options: The image rendering options.
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_create_pages_cache_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_create_pages_cache_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_create_pages_cache_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates pages as image and saves them in cache for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageCreatePagesCacheFromUrlRequest request object with parameters
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_create_pages_cache_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `image_create_pages_cache_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/pages'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.image_options is not None:
            body_params = request.image_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'ImagePageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_create_pdf_file(self, request,**kwargs):  # noqa: E501
        """Creates PDF document.  Removes PDF document if it was created before.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param PdfFileOptions pdf_file_options: The PDF file rendering options.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_create_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_create_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_create_pdf_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates PDF document.  Removes PDF document if it was created before.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageCreatePdfFileRequest request object with parameters
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_create_pdf_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_create_pdf_file`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pdf'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.pdf_file_options is not None:
            body_params = request.pdf_file_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PdfFileInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_create_pdf_file_from_content(self, request,**kwargs):  # noqa: E501
        """Creates PDF document from document passed in request body and saves it in cache. Content with document or multipart content is expected where first part is document and second is PdfFileOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param file file: File contents. (required)
        :param file pdf_file_options: PDF rendering options 'PdfFileOptions' as JSON or XML. (required)
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_create_pdf_file_from_content_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_create_pdf_file_from_content_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_create_pdf_file_from_content_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates PDF document from document passed in request body and saves it in cache. Content with document or multipart content is expected where first part is document and second is PdfFileOptions. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageCreatePdfFileFromContentRequest request object with parameters
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_create_pdf_file_from_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `image_create_pdf_file_from_content`")  # noqa: E501
        # verify the required parameter 'pdf_file_options' is set
        if request.pdf_file_options is None:
            raise ValueError("Missing the required parameter `pdf_file_options` when calling `image_create_pdf_file_from_content`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/pdf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501
        if request.pdf_file_options is not None:
            local_var_files.append((self.__downcase_first_letter('PdfFileOptions'), request.pdf_file_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PdfFileInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_create_pdf_file_from_url(self, request,**kwargs):  # noqa: E501
        """Creates PDF document for document at provided URL and saves it in cache.  Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file. Expects PdfFileOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param PdfFileOptions pdf_file_options: The PDF file rendering options.
        :param str file_name: The file name.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_create_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_create_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_create_pdf_file_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates PDF document for document at provided URL and saves it in cache.  Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file. Expects PdfFileOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageCreatePdfFileFromUrlRequest request object with parameters
        :return: PdfFileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_create_pdf_file_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `image_create_pdf_file_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/pdf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.pdf_file_options is not None:
            body_params = request.pdf_file_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PdfFileInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_delete_attachment_pages_cache(self, request,**kwargs):  # noqa: E501
        """Removes attachment cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: Name of the attachment. (required)
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_delete_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        self._image_delete_attachment_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        

    def _image_delete_attachment_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes attachment cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageDeleteAttachmentPagesCacheRequest request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_delete_attachment_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_delete_attachment_pages_cache`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_delete_attachment_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}/pages/cache'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'DELETE',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':None,  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_delete_pages_cache(self, request,**kwargs):  # noqa: E501
        """Removes document cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_delete_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        
        self._image_delete_pages_cache_with_http_info(request, **kwargs)  # noqa: E501
        

    def _image_delete_pages_cache_with_http_info(self, request, **kwargs):  # noqa: E501
        """Removes document cache.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageDeletePagesCacheRequest request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_delete_pages_cache" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_delete_pages_cache`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pages/cache'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'DELETE',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':None,  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_attachment(self, request,**kwargs):  # noqa: E501
        """Downloads attachment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: Name of the attachment. (required)
        :param str password: The document password.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_attachment_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_attachment_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_attachment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads attachment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetAttachmentRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_attachment`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_get_attachment`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_attachment_info(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_attachment_info_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_attachment_info_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_attachment_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetAttachmentInfoRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_attachment_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_attachment_info`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_get_attachment_info`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_attachment_info_with_options(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment information with specified DocumentInfoOptions. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param DocumentInfoOptions document_info_options: The rendering options.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_attachment_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_attachment_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_attachment_info_with_options_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment information with specified DocumentInfoOptions. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetAttachmentInfoWithOptionsRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_attachment_info_with_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_attachment_info_with_options`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_get_attachment_info_with_options`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.document_info_options is not None:
            body_params = request.document_info_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_attachment_page(self, request,**kwargs):  # noqa: E501
        """Downloads attachment page as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: Name of the attachment. (required)
        :param int page_number: The attachment page number. (required)
        :param str format: The image format (jpg, png or bmp). Default value is png.
        :param int width: The image width.
        :param int height: The image height.
        :param int quality: The image quality for jpg format. Default value is 90.
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_attachment_page_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_attachment_page_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_attachment_page_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads attachment page as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetAttachmentPageRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_attachment_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_attachment_page`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_get_attachment_page`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if request.page_number is None:
            raise ValueError("Missing the required parameter `page_number` when calling `image_get_attachment_page`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}/pages/{pageNumber}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501
        if request.page_number is not None:
            path_params[self.__downcase_first_letter('PageNumber')] = request.page_number  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Width') in path:
            path = path.replace('{' + self.__downcase_first_letter('Width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('Width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('Height') in path:
            path = path.replace('{' + self.__downcase_first_letter('Height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('Height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('Quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('Quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('Quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_attachment_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment pages as images.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param str format: The image format (jpg, png or bmp). Default value is png.
        :param int width: The image width.
        :param int height: The image height.
        :param int quality: The image quality for jpg format. Default value is 90.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: ImageAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_attachment_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment pages as images.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetAttachmentPagesRequest request object with parameters
        :return: ImageAttachmentPageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_attachment_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_attachment_pages`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_get_attachment_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Width') in path:
            path = path.replace('{' + self.__downcase_first_letter('Width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('Width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('Height') in path:
            path = path.replace('{' + self.__downcase_first_letter('Height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('Height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('Quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('Quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('Quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'ImageAttachmentPageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_attachments(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document attachments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str password: The document password.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: AttachmentCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_attachments_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_attachments_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_attachments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document attachments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetAttachmentsRequest request object with parameters
        :return: AttachmentCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_attachments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_attachments`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'AttachmentCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_document_info(self, request,**kwargs):  # noqa: E501
        """Retrieves document information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str password: The document password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_document_info_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_document_info_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_document_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetDocumentInfoRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_document_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_document_info`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_document_info_from_content(self, request,**kwargs):  # noqa: E501
        """Retrieves document information for posted document. Content with document or multipart content is expected where first part is document and second is DocumentInfoOptions. Saves file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param file file: File contents. (required)
        :param file document_info_options: Document info options 'DocumentInfoOptions' as JSON or XML. (required)
        :param str file_name: The document name.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_document_info_from_content_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_document_info_from_content_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_document_info_from_content_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information for posted document. Content with document or multipart content is expected where first part is document and second is DocumentInfoOptions. Saves file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetDocumentInfoFromContentRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_document_info_from_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `image_get_document_info_from_content`")  # noqa: E501
        # verify the required parameter 'document_info_options' is set
        if request.document_info_options is None:
            raise ValueError("Missing the required parameter `document_info_options` when calling `image_get_document_info_from_content`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/info'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501
        if request.document_info_options is not None:
            local_var_files.append((self.__downcase_first_letter('DocumentInfoOptions'), request.document_info_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_document_info_from_url(self, request,**kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param str file_name: The file name.
        :param str password: The document password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_document_info_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_document_info_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_document_info_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetDocumentInfoFromUrlRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_document_info_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `image_get_document_info_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/info'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_document_info_from_url_with_options(self, request,**kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param DocumentInfoOptions document_info_options: The rendering options.
        :param str file_name: The file name.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_document_info_from_url_with_options_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_document_info_from_url_with_options_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_document_info_from_url_with_options_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information for document at provided URL. Retrieves file from specified URL and tries to detect file type when fileName parameter is not specified. Saves retrieved file in storage. Use fileName and folder parameters to specify desired file name and folder to save file. When file with specified name already exists in storage new unique file name will be used for file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetDocumentInfoFromUrlWithOptionsRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_document_info_from_url_with_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `image_get_document_info_from_url_with_options`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/info'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.document_info_options is not None:
            body_params = request.document_info_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_document_info_with_options(self, request,**kwargs):  # noqa: E501
        """Retrieves document information with specified options. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param DocumentInfoOptions document_info_options: The rendering options.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_document_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_document_info_with_options_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_document_info_with_options_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves document information with specified options. Expects DocumentInfoOptions object data in request body.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetDocumentInfoWithOptionsRequest request object with parameters
        :return: DocumentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_document_info_with_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_document_info_with_options`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/info'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.document_info_options is not None:
            body_params = request.document_info_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'POST',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'DocumentInfo',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_page(self, request,**kwargs):  # noqa: E501
        """Downloads document page as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param int page_number: The page number. (required)
        :param str format: The image format (jpg, png or bmp). Default value is png.
        :param int width: The image width.
        :param int height: The image height.
        :param int quality: The image quality in JPG format. Valid values are between 1 and 100. Default value is 90.
        :param str password: The document password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_page_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_page_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_page_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads document page as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetPageRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_page`")  # noqa: E501
        # verify the required parameter 'page_number' is set
        if request.page_number is None:
            raise ValueError("Missing the required parameter `page_number` when calling `image_get_page`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pages/{pageNumber}'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.page_number is not None:
            path_params[self.__downcase_first_letter('PageNumber')] = request.page_number  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Width') in path:
            path = path.replace('{' + self.__downcase_first_letter('Width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('Width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('Height') in path:
            path = path.replace('{' + self.__downcase_first_letter('Height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('Height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('Quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('Quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('Quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document pages as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str format: The image format (jpg, png or bmp). Default value is png.
        :param int width: The image width.
        :param int height: The image height.
        :param int quality: The image quality for jpg format. Default value is 90.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param str password: The document password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document pages as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetPagesRequest request object with parameters
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Width') in path:
            path = path.replace('{' + self.__downcase_first_letter('Width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('Width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('Height') in path:
            path = path.replace('{' + self.__downcase_first_letter('Height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('Height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('Quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('Quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('Quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'ImagePageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_pages_from_url(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document pages as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param str file_name: The file name.
        :param str format: The image format (jpg, png or bmp). Default value is png.
        :param int width: The image width.
        :param int height: The image height.
        :param int quality: The image quality for jpg format. Default value is 90.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param str password: The document password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_pages_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_pages_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_pages_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document pages as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetPagesFromUrlRequest request object with parameters
        :return: ImagePageCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_pages_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `image_get_pages_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/pages'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Width') in path:
            path = path.replace('{' + self.__downcase_first_letter('Width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('Width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('Height') in path:
            path = path.replace('{' + self.__downcase_first_letter('Height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('Height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('Quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('Quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('Quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'ImagePageCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_pdf_file(self, request,**kwargs):  # noqa: E501
        """Downloads document as PDF.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str password: The document password. Not required if PDF document was created before.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_pdf_file_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_pdf_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads document as PDF.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetPdfFileRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_pdf_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_pdf_file`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pdf'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_pdf_file_from_url(self, request,**kwargs):  # noqa: E501
        """Downloads document at provided URL as PDF.  Document will be retrieved from the passed URL and added to Storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str url: The URL to retrieve document. (required)
        :param str file_name: The file name.
        :param str password: The document password. Not required if PDF document was created before.
        :param bool render_comments: Allows to render document comments. Not required if PDF document was created before.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_pdf_file_from_url_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_pdf_file_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Downloads document at provided URL as PDF.  Document will be retrieved from the passed URL and added to Storage.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetPdfFileFromUrlRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_pdf_file_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if request.url is None:
            raise ValueError("Missing the required parameter `url` when calling `image_get_pdf_file_from_url`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/image/pdf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('Url') in path:
            path = path.replace('{' + self.__downcase_first_letter('Url' + '}'), request.url if request.url is not None else '')
        else:
            if request.url is not None:
                query_params.append((self.__downcase_first_letter('Url'), request.url))  # noqa: E501
        if self.__downcase_first_letter('FileName') in path:
            path = path.replace('{' + self.__downcase_first_letter('FileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('FileName'), request.file_name))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_zip_with_attachment_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves attachment pages as images.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str attachment_name: The attachment name. (required)
        :param str format: The image format (jpg, png or bmp). Default value is png.
        :param int width: The image width.
        :param int height: The image height.
        :param int quality: The image quality for jpg format. Default value is 90.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str password: The document password.
        :param str attachment_password: The attachment password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_zip_with_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_zip_with_attachment_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_zip_with_attachment_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves attachment pages as images.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetZipWithAttachmentPagesRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_zip_with_attachment_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_zip_with_attachment_pages`")  # noqa: E501
        # verify the required parameter 'attachment_name' is set
        if request.attachment_name is None:
            raise ValueError("Missing the required parameter `attachment_name` when calling `image_get_zip_with_attachment_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/attachments/{attachmentName}/pages/zip'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501
        if request.attachment_name is not None:
            path_params[self.__downcase_first_letter('AttachmentName')] = request.attachment_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Width') in path:
            path = path.replace('{' + self.__downcase_first_letter('Width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('Width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('Height') in path:
            path = path.replace('{' + self.__downcase_first_letter('Height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('Height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('Quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('Quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('Quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('AttachmentPassword') in path:
            path = path.replace('{' + self.__downcase_first_letter('AttachmentPassword' + '}'), request.attachment_password if request.attachment_password is not None else '')
        else:
            if request.attachment_password is not None:
                query_params.append((self.__downcase_first_letter('AttachmentPassword'), request.attachment_password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/zip'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_get_zip_with_pages(self, request,**kwargs):  # noqa: E501
        """Retrieves list of document pages as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param str format: The image format (jpg, png or bmp). Default value is png.
        :param int width: The image width.
        :param int height: The image height.
        :param int quality: The image quality for jpg format. Default value is 90.
        :param int start_page_number: The starting document page number to render.
        :param int count_pages: The count of document pages to render.
        :param str password: The document password.
        :param bool extract_text: When this options is set to true text contained in document will be extracted and returned along with other information.
        :param bool render_comments: Allows to render document comments.
        :param bool render_hidden_pages: Enables rendering of document hidden pages, sheets or slides.
        :param str default_font_name: The name of the default font.
        :param str fonts_folder: The folder with custom fonts in storage.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_get_zip_with_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_get_zip_with_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_get_zip_with_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves list of document pages as image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageGetZipWithPagesRequest request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_get_zip_with_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_get_zip_with_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pages/zip'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Format') in path:
            path = path.replace('{' + self.__downcase_first_letter('Format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('Format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('Width') in path:
            path = path.replace('{' + self.__downcase_first_letter('Width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('Width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('Height') in path:
            path = path.replace('{' + self.__downcase_first_letter('Height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('Height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('Quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('Quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('Quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('StartPageNumber') in path:
            path = path.replace('{' + self.__downcase_first_letter('StartPageNumber' + '}'), request.start_page_number if request.start_page_number is not None else '')
        else:
            if request.start_page_number is not None:
                query_params.append((self.__downcase_first_letter('StartPageNumber'), request.start_page_number))  # noqa: E501
        if self.__downcase_first_letter('CountPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('CountPages' + '}'), request.count_pages if request.count_pages is not None else '')
        else:
            if request.count_pages is not None:
                query_params.append((self.__downcase_first_letter('CountPages'), request.count_pages))  # noqa: E501
        if self.__downcase_first_letter('Password') in path:
            path = path.replace('{' + self.__downcase_first_letter('Password' + '}'), request.password if request.password is not None else '')
        else:
            if request.password is not None:
                query_params.append((self.__downcase_first_letter('Password'), request.password))  # noqa: E501
        if self.__downcase_first_letter('ExtractText') in path:
            path = path.replace('{' + self.__downcase_first_letter('ExtractText' + '}'), request.extract_text if request.extract_text is not None else '')
        else:
            if request.extract_text is not None:
                query_params.append((self.__downcase_first_letter('ExtractText'), request.extract_text))  # noqa: E501
        if self.__downcase_first_letter('RenderComments') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderComments' + '}'), request.render_comments if request.render_comments is not None else '')
        else:
            if request.render_comments is not None:
                query_params.append((self.__downcase_first_letter('RenderComments'), request.render_comments))  # noqa: E501
        if self.__downcase_first_letter('RenderHiddenPages') in path:
            path = path.replace('{' + self.__downcase_first_letter('RenderHiddenPages' + '}'), request.render_hidden_pages if request.render_hidden_pages is not None else '')
        else:
            if request.render_hidden_pages is not None:
                query_params.append((self.__downcase_first_letter('RenderHiddenPages'), request.render_hidden_pages))  # noqa: E501
        if self.__downcase_first_letter('DefaultFontName') in path:
            path = path.replace('{' + self.__downcase_first_letter('DefaultFontName' + '}'), request.default_font_name if request.default_font_name is not None else '')
        else:
            if request.default_font_name is not None:
                query_params.append((self.__downcase_first_letter('DefaultFontName'), request.default_font_name))  # noqa: E501
        if self.__downcase_first_letter('FontsFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('FontsFolder' + '}'), request.fonts_folder if request.fonts_folder is not None else '')
        else:
            if request.fonts_folder is not None:
                query_params.append((self.__downcase_first_letter('FontsFolder'), request.fonts_folder))  # noqa: E501
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/zip'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'GET',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'file',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def image_transform_pages(self, request,**kwargs):  # noqa: E501
        """Rotates or reorders document page(s).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param str file_name: The file name. (required)
        :param TransformOptionsBase transform_options: The transformation options.
        :param str folder: The folder which contains specified file in storage.
        :param str storage: The file storage which have to be used.
        :return: PageInfoCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        if kwargs.get('is_async'):
            return self._image_transform_pages_with_http_info(request, **kwargs)  # noqa: E501
        
        (data) = self._image_transform_pages_with_http_info(request, **kwargs)  # noqa: E501
        return data

    def _image_transform_pages_with_http_info(self, request, **kwargs):  # noqa: E501
        """Rotates or reorders document page(s).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param ImageTransformPagesRequest request object with parameters
        :return: PageInfoCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method image_transform_pages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_name' is set
        if request.file_name is None:
            raise ValueError("Missing the required parameter `file_name` when calling `image_transform_pages`")  # noqa: E501

        collection_formats = {}
        path = '/viewer/{fileName}/image/pages'
        path_params = {}
        if request.file_name is not None:
            path_params[self.__downcase_first_letter('FileName')] = request.file_name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('Folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('Folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('Folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('Storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('Storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('Storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.transform_options is not None:
            body_params = request.transform_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        call_kwargs = {
            'resource_path':path, 
            'method':'PUT',
            'path_params':path_params,
            'query_params':query_params,
            'header_params':header_params,
            'body':body_params,
            'post_params':form_params,
            'files':local_var_files,
            'response_type':'PageInfoCollection',  # noqa: E501
            'auth_settings':self.auth.get_auth_settings(),
            'is_async':params.get('is_async'),
            '_return_http_data_only':params.get('_return_http_data_only'),
            '_preload_content':params.get('_preload_content', True),
            '_request_timeout':params.get('_request_timeout'),
            'collection_formats':collection_formats
        }

        return self.api_client.call_api(**call_kwargs)  # noqa: E501

    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return str
        else:
            return s[0].lower() + s[1:]

