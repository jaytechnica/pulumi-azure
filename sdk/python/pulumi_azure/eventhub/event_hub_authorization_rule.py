# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class EventHubAuthorizationRule(pulumi.CustomResource):
    eventhub_name: pulumi.Output[str]
    """
    Specifies the name of the EventHub. Changing this forces a new resource to be created.
    """
    listen: pulumi.Output[bool]
    """
    Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.
    """
    location: pulumi.Output[str]
    manage: pulumi.Output[bool]
    """
    Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.
    """
    namespace_name: pulumi.Output[str]
    """
    Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.
    """
    primary_connection_string: pulumi.Output[str]
    """
    The Primary Connection String for the Event Hubs authorization Rule.
    """
    primary_key: pulumi.Output[str]
    """
    The Primary Key for the Event Hubs authorization Rule.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.
    """
    secondary_connection_string: pulumi.Output[str]
    """
    The Secondary Connection String for the Event Hubs authorization Rule.
    """
    secondary_key: pulumi.Output[str]
    """
    The Secondary Key for the Event Hubs authorization Rule.
    """
    send: pulumi.Output[bool]
    """
    Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.
    """
    def __init__(__self__, resource_name, opts=None, eventhub_name=None, listen=None, location=None, manage=None, name=None, namespace_name=None, resource_group_name=None, send=None, __name__=None, __opts__=None):
        """
        Manages a Event Hubs authorization Rule within an Event Hub.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] eventhub_name: Specifies the name of the EventHub. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] listen: Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.
        :param pulumi.Input[bool] manage: Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        :param pulumi.Input[str] name: Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] send: Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if eventhub_name is None:
            raise TypeError("Missing required property 'eventhub_name'")
        __props__['eventhub_name'] = eventhub_name

        __props__['listen'] = listen

        __props__['location'] = location

        __props__['manage'] = manage

        __props__['name'] = name

        if namespace_name is None:
            raise TypeError("Missing required property 'namespace_name'")
        __props__['namespace_name'] = namespace_name

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        __props__['send'] = send

        __props__['primary_connection_string'] = None
        __props__['primary_key'] = None
        __props__['secondary_connection_string'] = None
        __props__['secondary_key'] = None

        super(EventHubAuthorizationRule, __self__).__init__(
            'azure:eventhub/eventHubAuthorizationRule:EventHubAuthorizationRule',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

