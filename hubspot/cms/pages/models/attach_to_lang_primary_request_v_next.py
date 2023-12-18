# coding: utf-8

"""
    Pages

    Use these endpoints for interacting with Landing Pages and Site Pages  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.cms.pages.configuration import Configuration


class AttachToLangPrimaryRequestVNext(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"language": "str", "id": "str", "primary_id": "str", "primary_language": "str"}

    attribute_map = {"language": "language", "id": "id", "primary_id": "primaryId", "primary_language": "primaryLanguage"}

    def __init__(self, language=None, id=None, primary_id=None, primary_language=None, local_vars_configuration=None):  # noqa: E501
        """AttachToLangPrimaryRequestVNext - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._language = None
        self._id = None
        self._primary_id = None
        self._primary_language = None
        self.discriminator = None

        self.language = language
        self.id = id
        self.primary_id = primary_id
        if primary_language is not None:
            self.primary_language = primary_language

    @property
    def language(self):
        """Gets the language of this AttachToLangPrimaryRequestVNext.  # noqa: E501

        Designated language of the object to add to a multi-language group.  # noqa: E501

        :return: The language of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AttachToLangPrimaryRequestVNext.

        Designated language of the object to add to a multi-language group.  # noqa: E501

        :param language: The language of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :type language: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def id(self):
        """Gets the id of this AttachToLangPrimaryRequestVNext.  # noqa: E501

        ID of the object to add to a multi-language group.  # noqa: E501

        :return: The id of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachToLangPrimaryRequestVNext.

        ID of the object to add to a multi-language group.  # noqa: E501

        :param id: The id of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def primary_id(self):
        """Gets the primary_id of this AttachToLangPrimaryRequestVNext.  # noqa: E501

        ID of primary language object in multi-language group.  # noqa: E501

        :return: The primary_id of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :rtype: str
        """
        return self._primary_id

    @primary_id.setter
    def primary_id(self, primary_id):
        """Sets the primary_id of this AttachToLangPrimaryRequestVNext.

        ID of primary language object in multi-language group.  # noqa: E501

        :param primary_id: The primary_id of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :type primary_id: str
        """
        if self.local_vars_configuration.client_side_validation and primary_id is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_id`, must not be `None`")  # noqa: E501

        self._primary_id = primary_id

    @property
    def primary_language(self):
        """Gets the primary_language of this AttachToLangPrimaryRequestVNext.  # noqa: E501

        Primary language of the multi-language group.  # noqa: E501

        :return: The primary_language of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :rtype: str
        """
        return self._primary_language

    @primary_language.setter
    def primary_language(self, primary_language):
        """Sets the primary_language of this AttachToLangPrimaryRequestVNext.

        Primary language of the multi-language group.  # noqa: E501

        :param primary_language: The primary_language of this AttachToLangPrimaryRequestVNext.  # noqa: E501
        :type primary_language: str
        """

        self._primary_language = primary_language

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AttachToLangPrimaryRequestVNext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachToLangPrimaryRequestVNext):
            return True

        return self.to_dict() != other.to_dict()
