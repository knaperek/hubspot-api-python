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


class PublicSurveyMonkeyValueFilter(object):
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
        "filter_type": "str",
        "survey_id": "str",
        "survey_question": "str",
        "survey_answer_row_id": "str",
        "survey_answer_col_id": "str",
        "value_comparison": "PublicPropertyFilterOperation",
        "operator": "str",
    }

    attribute_map = {
        "filter_type": "filterType",
        "survey_id": "surveyId",
        "survey_question": "surveyQuestion",
        "survey_answer_row_id": "surveyAnswerRowId",
        "survey_answer_col_id": "surveyAnswerColId",
        "value_comparison": "valueComparison",
        "operator": "operator",
    }

    def __init__(
        self,
        filter_type="SURVEY_MONKEY_VALUE",
        survey_id=None,
        survey_question=None,
        survey_answer_row_id=None,
        survey_answer_col_id=None,
        value_comparison=None,
        operator=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicSurveyMonkeyValueFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_type = None
        self._survey_id = None
        self._survey_question = None
        self._survey_answer_row_id = None
        self._survey_answer_col_id = None
        self._value_comparison = None
        self._operator = None
        self.discriminator = None

        self.filter_type = filter_type
        self.survey_id = survey_id
        self.survey_question = survey_question
        if survey_answer_row_id is not None:
            self.survey_answer_row_id = survey_answer_row_id
        if survey_answer_col_id is not None:
            self.survey_answer_col_id = survey_answer_col_id
        self.value_comparison = value_comparison
        self.operator = operator

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicSurveyMonkeyValueFilter.  # noqa: E501


        :return: The filter_type of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicSurveyMonkeyValueFilter.


        :param filter_type: The filter_type of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SURVEY_MONKEY_VALUE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

    @property
    def survey_id(self):
        """Gets the survey_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501


        :return: The survey_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :rtype: str
        """
        return self._survey_id

    @survey_id.setter
    def survey_id(self, survey_id):
        """Sets the survey_id of this PublicSurveyMonkeyValueFilter.


        :param survey_id: The survey_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :type survey_id: str
        """
        if self.local_vars_configuration.client_side_validation and survey_id is None:  # noqa: E501
            raise ValueError("Invalid value for `survey_id`, must not be `None`")  # noqa: E501

        self._survey_id = survey_id

    @property
    def survey_question(self):
        """Gets the survey_question of this PublicSurveyMonkeyValueFilter.  # noqa: E501


        :return: The survey_question of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :rtype: str
        """
        return self._survey_question

    @survey_question.setter
    def survey_question(self, survey_question):
        """Sets the survey_question of this PublicSurveyMonkeyValueFilter.


        :param survey_question: The survey_question of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :type survey_question: str
        """
        if self.local_vars_configuration.client_side_validation and survey_question is None:  # noqa: E501
            raise ValueError("Invalid value for `survey_question`, must not be `None`")  # noqa: E501

        self._survey_question = survey_question

    @property
    def survey_answer_row_id(self):
        """Gets the survey_answer_row_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501


        :return: The survey_answer_row_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :rtype: str
        """
        return self._survey_answer_row_id

    @survey_answer_row_id.setter
    def survey_answer_row_id(self, survey_answer_row_id):
        """Sets the survey_answer_row_id of this PublicSurveyMonkeyValueFilter.


        :param survey_answer_row_id: The survey_answer_row_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :type survey_answer_row_id: str
        """

        self._survey_answer_row_id = survey_answer_row_id

    @property
    def survey_answer_col_id(self):
        """Gets the survey_answer_col_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501


        :return: The survey_answer_col_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :rtype: str
        """
        return self._survey_answer_col_id

    @survey_answer_col_id.setter
    def survey_answer_col_id(self, survey_answer_col_id):
        """Sets the survey_answer_col_id of this PublicSurveyMonkeyValueFilter.


        :param survey_answer_col_id: The survey_answer_col_id of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :type survey_answer_col_id: str
        """

        self._survey_answer_col_id = survey_answer_col_id

    @property
    def value_comparison(self):
        """Gets the value_comparison of this PublicSurveyMonkeyValueFilter.  # noqa: E501


        :return: The value_comparison of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :rtype: PublicPropertyFilterOperation
        """
        return self._value_comparison

    @value_comparison.setter
    def value_comparison(self, value_comparison):
        """Sets the value_comparison of this PublicSurveyMonkeyValueFilter.


        :param value_comparison: The value_comparison of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :type value_comparison: PublicPropertyFilterOperation
        """
        if self.local_vars_configuration.client_side_validation and value_comparison is None:  # noqa: E501
            raise ValueError("Invalid value for `value_comparison`, must not be `None`")  # noqa: E501

        self._value_comparison = value_comparison

    @property
    def operator(self):
        """Gets the operator of this PublicSurveyMonkeyValueFilter.  # noqa: E501


        :return: The operator of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicSurveyMonkeyValueFilter.


        :param operator: The operator of this PublicSurveyMonkeyValueFilter.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

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
        if not isinstance(other, PublicSurveyMonkeyValueFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicSurveyMonkeyValueFilter):
            return True

        return self.to_dict() != other.to_dict()
