# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="DiagramMasterSetting.py">
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

class DiagramMasterSetting(object):
    """
    DiagramMasterSetting Object fields
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'master_path': 'str',
        'use_source_master': 'bool'
    }

    attribute_map = {
        'master_path': 'MasterPath',
        'use_source_master': 'UseSourceMaster'
    }

    def __init__(self, master_path=None, use_source_master=None, **kwargs):  # noqa: E501
        """Initializes new instance of DiagramMasterSetting"""  # noqa: E501

        self._master_path = None
        self._use_source_master = None

        if master_path is not None:
            self.master_path = master_path
        if use_source_master is not None:
            self.use_source_master = use_source_master
    
    @property
    def master_path(self):
        """
        Gets the master_path.  # noqa: E501

        Path to custom master path  # noqa: E501

        :return: The master_path.  # noqa: E501
        :rtype: str
        """
        return self._master_path

    @master_path.setter
    def master_path(self, master_path):
        """
        Sets the master_path.

        Path to custom master path  # noqa: E501

        :param master_path: The master_path.  # noqa: E501
        :type: str
        """
        self._master_path = master_path
    
    @property
    def use_source_master(self):
        """
        Gets the use_source_master.  # noqa: E501

        Value of using master from source and target document together  # noqa: E501

        :return: The use_source_master.  # noqa: E501
        :rtype: bool
        """
        return self._use_source_master

    @use_source_master.setter
    def use_source_master(self, use_source_master):
        """
        Sets the use_source_master.

        Value of using master from source and target document together  # noqa: E501

        :param use_source_master: The use_source_master.  # noqa: E501
        :type: bool
        """
        if use_source_master is None:
            raise ValueError("Invalid value for `use_source_master`, must not be `None`")  # noqa: E501
        self._use_source_master = use_source_master

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
        if not isinstance(other, DiagramMasterSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
