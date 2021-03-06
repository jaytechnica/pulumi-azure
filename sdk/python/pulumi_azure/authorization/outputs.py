# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'RoleDefinitionPermission',
    'GetRoleDefinitionPermissionResult',
]

@pulumi.output_type
class RoleDefinitionPermission(dict):
    def __init__(__self__, *,
                 actions: Optional[Sequence[str]] = None,
                 data_actions: Optional[Sequence[str]] = None,
                 not_actions: Optional[Sequence[str]] = None,
                 not_data_actions: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] actions: One or more Allowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        :param Sequence[str] data_actions: One or more Allowed Data Actions, such as `*`, `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        :param Sequence[str] not_actions: One or more Disallowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        :param Sequence[str] not_data_actions: One or more Disallowed Data Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        """
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if data_actions is not None:
            pulumi.set(__self__, "data_actions", data_actions)
        if not_actions is not None:
            pulumi.set(__self__, "not_actions", not_actions)
        if not_data_actions is not None:
            pulumi.set(__self__, "not_data_actions", not_data_actions)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[str]]:
        """
        One or more Allowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[str]]:
        """
        One or more Allowed Data Actions, such as `*`, `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "data_actions")

    @property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[Sequence[str]]:
        """
        One or more Disallowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "not_actions")

    @property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[str]]:
        """
        One or more Disallowed Data Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.
        """
        return pulumi.get(self, "not_data_actions")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetRoleDefinitionPermissionResult(dict):
    def __init__(__self__, *,
                 actions: Sequence[str],
                 not_actions: Sequence[str],
                 data_actions: Optional[Sequence[str]] = None,
                 not_data_actions: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] actions: a list of actions supported by this role
        :param Sequence[str] not_actions: a list of actions which are denied by this role
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "not_actions", not_actions)
        if data_actions is not None:
            pulumi.set(__self__, "data_actions", data_actions)
        if not_data_actions is not None:
            pulumi.set(__self__, "not_data_actions", not_data_actions)

    @property
    @pulumi.getter
    def actions(self) -> Sequence[str]:
        """
        a list of actions supported by this role
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Sequence[str]:
        """
        a list of actions which are denied by this role
        """
        return pulumi.get(self, "not_actions")

    @property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "data_actions")

    @property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "not_data_actions")


