# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetRoleDefinitionResult(object):
    """
    A collection of values returned by getRoleDefinition.
    """
    def __init__(__self__, assignable_scopes=None, description=None, name=None, permissions=None, type=None):
        if not assignable_scopes:
            raise TypeError('Missing required argument assignable_scopes')
        elif not isinstance(assignable_scopes, list):
            raise TypeError('Expected argument assignable_scopes to be a list')
        __self__.assignable_scopes = assignable_scopes
        """
        One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
        """
        if not description:
            raise TypeError('Missing required argument description')
        elif not isinstance(description, basestring):
            raise TypeError('Expected argument description to be a basestring')
        __self__.description = description
        """
        the Description of the built-in Role.
        """
        if not name:
            raise TypeError('Missing required argument name')
        elif not isinstance(name, basestring):
            raise TypeError('Expected argument name to be a basestring')
        __self__.name = name
        if not permissions:
            raise TypeError('Missing required argument permissions')
        elif not isinstance(permissions, list):
            raise TypeError('Expected argument permissions to be a list')
        __self__.permissions = permissions
        """
        a `permissions` block as documented below.
        """
        if not type:
            raise TypeError('Missing required argument type')
        elif not isinstance(type, basestring):
            raise TypeError('Expected argument type to be a basestring')
        __self__.type = type
        """
        the Type of the Role.
        """

def get_role_definition(role_definition_id=None, scope=None):
    """
    Use this data source to access the properties of a custom Role Definition. To access information about a built-in Role Definition, [please see the `azurerm_builtin_role_definition` data source](builtin_role_definition.html) instead.
    """
    __args__ = dict()

    __args__['roleDefinitionId'] = role_definition_id
    __args__['scope'] = scope
    __ret__ = pulumi.runtime.invoke('azure:role/getRoleDefinition:getRoleDefinition', __args__)

    return GetRoleDefinitionResult(
        assignable_scopes=__ret__['assignableScopes'],
        description=__ret__['description'],
        name=__ret__['name'],
        permissions=__ret__['permissions'],
        type=__ret__['type'])