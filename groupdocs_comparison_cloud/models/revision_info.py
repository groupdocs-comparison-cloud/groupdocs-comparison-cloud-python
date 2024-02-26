# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="RevisionInfo.py">
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

class RevisionInfo(object):
    """
    Provides information about one revision.
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
        'action': 'str',
        'text': 'str',
        'author': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'action': 'Action',
        'text': 'Text',
        'author': 'Author',
        'type': 'Type'
    }

    def __init__(self, id=None, action=None, text=None, author=None, type=None, **kwargs):  # noqa: E501
        """Initializes new instance of RevisionInfo"""  # noqa: E501

        self._id = None
        self._action = None
        self._text = None
        self._author = None
        self._type = None

        if id is not None:
            self.id = id
        if action is not None:
            self.action = action
        if text is not None:
            self.text = text
        if author is not None:
            self.author = author
        if type is not None:
            self.type = type
    
    @property
    def id(self):
        """
        Gets the id.  # noqa: E501

        Id of revision  # noqa: E501

        :return: The id.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id.

        Id of revision  # noqa: E501

        :param id: The id.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id
    
    @property
    def action(self):
        """
        Gets the action.  # noqa: E501

        Action (accept or reject). This field allows you to influence the display of the revision.               # noqa: E501

        :return: The action.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action.

        Action (accept or reject). This field allows you to influence the display of the revision.               # noqa: E501

        :param action: The action.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Accept", "Reject"]  # noqa: E501
        if not action.isdigit():	
            if action not in allowed_values:
                raise ValueError(
                    "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                    .format(action, allowed_values))
            self._action = action
        else:
            self._action = allowed_values[int(action) if six.PY3 else long(action)]
    
    @property
    def text(self):
        """
        Gets the text.  # noqa: E501

        The text that is in revision.  # noqa: E501

        :return: The text.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text.

        The text that is in revision.  # noqa: E501

        :param text: The text.  # noqa: E501
        :type: str
        """
        self._text = text
    
    @property
    def author(self):
        """
        Gets the author.  # noqa: E501

        Author.  # noqa: E501

        :return: The author.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author.

        Author.  # noqa: E501

        :param author: The author.  # noqa: E501
        :type: str
        """
        self._author = author
    
    @property
    def type(self):
        """
        Gets the type.  # noqa: E501

        RevisionHandler type, depending on the type the Action (accept or reject) logic changes.               # noqa: E501

        :return: The type.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type.

        RevisionHandler type, depending on the type the Action (accept or reject) logic changes.               # noqa: E501

        :param type: The type.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Insertion", "Deletion", "FormatChange", "StyleDefinitionChange", "Moving"]  # noqa: E501
        if not type.isdigit():	
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values))
            self._type = type
        else:
            self._type = allowed_values[int(type) if six.PY3 else long(type)]

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
        if not isinstance(other, RevisionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
