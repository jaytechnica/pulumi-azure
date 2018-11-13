# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class NetworkInterfaceBackendAddressPoolAssociation(pulumi.CustomResource):
    """
    Manages the association between a Network Interface and a Load Balancer's Backend Address Pool.
    """
    def __init__(__self__, __name__, __opts__=None, backend_address_pool_id=None, ip_configuration_name=None, network_interface_id=None):
        """Create a NetworkInterfaceBackendAddressPoolAssociation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not backend_address_pool_id:
            raise TypeError('Missing required property backend_address_pool_id')
        __props__['backend_address_pool_id'] = backend_address_pool_id

        if not ip_configuration_name:
            raise TypeError('Missing required property ip_configuration_name')
        __props__['ip_configuration_name'] = ip_configuration_name

        if not network_interface_id:
            raise TypeError('Missing required property network_interface_id')
        __props__['network_interface_id'] = network_interface_id

        super(NetworkInterfaceBackendAddressPoolAssociation, __self__).__init__(
            'azure:network/networkInterfaceBackendAddressPoolAssociation:NetworkInterfaceBackendAddressPoolAssociation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

