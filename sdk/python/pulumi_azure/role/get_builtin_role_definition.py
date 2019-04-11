# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetBuiltinRoleDefinitionResult:
    """
    A collection of values returned by getBuiltinRoleDefinition.
    """
    def __init__(__self__, assignable_scopes=None, description=None, name=None, permissions=None, type=None, id=None):
        if assignable_scopes and not isinstance(assignable_scopes, list):
            raise TypeError("Expected argument 'assignable_scopes' to be a list")
        __self__.assignable_scopes = assignable_scopes
        """
        One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        the Description of the built-in Role.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        __self__.permissions = permissions
        """
        a `permissions` block as documented below.
        """
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        """
        the Type of the Role.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_builtin_role_definition(name=None,opts=None):
    """
    Use this data source to access information about a built-in Role Definition. To access information about a custom Role Definition, please see the `azurerm_role_definition` data source instead.
    
    > **NOTE:** The this datasource has been deprecated in favour of `azurerm_role_definition` that now can look up role definitions by name. As such this data source will be removed in version 2.0 of the AzureRM Provider.
    """
    __args__ = dict()

    __args__['name'] = name
    __ret__ = await pulumi.runtime.invoke('azure:role/getBuiltinRoleDefinition:getBuiltinRoleDefinition', __args__, opts=opts)

    return GetBuiltinRoleDefinitionResult(
        assignable_scopes=__ret__.get('assignableScopes'),
        description=__ret__.get('description'),
        name=__ret__.get('name'),
        permissions=__ret__.get('permissions'),
        type=__ret__.get('type'),
        id=__ret__.get('id'))
