# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="ComparisonOptions.py">
#   Copyright (c) 2003-2021 Aspose Pty Ltd
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

class ComparisonOptions(object):
    """
    Defines comparison options
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
        'target_files': 'list[FileInfo]',
        'settings': 'Settings',
        'change_type': 'str',
        'output_path': 'str'
    }

    attribute_map = {
        'source_file': 'SourceFile',
        'target_files': 'TargetFiles',
        'settings': 'Settings',
        'change_type': 'ChangeType',
        'output_path': 'OutputPath'
    }

    def __init__(self, source_file=None, target_files=None, settings=None, change_type=None, output_path=None, **kwargs):  # noqa: E501
        """Initializes new instance of ComparisonOptions"""  # noqa: E501

        self._source_file = None
        self._target_files = None
        self._settings = None
        self._change_type = None
        self._output_path = None

        if source_file is not None:
            self.source_file = source_file
        if target_files is not None:
            self.target_files = target_files
        if settings is not None:
            self.settings = settings
        if change_type is not None:
            self.change_type = change_type
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
    def target_files(self):
        """
        Gets the target_files.  # noqa: E501

        Information about target file(s)  # noqa: E501

        :return: The target_files.  # noqa: E501
        :rtype: list[FileInfo]
        """
        return self._target_files

    @target_files.setter
    def target_files(self, target_files):
        """
        Sets the target_files.

        Information about target file(s)  # noqa: E501

        :param target_files: The target_files.  # noqa: E501
        :type: list[FileInfo]
        """
        self._target_files = target_files
    
    @property
    def settings(self):
        """
        Gets the settings.  # noqa: E501

        Comparison settings  # noqa: E501

        :return: The settings.  # noqa: E501
        :rtype: Settings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings.

        Comparison settings  # noqa: E501

        :param settings: The settings.  # noqa: E501
        :type: Settings
        """
        self._settings = settings
    
    @property
    def change_type(self):
        """
        Gets the change_type.  # noqa: E501

        Changes type. Used only for Changes resource(/comparison/changes)  # noqa: E501

        :return: The change_type.  # noqa: E501
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """
        Sets the change_type.

        Changes type. Used only for Changes resource(/comparison/changes)  # noqa: E501

        :param change_type: The change_type.  # noqa: E501
        :type: str
        """
        if change_type is None:
            raise ValueError("Invalid value for `change_type`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Modified", "Inserted", "Deleted", "Added", "NotModified", "StyleChanged", "Resized", "Moved", "MovedAndResized", "ShiftedAndResized"]  # noqa: E501
        if not change_type.isdigit():	
            if change_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `change_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(change_type, allowed_values))
            self._change_type = change_type
        else:
            self._change_type = allowed_values[int(change_type) if six.PY3 else long(change_type)]
    
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
        if not isinstance(other, ComparisonOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
