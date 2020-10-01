# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['ElasticPool']


class ElasticPool(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 license_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_size_bytes: Optional[pulumi.Input[int]] = None,
                 max_size_gb: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 per_database_settings: Optional[pulumi.Input[pulumi.InputType['ElasticPoolPerDatabaseSettingsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ElasticPoolSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows you to manage an Azure SQL Elastic Pool via the `v3.0` API which allows for `vCore` and `DTU` based configurations.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="westeurope")
        example_sql_server = azure.sql.SqlServer("exampleSqlServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="4dm1n157r470r",
            administrator_login_password="4-v3ry-53cr37-p455w0rd")
        example_elastic_pool = azure.mssql.ElasticPool("exampleElasticPool",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            server_name=example_sql_server.name,
            license_type="LicenseIncluded",
            max_size_gb=756,
            sku=azure.mssql.ElasticPoolSkuArgs(
                name="GP_Gen5",
                tier="GeneralPurpose",
                family="Gen5",
                capacity=4,
            ),
            per_database_settings=azure.mssql.ElasticPoolPerDatabaseSettingsArgs(
                min_capacity=0.25,
                max_capacity=4,
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] license_type: Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] max_size_bytes: The max data size of the elastic pool in bytes. Conflicts with `max_size_gb`.
        :param pulumi.Input[float] max_size_gb: The max data size of the elastic pool in gigabytes. Conflicts with `max_size_bytes`.
        :param pulumi.Input[str] name: The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ElasticPoolPerDatabaseSettingsArgs']] per_database_settings: A `per_database_settings` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.
        :param pulumi.Input[str] server_name: The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ElasticPoolSkuArgs']] sku: A `sku` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_redundant: Whether or not this elastic pool is zone redundant. `tier` needs to be `Premium` for `DTU` based  or `BusinessCritical` for `vCore` based `sku`. Defaults to `false`.
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

            __props__['license_type'] = license_type
            __props__['location'] = location
            __props__['max_size_bytes'] = max_size_bytes
            __props__['max_size_gb'] = max_size_gb
            __props__['name'] = name
            if per_database_settings is None:
                raise TypeError("Missing required property 'per_database_settings'")
            __props__['per_database_settings'] = per_database_settings
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if server_name is None:
                raise TypeError("Missing required property 'server_name'")
            __props__['server_name'] = server_name
            if sku is None:
                raise TypeError("Missing required property 'sku'")
            __props__['sku'] = sku
            __props__['tags'] = tags
            __props__['zone_redundant'] = zone_redundant
        super(ElasticPool, __self__).__init__(
            'azure:mssql/elasticPool:ElasticPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            license_type: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            max_size_bytes: Optional[pulumi.Input[int]] = None,
            max_size_gb: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            per_database_settings: Optional[pulumi.Input[pulumi.InputType['ElasticPoolPerDatabaseSettingsArgs']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            server_name: Optional[pulumi.Input[str]] = None,
            sku: Optional[pulumi.Input[pulumi.InputType['ElasticPoolSkuArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            zone_redundant: Optional[pulumi.Input[bool]] = None) -> 'ElasticPool':
        """
        Get an existing ElasticPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] license_type: Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] max_size_bytes: The max data size of the elastic pool in bytes. Conflicts with `max_size_gb`.
        :param pulumi.Input[float] max_size_gb: The max data size of the elastic pool in gigabytes. Conflicts with `max_size_bytes`.
        :param pulumi.Input[str] name: The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ElasticPoolPerDatabaseSettingsArgs']] per_database_settings: A `per_database_settings` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.
        :param pulumi.Input[str] server_name: The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ElasticPoolSkuArgs']] sku: A `sku` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] zone_redundant: Whether or not this elastic pool is zone redundant. `tier` needs to be `Premium` for `DTU` based  or `BusinessCritical` for `vCore` based `sku`. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["license_type"] = license_type
        __props__["location"] = location
        __props__["max_size_bytes"] = max_size_bytes
        __props__["max_size_gb"] = max_size_gb
        __props__["name"] = name
        __props__["per_database_settings"] = per_database_settings
        __props__["resource_group_name"] = resource_group_name
        __props__["server_name"] = server_name
        __props__["sku"] = sku
        __props__["tags"] = tags
        __props__["zone_redundant"] = zone_redundant
        return ElasticPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[str]:
        """
        Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> pulumi.Output[int]:
        """
        The max data size of the elastic pool in bytes. Conflicts with `max_size_gb`.
        """
        return pulumi.get(self, "max_size_bytes")

    @property
    @pulumi.getter(name="maxSizeGb")
    def max_size_gb(self) -> pulumi.Output[float]:
        """
        The max data size of the elastic pool in gigabytes. Conflicts with `max_size_bytes`.
        """
        return pulumi.get(self, "max_size_gb")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perDatabaseSettings")
    def per_database_settings(self) -> pulumi.Output['outputs.ElasticPoolPerDatabaseSettings']:
        """
        A `per_database_settings` block as defined below.
        """
        return pulumi.get(self, "per_database_settings")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[str]:
        """
        The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.ElasticPoolSku']:
        """
        A `sku` block as defined below.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not this elastic pool is zone redundant. `tier` needs to be `Premium` for `DTU` based  or `BusinessCritical` for `vCore` based `sku`. Defaults to `false`.
        """
        return pulumi.get(self, "zone_redundant")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

