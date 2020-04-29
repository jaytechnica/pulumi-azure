# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetNatGatewayResult:
    """
    A collection of values returned by getNatGateway.
    """
    def __init__(__self__, id=None, idle_timeout_in_minutes=None, location=None, name=None, public_ip_address_ids=None, public_ip_prefix_ids=None, resource_group_name=None, resource_guid=None, sku_name=None, tags=None, zones=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if idle_timeout_in_minutes and not isinstance(idle_timeout_in_minutes, float):
            raise TypeError("Expected argument 'idle_timeout_in_minutes' to be a float")
        __self__.idle_timeout_in_minutes = idle_timeout_in_minutes
        """
        The idle timeout in minutes which is used for the NAT Gateway.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The location where the NAT Gateway exists.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if public_ip_address_ids and not isinstance(public_ip_address_ids, list):
            raise TypeError("Expected argument 'public_ip_address_ids' to be a list")
        __self__.public_ip_address_ids = public_ip_address_ids
        """
        A list of existing Public IP Address resource IDs which the NAT Gateway is using.
        """
        if public_ip_prefix_ids and not isinstance(public_ip_prefix_ids, list):
            raise TypeError("Expected argument 'public_ip_prefix_ids' to be a list")
        __self__.public_ip_prefix_ids = public_ip_prefix_ids
        """
        A list of existing Public IP Prefix resource IDs which the NAT Gateway is using.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        __self__.resource_guid = resource_guid
        """
        The Resource GUID of the NAT Gateway.
        """
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        __self__.sku_name = sku_name
        """
        The SKU used by the NAT Gateway.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the resource.
        """
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        __self__.zones = zones
        """
        A list of Availability Zones which the NAT Gateway exists in.
        """
class AwaitableGetNatGatewayResult(GetNatGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNatGatewayResult(
            id=self.id,
            idle_timeout_in_minutes=self.idle_timeout_in_minutes,
            location=self.location,
            name=self.name,
            public_ip_address_ids=self.public_ip_address_ids,
            public_ip_prefix_ids=self.public_ip_prefix_ids,
            resource_group_name=self.resource_group_name,
            resource_guid=self.resource_guid,
            sku_name=self.sku_name,
            tags=self.tags,
            zones=self.zones)

def get_nat_gateway(name=None,public_ip_address_ids=None,public_ip_prefix_ids=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing NAT Gateway.


    :param str name: Specifies the Name of the NAT Gateway.
    :param list public_ip_address_ids: A list of existing Public IP Address resource IDs which the NAT Gateway is using.
    :param list public_ip_prefix_ids: A list of existing Public IP Prefix resource IDs which the NAT Gateway is using.
    :param str resource_group_name: Specifies the name of the Resource Group where the NAT Gateway exists.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['publicIpAddressIds'] = public_ip_address_ids
    __args__['publicIpPrefixIds'] = public_ip_prefix_ids
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:network/getNatGateway:getNatGateway', __args__, opts=opts).value

    return AwaitableGetNatGatewayResult(
        id=__ret__.get('id'),
        idle_timeout_in_minutes=__ret__.get('idleTimeoutInMinutes'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        public_ip_address_ids=__ret__.get('publicIpAddressIds'),
        public_ip_prefix_ids=__ret__.get('publicIpPrefixIds'),
        resource_group_name=__ret__.get('resourceGroupName'),
        resource_guid=__ret__.get('resourceGuid'),
        sku_name=__ret__.get('skuName'),
        tags=__ret__.get('tags'),
        zones=__ret__.get('zones'))
