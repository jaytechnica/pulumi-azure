# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class KubernetesClusterNodePool(pulumi.CustomResource):
    availability_zones: pulumi.Output[list]
    """
    A list of Availability Zones where the Nodes in this Node Pool should be created in.
    """
    enable_auto_scaling: pulumi.Output[bool]
    """
    Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.
    """
    enable_node_public_ip: pulumi.Output[bool]
    """
    Should each node have a Public IP Address? Defaults to `false`.
    """
    eviction_policy: pulumi.Output[str]
    """
    The Eviction Policy which should be used for Virtual Machines within the Virtual Machine Scale Set powering this Node Pool. Possible values are `Deallocate` and `Delete`. Changing this forces a new resource to be created.
    """
    kubernetes_cluster_id: pulumi.Output[str]
    """
    The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.
    """
    max_count: pulumi.Output[float]
    """
    The maximum number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be greater than or equal to `min_count`.
    """
    max_pods: pulumi.Output[float]
    """
    The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
    """
    min_count: pulumi.Output[float]
    """
    The minimum number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be less than or equal to `max_count`.
    """
    mode: pulumi.Output[str]
    """
    Should this Node Pool be used for System or User resources? Possible values are `System` and `User`. Defaults to `User`.
    """
    name: pulumi.Output[str]
    """
    The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.
    """
    node_count: pulumi.Output[float]
    """
    The initial number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be a value in the range `min_count` - `max_count`.
    """
    node_labels: pulumi.Output[dict]
    """
    A map of Kubernetes labels which should be applied to nodes in this Node Pool. Changing this forces a new resource to be created.
    """
    node_taints: pulumi.Output[list]
    """
    A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`). Changing this forces a new resource to be created.
    """
    orchestrator_version: pulumi.Output[str]
    """
    Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade)
    """
    os_disk_size_gb: pulumi.Output[float]
    """
    The Agent Operating System disk size in GB. Changing this forces a new resource to be created.
    """
    os_type: pulumi.Output[str]
    """
    The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.
    """
    priority: pulumi.Output[str]
    """
    The Priority for Virtual Machines within the Virtual Machine Scale Set that powers this Node Pool. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.
    """
    spot_max_price: pulumi.Output[float]
    """
    The maximum price you're willing to pay in USD per Virtual Machine. Valid values are `-1` (the current on-demand price for a Virtual Machine) or a positive value with up to five decimal places. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    vm_size: pulumi.Output[str]
    """
    The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.
    """
    vnet_subnet_id: pulumi.Output[str]
    """
    The ID of the Subnet where this Node Pool should exist.
    """
    def __init__(__self__, resource_name, opts=None, availability_zones=None, enable_auto_scaling=None, enable_node_public_ip=None, eviction_policy=None, kubernetes_cluster_id=None, max_count=None, max_pods=None, min_count=None, mode=None, name=None, node_count=None, node_labels=None, node_taints=None, orchestrator_version=None, os_disk_size_gb=None, os_type=None, priority=None, spot_max_price=None, tags=None, vm_size=None, vnet_subnet_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a KubernetesClusterNodePool resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] availability_zones: A list of Availability Zones where the Nodes in this Node Pool should be created in.
        :param pulumi.Input[bool] enable_auto_scaling: Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.
        :param pulumi.Input[bool] enable_node_public_ip: Should each node have a Public IP Address? Defaults to `false`.
        :param pulumi.Input[str] eviction_policy: The Eviction Policy which should be used for Virtual Machines within the Virtual Machine Scale Set powering this Node Pool. Possible values are `Deallocate` and `Delete`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kubernetes_cluster_id: The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[float] max_count: The maximum number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be greater than or equal to `min_count`.
        :param pulumi.Input[float] max_pods: The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
        :param pulumi.Input[float] min_count: The minimum number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be less than or equal to `max_count`.
        :param pulumi.Input[str] mode: Should this Node Pool be used for System or User resources? Possible values are `System` and `User`. Defaults to `User`.
        :param pulumi.Input[str] name: The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[float] node_count: The initial number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be a value in the range `min_count` - `max_count`.
        :param pulumi.Input[dict] node_labels: A map of Kubernetes labels which should be applied to nodes in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[list] node_taints: A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`). Changing this forces a new resource to be created.
        :param pulumi.Input[str] orchestrator_version: Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade)
        :param pulumi.Input[float] os_disk_size_gb: The Agent Operating System disk size in GB. Changing this forces a new resource to be created.
        :param pulumi.Input[str] os_type: The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.
        :param pulumi.Input[str] priority: The Priority for Virtual Machines within the Virtual Machine Scale Set that powers this Node Pool. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.
        :param pulumi.Input[float] spot_max_price: The maximum price you're willing to pay in USD per Virtual Machine. Valid values are `-1` (the current on-demand price for a Virtual Machine) or a positive value with up to five decimal places. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] vm_size: The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[str] vnet_subnet_id: The ID of the Subnet where this Node Pool should exist.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['availability_zones'] = availability_zones
            __props__['enable_auto_scaling'] = enable_auto_scaling
            __props__['enable_node_public_ip'] = enable_node_public_ip
            __props__['eviction_policy'] = eviction_policy
            if kubernetes_cluster_id is None:
                raise TypeError("Missing required property 'kubernetes_cluster_id'")
            __props__['kubernetes_cluster_id'] = kubernetes_cluster_id
            __props__['max_count'] = max_count
            __props__['max_pods'] = max_pods
            __props__['min_count'] = min_count
            __props__['mode'] = mode
            __props__['name'] = name
            __props__['node_count'] = node_count
            __props__['node_labels'] = node_labels
            __props__['node_taints'] = node_taints
            __props__['orchestrator_version'] = orchestrator_version
            __props__['os_disk_size_gb'] = os_disk_size_gb
            __props__['os_type'] = os_type
            __props__['priority'] = priority
            __props__['spot_max_price'] = spot_max_price
            __props__['tags'] = tags
            if vm_size is None:
                raise TypeError("Missing required property 'vm_size'")
            __props__['vm_size'] = vm_size
            __props__['vnet_subnet_id'] = vnet_subnet_id
        super(KubernetesClusterNodePool, __self__).__init__(
            'azure:containerservice/kubernetesClusterNodePool:KubernetesClusterNodePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, availability_zones=None, enable_auto_scaling=None, enable_node_public_ip=None, eviction_policy=None, kubernetes_cluster_id=None, max_count=None, max_pods=None, min_count=None, mode=None, name=None, node_count=None, node_labels=None, node_taints=None, orchestrator_version=None, os_disk_size_gb=None, os_type=None, priority=None, spot_max_price=None, tags=None, vm_size=None, vnet_subnet_id=None):
        """
        Get an existing KubernetesClusterNodePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] availability_zones: A list of Availability Zones where the Nodes in this Node Pool should be created in.
        :param pulumi.Input[bool] enable_auto_scaling: Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.
        :param pulumi.Input[bool] enable_node_public_ip: Should each node have a Public IP Address? Defaults to `false`.
        :param pulumi.Input[str] eviction_policy: The Eviction Policy which should be used for Virtual Machines within the Virtual Machine Scale Set powering this Node Pool. Possible values are `Deallocate` and `Delete`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kubernetes_cluster_id: The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[float] max_count: The maximum number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be greater than or equal to `min_count`.
        :param pulumi.Input[float] max_pods: The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
        :param pulumi.Input[float] min_count: The minimum number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be less than or equal to `max_count`.
        :param pulumi.Input[str] mode: Should this Node Pool be used for System or User resources? Possible values are `System` and `User`. Defaults to `User`.
        :param pulumi.Input[str] name: The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[float] node_count: The initial number of nodes which should exist within this Node Pool. Valid values are between `1` and `100` and must be a value in the range `min_count` - `max_count`.
        :param pulumi.Input[dict] node_labels: A map of Kubernetes labels which should be applied to nodes in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[list] node_taints: A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`). Changing this forces a new resource to be created.
        :param pulumi.Input[str] orchestrator_version: Version of Kubernetes used for the Agents. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade)
        :param pulumi.Input[float] os_disk_size_gb: The Agent Operating System disk size in GB. Changing this forces a new resource to be created.
        :param pulumi.Input[str] os_type: The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.
        :param pulumi.Input[str] priority: The Priority for Virtual Machines within the Virtual Machine Scale Set that powers this Node Pool. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.
        :param pulumi.Input[float] spot_max_price: The maximum price you're willing to pay in USD per Virtual Machine. Valid values are `-1` (the current on-demand price for a Virtual Machine) or a positive value with up to five decimal places. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] vm_size: The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.
        :param pulumi.Input[str] vnet_subnet_id: The ID of the Subnet where this Node Pool should exist.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["availability_zones"] = availability_zones
        __props__["enable_auto_scaling"] = enable_auto_scaling
        __props__["enable_node_public_ip"] = enable_node_public_ip
        __props__["eviction_policy"] = eviction_policy
        __props__["kubernetes_cluster_id"] = kubernetes_cluster_id
        __props__["max_count"] = max_count
        __props__["max_pods"] = max_pods
        __props__["min_count"] = min_count
        __props__["mode"] = mode
        __props__["name"] = name
        __props__["node_count"] = node_count
        __props__["node_labels"] = node_labels
        __props__["node_taints"] = node_taints
        __props__["orchestrator_version"] = orchestrator_version
        __props__["os_disk_size_gb"] = os_disk_size_gb
        __props__["os_type"] = os_type
        __props__["priority"] = priority
        __props__["spot_max_price"] = spot_max_price
        __props__["tags"] = tags
        __props__["vm_size"] = vm_size
        __props__["vnet_subnet_id"] = vnet_subnet_id
        return KubernetesClusterNodePool(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

