# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ApplicationGroup']


class ApplicationGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pool_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Virtual Desktop Application Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example", location="eastus")
        pooledbreadthfirst = azure.desktopvirtualization.HostPool("pooledbreadthfirst",
            location=example.location,
            resource_group_name=example.name,
            type="Pooled",
            load_balancer_type="BreadthFirst")
        personalautomatic = azure.desktopvirtualization.HostPool("personalautomatic",
            location=example.location,
            resource_group_name=example.name,
            type="Personal",
            personal_desktop_assignment_type="Automatic")
        remoteapp = azure.desktopvirtualization.ApplicationGroup("remoteapp",
            location=example.location,
            resource_group_name=example.name,
            type="RemoteApp",
            host_pool_id=pooledbreadthfirst.id,
            friendly_name="TestAppGroup",
            description="Acceptance Test: An application group")
        desktopapp = azure.desktopvirtualization.ApplicationGroup("desktopapp",
            location=example.location,
            resource_group_name=example.name,
            type="Desktop",
            host_pool_id=personalautomatic.id,
            friendly_name="TestAppGroup",
            description="Acceptance Test: An application group")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Option to set a description for the Virtual Desktop Application Group.
        :param pulumi.Input[str] friendly_name: Option to set a friendly name for the Virtual Desktop Application Group.
        :param pulumi.Input[str] host_pool_id: Resource ID for a Virtual Desktop Host Pool to associate with the
               Virtual Desktop Application Group.
        :param pulumi.Input[str] location: The location/region where the Virtual Desktop Application Group is
               located. Changing the location/region forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Virtual Desktop Application Group. Changing the name forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the Virtual Desktop Application Group. Changing the resource group name forces
               a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] type: Type of Virtual Desktop Application Group.
               Valid options are `RemoteApp` or `Desktop` application groups.
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

            __props__['description'] = description
            __props__['friendly_name'] = friendly_name
            if host_pool_id is None:
                raise TypeError("Missing required property 'host_pool_id'")
            __props__['host_pool_id'] = host_pool_id
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
        super(ApplicationGroup, __self__).__init__(
            'azure:desktopvirtualization/applicationGroup:ApplicationGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            friendly_name: Optional[pulumi.Input[str]] = None,
            host_pool_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'ApplicationGroup':
        """
        Get an existing ApplicationGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Option to set a description for the Virtual Desktop Application Group.
        :param pulumi.Input[str] friendly_name: Option to set a friendly name for the Virtual Desktop Application Group.
        :param pulumi.Input[str] host_pool_id: Resource ID for a Virtual Desktop Host Pool to associate with the
               Virtual Desktop Application Group.
        :param pulumi.Input[str] location: The location/region where the Virtual Desktop Application Group is
               located. Changing the location/region forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Virtual Desktop Application Group. Changing the name forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the Virtual Desktop Application Group. Changing the resource group name forces
               a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] type: Type of Virtual Desktop Application Group.
               Valid options are `RemoteApp` or `Desktop` application groups.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["friendly_name"] = friendly_name
        __props__["host_pool_id"] = host_pool_id
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        __props__["type"] = type
        return ApplicationGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Option to set a description for the Virtual Desktop Application Group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        Option to set a friendly name for the Virtual Desktop Application Group.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPoolId")
    def host_pool_id(self) -> pulumi.Output[str]:
        """
        Resource ID for a Virtual Desktop Host Pool to associate with the
        Virtual Desktop Application Group.
        """
        return pulumi.get(self, "host_pool_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location/region where the Virtual Desktop Application Group is
        located. Changing the location/region forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Virtual Desktop Application Group. Changing the name forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to
        create the Virtual Desktop Application Group. Changing the resource group name forces
        a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of Virtual Desktop Application Group.
        Valid options are `RemoteApp` or `Desktop` application groups.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

