# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ChangeInfo.py">
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

class ChangeInfo(object):
    """
    ChangeInfo Object fields
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'comparison_action': 'str',
        'comparison_type_changed': 'str',
        'text': 'str',
        'authors': 'list[str]',
        'style_change_info': 'list[StyleChangeInfo]'
    }

    attribute_map = {
        'id': 'Id',
        'comparison_action': 'ComparisonAction',
        'comparison_type_changed': 'ComparisonTypeChanged',
        'text': 'Text',
        'authors': 'Authors',
        'style_change_info': 'StyleChangeInfo'
    }

    def __init__(self, id=None, comparison_action=None, comparison_type_changed=None, text=None, authors=None, style_change_info=None, **kwargs):  # noqa: E501
        """Initializes new instance of ChangeInfo"""  # noqa: E501

        self._id = None
        self._comparison_action = None
        self._comparison_type_changed = None
        self._text = None
        self._authors = None
        self._style_change_info = None

        if id is not None:
            self.id = id
        if comparison_action is not None:
            self.comparison_action = comparison_action
        if comparison_type_changed is not None:
            self.comparison_type_changed = comparison_type_changed
        if text is not None:
            self.text = text
        if authors is not None:
            self.authors = authors
        if style_change_info is not None:
            self.style_change_info = style_change_info
    
    @property
    def id(self):
        """
        Gets the id.  # noqa: E501

        Id of change  # noqa: E501

        :return: The id.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id.

        Id of change  # noqa: E501

        :param id: The id.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    
    @property
    def comparison_action(self):
        """
        Gets the comparison_action.  # noqa: E501

        Action (accept or reject). This field shows comparison what to do with this change  # noqa: E501

        :return: The comparison_action.  # noqa: E501
        :rtype: str
        """
        return self._comparison_action

    @comparison_action.setter
    def comparison_action(self, comparison_action):
        """
        Sets the comparison_action.

        Action (accept or reject). This field shows comparison what to do with this change  # noqa: E501

        :param comparison_action: The comparison_action.  # noqa: E501
        :type: str
        """
        self._comparison_action = comparison_action
    
    @property
    def comparison_type_changed(self):
        """
        Gets the comparison_type_changed.  # noqa: E501

        Type of change (Inserted, Deleted or StyleChanged)  # noqa: E501

        :return: The comparison_type_changed.  # noqa: E501
        :rtype: str
        """
        return self._comparison_type_changed

    @comparison_type_changed.setter
    def comparison_type_changed(self, comparison_type_changed):
        """
        Sets the comparison_type_changed.

        Type of change (Inserted, Deleted or StyleChanged)  # noqa: E501

        :param comparison_type_changed: The comparison_type_changed.  # noqa: E501
        :type: str
        """
        self._comparison_type_changed = comparison_type_changed
    
    @property
    def text(self):
        """
        Gets the text.  # noqa: E501

        Text of changed element  # noqa: E501

        :return: The text.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text.

        Text of changed element  # noqa: E501

        :param text: The text.  # noqa: E501
        :type: str
        """
        self._text = text
    
    @property
    def authors(self):
        """
        Gets the authors.  # noqa: E501

        Array of authors who made this change (used for multi comparison)  # noqa: E501

        :return: The authors.  # noqa: E501
        :rtype: list[str]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """
        Sets the authors.

        Array of authors who made this change (used for multi comparison)  # noqa: E501

        :param authors: The authors.  # noqa: E501
        :type: list[str]
        """
        self._authors = authors
    
    @property
    def style_change_info(self):
        """
        Gets the style_change_info.  # noqa: E501

        Array of style changes  # noqa: E501

        :return: The style_change_info.  # noqa: E501
        :rtype: list[StyleChangeInfo]
        """
        return self._style_change_info

    @style_change_info.setter
    def style_change_info(self, style_change_info):
        """
        Sets the style_change_info.

        Array of style changes  # noqa: E501

        :param style_change_info: The style_change_info.  # noqa: E501
        :type: list[StyleChangeInfo]
        """
        self._style_change_info = style_change_info

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
        if not isinstance(other, ChangeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
