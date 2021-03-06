# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ServiceCor',
    'ServiceFeature',
    'ServiceSku',
]

@pulumi.output_type
class ServiceCor(dict):
    def __init__(__self__, *,
                 allowed_origins: Sequence[str]):
        """
        :param Sequence[str] allowed_origins: A list of origins which should be able to make cross-origin calls. `*` can be used to allow all calls.
        """
        pulumi.set(__self__, "allowed_origins", allowed_origins)

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[str]:
        """
        A list of origins which should be able to make cross-origin calls. `*` can be used to allow all calls.
        """
        return pulumi.get(self, "allowed_origins")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ServiceFeature(dict):
    def __init__(__self__, *,
                 flag: str,
                 value: str):
        """
        :param str flag: The kind of Feature. Possible values are `EnableConnectivityLogs`, `EnableMessagingLogs`, and `ServiceMode`.
        :param str value: A value of a feature flag. Possible values are `Classic`, `Default` and `Serverless`.
        """
        pulumi.set(__self__, "flag", flag)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def flag(self) -> str:
        """
        The kind of Feature. Possible values are `EnableConnectivityLogs`, `EnableMessagingLogs`, and `ServiceMode`.
        """
        return pulumi.get(self, "flag")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        A value of a feature flag. Possible values are `Classic`, `Default` and `Serverless`.
        """
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ServiceSku(dict):
    def __init__(__self__, *,
                 capacity: int,
                 name: str):
        """
        :param int capacity: Specifies the number of units associated with this SignalR service. Valid values are `1`, `2`, `5`, `10`, `20`, `50` and `100`.
        :param str name: Specifies which tier to use. Valid values are `Free_F1` and `Standard_S1`.
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> int:
        """
        Specifies the number of units associated with this SignalR service. Valid values are `1`, `2`, `5`, `10`, `20`, `50` and `100`.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies which tier to use. Valid values are `Free_F1` and `Standard_S1`.
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


