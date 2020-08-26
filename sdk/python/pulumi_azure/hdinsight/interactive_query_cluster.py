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

__all__ = ['InteractiveQueryCluster']


class InteractiveQueryCluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 component_version: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterComponentVersionArgs']]] = None,
                 gateway: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterGatewayArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metastores: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterMetastoresArgs']]] = None,
                 monitor: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterMonitorArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterRolesArgs']]] = None,
                 storage_account_gen2: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountGen2Args']]] = None,
                 storage_accounts: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 tls_min_version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a HDInsight Interactive Query Cluster.

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
        example_interactive_query_cluster = azure.hdinsight.InteractiveQueryCluster("exampleInteractiveQueryCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            cluster_version="3.6",
            tier="Standard",
            component_version=azure.hdinsight.InteractiveQueryClusterComponentVersionArgs(
                interactive_hive="2.1",
            ),
            gateway=azure.hdinsight.InteractiveQueryClusterGatewayArgs(
                enabled=True,
                username="acctestusrgw",
                password="Password!",
            ),
            storage_accounts=[azure.hdinsight.InteractiveQueryClusterStorageAccountArgs(
                storage_container_id=example_container.id,
                storage_account_key=example_account.primary_access_key,
                is_default=True,
            )],
            roles=azure.hdinsight.InteractiveQueryClusterRolesArgs(
                head_node=azure.hdinsight.InteractiveQueryClusterRolesHeadNodeArgs(
                    vm_size="Standard_D13_V2",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                ),
                worker_node=azure.hdinsight.InteractiveQueryClusterRolesWorkerNodeArgs(
                    vm_size="Standard_D14_V2",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                    target_instance_count=3,
                ),
                zookeeper_node=azure.hdinsight.InteractiveQueryClusterRolesZookeeperNodeArgs(
                    vm_size="Standard_A4_V2",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                ),
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterComponentVersionArgs']] component_version: A `component_version` block as defined below.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterGatewayArgs']] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterMetastoresArgs']] metastores: A `metastores` block as defined below.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterMonitorArgs']] monitor: A `monitor` block as defined below.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterRolesArgs']] roles: A `roles` block as defined below.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountGen2Args']] storage_account_gen2: A `storage_account_gen2` block as defined below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountArgs']]]] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
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
            __props__['storage_account_gen2'] = storage_account_gen2
            __props__['storage_accounts'] = storage_accounts
            __props__['tags'] = tags
            if tier is None:
                raise TypeError("Missing required property 'tier'")
            __props__['tier'] = tier
            __props__['tls_min_version'] = tls_min_version
            __props__['https_endpoint'] = None
            __props__['ssh_endpoint'] = None
        super(InteractiveQueryCluster, __self__).__init__(
            'azure:hdinsight/interactiveQueryCluster:InteractiveQueryCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_version: Optional[pulumi.Input[str]] = None,
            component_version: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterComponentVersionArgs']]] = None,
            gateway: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterGatewayArgs']]] = None,
            https_endpoint: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            metastores: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterMetastoresArgs']]] = None,
            monitor: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterMonitorArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterRolesArgs']]] = None,
            ssh_endpoint: Optional[pulumi.Input[str]] = None,
            storage_account_gen2: Optional[pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountGen2Args']]] = None,
            storage_accounts: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tier: Optional[pulumi.Input[str]] = None,
            tls_min_version: Optional[pulumi.Input[str]] = None) -> 'InteractiveQueryCluster':
        """
        Get an existing InteractiveQueryCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterComponentVersionArgs']] component_version: A `component_version` block as defined below.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterGatewayArgs']] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] https_endpoint: The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterMetastoresArgs']] metastores: A `metastores` block as defined below.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterMonitorArgs']] monitor: A `monitor` block as defined below.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterRolesArgs']] roles: A `roles` block as defined below.
        :param pulumi.Input[str] ssh_endpoint: The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
        :param pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountGen2Args']] storage_account_gen2: A `storage_account_gen2` block as defined below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['InteractiveQueryClusterStorageAccountArgs']]]] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
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
        __props__["storage_account_gen2"] = storage_account_gen2
        __props__["storage_accounts"] = storage_accounts
        __props__["tags"] = tags
        __props__["tier"] = tier
        __props__["tls_min_version"] = tls_min_version
        return InteractiveQueryCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Output[str]:
        """
        Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_version")

    @property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> pulumi.Output['outputs.InteractiveQueryClusterComponentVersion']:
        """
        A `component_version` block as defined below.
        """
        return pulumi.get(self, "component_version")

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output['outputs.InteractiveQueryClusterGateway']:
        """
        A `gateway` block as defined below.
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="httpsEndpoint")
    def https_endpoint(self) -> pulumi.Output[str]:
        """
        The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
        """
        return pulumi.get(self, "https_endpoint")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metastores(self) -> pulumi.Output[Optional['outputs.InteractiveQueryClusterMetastores']]:
        """
        A `metastores` block as defined below.
        """
        return pulumi.get(self, "metastores")

    @property
    @pulumi.getter
    def monitor(self) -> pulumi.Output[Optional['outputs.InteractiveQueryClusterMonitor']]:
        """
        A `monitor` block as defined below.
        """
        return pulumi.get(self, "monitor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output['outputs.InteractiveQueryClusterRoles']:
        """
        A `roles` block as defined below.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="sshEndpoint")
    def ssh_endpoint(self) -> pulumi.Output[str]:
        """
        The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
        """
        return pulumi.get(self, "ssh_endpoint")

    @property
    @pulumi.getter(name="storageAccountGen2")
    def storage_account_gen2(self) -> pulumi.Output[Optional['outputs.InteractiveQueryClusterStorageAccountGen2']]:
        """
        A `storage_account_gen2` block as defined below.
        """
        return pulumi.get(self, "storage_account_gen2")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> pulumi.Output[Optional[List['outputs.InteractiveQueryClusterStorageAccount']]]:
        """
        One or more `storage_account` block as defined below.
        """
        return pulumi.get(self, "storage_accounts")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[str]:
        """
        Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
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

