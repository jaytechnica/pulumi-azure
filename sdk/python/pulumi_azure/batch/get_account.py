# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetAccountResult:
    """
    A collection of values returned by getAccount.
    """
    def __init__(__self__, account_endpoint=None, id=None, key_vault_references=None, location=None, name=None, pool_allocation_mode=None, primary_access_key=None, resource_group_name=None, secondary_access_key=None, storage_account_id=None, tags=None):
        if account_endpoint and not isinstance(account_endpoint, str):
            raise TypeError("Expected argument 'account_endpoint' to be a str")
        __self__.account_endpoint = account_endpoint
        """
        The account endpoint used to interact with the Batch service.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if key_vault_references and not isinstance(key_vault_references, list):
            raise TypeError("Expected argument 'key_vault_references' to be a list")
        __self__.key_vault_references = key_vault_references
        """
        The `key_vault_reference` block that describes the Azure KeyVault reference to use when deploying the Azure Batch account using the `UserSubscription` pool allocation mode. 
        """
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The Azure Region in which this Batch account exists.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The Batch account name.
        """
        if pool_allocation_mode and not isinstance(pool_allocation_mode, str):
            raise TypeError("Expected argument 'pool_allocation_mode' to be a str")
        __self__.pool_allocation_mode = pool_allocation_mode
        """
        The pool allocation mode configured for this Batch account.
        """
        if primary_access_key and not isinstance(primary_access_key, str):
            raise TypeError("Expected argument 'primary_access_key' to be a str")
        __self__.primary_access_key = primary_access_key
        """
        The Batch account primary access key.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if secondary_access_key and not isinstance(secondary_access_key, str):
            raise TypeError("Expected argument 'secondary_access_key' to be a str")
        __self__.secondary_access_key = secondary_access_key
        """
        The Batch account secondary access key.
        """
        if storage_account_id and not isinstance(storage_account_id, str):
            raise TypeError("Expected argument 'storage_account_id' to be a str")
        __self__.storage_account_id = storage_account_id
        """
        The ID of the Storage Account used for this Batch account.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A map of tags assigned to the Batch account.
        """
class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            account_endpoint=self.account_endpoint,
            id=self.id,
            key_vault_references=self.key_vault_references,
            location=self.location,
            name=self.name,
            pool_allocation_mode=self.pool_allocation_mode,
            primary_access_key=self.primary_access_key,
            resource_group_name=self.resource_group_name,
            secondary_access_key=self.secondary_access_key,
            storage_account_id=self.storage_account_id,
            tags=self.tags)

def get_account(name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Batch Account.




    :param str name: The name of the Batch account.
    :param str resource_group_name: The Name of the Resource Group where this Batch account exists.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:batch/getAccount:getAccount', __args__, opts=opts).value

    return AwaitableGetAccountResult(
        account_endpoint=__ret__.get('accountEndpoint'),
        id=__ret__.get('id'),
        key_vault_references=__ret__.get('keyVaultReferences'),
        location=__ret__.get('location'),
        name=__ret__.get('name'),
        pool_allocation_mode=__ret__.get('poolAllocationMode'),
        primary_access_key=__ret__.get('primaryAccessKey'),
        resource_group_name=__ret__.get('resourceGroupName'),
        secondary_access_key=__ret__.get('secondaryAccessKey'),
        storage_account_id=__ret__.get('storageAccountId'),
        tags=__ret__.get('tags'))
