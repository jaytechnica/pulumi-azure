# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetFirewallResult:
    """
    A collection of values returned by getFirewall.
    """
    def __init__(__self__, id=None, ip_configurations=None, location=None, name=None, resource_group_name=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ip_configurations and not isinstance(ip_configurations, list):
            raise TypeError("Expected argument 'ip_configurations' to be a list")
        __self__.ip_configurations = ip_configurations
        """
        A `ip_configuration` block as defined below.
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
class AwaitableGetFirewallResult(GetFirewallResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallResult(
            id=self.id,
            ip_configurations=self.ip_configurations,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags)

def get_firewall(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Azure Firewall.




    :param str name: The name of the Azure Firewall.
    :param str resource_group_name: The name of the Resource Group in which the Azure Firewall exists.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:network/getFirewall:getFirewall', __args__, opts=opts).value

    return AwaitableGetFirewallResult(
        id=__ret__.get('id'),
        ip_configurations=__ret__.get('ipConfigurations'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        resource_group_name=__ret__.get('resourceGroupName'),
        tags=__ret__.get('tags'))
