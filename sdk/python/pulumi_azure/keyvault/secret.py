# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Secret(pulumi.CustomResource):
    """
    Manages a Key Vault Secret.
    
    ~> **Note:** All arguments including the secret value will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    """
    def __init__(__self__, __name__, __opts__=None, content_type=None, name=None, tags=None, value=None, vault_uri=None):
        """Create a Secret resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['content_type'] = content_type

        __props__['name'] = name

        __props__['tags'] = tags

        if not value:
            raise TypeError('Missing required property value')
        __props__['value'] = value

        if not vault_uri:
            raise TypeError('Missing required property vault_uri')
        __props__['vault_uri'] = vault_uri

        __props__['version'] = None

        super(Secret, __self__).__init__(
            'azure:keyvault/secret:Secret',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

