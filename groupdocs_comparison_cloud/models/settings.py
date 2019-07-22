# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="Settings.py">
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
        'style_change_detection': 'bool',
        'inserted_items_style': 'ItemsStyle',
        'deleted_items_style': 'ItemsStyle',
        'style_changed_items_style': 'ItemsStyle',
        'words_separator_chars': 'list[str]',
        'detail_level': 'str',
        'use_frames_for_del_ins_elements': 'bool',
        'calculate_component_coordinates': 'bool',
        'mark_deleted_inserted_content_deep': 'bool',
        'clone_metadata': 'str',
        'meta_data': 'Metadata',
        'password_save_option': 'str',
        'password': 'str',
        'diagram_master_setting': 'DiagramMasterSetting',
        'original_size': 'OriginalSize'
    }

    attribute_map = {
        'generate_summary_page': 'GenerateSummaryPage',
        'show_deleted_content': 'ShowDeletedContent',
        'style_change_detection': 'StyleChangeDetection',
        'inserted_items_style': 'InsertedItemsStyle',
        'deleted_items_style': 'DeletedItemsStyle',
        'style_changed_items_style': 'StyleChangedItemsStyle',
        'words_separator_chars': 'WordsSeparatorChars',
        'detail_level': 'DetailLevel',
        'use_frames_for_del_ins_elements': 'UseFramesForDelInsElements',
        'calculate_component_coordinates': 'CalculateComponentCoordinates',
        'mark_deleted_inserted_content_deep': 'MarkDeletedInsertedContentDeep',
        'clone_metadata': 'CloneMetadata',
        'meta_data': 'MetaData',
        'password_save_option': 'PasswordSaveOption',
        'password': 'Password',
        'diagram_master_setting': 'DiagramMasterSetting',
        'original_size': 'OriginalSize'
    }

    def __init__(self, generate_summary_page=None, show_deleted_content=None, style_change_detection=None, inserted_items_style=None, deleted_items_style=None, style_changed_items_style=None, words_separator_chars=None, detail_level=None, use_frames_for_del_ins_elements=None, calculate_component_coordinates=None, mark_deleted_inserted_content_deep=None, clone_metadata=None, meta_data=None, password_save_option=None, password=None, diagram_master_setting=None, original_size=None, **kwargs):  # noqa: E501
        """Initializes new instance of Settings"""  # noqa: E501

        self._generate_summary_page = None
        self._show_deleted_content = None
        self._style_change_detection = None
        self._inserted_items_style = None
        self._deleted_items_style = None
        self._style_changed_items_style = None
        self._words_separator_chars = None
        self._detail_level = None
        self._use_frames_for_del_ins_elements = None
        self._calculate_component_coordinates = None
        self._mark_deleted_inserted_content_deep = None
        self._clone_metadata = None
        self._meta_data = None
        self._password_save_option = None
        self._password = None
        self._diagram_master_setting = None
        self._original_size = None

        if generate_summary_page is not None:
            self.generate_summary_page = generate_summary_page
        if show_deleted_content is not None:
            self.show_deleted_content = show_deleted_content
        if style_change_detection is not None:
            self.style_change_detection = style_change_detection
        if inserted_items_style is not None:
            self.inserted_items_style = inserted_items_style
        if deleted_items_style is not None:
            self.deleted_items_style = deleted_items_style
        if style_changed_items_style is not None:
            self.style_changed_items_style = style_changed_items_style
        if words_separator_chars is not None:
            self.words_separator_chars = words_separator_chars
        if detail_level is not None:
            self.detail_level = detail_level
        if use_frames_for_del_ins_elements is not None:
            self.use_frames_for_del_ins_elements = use_frames_for_del_ins_elements
        if calculate_component_coordinates is not None:
            self.calculate_component_coordinates = calculate_component_coordinates
        if mark_deleted_inserted_content_deep is not None:
            self.mark_deleted_inserted_content_deep = mark_deleted_inserted_content_deep
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
    def style_changed_items_style(self):
        """
        Gets the style_changed_items_style.  # noqa: E501

        Style for components with changed style  # noqa: E501

        :return: The style_changed_items_style.  # noqa: E501
        :rtype: ItemsStyle
        """
        return self._style_changed_items_style

    @style_changed_items_style.setter
    def style_changed_items_style(self, style_changed_items_style):
        """
        Sets the style_changed_items_style.

        Style for components with changed style  # noqa: E501

        :param style_changed_items_style: The style_changed_items_style.  # noqa: E501
        :type: ItemsStyle
        """
        self._style_changed_items_style = style_changed_items_style
    
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
    def detail_level(self):
        """
        Gets the detail_level.  # noqa: E501

        Gets of sets the comparison detalisation level   # noqa: E501

        :return: The detail_level.  # noqa: E501
        :rtype: str
        """
        return self._detail_level

    @detail_level.setter
    def detail_level(self, detail_level):
        """
        Sets the detail_level.

        Gets of sets the comparison detalisation level   # noqa: E501

        :param detail_level: The detail_level.  # noqa: E501
        :type: str
        """
        self._detail_level = detail_level
    
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
    def mark_deleted_inserted_content_deep(self):
        """
        Gets the mark_deleted_inserted_content_deep.  # noqa: E501

        Indicates whether to accept inserted/deleted styles for all children of inserted/deleted components  # noqa: E501

        :return: The mark_deleted_inserted_content_deep.  # noqa: E501
        :rtype: bool
        """
        return self._mark_deleted_inserted_content_deep

    @mark_deleted_inserted_content_deep.setter
    def mark_deleted_inserted_content_deep(self, mark_deleted_inserted_content_deep):
        """
        Sets the mark_deleted_inserted_content_deep.

        Indicates whether to accept inserted/deleted styles for all children of inserted/deleted components  # noqa: E501

        :param mark_deleted_inserted_content_deep: The mark_deleted_inserted_content_deep.  # noqa: E501
        :type: bool
        """
        if mark_deleted_inserted_content_deep is None:
            raise ValueError("Invalid value for `mark_deleted_inserted_content_deep`, must not be `None`")  # noqa: E501
        self._mark_deleted_inserted_content_deep = mark_deleted_inserted_content_deep
    
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
        self._clone_metadata = clone_metadata
    
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
        self._password_save_option = password_save_option
    
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
        :rtype: OriginalSize
        """
        return self._original_size

    @original_size.setter
    def original_size(self, original_size):
        """
        Sets the original_size.

        Gets or sets original document size when picture is compared with other different formats  # noqa: E501

        :param original_size: The original_size.  # noqa: E501
        :type: OriginalSize
        """
        self._original_size = original_size

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
