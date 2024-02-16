# coding: utf-8

"""
    CRM Associations Schema

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.associations.v4.schema.configuration import Configuration


class PublicAssociationDefinitionUpdateRequest(object):
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
    openapi_types = {"inverse_label": "str", "association_type_id": "int", "label": "str"}

    attribute_map = {"inverse_label": "inverseLabel", "association_type_id": "associationTypeId", "label": "label"}

    def __init__(self, inverse_label=None, association_type_id=None, label=None, local_vars_configuration=None):  # noqa: E501
        """PublicAssociationDefinitionUpdateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._inverse_label = None
        self._association_type_id = None
        self._label = None
        self.discriminator = None

        if inverse_label is not None:
            self.inverse_label = inverse_label
        self.association_type_id = association_type_id
        self.label = label

    @property
    def inverse_label(self):
        """Gets the inverse_label of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501


        :return: The inverse_label of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._inverse_label

    @inverse_label.setter
    def inverse_label(self, inverse_label):
        """Sets the inverse_label of this PublicAssociationDefinitionUpdateRequest.


        :param inverse_label: The inverse_label of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501
        :type inverse_label: str
        """

        self._inverse_label = inverse_label

    @property
    def association_type_id(self):
        """Gets the association_type_id of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501


        :return: The association_type_id of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._association_type_id

    @association_type_id.setter
    def association_type_id(self, association_type_id):
        """Sets the association_type_id of this PublicAssociationDefinitionUpdateRequest.


        :param association_type_id: The association_type_id of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501
        :type association_type_id: int
        """
        if self.local_vars_configuration.client_side_validation and association_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `association_type_id`, must not be `None`")  # noqa: E501

        self._association_type_id = association_type_id

    @property
    def label(self):
        """Gets the label of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501


        :return: The label of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PublicAssociationDefinitionUpdateRequest.


        :param label: The label of this PublicAssociationDefinitionUpdateRequest.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

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
        if not isinstance(other, PublicAssociationDefinitionUpdateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAssociationDefinitionUpdateRequest):
            return True

        return self.to_dict() != other.to_dict()
