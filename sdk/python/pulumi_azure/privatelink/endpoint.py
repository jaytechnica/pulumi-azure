# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Endpoint']


class Endpoint(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_dns_zone_group: Optional[pulumi.Input[pulumi.InputType['EndpointPrivateDnsZoneGroupArgs']]] = None,
                 private_service_connection: Optional[pulumi.Input[pulumi.InputType['EndpointPrivateServiceConnectionArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Private Endpoint.

        > **NOTE** Private Endpoint is currently in Public Preview.

        Azure Private Endpoint is a network interface that connects you privately and securely to a service powered by Azure Private Link. Private Endpoint uses a private IP address from your VNet, effectively bringing the service into your VNet. The service could be an Azure service such as Azure Storage, SQL, etc. or your own Private Link Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        service = azure.network.Subnet("service",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.1.0/24"],
            enforce_private_link_service_network_policies=True)
        endpoint = azure.network.Subnet("endpoint",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.2.0/24"],
            enforce_private_link_endpoint_network_policies=True)
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            sku="Standard",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            allocation_method="Static")
        example_load_balancer = azure.lb.LoadBalancer("exampleLoadBalancer",
            sku="Standard",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            frontend_ip_configurations=[azure.lb.LoadBalancerFrontendIpConfigurationArgs(
                name=example_public_ip.name,
                public_ip_address_id=example_public_ip.id,
            )])
        example_link_service = azure.privatedns.LinkService("exampleLinkService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            nat_ip_configurations=[azure.privatedns.LinkServiceNatIpConfigurationArgs(
                name=example_public_ip.name,
                primary=True,
                subnet_id=service.id,
            )],
            load_balancer_frontend_ip_configuration_ids=[example_load_balancer.frontend_ip_configurations[0].id])
        example_endpoint = azure.privatelink.Endpoint("exampleEndpoint",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            subnet_id=endpoint.id,
            private_service_connection=azure.privatelink.EndpointPrivateServiceConnectionArgs(
                name="example-privateserviceconnection",
                private_connection_resource_id=example_link_service.id,
                is_manual_connection=False,
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the Name of the Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['EndpointPrivateDnsZoneGroupArgs']] private_dns_zone_group: A `private_dns_zone_group` block as defined below.
        :param pulumi.Input[pulumi.InputType['EndpointPrivateServiceConnectionArgs']] private_service_connection: A `private_service_connection` block as defined below.
        :param pulumi.Input[str] resource_group_name: Specifies the Name of the Resource Group within which the Private Endpoint should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet from which Private IP Addresses will be allocated for this Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
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

            __props__['location'] = location
            __props__['name'] = name
            __props__['private_dns_zone_group'] = private_dns_zone_group
            if private_service_connection is None:
                raise TypeError("Missing required property 'private_service_connection'")
            __props__['private_service_connection'] = private_service_connection
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if subnet_id is None:
                raise TypeError("Missing required property 'subnet_id'")
            __props__['subnet_id'] = subnet_id
            __props__['tags'] = tags
            __props__['custom_dns_configs'] = None
            __props__['private_dns_zone_configs'] = None
        super(Endpoint, __self__).__init__(
            'azure:privatelink/endpoint:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_dns_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointCustomDnsConfigArgs']]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_dns_zone_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointPrivateDnsZoneConfigArgs']]]]] = None,
            private_dns_zone_group: Optional[pulumi.Input[pulumi.InputType['EndpointPrivateDnsZoneGroupArgs']]] = None,
            private_service_connection: Optional[pulumi.Input[pulumi.InputType['EndpointPrivateServiceConnectionArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Endpoint':
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the Name of the Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['EndpointPrivateDnsZoneGroupArgs']] private_dns_zone_group: A `private_dns_zone_group` block as defined below.
        :param pulumi.Input[pulumi.InputType['EndpointPrivateServiceConnectionArgs']] private_service_connection: A `private_service_connection` block as defined below.
        :param pulumi.Input[str] resource_group_name: Specifies the Name of the Resource Group within which the Private Endpoint should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet from which Private IP Addresses will be allocated for this Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["custom_dns_configs"] = custom_dns_configs
        __props__["location"] = location
        __props__["name"] = name
        __props__["private_dns_zone_configs"] = private_dns_zone_configs
        __props__["private_dns_zone_group"] = private_dns_zone_group
        __props__["private_service_connection"] = private_service_connection
        __props__["resource_group_name"] = resource_group_name
        __props__["subnet_id"] = subnet_id
        __props__["tags"] = tags
        return Endpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customDnsConfigs")
    def custom_dns_configs(self) -> pulumi.Output[Sequence['outputs.EndpointCustomDnsConfig']]:
        return pulumi.get(self, "custom_dns_configs")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the Name of the Private Endpoint. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateDnsZoneConfigs")
    def private_dns_zone_configs(self) -> pulumi.Output[Sequence['outputs.EndpointPrivateDnsZoneConfig']]:
        return pulumi.get(self, "private_dns_zone_configs")

    @property
    @pulumi.getter(name="privateDnsZoneGroup")
    def private_dns_zone_group(self) -> pulumi.Output[Optional['outputs.EndpointPrivateDnsZoneGroup']]:
        """
        A `private_dns_zone_group` block as defined below.
        """
        return pulumi.get(self, "private_dns_zone_group")

    @property
    @pulumi.getter(name="privateServiceConnection")
    def private_service_connection(self) -> pulumi.Output['outputs.EndpointPrivateServiceConnection']:
        """
        A `private_service_connection` block as defined below.
        """
        return pulumi.get(self, "private_service_connection")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the Name of the Resource Group within which the Private Endpoint should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the Subnet from which Private IP Addresses will be allocated for this Private Endpoint. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

