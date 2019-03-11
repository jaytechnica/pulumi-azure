# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetStoreResult:
    """
    A collection of values returned by getStore.
    """
    def __init__(__self__, encryption_state=None, encryption_type=None, firewall_allow_azure_ips=None, firewall_state=None, location=None, tags=None, tier=None, id=None):
        if encryption_state and not isinstance(encryption_state, str):
            raise TypeError('Expected argument encryption_state to be a str')
        __self__.encryption_state = encryption_state
        """
        the Encryption State of this Data Lake Store Account, such as `Enabled` or `Disabled`.
        """
        if encryption_type and not isinstance(encryption_type, str):
            raise TypeError('Expected argument encryption_type to be a str')
        __self__.encryption_type = encryption_type
        """
        the Encryption Type used for this Data Lake Store Account.
        """
        if firewall_allow_azure_ips and not isinstance(firewall_allow_azure_ips, str):
            raise TypeError('Expected argument firewall_allow_azure_ips to be a str')
        __self__.firewall_allow_azure_ips = firewall_allow_azure_ips
        """
        are Azure Service IP's allowed through the firewall?
        """
        if firewall_state and not isinstance(firewall_state, str):
            raise TypeError('Expected argument firewall_state to be a str')
        __self__.firewall_state = firewall_state
        """
        the state of the firewall, such as `Enabled` or `Disabled`.
        """
        if location and not isinstance(location, str):
            raise TypeError('Expected argument location to be a str')
        __self__.location = location
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the Data Lake Store.
        """
        if tier and not isinstance(tier, str):
            raise TypeError('Expected argument tier to be a str')
        __self__.tier = tier
        """
        Current monthly commitment tier for the account.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_store(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Data Lake Store.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __ret__ = await pulumi.runtime.invoke('azure:datalake/getStore:getStore', __args__, opts=opts)

    return GetStoreResult(
        encryption_state=__ret__.get('encryptionState'),
        encryption_type=__ret__.get('encryptionType'),
        firewall_allow_azure_ips=__ret__.get('firewallAllowAzureIps'),
        firewall_state=__ret__.get('firewallState'),
        location=__ret__.get('location'),
        tags=__ret__.get('tags'),
        tier=__ret__.get('tier'),
        id=__ret__.get('id'))
