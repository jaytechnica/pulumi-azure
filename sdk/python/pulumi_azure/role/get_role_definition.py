# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetRoleDefinitionResult:
    """
    A collection of values returned by getRoleDefinition.
    """
    def __init__(__self__, assignable_scopes=None, description=None, name=None, permissions=None, role_definition_id=None, scope=None, type=None, id=None):
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
        if role_definition_id and not isinstance(role_definition_id, str):
            raise TypeError("Expected argument 'role_definition_id' to be a str")
        __self__.role_definition_id = role_definition_id
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        __self__.scope = scope
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
class AwaitableGetRoleDefinitionResult(GetRoleDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleDefinitionResult(
            assignable_scopes=self.assignable_scopes,
            description=self.description,
            name=self.name,
            permissions=self.permissions,
            role_definition_id=self.role_definition_id,
            scope=self.scope,
            type=self.type,
            id=self.id)

def get_role_definition(name=None,role_definition_id=None,scope=None,opts=None):
    """
    Use this data source to access information about an existing Role Definition.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/role_definition_legacy.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['roleDefinitionId'] = role_definition_id
    __args__['scope'] = scope
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:role/getRoleDefinition:getRoleDefinition', __args__, opts=opts).value

    return AwaitableGetRoleDefinitionResult(
        assignable_scopes=__ret__.get('assignableScopes'),
        description=__ret__.get('description'),
        name=__ret__.get('name'),
        permissions=__ret__.get('permissions'),
        role_definition_id=__ret__.get('roleDefinitionId'),
        scope=__ret__.get('scope'),
        type=__ret__.get('type'),
        id=__ret__.get('id'))
