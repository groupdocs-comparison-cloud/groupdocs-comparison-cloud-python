# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ItemsStyle.py">
#   Copyright (c) 2003-2024 Aspose Pty Ltd
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

class ItemsStyle(object):
    """
    ItemsStyle Object fields
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'font_color': 'str',
        'highlight_color': 'str',
        'begin_separator_string': 'str',
        'end_separator_string': 'str',
        'bold': 'bool',
        'italic': 'bool',
        'strike_through': 'bool',
        'underline': 'bool'
    }

    attribute_map = {
        'font_color': 'FontColor',
        'highlight_color': 'HighlightColor',
        'begin_separator_string': 'BeginSeparatorString',
        'end_separator_string': 'EndSeparatorString',
        'bold': 'Bold',
        'italic': 'Italic',
        'strike_through': 'StrikeThrough',
        'underline': 'Underline'
    }

    def __init__(self, font_color=None, highlight_color=None, begin_separator_string=None, end_separator_string=None, bold=None, italic=None, strike_through=None, underline=None, **kwargs):  # noqa: E501
        """Initializes new instance of ItemsStyle"""  # noqa: E501

        self._font_color = None
        self._highlight_color = None
        self._begin_separator_string = None
        self._end_separator_string = None
        self._bold = None
        self._italic = None
        self._strike_through = None
        self._underline = None

        if font_color is not None:
            self.font_color = font_color
        if highlight_color is not None:
            self.highlight_color = highlight_color
        if begin_separator_string is not None:
            self.begin_separator_string = begin_separator_string
        if end_separator_string is not None:
            self.end_separator_string = end_separator_string
        if bold is not None:
            self.bold = bold
        if italic is not None:
            self.italic = italic
        if strike_through is not None:
            self.strike_through = strike_through
        if underline is not None:
            self.underline = underline
    
    @property
    def font_color(self):
        """
        Gets the font_color.  # noqa: E501

        Font color for changed components  # noqa: E501

        :return: The font_color.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """
        Sets the font_color.

        Font color for changed components  # noqa: E501

        :param font_color: The font_color.  # noqa: E501
        :type: str
        """
        self._font_color = font_color
    
    @property
    def highlight_color(self):
        """
        Gets the highlight_color.  # noqa: E501

        Highlight color for changed components  # noqa: E501

        :return: The highlight_color.  # noqa: E501
        :rtype: str
        """
        return self._highlight_color

    @highlight_color.setter
    def highlight_color(self, highlight_color):
        """
        Sets the highlight_color.

        Highlight color for changed components  # noqa: E501

        :param highlight_color: The highlight_color.  # noqa: E501
        :type: str
        """
        self._highlight_color = highlight_color
    
    @property
    def begin_separator_string(self):
        """
        Gets the begin_separator_string.  # noqa: E501

        Start tag for changed components  # noqa: E501

        :return: The begin_separator_string.  # noqa: E501
        :rtype: str
        """
        return self._begin_separator_string

    @begin_separator_string.setter
    def begin_separator_string(self, begin_separator_string):
        """
        Sets the begin_separator_string.

        Start tag for changed components  # noqa: E501

        :param begin_separator_string: The begin_separator_string.  # noqa: E501
        :type: str
        """
        self._begin_separator_string = begin_separator_string
    
    @property
    def end_separator_string(self):
        """
        Gets the end_separator_string.  # noqa: E501

        End tag for changed components  # noqa: E501

        :return: The end_separator_string.  # noqa: E501
        :rtype: str
        """
        return self._end_separator_string

    @end_separator_string.setter
    def end_separator_string(self, end_separator_string):
        """
        Sets the end_separator_string.

        End tag for changed components  # noqa: E501

        :param end_separator_string: The end_separator_string.  # noqa: E501
        :type: str
        """
        self._end_separator_string = end_separator_string
    
    @property
    def bold(self):
        """
        Gets the bold.  # noqa: E501

        Bold style for changed components  # noqa: E501

        :return: The bold.  # noqa: E501
        :rtype: bool
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """
        Sets the bold.

        Bold style for changed components  # noqa: E501

        :param bold: The bold.  # noqa: E501
        :type: bool
        """
        if bold is None:
            raise ValueError("Invalid value for `bold`, must not be `None`")  # noqa: E501
        self._bold = bold
    
    @property
    def italic(self):
        """
        Gets the italic.  # noqa: E501

        Italic style for changed components  # noqa: E501

        :return: The italic.  # noqa: E501
        :rtype: bool
        """
        return self._italic

    @italic.setter
    def italic(self, italic):
        """
        Sets the italic.

        Italic style for changed components  # noqa: E501

        :param italic: The italic.  # noqa: E501
        :type: bool
        """
        if italic is None:
            raise ValueError("Invalid value for `italic`, must not be `None`")  # noqa: E501
        self._italic = italic
    
    @property
    def strike_through(self):
        """
        Gets the strike_through.  # noqa: E501

        Strike through style for changed components  # noqa: E501

        :return: The strike_through.  # noqa: E501
        :rtype: bool
        """
        return self._strike_through

    @strike_through.setter
    def strike_through(self, strike_through):
        """
        Sets the strike_through.

        Strike through style for changed components  # noqa: E501

        :param strike_through: The strike_through.  # noqa: E501
        :type: bool
        """
        if strike_through is None:
            raise ValueError("Invalid value for `strike_through`, must not be `None`")  # noqa: E501
        self._strike_through = strike_through
    
    @property
    def underline(self):
        """
        Gets the underline.  # noqa: E501

        Underline style for changed components  # noqa: E501

        :return: The underline.  # noqa: E501
        :rtype: bool
        """
        return self._underline

    @underline.setter
    def underline(self, underline):
        """
        Sets the underline.

        Underline style for changed components  # noqa: E501

        :param underline: The underline.  # noqa: E501
        :type: bool
        """
        if underline is None:
            raise ValueError("Invalid value for `underline`, must not be `None`")  # noqa: E501
        self._underline = underline

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
        if not isinstance(other, ItemsStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
