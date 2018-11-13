# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetSecretResult(object):
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, content_type=None, tags=None, value=None, version=None, id=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError('Expected argument content_type to be a str')
        __self__.content_type = content_type
        """
        The content type for the Key Vault Secret.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        Any tags assigned to this resource.
        """
        if value and not isinstance(value, str):
            raise TypeError('Expected argument value to be a str')
        __self__.value = value
        """
        The value of the Key Vault Secret.
        """
        if version and not isinstance(version, str):
            raise TypeError('Expected argument version to be a str')
        __self__.version = version
        """
        The current version of the Key Vault Secret.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_secret(name=None, vault_uri=None):
    """
    Use this data source to access information about an existing Key Vault Secret.
    
    ~> **Note:** All arguments including the secret value will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['vaultUri'] = vault_uri
    __ret__ = await pulumi.runtime.invoke('azure:keyvault/getSecret:getSecret', __args__)

    return GetSecretResult(
        content_type=__ret__.get('contentType'),
        tags=__ret__.get('tags'),
        value=__ret__.get('value'),
        version=__ret__.get('version'),
        id=__ret__.get('id'))
