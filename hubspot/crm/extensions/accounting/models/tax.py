# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class Tax(object):
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
    openapi_types = {
        'code': 'str',
        'percentage': 'float',
        'name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'percentage': 'percentage',
        'name': 'name'
    }

    def __init__(self, code=None, percentage=None, name=None, local_vars_configuration=None):  # noqa: E501
        """Tax - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._percentage = None
        self._name = None
        self.discriminator = None

        self.code = code
        self.percentage = percentage
        self.name = name

    @property
    def code(self):
        """Gets the code of this Tax.  # noqa: E501

        The code/ID of the tax in the external accounting system.  # noqa: E501

        :return: The code of this Tax.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Tax.

        The code/ID of the tax in the external accounting system.  # noqa: E501

        :param code: The code of this Tax.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def percentage(self):
        """Gets the percentage of this Tax.  # noqa: E501

        The tax percentage.  For example, 8.05 represents a 8.05% tax rate.  # noqa: E501

        :return: The percentage of this Tax.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Tax.

        The tax percentage.  For example, 8.05 represents a 8.05% tax rate.  # noqa: E501

        :param percentage: The percentage of this Tax.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and percentage is None:  # noqa: E501
            raise ValueError("Invalid value for `percentage`, must not be `None`")  # noqa: E501

        self._percentage = percentage

    @property
    def name(self):
        """Gets the name of this Tax.  # noqa: E501

        The display name of the tax.  # noqa: E501

        :return: The name of this Tax.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tax.

        The display name of the tax.  # noqa: E501

        :param name: The name of this Tax.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Tax):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tax):
            return True

        return self.to_dict() != other.to_dict()
