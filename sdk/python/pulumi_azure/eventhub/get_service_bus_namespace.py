# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetServiceBusNamespaceResult:
    """
    A collection of values returned by getServiceBusNamespace.
    """
    def __init__(__self__, capacity=None, default_primary_connection_string=None, default_primary_key=None, default_secondary_connection_string=None, default_secondary_key=None, location=None, name=None, resource_group_name=None, sku=None, tags=None, id=None):
        if capacity and not isinstance(capacity, float):
            raise TypeError("Expected argument 'capacity' to be a float")
        __self__.capacity = capacity
        """
        The capacity of the ServiceBus Namespace.
        """
        if default_primary_connection_string and not isinstance(default_primary_connection_string, str):
            raise TypeError("Expected argument 'default_primary_connection_string' to be a str")
        __self__.default_primary_connection_string = default_primary_connection_string
        """
        The primary connection string for the authorization
        rule `RootManageSharedAccessKey`.
        """
        if default_primary_key and not isinstance(default_primary_key, str):
            raise TypeError("Expected argument 'default_primary_key' to be a str")
        __self__.default_primary_key = default_primary_key
        """
        The primary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        if default_secondary_connection_string and not isinstance(default_secondary_connection_string, str):
            raise TypeError("Expected argument 'default_secondary_connection_string' to be a str")
        __self__.default_secondary_connection_string = default_secondary_connection_string
        """
        The secondary connection string for the
        authorization rule `RootManageSharedAccessKey`.
        """
        if default_secondary_key and not isinstance(default_secondary_key, str):
            raise TypeError("Expected argument 'default_secondary_key' to be a str")
        __self__.default_secondary_key = default_secondary_key
        """
        The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The location of the Resource Group in which the ServiceBus Namespace exists.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if sku and not isinstance(sku, str):
            raise TypeError("Expected argument 'sku' to be a str")
        __self__.sku = sku
        """
        The Tier used for the ServiceBus Namespace.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the resource.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetServiceBusNamespaceResult(GetServiceBusNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceBusNamespaceResult(
            capacity=self.capacity,
            default_primary_connection_string=self.default_primary_connection_string,
            default_primary_key=self.default_primary_key,
            default_secondary_connection_string=self.default_secondary_connection_string,
            default_secondary_key=self.default_secondary_key,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            sku=self.sku,
            tags=self.tags,
            id=self.id)

def get_service_bus_namespace(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing ServiceBus Namespace.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/servicebus_namespace_legacy.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:eventhub/getServiceBusNamespace:getServiceBusNamespace', __args__, opts=opts).value

    return AwaitableGetServiceBusNamespaceResult(
        capacity=__ret__.get('capacity'),
        default_primary_connection_string=__ret__.get('defaultPrimaryConnectionString'),
        default_primary_key=__ret__.get('defaultPrimaryKey'),
        default_secondary_connection_string=__ret__.get('defaultSecondaryConnectionString'),
        default_secondary_key=__ret__.get('defaultSecondaryKey'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        resource_group_name=__ret__.get('resourceGroupName'),
        sku=__ret__.get('sku'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
