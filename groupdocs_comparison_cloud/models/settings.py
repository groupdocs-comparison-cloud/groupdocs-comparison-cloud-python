# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Settings.py">
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

class Settings(object):
    """
    Defines comparison process additional settings 
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'generate_summary_page': 'bool',
        'show_deleted_content': 'bool',
        'show_inserted_content': 'bool',
        'style_change_detection': 'bool',
        'inserted_items_style': 'ItemsStyle',
        'deleted_items_style': 'ItemsStyle',
        'changed_items_style': 'ItemsStyle',
        'words_separator_chars': 'list[str]',
        'details_level': 'str',
        'use_frames_for_del_ins_elements': 'bool',
        'calculate_component_coordinates': 'bool',
        'mark_changed_content': 'bool',
        'mark_nested_content': 'bool',
        'clone_metadata': 'str',
        'meta_data': 'Metadata',
        'password_save_option': 'str',
        'password': 'str',
        'diagram_master_setting': 'DiagramMasterSetting',
        'original_size': 'Size',
        'header_footers_comparison': 'bool',
        'paper_size': 'str',
        'sensitivity_of_comparison': 'int'
    }

    attribute_map = {
        'generate_summary_page': 'GenerateSummaryPage',
        'show_deleted_content': 'ShowDeletedContent',
        'show_inserted_content': 'ShowInsertedContent',
        'style_change_detection': 'StyleChangeDetection',
        'inserted_items_style': 'InsertedItemsStyle',
        'deleted_items_style': 'DeletedItemsStyle',
        'changed_items_style': 'ChangedItemsStyle',
        'words_separator_chars': 'WordsSeparatorChars',
        'details_level': 'DetailsLevel',
        'use_frames_for_del_ins_elements': 'UseFramesForDelInsElements',
        'calculate_component_coordinates': 'CalculateComponentCoordinates',
        'mark_changed_content': 'MarkChangedContent',
        'mark_nested_content': 'MarkNestedContent',
        'clone_metadata': 'CloneMetadata',
        'meta_data': 'MetaData',
        'password_save_option': 'PasswordSaveOption',
        'password': 'Password',
        'diagram_master_setting': 'DiagramMasterSetting',
        'original_size': 'OriginalSize',
        'header_footers_comparison': 'HeaderFootersComparison',
        'paper_size': 'PaperSize',
        'sensitivity_of_comparison': 'SensitivityOfComparison'
    }

    def __init__(self, generate_summary_page=None, show_deleted_content=None, show_inserted_content=None, style_change_detection=None, inserted_items_style=None, deleted_items_style=None, changed_items_style=None, words_separator_chars=None, details_level=None, use_frames_for_del_ins_elements=None, calculate_component_coordinates=None, mark_changed_content=None, mark_nested_content=None, clone_metadata=None, meta_data=None, password_save_option=None, password=None, diagram_master_setting=None, original_size=None, header_footers_comparison=None, paper_size=None, sensitivity_of_comparison=None, **kwargs):  # noqa: E501
        """Initializes new instance of Settings"""  # noqa: E501

        self._generate_summary_page = None
        self._show_deleted_content = None
        self._show_inserted_content = None
        self._style_change_detection = None
        self._inserted_items_style = None
        self._deleted_items_style = None
        self._changed_items_style = None
        self._words_separator_chars = None
        self._details_level = None
        self._use_frames_for_del_ins_elements = None
        self._calculate_component_coordinates = None
        self._mark_changed_content = None
        self._mark_nested_content = None
        self._clone_metadata = None
        self._meta_data = None
        self._password_save_option = None
        self._password = None
        self._diagram_master_setting = None
        self._original_size = None
        self._header_footers_comparison = None
        self._paper_size = None
        self._sensitivity_of_comparison = None

        if generate_summary_page is not None:
            self.generate_summary_page = generate_summary_page
        if show_deleted_content is not None:
            self.show_deleted_content = show_deleted_content
        if show_inserted_content is not None:
            self.show_inserted_content = show_inserted_content
        if style_change_detection is not None:
            self.style_change_detection = style_change_detection
        if inserted_items_style is not None:
            self.inserted_items_style = inserted_items_style
        if deleted_items_style is not None:
            self.deleted_items_style = deleted_items_style
        if changed_items_style is not None:
            self.changed_items_style = changed_items_style
        if words_separator_chars is not None:
            self.words_separator_chars = words_separator_chars
        if details_level is not None:
            self.details_level = details_level
        if use_frames_for_del_ins_elements is not None:
            self.use_frames_for_del_ins_elements = use_frames_for_del_ins_elements
        if calculate_component_coordinates is not None:
            self.calculate_component_coordinates = calculate_component_coordinates
        if mark_changed_content is not None:
            self.mark_changed_content = mark_changed_content
        if mark_nested_content is not None:
            self.mark_nested_content = mark_nested_content
        if clone_metadata is not None:
            self.clone_metadata = clone_metadata
        if meta_data is not None:
            self.meta_data = meta_data
        if password_save_option is not None:
            self.password_save_option = password_save_option
        if password is not None:
            self.password = password
        if diagram_master_setting is not None:
            self.diagram_master_setting = diagram_master_setting
        if original_size is not None:
            self.original_size = original_size
        if header_footers_comparison is not None:
            self.header_footers_comparison = header_footers_comparison
        if paper_size is not None:
            self.paper_size = paper_size
        if sensitivity_of_comparison is not None:
            self.sensitivity_of_comparison = sensitivity_of_comparison
    
    @property
    def generate_summary_page(self):
        """
        Gets the generate_summary_page.  # noqa: E501

        Indicates whether to add summary page to resultant document or not  # noqa: E501

        :return: The generate_summary_page.  # noqa: E501
        :rtype: bool
        """
        return self._generate_summary_page

    @generate_summary_page.setter
    def generate_summary_page(self, generate_summary_page):
        """
        Sets the generate_summary_page.

        Indicates whether to add summary page to resultant document or not  # noqa: E501

        :param generate_summary_page: The generate_summary_page.  # noqa: E501
        :type: bool
        """
        if generate_summary_page is None:
            raise ValueError("Invalid value for `generate_summary_page`, must not be `None`")  # noqa: E501
        self._generate_summary_page = generate_summary_page
    
    @property
    def show_deleted_content(self):
        """
        Gets the show_deleted_content.  # noqa: E501

        Indicates whether to show deleted components in resultant document or not  # noqa: E501

        :return: The show_deleted_content.  # noqa: E501
        :rtype: bool
        """
        return self._show_deleted_content

    @show_deleted_content.setter
    def show_deleted_content(self, show_deleted_content):
        """
        Sets the show_deleted_content.

        Indicates whether to show deleted components in resultant document or not  # noqa: E501

        :param show_deleted_content: The show_deleted_content.  # noqa: E501
        :type: bool
        """
        if show_deleted_content is None:
            raise ValueError("Invalid value for `show_deleted_content`, must not be `None`")  # noqa: E501
        self._show_deleted_content = show_deleted_content
    
    @property
    def show_inserted_content(self):
        """
        Gets the show_inserted_content.  # noqa: E501

        Indicates whether to show inserted components in resultant document or not  # noqa: E501

        :return: The show_inserted_content.  # noqa: E501
        :rtype: bool
        """
        return self._show_inserted_content

    @show_inserted_content.setter
    def show_inserted_content(self, show_inserted_content):
        """
        Sets the show_inserted_content.

        Indicates whether to show inserted components in resultant document or not  # noqa: E501

        :param show_inserted_content: The show_inserted_content.  # noqa: E501
        :type: bool
        """
        if show_inserted_content is None:
            raise ValueError("Invalid value for `show_inserted_content`, must not be `None`")  # noqa: E501
        self._show_inserted_content = show_inserted_content
    
    @property
    def style_change_detection(self):
        """
        Gets the style_change_detection.  # noqa: E501

        Indicates whether to detect style changes or not  # noqa: E501

        :return: The style_change_detection.  # noqa: E501
        :rtype: bool
        """
        return self._style_change_detection

    @style_change_detection.setter
    def style_change_detection(self, style_change_detection):
        """
        Sets the style_change_detection.

        Indicates whether to detect style changes or not  # noqa: E501

        :param style_change_detection: The style_change_detection.  # noqa: E501
        :type: bool
        """
        if style_change_detection is None:
            raise ValueError("Invalid value for `style_change_detection`, must not be `None`")  # noqa: E501
        self._style_change_detection = style_change_detection
    
    @property
    def inserted_items_style(self):
        """
        Gets the inserted_items_style.  # noqa: E501

        Style for inserted components  # noqa: E501

        :return: The inserted_items_style.  # noqa: E501
        :rtype: ItemsStyle
        """
        return self._inserted_items_style

    @inserted_items_style.setter
    def inserted_items_style(self, inserted_items_style):
        """
        Sets the inserted_items_style.

        Style for inserted components  # noqa: E501

        :param inserted_items_style: The inserted_items_style.  # noqa: E501
        :type: ItemsStyle
        """
        self._inserted_items_style = inserted_items_style
    
    @property
    def deleted_items_style(self):
        """
        Gets the deleted_items_style.  # noqa: E501

        Style for deleted components  # noqa: E501

        :return: The deleted_items_style.  # noqa: E501
        :rtype: ItemsStyle
        """
        return self._deleted_items_style

    @deleted_items_style.setter
    def deleted_items_style(self, deleted_items_style):
        """
        Sets the deleted_items_style.

        Style for deleted components  # noqa: E501

        :param deleted_items_style: The deleted_items_style.  # noqa: E501
        :type: ItemsStyle
        """
        self._deleted_items_style = deleted_items_style
    
    @property
    def changed_items_style(self):
        """
        Gets the changed_items_style.  # noqa: E501

        Style for components with changed style  # noqa: E501

        :return: The changed_items_style.  # noqa: E501
        :rtype: ItemsStyle
        """
        return self._changed_items_style

    @changed_items_style.setter
    def changed_items_style(self, changed_items_style):
        """
        Sets the changed_items_style.

        Style for components with changed style  # noqa: E501

        :param changed_items_style: The changed_items_style.  # noqa: E501
        :type: ItemsStyle
        """
        self._changed_items_style = changed_items_style
    
    @property
    def words_separator_chars(self):
        """
        Gets the words_separator_chars.  # noqa: E501

        An array of delimiters to split text into words  # noqa: E501

        :return: The words_separator_chars.  # noqa: E501
        :rtype: list[str]
        """
        return self._words_separator_chars

    @words_separator_chars.setter
    def words_separator_chars(self, words_separator_chars):
        """
        Sets the words_separator_chars.

        An array of delimiters to split text into words  # noqa: E501

        :param words_separator_chars: The words_separator_chars.  # noqa: E501
        :type: list[str]
        """
        self._words_separator_chars = words_separator_chars
    
    @property
    def details_level(self):
        """
        Gets the details_level.  # noqa: E501

        Gets of sets the comparison details level   # noqa: E501

        :return: The details_level.  # noqa: E501
        :rtype: str
        """
        return self._details_level

    @details_level.setter
    def details_level(self, details_level):
        """
        Sets the details_level.

        Gets of sets the comparison details level   # noqa: E501

        :param details_level: The details_level.  # noqa: E501
        :type: str
        """
        if details_level is None:
            raise ValueError("Invalid value for `details_level`, must not be `None`")  # noqa: E501
        allowed_values = ["Low", "Middle", "High"]  # noqa: E501
        if not details_level.isdigit():	
            if details_level not in allowed_values:
                raise ValueError(
                    "Invalid value for `details_level` ({0}), must be one of {1}"  # noqa: E501
                    .format(details_level, allowed_values))
            self._details_level = details_level
        else:
            self._details_level = allowed_values[int(details_level) if six.PY3 else long(details_level)]
    
    @property
    def use_frames_for_del_ins_elements(self):
        """
        Gets the use_frames_for_del_ins_elements.  # noqa: E501

        Indicates whether to use frames for shapes in Word Processing and for rectangles in Image documents  # noqa: E501

        :return: The use_frames_for_del_ins_elements.  # noqa: E501
        :rtype: bool
        """
        return self._use_frames_for_del_ins_elements

    @use_frames_for_del_ins_elements.setter
    def use_frames_for_del_ins_elements(self, use_frames_for_del_ins_elements):
        """
        Sets the use_frames_for_del_ins_elements.

        Indicates whether to use frames for shapes in Word Processing and for rectangles in Image documents  # noqa: E501

        :param use_frames_for_del_ins_elements: The use_frames_for_del_ins_elements.  # noqa: E501
        :type: bool
        """
        if use_frames_for_del_ins_elements is None:
            raise ValueError("Invalid value for `use_frames_for_del_ins_elements`, must not be `None`")  # noqa: E501
        self._use_frames_for_del_ins_elements = use_frames_for_del_ins_elements
    
    @property
    def calculate_component_coordinates(self):
        """
        Gets the calculate_component_coordinates.  # noqa: E501

        Indicates whether to calculate coordinates for changed components  # noqa: E501

        :return: The calculate_component_coordinates.  # noqa: E501
        :rtype: bool
        """
        return self._calculate_component_coordinates

    @calculate_component_coordinates.setter
    def calculate_component_coordinates(self, calculate_component_coordinates):
        """
        Sets the calculate_component_coordinates.

        Indicates whether to calculate coordinates for changed components  # noqa: E501

        :param calculate_component_coordinates: The calculate_component_coordinates.  # noqa: E501
        :type: bool
        """
        if calculate_component_coordinates is None:
            raise ValueError("Invalid value for `calculate_component_coordinates`, must not be `None`")  # noqa: E501
        self._calculate_component_coordinates = calculate_component_coordinates
    
    @property
    def mark_changed_content(self):
        """
        Gets the mark_changed_content.  # noqa: E501

        Indicates whether to use frames for shapes in Word Processing and for rectangles in Image documents  # noqa: E501

        :return: The mark_changed_content.  # noqa: E501
        :rtype: bool
        """
        return self._mark_changed_content

    @mark_changed_content.setter
    def mark_changed_content(self, mark_changed_content):
        """
        Sets the mark_changed_content.

        Indicates whether to use frames for shapes in Word Processing and for rectangles in Image documents  # noqa: E501

        :param mark_changed_content: The mark_changed_content.  # noqa: E501
        :type: bool
        """
        if mark_changed_content is None:
            raise ValueError("Invalid value for `mark_changed_content`, must not be `None`")  # noqa: E501
        self._mark_changed_content = mark_changed_content
    
    @property
    def mark_nested_content(self):
        """
        Gets the mark_nested_content.  # noqa: E501

        Gets or sets a value indicating whether to mark the children of the deleted or inserted element as deleted or inserted  # noqa: E501

        :return: The mark_nested_content.  # noqa: E501
        :rtype: bool
        """
        return self._mark_nested_content

    @mark_nested_content.setter
    def mark_nested_content(self, mark_nested_content):
        """
        Sets the mark_nested_content.

        Gets or sets a value indicating whether to mark the children of the deleted or inserted element as deleted or inserted  # noqa: E501

        :param mark_nested_content: The mark_nested_content.  # noqa: E501
        :type: bool
        """
        if mark_nested_content is None:
            raise ValueError("Invalid value for `mark_nested_content`, must not be `None`")  # noqa: E501
        self._mark_nested_content = mark_nested_content
    
    @property
    def clone_metadata(self):
        """
        Gets the clone_metadata.  # noqa: E501

        Gets or sets type of metadata to clone  # noqa: E501

        :return: The clone_metadata.  # noqa: E501
        :rtype: str
        """
        return self._clone_metadata

    @clone_metadata.setter
    def clone_metadata(self, clone_metadata):
        """
        Sets the clone_metadata.

        Gets or sets type of metadata to clone  # noqa: E501

        :param clone_metadata: The clone_metadata.  # noqa: E501
        :type: str
        """
        if clone_metadata is None:
            raise ValueError("Invalid value for `clone_metadata`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "Source", "Target", "FileAuthor"]  # noqa: E501
        if not clone_metadata.isdigit():	
            if clone_metadata not in allowed_values:
                raise ValueError(
                    "Invalid value for `clone_metadata` ({0}), must be one of {1}"  # noqa: E501
                    .format(clone_metadata, allowed_values))
            self._clone_metadata = clone_metadata
        else:
            self._clone_metadata = allowed_values[int(clone_metadata) if six.PY3 else long(clone_metadata)]
    
    @property
    def meta_data(self):
        """
        Gets the meta_data.  # noqa: E501

        Gets or sets user metadata  # noqa: E501

        :return: The meta_data.  # noqa: E501
        :rtype: Metadata
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """
        Sets the meta_data.

        Gets or sets user metadata  # noqa: E501

        :param meta_data: The meta_data.  # noqa: E501
        :type: Metadata
        """
        self._meta_data = meta_data
    
    @property
    def password_save_option(self):
        """
        Gets the password_save_option.  # noqa: E501

        Gets or sets type of password saving  # noqa: E501

        :return: The password_save_option.  # noqa: E501
        :rtype: str
        """
        return self._password_save_option

    @password_save_option.setter
    def password_save_option(self, password_save_option):
        """
        Sets the password_save_option.

        Gets or sets type of password saving  # noqa: E501

        :param password_save_option: The password_save_option.  # noqa: E501
        :type: str
        """
        if password_save_option is None:
            raise ValueError("Invalid value for `password_save_option`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Source", "Target", "User"]  # noqa: E501
        if not password_save_option.isdigit():	
            if password_save_option not in allowed_values:
                raise ValueError(
                    "Invalid value for `password_save_option` ({0}), must be one of {1}"  # noqa: E501
                    .format(password_save_option, allowed_values))
            self._password_save_option = password_save_option
        else:
            self._password_save_option = allowed_values[int(password_save_option) if six.PY3 else long(password_save_option)]
    
    @property
    def password(self):
        """
        Gets the password.  # noqa: E501

        Gets or sets user password to resultant document  # noqa: E501

        :return: The password.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password.

        Gets or sets user password to resultant document  # noqa: E501

        :param password: The password.  # noqa: E501
        :type: str
        """
        self._password = password
    
    @property
    def diagram_master_setting(self):
        """
        Gets the diagram_master_setting.  # noqa: E501

        Gets or sets master for Diagram document  # noqa: E501

        :return: The diagram_master_setting.  # noqa: E501
        :rtype: DiagramMasterSetting
        """
        return self._diagram_master_setting

    @diagram_master_setting.setter
    def diagram_master_setting(self, diagram_master_setting):
        """
        Sets the diagram_master_setting.

        Gets or sets master for Diagram document  # noqa: E501

        :param diagram_master_setting: The diagram_master_setting.  # noqa: E501
        :type: DiagramMasterSetting
        """
        self._diagram_master_setting = diagram_master_setting
    
    @property
    def original_size(self):
        """
        Gets the original_size.  # noqa: E501

        Gets or sets original document size when picture is compared with other different formats  # noqa: E501

        :return: The original_size.  # noqa: E501
        :rtype: Size
        """
        return self._original_size

    @original_size.setter
    def original_size(self, original_size):
        """
        Sets the original_size.

        Gets or sets original document size when picture is compared with other different formats  # noqa: E501

        :param original_size: The original_size.  # noqa: E501
        :type: Size
        """
        self._original_size = original_size
    
    @property
    def header_footers_comparison(self):
        """
        Gets the header_footers_comparison.  # noqa: E501

        Control to turn on comparison of header/footer contents  # noqa: E501

        :return: The header_footers_comparison.  # noqa: E501
        :rtype: bool
        """
        return self._header_footers_comparison

    @header_footers_comparison.setter
    def header_footers_comparison(self, header_footers_comparison):
        """
        Sets the header_footers_comparison.

        Control to turn on comparison of header/footer contents  # noqa: E501

        :param header_footers_comparison: The header_footers_comparison.  # noqa: E501
        :type: bool
        """
        if header_footers_comparison is None:
            raise ValueError("Invalid value for `header_footers_comparison`, must not be `None`")  # noqa: E501
        self._header_footers_comparison = header_footers_comparison
    
    @property
    def paper_size(self):
        """
        Gets the paper_size.  # noqa: E501

        Gets or sets the result document paper size  # noqa: E501

        :return: The paper_size.  # noqa: E501
        :rtype: str
        """
        return self._paper_size

    @paper_size.setter
    def paper_size(self, paper_size):
        """
        Sets the paper_size.

        Gets or sets the result document paper size  # noqa: E501

        :param paper_size: The paper_size.  # noqa: E501
        :type: str
        """
        if paper_size is None:
            raise ValueError("Invalid value for `paper_size`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]  # noqa: E501
        if not paper_size.isdigit():	
            if paper_size not in allowed_values:
                raise ValueError(
                    "Invalid value for `paper_size` ({0}), must be one of {1}"  # noqa: E501
                    .format(paper_size, allowed_values))
            self._paper_size = paper_size
        else:
            self._paper_size = allowed_values[int(paper_size) if six.PY3 else long(paper_size)]
    
    @property
    def sensitivity_of_comparison(self):
        """
        Gets the sensitivity_of_comparison.  # noqa: E501

        Gets or sets a sensitivity of comparison. Default is 75  # noqa: E501

        :return: The sensitivity_of_comparison.  # noqa: E501
        :rtype: int
        """
        return self._sensitivity_of_comparison

    @sensitivity_of_comparison.setter
    def sensitivity_of_comparison(self, sensitivity_of_comparison):
        """
        Sets the sensitivity_of_comparison.

        Gets or sets a sensitivity of comparison. Default is 75  # noqa: E501

        :param sensitivity_of_comparison: The sensitivity_of_comparison.  # noqa: E501
        :type: int
        """
        if sensitivity_of_comparison is None:
            raise ValueError("Invalid value for `sensitivity_of_comparison`, must not be `None`")  # noqa: E501
        self._sensitivity_of_comparison = sensitivity_of_comparison

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
        if not isinstance(other, Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
