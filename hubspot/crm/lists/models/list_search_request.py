# coding: utf-8

"""
    Lists

    CRUD operations to manage lists and list memberships  # noqa: E501

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

from hubspot.crm.lists.configuration import Configuration


class ListSearchRequest(object):
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
    openapi_types = {"offset": "int", "query": "str", "count": "int", "additional_properties": "list[str]"}

    attribute_map = {"offset": "offset", "query": "query", "count": "count", "additional_properties": "additionalProperties"}

    def __init__(self, offset=None, query=None, count=None, additional_properties=None, local_vars_configuration=None):  # noqa: E501
        """ListSearchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._offset = None
        self._query = None
        self._count = None
        self._additional_properties = None
        self.discriminator = None

        self.offset = offset
        if query is not None:
            self.query = query
        if count is not None:
            self.count = count
        self.additional_properties = additional_properties

    @property
    def offset(self):
        """Gets the offset of this ListSearchRequest.  # noqa: E501

        Value used to paginate through lists. The `offset` provided in the response can be used in the next request to fetch the next page of results. Defaults to `0` if no offset is provided.  # noqa: E501

        :return: The offset of this ListSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSearchRequest.

        Value used to paginate through lists. The `offset` provided in the response can be used in the next request to fetch the next page of results. Defaults to `0` if no offset is provided.  # noqa: E501

        :param offset: The offset of this ListSearchRequest.  # noqa: E501
        :type offset: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def query(self):
        """Gets the query of this ListSearchRequest.  # noqa: E501

        The `query` that will be used to search for lists by list name. If no `query` is provided, then the results will include all lists.  # noqa: E501

        :return: The query of this ListSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ListSearchRequest.

        The `query` that will be used to search for lists by list name. If no `query` is provided, then the results will include all lists.  # noqa: E501

        :param query: The query of this ListSearchRequest.  # noqa: E501
        :type query: str
        """

        self._query = query

    @property
    def count(self):
        """Gets the count of this ListSearchRequest.  # noqa: E501

        The number of lists to include in the response. Defaults to `20` if no value is provided. The max `count` is `500`.  # noqa: E501

        :return: The count of this ListSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSearchRequest.

        The number of lists to include in the response. Defaults to `20` if no value is provided. The max `count` is `500`.  # noqa: E501

        :param count: The count of this ListSearchRequest.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def additional_properties(self):
        """Gets the additional_properties of this ListSearchRequest.  # noqa: E501

        The property names of any additional list properties to include in the response. Properties that do not exist or that are empty for a particular list are not included in the response.  By default, all requests will fetch the following properties for each list: `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`, `hs_folder_name`, and `hs_list_reference_count`.  # noqa: E501

        :return: The additional_properties of this ListSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """Sets the additional_properties of this ListSearchRequest.

        The property names of any additional list properties to include in the response. Properties that do not exist or that are empty for a particular list are not included in the response.  By default, all requests will fetch the following properties for each list: `hs_list_size`, `hs_last_record_added_at`, `hs_last_record_removed_at`, `hs_folder_name`, and `hs_list_reference_count`.  # noqa: E501

        :param additional_properties: The additional_properties of this ListSearchRequest.  # noqa: E501
        :type additional_properties: list[str]
        """
        if self.local_vars_configuration.client_side_validation and additional_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `additional_properties`, must not be `None`")  # noqa: E501

        self._additional_properties = additional_properties

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
        if not isinstance(other, ListSearchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListSearchRequest):
            return True

        return self.to_dict() != other.to_dict()
