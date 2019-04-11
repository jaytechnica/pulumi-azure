# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Endpoint(pulumi.CustomResource):
    endpoint_location: pulumi.Output[str]
    """
    Specifies the Azure location of the Endpoint,
    this must be specified for Profiles using the `Performance` routing method
    if the Endpoint is of either type `nestedEndpoints` or `externalEndpoints`.
    For Endpoints of type `azureEndpoints` the value will be taken from the
    location of the Azure target resource.
    """
    endpoint_monitor_status: pulumi.Output[str]
    endpoint_status: pulumi.Output[str]
    """
    The status of the Endpoint, can be set to
    either `Enabled` or `Disabled`. Defaults to `Enabled`.
    """
    geo_mappings: pulumi.Output[list]
    """
    A list of Geographic Regions used to distribute traffic, such as `WORLD`, `UK` or `DE`. The same location can't be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault).
    """
    min_child_endpoints: pulumi.Output[float]
    """
    This argument specifies the minimum number
    of endpoints that must be ‘online’ in the child profile in order for the
    parent profile to direct traffic to any of the endpoints in that child
    profile. This argument only applies to Endpoints of type `nestedEndpoints`
    and defaults to `1`.
    """
    name: pulumi.Output[str]
    """
    The name of the Traffic Manager endpoint. Changing this forces a
    new resource to be created.
    """
    priority: pulumi.Output[float]
    """
    Specifies the priority of this Endpoint, this must be
    specified for Profiles using the `Priority` traffic routing method. Supports
    values between 1 and 1000, with no Endpoints sharing the same value. If
    omitted the value will be computed in order of creation.
    """
    profile_name: pulumi.Output[str]
    """
    The name of the Traffic Manager Profile to attach
    create the Traffic Manager endpoint.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to
    create the Traffic Manager endpoint.
    """
    target: pulumi.Output[str]
    """
    The FQDN DNS name of the target. This argument must be
    provided for an endpoint of type `externalEndpoints`, for other types it
    will be computed.
    """
    target_resource_id: pulumi.Output[str]
    """
    The resource id of an Azure resource to
    target. This argument must be provided for an endpoint of type
    `azureEndpoints` or `nestedEndpoints`.
    """
    type: pulumi.Output[str]
    """
    The Endpoint type, must be one of:
    - `azureEndpoints`
    - `externalEndpoints`
    - `nestedEndpoints`
    """
    weight: pulumi.Output[float]
    """
    Specifies how much traffic should be distributed to this
    endpoint, this must be specified for Profiles using the  `Weighted` traffic
    routing method. Supports values between 1 and 1000.
    """
    def __init__(__self__, resource_name, opts=None, endpoint_location=None, endpoint_status=None, geo_mappings=None, min_child_endpoints=None, name=None, priority=None, profile_name=None, resource_group_name=None, target=None, target_resource_id=None, type=None, weight=None, __name__=None, __opts__=None):
        """
        Manages a Traffic Manager Endpoint.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint_location: Specifies the Azure location of the Endpoint,
               this must be specified for Profiles using the `Performance` routing method
               if the Endpoint is of either type `nestedEndpoints` or `externalEndpoints`.
               For Endpoints of type `azureEndpoints` the value will be taken from the
               location of the Azure target resource.
        :param pulumi.Input[str] endpoint_status: The status of the Endpoint, can be set to
               either `Enabled` or `Disabled`. Defaults to `Enabled`.
        :param pulumi.Input[list] geo_mappings: A list of Geographic Regions used to distribute traffic, such as `WORLD`, `UK` or `DE`. The same location can't be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault).
        :param pulumi.Input[float] min_child_endpoints: This argument specifies the minimum number
               of endpoints that must be ‘online’ in the child profile in order for the
               parent profile to direct traffic to any of the endpoints in that child
               profile. This argument only applies to Endpoints of type `nestedEndpoints`
               and defaults to `1`.
        :param pulumi.Input[str] name: The name of the Traffic Manager endpoint. Changing this forces a
               new resource to be created.
        :param pulumi.Input[float] priority: Specifies the priority of this Endpoint, this must be
               specified for Profiles using the `Priority` traffic routing method. Supports
               values between 1 and 1000, with no Endpoints sharing the same value. If
               omitted the value will be computed in order of creation.
        :param pulumi.Input[str] profile_name: The name of the Traffic Manager Profile to attach
               create the Traffic Manager endpoint.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the Traffic Manager endpoint.
        :param pulumi.Input[str] target: The FQDN DNS name of the target. This argument must be
               provided for an endpoint of type `externalEndpoints`, for other types it
               will be computed.
        :param pulumi.Input[str] target_resource_id: The resource id of an Azure resource to
               target. This argument must be provided for an endpoint of type
               `azureEndpoints` or `nestedEndpoints`.
        :param pulumi.Input[str] type: The Endpoint type, must be one of:
               - `azureEndpoints`
               - `externalEndpoints`
               - `nestedEndpoints`
        :param pulumi.Input[float] weight: Specifies how much traffic should be distributed to this
               endpoint, this must be specified for Profiles using the  `Weighted` traffic
               routing method. Supports values between 1 and 1000.
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

        __props__['endpoint_location'] = endpoint_location

        __props__['endpoint_status'] = endpoint_status

        __props__['geo_mappings'] = geo_mappings

        __props__['min_child_endpoints'] = min_child_endpoints

        __props__['name'] = name

        __props__['priority'] = priority

        if profile_name is None:
            raise TypeError("Missing required property 'profile_name'")
        __props__['profile_name'] = profile_name

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        __props__['target'] = target

        __props__['target_resource_id'] = target_resource_id

        if type is None:
            raise TypeError("Missing required property 'type'")
        __props__['type'] = type

        __props__['weight'] = weight

        __props__['endpoint_monitor_status'] = None

        super(Endpoint, __self__).__init__(
            'azure:trafficmanager/endpoint:Endpoint',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

