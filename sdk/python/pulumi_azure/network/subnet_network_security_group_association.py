# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class SubnetNetworkSecurityGroupAssociation(pulumi.CustomResource):
    """
    Associates a Network Security Group with a Subnet within a Virtual Network.
    
    -> **NOTE:** Subnet <-> Network Security Group associations currently need to be configured on both this resource and using the `network_security_group_id` field on the `azurerm_subnet` resource. The next major version of the AzureRM Provider (2.0) will remove the `network_security_group_id` field from the `azurerm_subnet` resource such that this resource is used to link resources in future.
    """
    def __init__(__self__, __name__, __opts__=None, network_security_group_id=None, subnet_id=None):
        """Create a SubnetNetworkSecurityGroupAssociation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not network_security_group_id:
            raise TypeError('Missing required property network_security_group_id')
        __props__['network_security_group_id'] = network_security_group_id

        if not subnet_id:
            raise TypeError('Missing required property subnet_id')
        __props__['subnet_id'] = subnet_id

        super(SubnetNetworkSecurityGroupAssociation, __self__).__init__(
            'azure:network/subnetNetworkSecurityGroupAssociation:SubnetNetworkSecurityGroupAssociation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

