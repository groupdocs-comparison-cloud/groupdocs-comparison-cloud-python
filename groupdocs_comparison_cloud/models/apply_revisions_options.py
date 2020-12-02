# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ApplyRevisionsOptions.py">
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

class ApplyRevisionsOptions(object):
    """
    Options for apply revisions method
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source_file': 'FileInfo',
        'revisions': 'list[RevisionInfo]',
        'output_path': 'str'
    }

    attribute_map = {
        'source_file': 'SourceFile',
        'revisions': 'Revisions',
        'output_path': 'OutputPath'
    }

    def __init__(self, source_file=None, revisions=None, output_path=None, **kwargs):  # noqa: E501
        """Initializes new instance of ApplyRevisionsOptions"""  # noqa: E501

        self._source_file = None
        self._revisions = None
        self._output_path = None

        if source_file is not None:
            self.source_file = source_file
        if revisions is not None:
            self.revisions = revisions
        if output_path is not None:
            self.output_path = output_path
    
    @property
    def source_file(self):
        """
        Gets the source_file.  # noqa: E501

        Information about source file  # noqa: E501

        :return: The source_file.  # noqa: E501
        :rtype: FileInfo
        """
        return self._source_file

    @source_file.setter
    def source_file(self, source_file):
        """
        Sets the source_file.

        Information about source file  # noqa: E501

        :param source_file: The source_file.  # noqa: E501
        :type: FileInfo
        """
        self._source_file = source_file
    
    @property
    def revisions(self):
        """
        Gets the revisions.  # noqa: E501

        Revisions to apply or reject.  # noqa: E501

        :return: The revisions.  # noqa: E501
        :rtype: list[RevisionInfo]
        """
        return self._revisions

    @revisions.setter
    def revisions(self, revisions):
        """
        Sets the revisions.

        Revisions to apply or reject.  # noqa: E501

        :param revisions: The revisions.  # noqa: E501
        :type: list[RevisionInfo]
        """
        self._revisions = revisions
    
    @property
    def output_path(self):
        """
        Gets the output_path.  # noqa: E501

        Path to the resultant document (if not specified the document will not be saved)  # noqa: E501

        :return: The output_path.  # noqa: E501
        :rtype: str
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path):
        """
        Sets the output_path.

        Path to the resultant document (if not specified the document will not be saved)  # noqa: E501

        :param output_path: The output_path.  # noqa: E501
        :type: str
        """
        self._output_path = output_path

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
        if not isinstance(other, ApplyRevisionsOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
