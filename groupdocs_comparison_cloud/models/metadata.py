# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Metadata.py">
#   Copyright (c) 2003-2023 Aspose Pty Ltd
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

class Metadata(object):
    """
    MetaData Object fields
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'author': 'str',
        'last_save_by': 'str',
        'company': 'str'
    }

    attribute_map = {
        'author': 'Author',
        'last_save_by': 'LastSaveBy',
        'company': 'Company'
    }

    def __init__(self, author=None, last_save_by=None, company=None, **kwargs):  # noqa: E501
        """Initializes new instance of Metadata"""  # noqa: E501

        self._author = None
        self._last_save_by = None
        self._company = None

        if author is not None:
            self.author = author
        if last_save_by is not None:
            self.last_save_by = last_save_by
        if company is not None:
            self.company = company
    
    @property
    def author(self):
        """
        Gets the author.  # noqa: E501

        Value of document Author  # noqa: E501

        :return: The author.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author.

        Value of document Author  # noqa: E501

        :param author: The author.  # noqa: E501
        :type: str
        """
        self._author = author
    
    @property
    def last_save_by(self):
        """
        Gets the last_save_by.  # noqa: E501

        Value of last save by author of document  # noqa: E501

        :return: The last_save_by.  # noqa: E501
        :rtype: str
        """
        return self._last_save_by

    @last_save_by.setter
    def last_save_by(self, last_save_by):
        """
        Sets the last_save_by.

        Value of last save by author of document  # noqa: E501

        :param last_save_by: The last_save_by.  # noqa: E501
        :type: str
        """
        self._last_save_by = last_save_by
    
    @property
    def company(self):
        """
        Gets the company.  # noqa: E501

        Value of Company of document  # noqa: E501

        :return: The company.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company.

        Value of Company of document  # noqa: E501

        :param company: The company.  # noqa: E501
        :type: str
        """
        self._company = company

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
