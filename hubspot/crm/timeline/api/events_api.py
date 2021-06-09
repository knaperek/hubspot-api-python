# coding: utf-8

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM objects like contacts, companies, tickets, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.timeline.api_client import ApiClient
from hubspot.crm.timeline.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, timeline_event, **kwargs):  # noqa: E501
        """Create a single event  # noqa: E501

        Creates an instance of a timeline event based on an event template. Once created, this event is immutable on the object timeline and cannot be modified. If the event template was configured to update object properties via `objectPropertyName`, this call will also attempt to updates those properties, or add them if they don't exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(timeline_event, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TimelineEvent timeline_event: The timeline event definition. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TimelineEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(timeline_event, **kwargs)  # noqa: E501

    def create_with_http_info(self, timeline_event, **kwargs):  # noqa: E501
        """Create a single event  # noqa: E501

        Creates an instance of a timeline event based on an event template. Once created, this event is immutable on the object timeline and cannot be modified. If the event template was configured to update object properties via `objectPropertyName`, this call will also attempt to updates those properties, or add them if they don't exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(timeline_event, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TimelineEvent timeline_event: The timeline event definition. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TimelineEventResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'timeline_event'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'timeline_event' is set
        if self.api_client.client_side_validation and ('timeline_event' not in local_var_params or  # noqa: E501
                                                        local_var_params['timeline_event'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `timeline_event` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'timeline_event' in local_var_params:
            body_params = local_var_params['timeline_event']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/timeline/events', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimelineEventResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_batch(self, batch_input_timeline_event, **kwargs):  # noqa: E501
        """Creates multiple events  # noqa: E501

        Creates multiple instances of timeline events based on an event template. Once created, these event are immutable on the object timeline and cannot be modified. If the event template was configured to update object properties via `objectPropertyName`, this call will also attempt to updates those properties, or add them if they don't exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_batch(batch_input_timeline_event, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputTimelineEvent batch_input_timeline_event: The timeline event definition. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseTimelineEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_batch_with_http_info(batch_input_timeline_event, **kwargs)  # noqa: E501

    def create_batch_with_http_info(self, batch_input_timeline_event, **kwargs):  # noqa: E501
        """Creates multiple events  # noqa: E501

        Creates multiple instances of timeline events based on an event template. Once created, these event are immutable on the object timeline and cannot be modified. If the event template was configured to update object properties via `objectPropertyName`, this call will also attempt to updates those properties, or add them if they don't exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_batch_with_http_info(batch_input_timeline_event, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputTimelineEvent batch_input_timeline_event: The timeline event definition. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseTimelineEventResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'batch_input_timeline_event'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_batch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'batch_input_timeline_event' is set
        if self.api_client.client_side_validation and ('batch_input_timeline_event' not in local_var_params or  # noqa: E501
                                                        local_var_params['batch_input_timeline_event'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_timeline_event` when calling `create_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_input_timeline_event' in local_var_params:
            body_params = local_var_params['batch_input_timeline_event']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/timeline/events/batch/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchResponseTimelineEventResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_by_id(self, event_template_id, event_id, **kwargs):  # noqa: E501
        """Gets the event  # noqa: E501

        This returns the previously created event. It contains all existing info for the event, but not necessarily the CRM object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(event_template_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str event_id: The event ID. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TimelineEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_by_id_with_http_info(event_template_id, event_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, event_template_id, event_id, **kwargs):  # noqa: E501
        """Gets the event  # noqa: E501

        This returns the previously created event. It contains all existing info for the event, but not necessarily the CRM object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(event_template_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str event_id: The event ID. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TimelineEventResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'event_template_id',
            'event_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and ('event_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_template_id` when calling `get_by_id`")  # noqa: E501
        # verify the required parameter 'event_id' is set
        if self.api_client.client_side_validation and ('event_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_template_id' in local_var_params:
            path_params['eventTemplateId'] = local_var_params['event_template_id']  # noqa: E501
        if 'event_id' in local_var_params:
            path_params['eventId'] = local_var_params['event_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/timeline/events/{eventTemplateId}/{eventId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimelineEventResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_detail_by_id(self, event_template_id, event_id, **kwargs):  # noqa: E501
        """Gets the detailTemplate as rendered  # noqa: E501

        This will take the `detailTemplate` from the event template and return an object rendering the specified event. If the template references `extraData` that isn't found in the event, it will be ignored and we'll render without it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_detail_by_id(event_template_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str event_id: The event ID. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EventDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_detail_by_id_with_http_info(event_template_id, event_id, **kwargs)  # noqa: E501

    def get_detail_by_id_with_http_info(self, event_template_id, event_id, **kwargs):  # noqa: E501
        """Gets the detailTemplate as rendered  # noqa: E501

        This will take the `detailTemplate` from the event template and return an object rendering the specified event. If the template references `extraData` that isn't found in the event, it will be ignored and we'll render without it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_detail_by_id_with_http_info(event_template_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str event_id: The event ID. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EventDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'event_template_id',
            'event_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_detail_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and ('event_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_template_id` when calling `get_detail_by_id`")  # noqa: E501
        # verify the required parameter 'event_id' is set
        if self.api_client.client_side_validation and ('event_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_id` when calling `get_detail_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_template_id' in local_var_params:
            path_params['eventTemplateId'] = local_var_params['event_template_id']  # noqa: E501
        if 'event_id' in local_var_params:
            path_params['eventId'] = local_var_params['event_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/timeline/events/{eventTemplateId}/{eventId}/detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_render_by_id(self, event_template_id, event_id, **kwargs):  # noqa: E501
        """Renders the header or detail as HTML  # noqa: E501

        This will take either the `headerTemplate` or `detailTemplate` from the event template and render for the specified event as HTML. If the template references `extraData` that isn't found in the event, it will be ignored and we'll render without it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_render_by_id(event_template_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str event_id: The event ID. (required)
        :param bool detail: Set to 'true', we want to render the `detailTemplate` instead of the `headerTemplate`.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_render_by_id_with_http_info(event_template_id, event_id, **kwargs)  # noqa: E501

    def get_render_by_id_with_http_info(self, event_template_id, event_id, **kwargs):  # noqa: E501
        """Renders the header or detail as HTML  # noqa: E501

        This will take either the `headerTemplate` or `detailTemplate` from the event template and render for the specified event as HTML. If the template references `extraData` that isn't found in the event, it will be ignored and we'll render without it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_render_by_id_with_http_info(event_template_id, event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str event_id: The event ID. (required)
        :param bool detail: Set to 'true', we want to render the `detailTemplate` instead of the `headerTemplate`.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'event_template_id',
            'event_id',
            'detail'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_render_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and ('event_template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_template_id` when calling `get_render_by_id`")  # noqa: E501
        # verify the required parameter 'event_id' is set
        if self.api_client.client_side_validation and ('event_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_id` when calling `get_render_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_template_id' in local_var_params:
            path_params['eventTemplateId'] = local_var_params['event_template_id']  # noqa: E501
        if 'event_id' in local_var_params:
            path_params['eventId'] = local_var_params['event_id']  # noqa: E501

        query_params = []
        if 'detail' in local_var_params and local_var_params['detail'] is not None:  # noqa: E501
            query_params.append(('detail', local_var_params['detail']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/timeline/events/{eventTemplateId}/{eventId}/render', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
