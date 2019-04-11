# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class JobCollection(pulumi.CustomResource):
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.
    """
    quota: pulumi.Output[dict]
    """
    Configures the Job collection quotas as documented in the `quota` block below. 
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.
    """
    sku: pulumi.Output[str]
    """
    Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.
    """
    state: pulumi.Output[str]
    """
    Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, location=None, name=None, quota=None, resource_group_name=None, sku=None, state=None, tags=None, __name__=None, __opts__=None):
        """
        Manages a Scheduler Job Collection.
        
        > **NOTE:** Support for Scheduler Job Collections has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] quota: Configures the Job collection quotas as documented in the `quota` block below. 
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.
        :param pulumi.Input[str] state: Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
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

        if location is None:
            raise TypeError("Missing required property 'location'")
        __props__['location'] = location

        __props__['name'] = name

        __props__['quota'] = quota

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        if sku is None:
            raise TypeError("Missing required property 'sku'")
        __props__['sku'] = sku

        __props__['state'] = state

        __props__['tags'] = tags

        super(JobCollection, __self__).__init__(
            'azure:scheduler/jobCollection:JobCollection',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

