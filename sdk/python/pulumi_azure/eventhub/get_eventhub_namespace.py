# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetEventhubNamespaceResult:
    """
    A collection of values returned by getEventhubNamespace.
    """
    def __init__(__self__, auto_inflate_enabled=None, capacity=None, default_primary_connection_string=None, default_primary_key=None, default_secondary_connection_string=None, default_secondary_key=None, kafka_enabled=None, location=None, maximum_throughput_units=None, sku=None, tags=None, id=None):
        if auto_inflate_enabled and not isinstance(auto_inflate_enabled, bool):
            raise TypeError('Expected argument auto_inflate_enabled to be a bool')
        __self__.auto_inflate_enabled = auto_inflate_enabled
        """
        Is Auto Inflate enabled for the EventHub Namespace?
        """
        if capacity and not isinstance(capacity, int):
            raise TypeError('Expected argument capacity to be a int')
        __self__.capacity = capacity
        """
        The Capacity / Throughput Units for a `Standard` SKU namespace.
        """
        if default_primary_connection_string and not isinstance(default_primary_connection_string, str):
            raise TypeError('Expected argument default_primary_connection_string to be a str')
        __self__.default_primary_connection_string = default_primary_connection_string
        """
        The primary connection string for the authorization
        rule `RootManageSharedAccessKey`.
        """
        if default_primary_key and not isinstance(default_primary_key, str):
            raise TypeError('Expected argument default_primary_key to be a str')
        __self__.default_primary_key = default_primary_key
        """
        The primary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        if default_secondary_connection_string and not isinstance(default_secondary_connection_string, str):
            raise TypeError('Expected argument default_secondary_connection_string to be a str')
        __self__.default_secondary_connection_string = default_secondary_connection_string
        """
        The secondary connection string for the
        authorization rule `RootManageSharedAccessKey`.
        """
        if default_secondary_key and not isinstance(default_secondary_key, str):
            raise TypeError('Expected argument default_secondary_key to be a str')
        __self__.default_secondary_key = default_secondary_key
        """
        The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        if kafka_enabled and not isinstance(kafka_enabled, bool):
            raise TypeError('Expected argument kafka_enabled to be a bool')
        __self__.kafka_enabled = kafka_enabled
        if location and not isinstance(location, str):
            raise TypeError('Expected argument location to be a str')
        __self__.location = location
        """
        The Azure location where the EventHub Namespace exists
        """
        if maximum_throughput_units and not isinstance(maximum_throughput_units, int):
            raise TypeError('Expected argument maximum_throughput_units to be a int')
        __self__.maximum_throughput_units = maximum_throughput_units
        """
        Specifies the maximum number of throughput units when Auto Inflate is Enabled.
        """
        if sku and not isinstance(sku, str):
            raise TypeError('Expected argument sku to be a str')
        __self__.sku = sku
        """
        Defines which tier to use.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the EventHub Namespace.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_eventhub_namespace(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing EventHub Namespace.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __ret__ = await pulumi.runtime.invoke('azure:eventhub/getEventhubNamespace:getEventhubNamespace', __args__, opts=opts)

    return GetEventhubNamespaceResult(
        auto_inflate_enabled=__ret__.get('autoInflateEnabled'),
        capacity=__ret__.get('capacity'),
        default_primary_connection_string=__ret__.get('defaultPrimaryConnectionString'),
        default_primary_key=__ret__.get('defaultPrimaryKey'),
        default_secondary_connection_string=__ret__.get('defaultSecondaryConnectionString'),
        default_secondary_key=__ret__.get('defaultSecondaryKey'),
        kafka_enabled=__ret__.get('kafkaEnabled'),
        location=__ret__.get('location'),
        maximum_throughput_units=__ret__.get('maximumThroughputUnits'),
        sku=__ret__.get('sku'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
