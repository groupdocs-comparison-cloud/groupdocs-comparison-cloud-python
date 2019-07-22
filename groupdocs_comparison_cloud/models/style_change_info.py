# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="StyleChangeInfo.py">
#   Copyright (c) 2003-2019 Aspose Pty Ltd
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

class StyleChangeInfo(object):
    """
    StyleChangeInfo Object fields
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'changed_property': 'str',
        'old_value': 'str',
        'new_value': 'str'
    }

    attribute_map = {
        'changed_property': 'ChangedProperty',
        'old_value': 'OldValue',
        'new_value': 'NewValue'
    }

    def __init__(self, changed_property=None, old_value=None, new_value=None, **kwargs):  # noqa: E501
        """Initializes new instance of StyleChangeInfo"""  # noqa: E501

        self._changed_property = None
        self._old_value = None
        self._new_value = None

        if changed_property is not None:
            self.changed_property = changed_property
        if old_value is not None:
            self.old_value = old_value
        if new_value is not None:
            self.new_value = new_value
    
    @property
    def changed_property(self):
        """
        Gets the changed_property.  # noqa: E501

        Name of changed style  # noqa: E501

        :return: The changed_property.  # noqa: E501
        :rtype: str
        """
        return self._changed_property

    @changed_property.setter
    def changed_property(self, changed_property):
        """
        Sets the changed_property.

        Name of changed style  # noqa: E501

        :param changed_property: The changed_property.  # noqa: E501
        :type: str
        """
        self._changed_property = changed_property
    
    @property
    def old_value(self):
        """
        Gets the old_value.  # noqa: E501

        Value of changed style from source document  # noqa: E501

        :return: The old_value.  # noqa: E501
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """
        Sets the old_value.

        Value of changed style from source document  # noqa: E501

        :param old_value: The old_value.  # noqa: E501
        :type: str
        """
        self._old_value = old_value
    
    @property
    def new_value(self):
        """
        Gets the new_value.  # noqa: E501

        Value of changed style from target document  # noqa: E501

        :return: The new_value.  # noqa: E501
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """
        Sets the new_value.

        Value of changed style from target document  # noqa: E501

        :param new_value: The new_value.  # noqa: E501
        :type: str
        """
        self._new_value = new_value

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
        if not isinstance(other, StyleChangeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
