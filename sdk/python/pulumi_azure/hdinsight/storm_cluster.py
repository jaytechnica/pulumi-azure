# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['StormCluster']


class StormCluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 component_version: Optional[pulumi.Input[pulumi.InputType['StormClusterComponentVersionArgs']]] = None,
                 gateway: Optional[pulumi.Input[pulumi.InputType['StormClusterGatewayArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metastores: Optional[pulumi.Input[pulumi.InputType['StormClusterMetastoresArgs']]] = None,
                 monitor: Optional[pulumi.Input[pulumi.InputType['StormClusterMonitorArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[pulumi.InputType['StormClusterRolesArgs']]] = None,
                 storage_accounts: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['StormClusterStorageAccountArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 tls_min_version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a HDInsight Storm Cluster.

        !> **Note:** [HDInsight 3.6 is deprecated and will be retired on 2020-12-31 - HDInsight 4.0 no longer supports Storm Clusters](https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-component-versioning#available-versions) - as such this resource is deprecated and will be removed in the next major version of the Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_container = azure.storage.Container("exampleContainer",
            storage_account_name=example_account.name,
            container_access_type="private")
        example_storm_cluster = azure.hdinsight.StormCluster("exampleStormCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            cluster_version="3.6",
            tier="Standard",
            component_version=azure.hdinsight.StormClusterComponentVersionArgs(
                storm="1.1",
            ),
            gateway=azure.hdinsight.StormClusterGatewayArgs(
                enabled=True,
                username="acctestusrgw",
                password="Password123!",
            ),
            storage_accounts=[azure.hdinsight.StormClusterStorageAccountArgs(
                storage_container_id=example_container.id,
                storage_account_key=example_account.primary_access_key,
                is_default=True,
            )],
            roles=azure.hdinsight.StormClusterRolesArgs(
                head_node=azure.hdinsight.StormClusterRolesHeadNodeArgs(
                    vm_size="Standard_A3",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                ),
                worker_node=azure.hdinsight.StormClusterRolesWorkerNodeArgs(
                    vm_size="Standard_D3_V2",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                    target_instance_count=3,
                ),
                zookeeper_node=azure.hdinsight.StormClusterRolesZookeeperNodeArgs(
                    vm_size="Standard_A4_V2",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                ),
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['StormClusterComponentVersionArgs']] component_version: A `component_version` block as defined below.
        :param pulumi.Input[pulumi.InputType['StormClusterGatewayArgs']] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['StormClusterMetastoresArgs']] metastores: A `metastores` block as defined below.
        :param pulumi.Input[pulumi.InputType['StormClusterMonitorArgs']] monitor: A `monitor` block as defined below.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['StormClusterRolesArgs']] roles: A `roles` block as defined below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['StormClusterStorageAccountArgs']]]] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of Tags which should be assigned to this HDInsight Storm Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
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

            if cluster_version is None:
                raise TypeError("Missing required property 'cluster_version'")
            __props__['cluster_version'] = cluster_version
            if component_version is None:
                raise TypeError("Missing required property 'component_version'")
            __props__['component_version'] = component_version
            if gateway is None:
                raise TypeError("Missing required property 'gateway'")
            __props__['gateway'] = gateway
            __props__['location'] = location
            __props__['metastores'] = metastores
            __props__['monitor'] = monitor
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if roles is None:
                raise TypeError("Missing required property 'roles'")
            __props__['roles'] = roles
            __props__['storage_accounts'] = storage_accounts
            __props__['tags'] = tags
            if tier is None:
                raise TypeError("Missing required property 'tier'")
            __props__['tier'] = tier
            __props__['tls_min_version'] = tls_min_version
            __props__['https_endpoint'] = None
            __props__['ssh_endpoint'] = None
        super(StormCluster, __self__).__init__(
            'azure:hdinsight/stormCluster:StormCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_version: Optional[pulumi.Input[str]] = None,
            component_version: Optional[pulumi.Input[pulumi.InputType['StormClusterComponentVersionArgs']]] = None,
            gateway: Optional[pulumi.Input[pulumi.InputType['StormClusterGatewayArgs']]] = None,
            https_endpoint: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            metastores: Optional[pulumi.Input[pulumi.InputType['StormClusterMetastoresArgs']]] = None,
            monitor: Optional[pulumi.Input[pulumi.InputType['StormClusterMonitorArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[pulumi.InputType['StormClusterRolesArgs']]] = None,
            ssh_endpoint: Optional[pulumi.Input[str]] = None,
            storage_accounts: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['StormClusterStorageAccountArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tier: Optional[pulumi.Input[str]] = None,
            tls_min_version: Optional[pulumi.Input[str]] = None) -> 'StormCluster':
        """
        Get an existing StormCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['StormClusterComponentVersionArgs']] component_version: A `component_version` block as defined below.
        :param pulumi.Input[pulumi.InputType['StormClusterGatewayArgs']] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] https_endpoint: The HTTPS Connectivity Endpoint for this HDInsight Storm Cluster.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['StormClusterMetastoresArgs']] metastores: A `metastores` block as defined below.
        :param pulumi.Input[pulumi.InputType['StormClusterMonitorArgs']] monitor: A `monitor` block as defined below.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['StormClusterRolesArgs']] roles: A `roles` block as defined below.
        :param pulumi.Input[str] ssh_endpoint: The SSH Connectivity Endpoint for this HDInsight Storm Cluster.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['StormClusterStorageAccountArgs']]]] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of Tags which should be assigned to this HDInsight Storm Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_version"] = cluster_version
        __props__["component_version"] = component_version
        __props__["gateway"] = gateway
        __props__["https_endpoint"] = https_endpoint
        __props__["location"] = location
        __props__["metastores"] = metastores
        __props__["monitor"] = monitor
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["roles"] = roles
        __props__["ssh_endpoint"] = ssh_endpoint
        __props__["storage_accounts"] = storage_accounts
        __props__["tags"] = tags
        __props__["tier"] = tier
        __props__["tls_min_version"] = tls_min_version
        return StormCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Output[str]:
        """
        Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_version")

    @property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> pulumi.Output['outputs.StormClusterComponentVersion']:
        """
        A `component_version` block as defined below.
        """
        return pulumi.get(self, "component_version")

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output['outputs.StormClusterGateway']:
        """
        A `gateway` block as defined below.
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="httpsEndpoint")
    def https_endpoint(self) -> pulumi.Output[str]:
        """
        The HTTPS Connectivity Endpoint for this HDInsight Storm Cluster.
        """
        return pulumi.get(self, "https_endpoint")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metastores(self) -> pulumi.Output[Optional['outputs.StormClusterMetastores']]:
        """
        A `metastores` block as defined below.
        """
        return pulumi.get(self, "metastores")

    @property
    @pulumi.getter
    def monitor(self) -> pulumi.Output[Optional['outputs.StormClusterMonitor']]:
        """
        A `monitor` block as defined below.
        """
        return pulumi.get(self, "monitor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output['outputs.StormClusterRoles']:
        """
        A `roles` block as defined below.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="sshEndpoint")
    def ssh_endpoint(self) -> pulumi.Output[str]:
        """
        The SSH Connectivity Endpoint for this HDInsight Storm Cluster.
        """
        return pulumi.get(self, "ssh_endpoint")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> pulumi.Output[Optional[List['outputs.StormClusterStorageAccount']]]:
        """
        One or more `storage_account` block as defined below.
        """
        return pulumi.get(self, "storage_accounts")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of Tags which should be assigned to this HDInsight Storm Cluster.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[str]:
        """
        Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="tlsMinVersion")
    def tls_min_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "tls_min_version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

