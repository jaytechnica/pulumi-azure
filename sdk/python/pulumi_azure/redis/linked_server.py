# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['LinkedServer']


class LinkedServer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_redis_cache_id: Optional[pulumi.Input[str]] = None,
                 linked_redis_cache_location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_role: Optional[pulumi.Input[str]] = None,
                 target_redis_cache_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Redis Linked Server (ie Geo Location)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_primary_resource_group = azure.core.ResourceGroup("example-primaryResourceGroup", location="East US")
        example_primary_cache = azure.redis.Cache("example-primaryCache",
            location=example_primary_resource_group.location,
            resource_group_name=example_primary_resource_group.name,
            capacity=1,
            family="P",
            sku_name="Premium",
            enable_non_ssl_port=False,
            redis_configuration=azure.redis.CacheRedisConfigurationArgs(
                maxmemory_reserved=2,
                maxmemory_delta=2,
                maxmemory_policy="allkeys-lru",
            ))
        example_secondary_resource_group = azure.core.ResourceGroup("example-secondaryResourceGroup", location="West US")
        example_secondary_cache = azure.redis.Cache("example-secondaryCache",
            location=example_secondary_resource_group.location,
            resource_group_name=example_secondary_resource_group.name,
            capacity=1,
            family="P",
            sku_name="Premium",
            enable_non_ssl_port=False,
            redis_configuration=azure.redis.CacheRedisConfigurationArgs(
                maxmemory_reserved=2,
                maxmemory_delta=2,
                maxmemory_policy="allkeys-lru",
            ))
        example_link = azure.redis.LinkedServer("example-link",
            target_redis_cache_name=example_primary_cache.name,
            resource_group_name=example_primary_cache.resource_group_name,
            linked_redis_cache_id=example_secondary_cache.id,
            linked_redis_cache_location=example_secondary_cache.location,
            server_role="Secondary")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] linked_redis_cache_id: The ID of the linked Redis cache. Changing this forces a new Redis to be created.
        :param pulumi.Input[str] linked_redis_cache_location: The location of the linked Redis cache. Changing this forces a new Redis to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Redis caches exists. Changing this forces a new Redis to be created.
        :param pulumi.Input[str] server_role: The role of the linked Redis cache (eg "Secondary"). Changing this forces a new Redis to be created.
        :param pulumi.Input[str] target_redis_cache_name: The name of Redis cache to link with. Changing this forces a new Redis to be created. (eg The primary role)
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

            if linked_redis_cache_id is None:
                raise TypeError("Missing required property 'linked_redis_cache_id'")
            __props__['linked_redis_cache_id'] = linked_redis_cache_id
            if linked_redis_cache_location is None:
                raise TypeError("Missing required property 'linked_redis_cache_location'")
            __props__['linked_redis_cache_location'] = linked_redis_cache_location
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if server_role is None:
                raise TypeError("Missing required property 'server_role'")
            __props__['server_role'] = server_role
            if target_redis_cache_name is None:
                raise TypeError("Missing required property 'target_redis_cache_name'")
            __props__['target_redis_cache_name'] = target_redis_cache_name
            __props__['name'] = None
        super(LinkedServer, __self__).__init__(
            'azure:redis/linkedServer:LinkedServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            linked_redis_cache_id: Optional[pulumi.Input[str]] = None,
            linked_redis_cache_location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            server_role: Optional[pulumi.Input[str]] = None,
            target_redis_cache_name: Optional[pulumi.Input[str]] = None) -> 'LinkedServer':
        """
        Get an existing LinkedServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] linked_redis_cache_id: The ID of the linked Redis cache. Changing this forces a new Redis to be created.
        :param pulumi.Input[str] linked_redis_cache_location: The location of the linked Redis cache. Changing this forces a new Redis to be created.
        :param pulumi.Input[str] name: The name of the linked server.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Redis caches exists. Changing this forces a new Redis to be created.
        :param pulumi.Input[str] server_role: The role of the linked Redis cache (eg "Secondary"). Changing this forces a new Redis to be created.
        :param pulumi.Input[str] target_redis_cache_name: The name of Redis cache to link with. Changing this forces a new Redis to be created. (eg The primary role)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["linked_redis_cache_id"] = linked_redis_cache_id
        __props__["linked_redis_cache_location"] = linked_redis_cache_location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["server_role"] = server_role
        __props__["target_redis_cache_name"] = target_redis_cache_name
        return LinkedServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="linkedRedisCacheId")
    def linked_redis_cache_id(self) -> pulumi.Output[str]:
        """
        The ID of the linked Redis cache. Changing this forces a new Redis to be created.
        """
        return pulumi.get(self, "linked_redis_cache_id")

    @property
    @pulumi.getter(name="linkedRedisCacheLocation")
    def linked_redis_cache_location(self) -> pulumi.Output[str]:
        """
        The location of the linked Redis cache. Changing this forces a new Redis to be created.
        """
        return pulumi.get(self, "linked_redis_cache_location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the linked server.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Redis caches exists. Changing this forces a new Redis to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="serverRole")
    def server_role(self) -> pulumi.Output[str]:
        """
        The role of the linked Redis cache (eg "Secondary"). Changing this forces a new Redis to be created.
        """
        return pulumi.get(self, "server_role")

    @property
    @pulumi.getter(name="targetRedisCacheName")
    def target_redis_cache_name(self) -> pulumi.Output[str]:
        """
        The name of Redis cache to link with. Changing this forces a new Redis to be created. (eg The primary role)
        """
        return pulumi.get(self, "target_redis_cache_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

