# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['SubnetNetworkSecurityGroupAssociation']


class SubnetNetworkSecurityGroupAssociation(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_security_group_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Associates a Network Security Group with a Subnet within a Virtual Network.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.2.0/24"])
        example_network_security_group = azure.network.NetworkSecurityGroup("exampleNetworkSecurityGroup",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            security_rules=[azure.network.NetworkSecurityGroupSecurityRuleArgs(
                name="test123",
                priority=100,
                direction="Inbound",
                access="Allow",
                protocol="Tcp",
                source_port_range="*",
                destination_port_range="*",
                source_address_prefix="*",
                destination_address_prefix="*",
            )])
        example_subnet_network_security_group_association = azure.network.SubnetNetworkSecurityGroupAssociation("exampleSubnetNetworkSecurityGroupAssociation",
            subnet_id=example_subnet.id,
            network_security_group_id=example_network_security_group.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_security_group_id: The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet. Changing this forces a new resource to be created.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if network_security_group_id is None:
                raise TypeError("Missing required property 'network_security_group_id'")
            __props__['network_security_group_id'] = network_security_group_id
            if subnet_id is None:
                raise TypeError("Missing required property 'subnet_id'")
            __props__['subnet_id'] = subnet_id
        super(SubnetNetworkSecurityGroupAssociation, __self__).__init__(
            'azure:network/subnetNetworkSecurityGroupAssociation:SubnetNetworkSecurityGroupAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            network_security_group_id: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None) -> 'SubnetNetworkSecurityGroupAssociation':
        """
        Get an existing SubnetNetworkSecurityGroupAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_security_group_id: The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["network_security_group_id"] = network_security_group_id
        __props__["subnet_id"] = subnet_id
        return SubnetNetworkSecurityGroupAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="networkSecurityGroupId")
    def network_security_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "network_security_group_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the Subnet. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subnet_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

