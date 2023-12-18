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


class PublicPropertyFilterOperation(object):
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
        "operation_type": "str",
        "operator": "str",
        "include_objects_with_no_value_set": "bool",
        "value": "str",
        "requires_time_zone_conversion": "bool",
        "timestamp": "int",
        "upper_bound": "int",
        "lower_bound": "int",
        "comparison_property_name": "str",
        "default_comparison_value": "str",
        "number_of_days": "int",
        "values": "list[str]",
        "year": "int",
        "month": "str",
        "day": "int",
        "time_unit": "str",
        "fiscal_year_start": "str",
        "use_fiscal_year": "bool",
        "time_unit_count": "int",
        "time_point": "PublicTimePointOperationTimePoint",
        "endpoint_behavior": "str",
        "property_parser": "str",
        "type": "str",
        "lower_bound_endpoint_behavior": "str",
        "upper_bound_endpoint_behavior": "str",
        "lower_bound_time_point": "PublicTimePointOperationTimePoint",
        "upper_bound_time_point": "PublicTimePointOperationTimePoint",
    }

    attribute_map = {
        "operation_type": "operationType",
        "operator": "operator",
        "include_objects_with_no_value_set": "includeObjectsWithNoValueSet",
        "value": "value",
        "requires_time_zone_conversion": "requiresTimeZoneConversion",
        "timestamp": "timestamp",
        "upper_bound": "upperBound",
        "lower_bound": "lowerBound",
        "comparison_property_name": "comparisonPropertyName",
        "default_comparison_value": "defaultComparisonValue",
        "number_of_days": "numberOfDays",
        "values": "values",
        "year": "year",
        "month": "month",
        "day": "day",
        "time_unit": "timeUnit",
        "fiscal_year_start": "fiscalYearStart",
        "use_fiscal_year": "useFiscalYear",
        "time_unit_count": "timeUnitCount",
        "time_point": "timePoint",
        "endpoint_behavior": "endpointBehavior",
        "property_parser": "propertyParser",
        "type": "type",
        "lower_bound_endpoint_behavior": "lowerBoundEndpointBehavior",
        "upper_bound_endpoint_behavior": "upperBoundEndpointBehavior",
        "lower_bound_time_point": "lowerBoundTimePoint",
        "upper_bound_time_point": "upperBoundTimePoint",
    }

    def __init__(
        self,
        operation_type=None,
        operator=None,
        include_objects_with_no_value_set=None,
        value=None,
        requires_time_zone_conversion=None,
        timestamp=None,
        upper_bound=None,
        lower_bound=None,
        comparison_property_name=None,
        default_comparison_value=None,
        number_of_days=None,
        values=None,
        year=None,
        month=None,
        day=None,
        time_unit=None,
        fiscal_year_start=None,
        use_fiscal_year=None,
        time_unit_count=None,
        time_point=None,
        endpoint_behavior=None,
        property_parser=None,
        type="TIME_RANGED",
        lower_bound_endpoint_behavior=None,
        upper_bound_endpoint_behavior=None,
        lower_bound_time_point=None,
        upper_bound_time_point=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicPropertyFilterOperation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._operation_type = None
        self._operator = None
        self._include_objects_with_no_value_set = None
        self._value = None
        self._requires_time_zone_conversion = None
        self._timestamp = None
        self._upper_bound = None
        self._lower_bound = None
        self._comparison_property_name = None
        self._default_comparison_value = None
        self._number_of_days = None
        self._values = None
        self._year = None
        self._month = None
        self._day = None
        self._time_unit = None
        self._fiscal_year_start = None
        self._use_fiscal_year = None
        self._time_unit_count = None
        self._time_point = None
        self._endpoint_behavior = None
        self._property_parser = None
        self._type = None
        self._lower_bound_endpoint_behavior = None
        self._upper_bound_endpoint_behavior = None
        self._lower_bound_time_point = None
        self._upper_bound_time_point = None
        self.discriminator = None

        self.operation_type = operation_type
        self.operator = operator
        self.include_objects_with_no_value_set = include_objects_with_no_value_set
        self.value = value
        self.requires_time_zone_conversion = requires_time_zone_conversion
        self.timestamp = timestamp
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.comparison_property_name = comparison_property_name
        if default_comparison_value is not None:
            self.default_comparison_value = default_comparison_value
        self.number_of_days = number_of_days
        self.values = values
        self.year = year
        self.month = month
        self.day = day
        self.time_unit = time_unit
        if fiscal_year_start is not None:
            self.fiscal_year_start = fiscal_year_start
        if use_fiscal_year is not None:
            self.use_fiscal_year = use_fiscal_year
        if time_unit_count is not None:
            self.time_unit_count = time_unit_count
        self.time_point = time_point
        if endpoint_behavior is not None:
            self.endpoint_behavior = endpoint_behavior
        if property_parser is not None:
            self.property_parser = property_parser
        self.type = type
        if lower_bound_endpoint_behavior is not None:
            self.lower_bound_endpoint_behavior = lower_bound_endpoint_behavior
        if upper_bound_endpoint_behavior is not None:
            self.upper_bound_endpoint_behavior = upper_bound_endpoint_behavior
        self.lower_bound_time_point = lower_bound_time_point
        self.upper_bound_time_point = upper_bound_time_point

    @property
    def operation_type(self):
        """Gets the operation_type of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The operation_type of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this PublicPropertyFilterOperation.


        :param operation_type: The operation_type of this PublicPropertyFilterOperation.  # noqa: E501
        :type operation_type: str
        """
        if self.local_vars_configuration.client_side_validation and operation_type is None:  # noqa: E501
            raise ValueError("Invalid value for `operation_type`, must not be `None`")  # noqa: E501

        self._operation_type = operation_type

    @property
    def operator(self):
        """Gets the operator of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The operator of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicPropertyFilterOperation.


        :param operator: The operator of this PublicPropertyFilterOperation.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def include_objects_with_no_value_set(self):
        """Gets the include_objects_with_no_value_set of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The include_objects_with_no_value_set of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: bool
        """
        return self._include_objects_with_no_value_set

    @include_objects_with_no_value_set.setter
    def include_objects_with_no_value_set(self, include_objects_with_no_value_set):
        """Sets the include_objects_with_no_value_set of this PublicPropertyFilterOperation.


        :param include_objects_with_no_value_set: The include_objects_with_no_value_set of this PublicPropertyFilterOperation.  # noqa: E501
        :type include_objects_with_no_value_set: bool
        """
        if self.local_vars_configuration.client_side_validation and include_objects_with_no_value_set is None:  # noqa: E501
            raise ValueError("Invalid value for `include_objects_with_no_value_set`, must not be `None`")  # noqa: E501

        self._include_objects_with_no_value_set = include_objects_with_no_value_set

    @property
    def value(self):
        """Gets the value of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The value of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PublicPropertyFilterOperation.


        :param value: The value of this PublicPropertyFilterOperation.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def requires_time_zone_conversion(self):
        """Gets the requires_time_zone_conversion of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The requires_time_zone_conversion of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: bool
        """
        return self._requires_time_zone_conversion

    @requires_time_zone_conversion.setter
    def requires_time_zone_conversion(self, requires_time_zone_conversion):
        """Sets the requires_time_zone_conversion of this PublicPropertyFilterOperation.


        :param requires_time_zone_conversion: The requires_time_zone_conversion of this PublicPropertyFilterOperation.  # noqa: E501
        :type requires_time_zone_conversion: bool
        """
        if self.local_vars_configuration.client_side_validation and requires_time_zone_conversion is None:  # noqa: E501
            raise ValueError("Invalid value for `requires_time_zone_conversion`, must not be `None`")  # noqa: E501

        self._requires_time_zone_conversion = requires_time_zone_conversion

    @property
    def timestamp(self):
        """Gets the timestamp of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The timestamp of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PublicPropertyFilterOperation.


        :param timestamp: The timestamp of this PublicPropertyFilterOperation.  # noqa: E501
        :type timestamp: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def upper_bound(self):
        """Gets the upper_bound of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The upper_bound of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: int
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, upper_bound):
        """Sets the upper_bound of this PublicPropertyFilterOperation.


        :param upper_bound: The upper_bound of this PublicPropertyFilterOperation.  # noqa: E501
        :type upper_bound: int
        """
        if self.local_vars_configuration.client_side_validation and upper_bound is None:  # noqa: E501
            raise ValueError("Invalid value for `upper_bound`, must not be `None`")  # noqa: E501

        self._upper_bound = upper_bound

    @property
    def lower_bound(self):
        """Gets the lower_bound of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The lower_bound of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: int
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, lower_bound):
        """Sets the lower_bound of this PublicPropertyFilterOperation.


        :param lower_bound: The lower_bound of this PublicPropertyFilterOperation.  # noqa: E501
        :type lower_bound: int
        """
        if self.local_vars_configuration.client_side_validation and lower_bound is None:  # noqa: E501
            raise ValueError("Invalid value for `lower_bound`, must not be `None`")  # noqa: E501

        self._lower_bound = lower_bound

    @property
    def comparison_property_name(self):
        """Gets the comparison_property_name of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The comparison_property_name of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._comparison_property_name

    @comparison_property_name.setter
    def comparison_property_name(self, comparison_property_name):
        """Sets the comparison_property_name of this PublicPropertyFilterOperation.


        :param comparison_property_name: The comparison_property_name of this PublicPropertyFilterOperation.  # noqa: E501
        :type comparison_property_name: str
        """
        if self.local_vars_configuration.client_side_validation and comparison_property_name is None:  # noqa: E501
            raise ValueError("Invalid value for `comparison_property_name`, must not be `None`")  # noqa: E501

        self._comparison_property_name = comparison_property_name

    @property
    def default_comparison_value(self):
        """Gets the default_comparison_value of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The default_comparison_value of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._default_comparison_value

    @default_comparison_value.setter
    def default_comparison_value(self, default_comparison_value):
        """Sets the default_comparison_value of this PublicPropertyFilterOperation.


        :param default_comparison_value: The default_comparison_value of this PublicPropertyFilterOperation.  # noqa: E501
        :type default_comparison_value: str
        """

        self._default_comparison_value = default_comparison_value

    @property
    def number_of_days(self):
        """Gets the number_of_days of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The number_of_days of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: int
        """
        return self._number_of_days

    @number_of_days.setter
    def number_of_days(self, number_of_days):
        """Sets the number_of_days of this PublicPropertyFilterOperation.


        :param number_of_days: The number_of_days of this PublicPropertyFilterOperation.  # noqa: E501
        :type number_of_days: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_days is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_days`, must not be `None`")  # noqa: E501

        self._number_of_days = number_of_days

    @property
    def values(self):
        """Gets the values of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The values of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this PublicPropertyFilterOperation.


        :param values: The values of this PublicPropertyFilterOperation.  # noqa: E501
        :type values: list[str]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def year(self):
        """Gets the year of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The year of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this PublicPropertyFilterOperation.


        :param year: The year of this PublicPropertyFilterOperation.  # noqa: E501
        :type year: int
        """
        if self.local_vars_configuration.client_side_validation and year is None:  # noqa: E501
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def month(self):
        """Gets the month of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The month of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this PublicPropertyFilterOperation.


        :param month: The month of this PublicPropertyFilterOperation.  # noqa: E501
        :type month: str
        """
        if self.local_vars_configuration.client_side_validation and month is None:  # noqa: E501
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def day(self):
        """Gets the day of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The day of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this PublicPropertyFilterOperation.


        :param day: The day of this PublicPropertyFilterOperation.  # noqa: E501
        :type day: int
        """
        if self.local_vars_configuration.client_side_validation and day is None:  # noqa: E501
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    @property
    def time_unit(self):
        """Gets the time_unit of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The time_unit of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this PublicPropertyFilterOperation.


        :param time_unit: The time_unit of this PublicPropertyFilterOperation.  # noqa: E501
        :type time_unit: str
        """
        if self.local_vars_configuration.client_side_validation and time_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `time_unit`, must not be `None`")  # noqa: E501

        self._time_unit = time_unit

    @property
    def fiscal_year_start(self):
        """Gets the fiscal_year_start of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The fiscal_year_start of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_year_start

    @fiscal_year_start.setter
    def fiscal_year_start(self, fiscal_year_start):
        """Sets the fiscal_year_start of this PublicPropertyFilterOperation.


        :param fiscal_year_start: The fiscal_year_start of this PublicPropertyFilterOperation.  # noqa: E501
        :type fiscal_year_start: str
        """
        allowed_values = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fiscal_year_start not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `fiscal_year_start` ({0}), must be one of {1}".format(fiscal_year_start, allowed_values))  # noqa: E501

        self._fiscal_year_start = fiscal_year_start

    @property
    def use_fiscal_year(self):
        """Gets the use_fiscal_year of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The use_fiscal_year of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: bool
        """
        return self._use_fiscal_year

    @use_fiscal_year.setter
    def use_fiscal_year(self, use_fiscal_year):
        """Sets the use_fiscal_year of this PublicPropertyFilterOperation.


        :param use_fiscal_year: The use_fiscal_year of this PublicPropertyFilterOperation.  # noqa: E501
        :type use_fiscal_year: bool
        """

        self._use_fiscal_year = use_fiscal_year

    @property
    def time_unit_count(self):
        """Gets the time_unit_count of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The time_unit_count of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: int
        """
        return self._time_unit_count

    @time_unit_count.setter
    def time_unit_count(self, time_unit_count):
        """Sets the time_unit_count of this PublicPropertyFilterOperation.


        :param time_unit_count: The time_unit_count of this PublicPropertyFilterOperation.  # noqa: E501
        :type time_unit_count: int
        """

        self._time_unit_count = time_unit_count

    @property
    def time_point(self):
        """Gets the time_point of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The time_point of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: PublicTimePointOperationTimePoint
        """
        return self._time_point

    @time_point.setter
    def time_point(self, time_point):
        """Sets the time_point of this PublicPropertyFilterOperation.


        :param time_point: The time_point of this PublicPropertyFilterOperation.  # noqa: E501
        :type time_point: PublicTimePointOperationTimePoint
        """
        if self.local_vars_configuration.client_side_validation and time_point is None:  # noqa: E501
            raise ValueError("Invalid value for `time_point`, must not be `None`")  # noqa: E501

        self._time_point = time_point

    @property
    def endpoint_behavior(self):
        """Gets the endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_behavior

    @endpoint_behavior.setter
    def endpoint_behavior(self, endpoint_behavior):
        """Sets the endpoint_behavior of this PublicPropertyFilterOperation.


        :param endpoint_behavior: The endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501
        :type endpoint_behavior: str
        """

        self._endpoint_behavior = endpoint_behavior

    @property
    def property_parser(self):
        """Gets the property_parser of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The property_parser of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._property_parser

    @property_parser.setter
    def property_parser(self, property_parser):
        """Sets the property_parser of this PublicPropertyFilterOperation.


        :param property_parser: The property_parser of this PublicPropertyFilterOperation.  # noqa: E501
        :type property_parser: str
        """

        self._property_parser = property_parser

    @property
    def type(self):
        """Gets the type of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The type of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicPropertyFilterOperation.


        :param type: The type of this PublicPropertyFilterOperation.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["TIME_RANGED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def lower_bound_endpoint_behavior(self):
        """Gets the lower_bound_endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The lower_bound_endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._lower_bound_endpoint_behavior

    @lower_bound_endpoint_behavior.setter
    def lower_bound_endpoint_behavior(self, lower_bound_endpoint_behavior):
        """Sets the lower_bound_endpoint_behavior of this PublicPropertyFilterOperation.


        :param lower_bound_endpoint_behavior: The lower_bound_endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501
        :type lower_bound_endpoint_behavior: str
        """

        self._lower_bound_endpoint_behavior = lower_bound_endpoint_behavior

    @property
    def upper_bound_endpoint_behavior(self):
        """Gets the upper_bound_endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The upper_bound_endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: str
        """
        return self._upper_bound_endpoint_behavior

    @upper_bound_endpoint_behavior.setter
    def upper_bound_endpoint_behavior(self, upper_bound_endpoint_behavior):
        """Sets the upper_bound_endpoint_behavior of this PublicPropertyFilterOperation.


        :param upper_bound_endpoint_behavior: The upper_bound_endpoint_behavior of this PublicPropertyFilterOperation.  # noqa: E501
        :type upper_bound_endpoint_behavior: str
        """

        self._upper_bound_endpoint_behavior = upper_bound_endpoint_behavior

    @property
    def lower_bound_time_point(self):
        """Gets the lower_bound_time_point of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The lower_bound_time_point of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: PublicTimePointOperationTimePoint
        """
        return self._lower_bound_time_point

    @lower_bound_time_point.setter
    def lower_bound_time_point(self, lower_bound_time_point):
        """Sets the lower_bound_time_point of this PublicPropertyFilterOperation.


        :param lower_bound_time_point: The lower_bound_time_point of this PublicPropertyFilterOperation.  # noqa: E501
        :type lower_bound_time_point: PublicTimePointOperationTimePoint
        """
        if self.local_vars_configuration.client_side_validation and lower_bound_time_point is None:  # noqa: E501
            raise ValueError("Invalid value for `lower_bound_time_point`, must not be `None`")  # noqa: E501

        self._lower_bound_time_point = lower_bound_time_point

    @property
    def upper_bound_time_point(self):
        """Gets the upper_bound_time_point of this PublicPropertyFilterOperation.  # noqa: E501


        :return: The upper_bound_time_point of this PublicPropertyFilterOperation.  # noqa: E501
        :rtype: PublicTimePointOperationTimePoint
        """
        return self._upper_bound_time_point

    @upper_bound_time_point.setter
    def upper_bound_time_point(self, upper_bound_time_point):
        """Sets the upper_bound_time_point of this PublicPropertyFilterOperation.


        :param upper_bound_time_point: The upper_bound_time_point of this PublicPropertyFilterOperation.  # noqa: E501
        :type upper_bound_time_point: PublicTimePointOperationTimePoint
        """
        if self.local_vars_configuration.client_side_validation and upper_bound_time_point is None:  # noqa: E501
            raise ValueError("Invalid value for `upper_bound_time_point`, must not be `None`")  # noqa: E501

        self._upper_bound_time_point = upper_bound_time_point

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
        if not isinstance(other, PublicPropertyFilterOperation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicPropertyFilterOperation):
            return True

        return self.to_dict() != other.to_dict()
