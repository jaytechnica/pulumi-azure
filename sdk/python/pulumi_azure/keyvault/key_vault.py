# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class KeyVault(pulumi.CustomResource):
    access_policies: pulumi.Output[list]
    """
    [A list](https://www.terraform.io/docs/configuration/attr-as-blocks.html) of up to 16 objects describing access policies, as described below.
    """
    enabled_for_deployment: pulumi.Output[bool]
    """
    Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to `false`.
    """
    enabled_for_disk_encryption: pulumi.Output[bool]
    """
    Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to `false`.
    """
    enabled_for_template_deployment: pulumi.Output[bool]
    """
    Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to `false`.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Key Vault. Changing this forces a new resource to be created.
    """
    network_acls: pulumi.Output[dict]
    """
    A `network_acls` block as defined below.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.
    """
    sku: pulumi.Output[dict]
    """
    An SKU block as described below.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    tenant_id: pulumi.Output[str]
    """
    The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. Must match the `tenant_id` used above.
    """
    vault_uri: pulumi.Output[str]
    """
    The URI of the Key Vault, used for performing operations on keys and secrets.
    """
    def __init__(__self__, resource_name, opts=None, access_policies=None, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, location=None, name=None, network_acls=None, resource_group_name=None, sku=None, tags=None, tenant_id=None, __name__=None, __opts__=None):
        """
        Manages a Key Vault.
        
        > **NOTE:** It's possible to define Key Vault Access Policies both within the `azurerm_key_vault` resource via the `access_policy` block and by using the `azurerm_key_vault_access_policy` resource. However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] access_policies: [A list](https://www.terraform.io/docs/configuration/attr-as-blocks.html) of up to 16 objects describing access policies, as described below.
        :param pulumi.Input[bool] enabled_for_deployment: Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to `false`.
        :param pulumi.Input[bool] enabled_for_disk_encryption: Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to `false`.
        :param pulumi.Input[bool] enabled_for_template_deployment: Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to `false`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Key Vault. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] network_acls: A `network_acls` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] sku: An SKU block as described below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] tenant_id: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. Must match the `tenant_id` used above.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['access_policies'] = access_policies

        __props__['enabled_for_deployment'] = enabled_for_deployment

        __props__['enabled_for_disk_encryption'] = enabled_for_disk_encryption

        __props__['enabled_for_template_deployment'] = enabled_for_template_deployment

        __props__['location'] = location

        __props__['name'] = name

        __props__['network_acls'] = network_acls

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        if sku is None:
            raise TypeError("Missing required property 'sku'")
        __props__['sku'] = sku

        __props__['tags'] = tags

        if tenant_id is None:
            raise TypeError("Missing required property 'tenant_id'")
        __props__['tenant_id'] = tenant_id

        __props__['vault_uri'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(KeyVault, __self__).__init__(
            'azure:keyvault/keyVault:KeyVault',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

