# GroupDocs.Viewer Cloud Python SDK
Python package for communicating with the GroupDocs.Viewer Cloud API. This SDK allows you to work with GroupDocs.Viewer Cloud REST APIs in your python applications, which allows rendering a specific document in HTML, image or PDF format with the flexibility to render the whole document or custom range of pages.

## Requirements

Python 3.4+

## Installation
Install `groupdocs-viewer-cloud` with [PIP](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/) by:

```sh
pip install groupdocs-viewer-cloud
```

Or clone repository and install it via [Setuptools](http://pypi.python.org/pypi/setuptools): 

```sh
python setup.py install
```

## Getting Started

Please follow the [installation procedure](#installation) and then run following:

```python
# Import module
import groupdocs_viewer_cloud

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
client_id = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
client_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

apiInstance = groupdocs_viewer_cloud.ViewApi.from_keys(client_id, client_secret)

format = "jpg"      
file = File.open("myfile.txt", "r")

request = ConvertAndDownloadRequest.new format, file

response = apiInstance.convert_and_download(request)
```

Below is an example demonstrating how to upload the document, render it, and download the result using GroupDocs.Viewer Cloud SDK for Python.


```python
# Import module
import groupdocs_viewer_cloud

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
client_id = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
client_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Upload input file to cloud storage
fileApiInstance = groupdocs_viewer_cloud.FileApi.from_keys(client_id, client_secret)
request = groupdocs_viewer_cloud.UploadFileRequest("myfile.txt", "C:\\Data\\myfile.txt")
fileApiInstance.upload_file(request)

# Render to html format
apiInstance = groupdocs_viewer_cloud.ViewApi.from_keys(client_id, client_secret)
view_options = groupdocs_viewer_cloud.ViewOptions()
view_options.file_info = groupdocs_viewer_cloud.FileInfo()
view_options.file_info.file_path = "myfile.txt"
view_options.view_format = "HTML"
view_options.output_path = "myfile.html"

request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
response = apiInstance.create_view(request)

# Download result
request = groupdocs_viewer_cloud.DownloadFileRequest("myfile.html")
response = fileApiInstance.download_file(request)

print("Expected response type is Stream: " + str(len(response)))


```

## Licensing
GroupDocs.Viewer Cloud Python SDK licensed under [MIT License](http://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-python/LICENSE).

## Resources
+ [**Website**](https://www.groupdocs.cloud)
+ [**Product Home**](https://products.groupdocs.cloud/viewer)
+ [**Documentation**](https://docs.groupdocs.cloud/display/viewercloud/Home)
+ [**Free Support Forum**](https://forum.groupdocs.cloud/c/viewer)
+ [**Blog**](https://blog.groupdocs.cloud/category/viewer)

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.groupdocs.cloud/c/viewer).