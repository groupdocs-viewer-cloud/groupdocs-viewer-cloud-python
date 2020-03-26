# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="CadOptions.py">
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

class CadOptions(object):
    """
    Rendering options for CAD file formats. CAD file formats include files with extensions: .dwg, .dxf, .dgn, .ifc, .stl
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'scale_factor': 'float',
        'width': 'int',
        'height': 'int',
        'tiles': 'list[Tile]',
        'render_layouts': 'bool',
        'layout_name': 'str',
        'layers': 'list[str]'
    }

    attribute_map = {
        'scale_factor': 'ScaleFactor',
        'width': 'Width',
        'height': 'Height',
        'tiles': 'Tiles',
        'render_layouts': 'RenderLayouts',
        'layout_name': 'LayoutName',
        'layers': 'Layers'
    }

    def __init__(self, scale_factor=None, width=None, height=None, tiles=None, render_layouts=None, layout_name=None, layers=None, **kwargs):  # noqa: E501
        """Initializes new instance of CadOptions"""  # noqa: E501

        self._scale_factor = None
        self._width = None
        self._height = None
        self._tiles = None
        self._render_layouts = None
        self._layout_name = None
        self._layers = None

        if scale_factor is not None:
            self.scale_factor = scale_factor
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if tiles is not None:
            self.tiles = tiles
        if render_layouts is not None:
            self.render_layouts = render_layouts
        if layout_name is not None:
            self.layout_name = layout_name
        if layers is not None:
            self.layers = layers
    
    @property
    def scale_factor(self):
        """
        Gets the scale_factor.  # noqa: E501

        Scale factor allows to change the size of the output document. Values higher than 1 will enlarge output result and values between 0 and 1 will make output result smaller. This option is ignored when either Height or Width options are set.   # noqa: E501

        :return: The scale_factor.  # noqa: E501
        :rtype: float
        """
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, scale_factor):
        """
        Sets the scale_factor.

        Scale factor allows to change the size of the output document. Values higher than 1 will enlarge output result and values between 0 and 1 will make output result smaller. This option is ignored when either Height or Width options are set.   # noqa: E501

        :param scale_factor: The scale_factor.  # noqa: E501
        :type: float
        """
        if scale_factor is None:
            raise ValueError("Invalid value for `scale_factor`, must not be `None`")  # noqa: E501
        self._scale_factor = scale_factor
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Width of the output result in pixels          # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Width of the output result in pixels          # noqa: E501

        :param width: The width.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
        self._width = width
    
    @property
    def height(self):
        """
        Gets the height.  # noqa: E501

        Height of the output result in pixels       # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Height of the output result in pixels       # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def tiles(self):
        """
        Gets the tiles.  # noqa: E501

        The drawing regions to render This option supported only for DWG and DWT file types The RenderLayouts and LayoutName options are ignored when rendering by tiles  # noqa: E501

        :return: The tiles.  # noqa: E501
        :rtype: list[Tile]
        """
        return self._tiles

    @tiles.setter
    def tiles(self, tiles):
        """
        Sets the tiles.

        The drawing regions to render This option supported only for DWG and DWT file types The RenderLayouts and LayoutName options are ignored when rendering by tiles  # noqa: E501

        :param tiles: The tiles.  # noqa: E501
        :type: list[Tile]
        """
        self._tiles = tiles
    
    @property
    def render_layouts(self):
        """
        Gets the render_layouts.  # noqa: E501

        Indicates whether layouts from CAD document should be rendered  # noqa: E501

        :return: The render_layouts.  # noqa: E501
        :rtype: bool
        """
        return self._render_layouts

    @render_layouts.setter
    def render_layouts(self, render_layouts):
        """
        Sets the render_layouts.

        Indicates whether layouts from CAD document should be rendered  # noqa: E501

        :param render_layouts: The render_layouts.  # noqa: E501
        :type: bool
        """
        if render_layouts is None:
            raise ValueError("Invalid value for `render_layouts`, must not be `None`")  # noqa: E501
        self._render_layouts = render_layouts
    
    @property
    def layout_name(self):
        """
        Gets the layout_name.  # noqa: E501

        The name of the specific layout to render. Layout name is case-sensitive  # noqa: E501

        :return: The layout_name.  # noqa: E501
        :rtype: str
        """
        return self._layout_name

    @layout_name.setter
    def layout_name(self, layout_name):
        """
        Sets the layout_name.

        The name of the specific layout to render. Layout name is case-sensitive  # noqa: E501

        :param layout_name: The layout_name.  # noqa: E501
        :type: str
        """
        self._layout_name = layout_name
    
    @property
    def layers(self):
        """
        Gets the layers.  # noqa: E501

        The CAD drawing layers to render By default all layers are rendered; Layer names are case-sensitive  # noqa: E501

        :return: The layers.  # noqa: E501
        :rtype: list[str]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """
        Sets the layers.

        The CAD drawing layers to render By default all layers are rendered; Layer names are case-sensitive  # noqa: E501

        :param layers: The layers.  # noqa: E501
        :type: list[str]
        """
        self._layers = layers

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
        if not isinstance(other, CadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
