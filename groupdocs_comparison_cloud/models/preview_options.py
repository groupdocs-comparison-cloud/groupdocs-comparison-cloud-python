# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="PreviewOptions.py">
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

class PreviewOptions(object):
    """
    Defines preview options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_info': 'FileInfo',
        'format': 'str',
        'output_folder': 'str',
        'width': 'int',
        'height': 'int',
        'page_numbers': 'list[int]'
    }

    attribute_map = {
        'file_info': 'FileInfo',
        'format': 'Format',
        'output_folder': 'OutputFolder',
        'width': 'Width',
        'height': 'Height',
        'page_numbers': 'PageNumbers'
    }

    def __init__(self, file_info=None, format=None, output_folder=None, width=None, height=None, page_numbers=None, **kwargs):  # noqa: E501
        """Initializes new instance of PreviewOptions"""  # noqa: E501

        self._file_info = None
        self._format = None
        self._output_folder = None
        self._width = None
        self._height = None
        self._page_numbers = None

        if file_info is not None:
            self.file_info = file_info
        if format is not None:
            self.format = format
        if output_folder is not None:
            self.output_folder = output_folder
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if page_numbers is not None:
            self.page_numbers = page_numbers
    
    @property
    def file_info(self):
        """
        Gets the file_info.  # noqa: E501

        Input file info  # noqa: E501

        :return: The file_info.  # noqa: E501
        :rtype: FileInfo
        """
        return self._file_info

    @file_info.setter
    def file_info(self, file_info):
        """
        Sets the file_info.

        Input file info  # noqa: E501

        :param file_info: The file_info.  # noqa: E501
        :type: FileInfo
        """
        self._file_info = file_info
    
    @property
    def format(self):
        """
        Gets the format.  # noqa: E501

        Preview image format  # noqa: E501

        :return: The format.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format.

        Preview image format  # noqa: E501

        :param format: The format.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["Jpeg", "Png", "Bmp"]  # noqa: E501
        if not format.isdigit():	
            if format not in allowed_values:
                raise ValueError(
                    "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                    .format(format, allowed_values))
            self._format = format
        else:
            self._format = allowed_values[int(format) if six.PY3 else long(format)]
    
    @property
    def output_folder(self):
        """
        Gets the output_folder.  # noqa: E501

        Path to folder with preview results  # noqa: E501

        :return: The output_folder.  # noqa: E501
        :rtype: str
        """
        return self._output_folder

    @output_folder.setter
    def output_folder(self, output_folder):
        """
        Sets the output_folder.

        Path to folder with preview results  # noqa: E501

        :param output_folder: The output_folder.  # noqa: E501
        :type: str
        """
        self._output_folder = output_folder
    
    @property
    def width(self):
        """
        Gets the width.  # noqa: E501

        Preview width  # noqa: E501

        :return: The width.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width.

        Preview width  # noqa: E501

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

        Preview height  # noqa: E501

        :return: The height.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Preview height  # noqa: E501

        :param height: The height.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    
    @property
    def page_numbers(self):
        """
        Gets the page_numbers.  # noqa: E501

        Page numbers that will be previewed.  # noqa: E501

        :return: The page_numbers.  # noqa: E501
        :rtype: list[int]
        """
        return self._page_numbers

    @page_numbers.setter
    def page_numbers(self, page_numbers):
        """
        Sets the page_numbers.

        Page numbers that will be previewed.  # noqa: E501

        :param page_numbers: The page_numbers.  # noqa: E501
        :type: list[int]
        """
        self._page_numbers = page_numbers

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
        if not isinstance(other, PreviewOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
