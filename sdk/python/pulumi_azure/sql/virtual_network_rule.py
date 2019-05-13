# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class VirtualNetworkRule(pulumi.CustomResource):
    ignore_missing_vnet_service_endpoint: pulumi.Output[bool]
    """
    Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.
    """
    name: pulumi.Output[str]
    """
    The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.
    """
    server_name: pulumi.Output[str]
    """
    The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.
    """
    subnet_id: pulumi.Output[str]
    """
    The ID of the subnet that the SQL server will be connected to.
    """
    def __init__(__self__, resource_name, opts=None, ignore_missing_vnet_service_endpoint=None, name=None, resource_group_name=None, server_name=None, subnet_id=None, __name__=None, __opts__=None):
        """
        Allows you to add, update, or remove an Azure SQL server to a subnet of a virtual network.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.
        :param pulumi.Input[str] name: The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet that the SQL server will be connected to.
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

        __props__['ignore_missing_vnet_service_endpoint'] = ignore_missing_vnet_service_endpoint

        __props__['name'] = name

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        if server_name is None:
            raise TypeError("Missing required property 'server_name'")
        __props__['server_name'] = server_name

        if subnet_id is None:
            raise TypeError("Missing required property 'subnet_id'")
        __props__['subnet_id'] = subnet_id

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(VirtualNetworkRule, __self__).__init__(
            'azure:sql/virtualNetworkRule:VirtualNetworkRule',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

