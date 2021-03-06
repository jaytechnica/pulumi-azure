# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ModuleNetworkProfile',
]

@pulumi.output_type
class ModuleNetworkProfile(dict):
    def __init__(__self__, *,
                 network_interface_private_ip_addresses: Sequence[str],
                 subnet_id: str):
        """
        :param Sequence[str] network_interface_private_ip_addresses: The private IPv4 address of the network interface. Changing this forces a new Dedicated Hardware Security Module to be created.
        :param str subnet_id: The ID of the subnet. Changing this forces a new Dedicated Hardware Security Module to be created.
        """
        pulumi.set(__self__, "network_interface_private_ip_addresses", network_interface_private_ip_addresses)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="networkInterfacePrivateIpAddresses")
    def network_interface_private_ip_addresses(self) -> Sequence[str]:
        """
        The private IPv4 address of the network interface. Changing this forces a new Dedicated Hardware Security Module to be created.
        """
        return pulumi.get(self, "network_interface_private_ip_addresses")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The ID of the subnet. Changing this forces a new Dedicated Hardware Security Module to be created.
        """
        return pulumi.get(self, "subnet_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


