# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class AutoscaleSetting(pulumi.CustomResource):
    enabled: pulumi.Output[bool]
    """
    Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name of the AutoScale Setting. Changing this forces a new resource to be created.
    """
    notification: pulumi.Output[dict]
    """
    Specifies a `notification` block as defined below.
    """
    profiles: pulumi.Output[list]
    """
    Specifies one or more (up to 20) `profile` blocks as defined below.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    target_resource_id: pulumi.Output[str]
    """
    Specifies the resource ID of the resource that the autoscale setting should be added to.
    """
    def __init__(__self__, resource_name, opts=None, enabled=None, location=None, name=None, notification=None, profiles=None, resource_group_name=None, tags=None, target_resource_id=None, __name__=None, __opts__=None):
        """
        Manages a AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the AutoScale Setting. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] notification: Specifies a `notification` block as defined below.
        :param pulumi.Input[list] profiles: Specifies one or more (up to 20) `profile` blocks as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] target_resource_id: Specifies the resource ID of the resource that the autoscale setting should be added to.
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

        __props__['enabled'] = enabled

        if location is None:
            raise TypeError("Missing required property 'location'")
        __props__['location'] = location

        __props__['name'] = name

        __props__['notification'] = notification

        if profiles is None:
            raise TypeError("Missing required property 'profiles'")
        __props__['profiles'] = profiles

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        __props__['tags'] = tags

        if target_resource_id is None:
            raise TypeError("Missing required property 'target_resource_id'")
        __props__['target_resource_id'] = target_resource_id

        super(AutoscaleSetting, __self__).__init__(
            'azure:monitoring/autoscaleSetting:AutoscaleSetting',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

