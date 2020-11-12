![](https://img.shields.io/badge/api-v2.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-viewer-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-viewer-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-viewer-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-viewer-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-viewer-cloud/groupdocs-viewer-cloud-python)](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-python/blob/master/LICENSE) 

# Python SDK to View Documents in the Cloud

[GroupDocs.Viewer Cloud SDK for Python](https://products.groupdocs.cloud/viewer/python) wraps GroupDocs.Viewer RESTful APIs so you may integrate Document Viewing features in your own apps with zero initial cost.

GroupDocs.Viewer REST API allows the developers to view & render a number of popular files formats including Word documents, Excel spreadsheets, PowerPoint presentations, CAD drawings, Visio diagram, PDF, OpenDocument formats, emails & images.

## Document Viewer Services in REST

- 90+ supported file formats.
- View documents as PDF, HTML or images.
- Render documents as raster & vector images.
- Render documents with comments & notes.
- Flip or rotate documents pages at 90, 180 or 270 degrees.
- Reorder document pages.
- Render hidden, consecutive or selected document pages.
- Watermark PDF, image or HTML output pages.
- Render with custom fonts as well as replace any missing fonts.
- Load password-protected documents.
- Extract attachment information such as attachment count & names.
- Extract document information like file format, page count, size and visibility, text coordinates, and so on.
- Integrated storage API.

Check out the [Developer's Guide](https://docs.groupdocs.cloud/viewer/developer-guide/) to know more about GroupDocs.Viewer REST API.

## Microsoft File Formats

**Microsoft Word:** DOC, DOCM, DOCX, DOT, DOTM, DOTX\
**Microsoft Excel:** XLS, XLSX, XLSB, XLSM\
**Microsoft PowerPoint:** PPTX, PPTM, PPT, PPSX, PPSM, PPS, POTX, POTM\
**Microsoft Project:** MPP, MPT\
**Microsoft Outlook:** MSG, OST, PST\
**Microsoft Visio:** VDW, VDX, VSD, VSDM, VSDX, VSS, VSSM, VSSX, VST, VSTM, VSTX, VSX, VTX\
**Microsoft OneNote:** ONE

## Other Formats

**Page Layout Formats:** PDF, XPS, TEX\
**OpenDocument:** ODT, OTT, ODS, OTS, ODP, OTP\
**CAD:** DNG, DWF, DWG, DXF, IDC, STL\
**Images:** BMP, CGM, DCM, DJVU, EMP, EPS, GIF, ICO, JP2, JPG, ODG, PCL, PNG, PS, PSD, SVG, TIFF, WEBP, WMF\
**Web:** HTML, MHT, MHTML\
**Emails:** EML, EMLX\
**eBooks:** EPUB, MOBI\
**Others:** TXT, RTF, CSV, TSV

## Get Started with GroupDocs.Viewer Cloud SDK for Python

First create an account at [GroupDocs for Cloud](https://dashboard.groupdocs.cloud/) and get your application information. Next, execute the following command to install the package.

```sh
pip install groupdocs-viewer-cloud
```

Or clone repository and install it via [Setuptools](http://pypi.python.org/pypi/setuptools) as follows.

```sh
python setup.py install
```

## Get a List of Viewable File Formats

```python
# Import module
import groupdocs_viewer_cloud

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
app_sid = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
app_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Create instance of the API
api = groupdocs_viewer_cloud.InfoApi.from_keys(app_sid, app_key)

try:
    # Retrieve supported file-formats
    response = api.get_supported_file_formats()

    # Print out supported file-formats
    print("Supported file-formats:")
    for format in response.formats:
        print('{0} ({1})'.format(format.file_format, format.extension)) 
except groupdocs_viewer_cloud.ApiException as e:
    print("Exception when calling get_supported_file_formats: {0}".format(e.message))
```

## GroupDocs.Viewer Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js | Android |
|---|---|---|---|---|---|---|
| [GitHub](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-dotnet) | [GitHub](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-java) | [GitHub](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-php) | [GitHub](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-python) | [GitHub](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-ruby)  | [GitHub](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-node) | [GitHub](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-android) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.Viewer-Cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-viewer-cloud) | [Composer](https://packagist.org/packages/groupdocscloud/groupdocs-viewer-cloud) | [PIP](https://pypi.org/project/groupdocs-viewer-cloud/) | [GEM](https://rubygems.org/gems/groupdocs_viewer_cloud)  | [NPM](https://www.npmjs.com/package/groupdocs-viewer-cloud) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-viewer-cloud-android) | 

[Home](https://www.groupdocs.cloud/) | [Product Page](https://products.groupdocs.cloud/viewer/python) | [Documentation](https://docs.groupdocs.cloud/viewer/) | [Live Demo](https://products.groupdocs.app/viewer/total) | [API Reference](https://apireference.groupdocs.cloud/viewer/) | [Code Samples](https://github.com/groupdocs-viewer-cloud/groupdocs-viewer-cloud-python-samples) | [Blog](https://blog.groupdocs.cloud/category/viewer/) | [Free Support](https://forum.groupdocs.cloud/c/viewer) | [Free Trial](https://dashboard.groupdocs.cloud)
