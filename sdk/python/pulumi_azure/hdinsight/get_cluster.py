# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
]

@pulumi.output_type
class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    def __init__(__self__, cluster_version=None, component_versions=None, edge_ssh_endpoint=None, gateways=None, https_endpoint=None, id=None, kind=None, location=None, name=None, resource_group_name=None, ssh_endpoint=None, tags=None, tier=None, tls_min_version=None):
        if cluster_version and not isinstance(cluster_version, str):
            raise TypeError("Expected argument 'cluster_version' to be a str")
        pulumi.set(__self__, "cluster_version", cluster_version)
        if component_versions and not isinstance(component_versions, dict):
            raise TypeError("Expected argument 'component_versions' to be a dict")
        pulumi.set(__self__, "component_versions", component_versions)
        if edge_ssh_endpoint and not isinstance(edge_ssh_endpoint, str):
            raise TypeError("Expected argument 'edge_ssh_endpoint' to be a str")
        pulumi.set(__self__, "edge_ssh_endpoint", edge_ssh_endpoint)
        if gateways and not isinstance(gateways, list):
            raise TypeError("Expected argument 'gateways' to be a list")
        pulumi.set(__self__, "gateways", gateways)
        if https_endpoint and not isinstance(https_endpoint, str):
            raise TypeError("Expected argument 'https_endpoint' to be a str")
        pulumi.set(__self__, "https_endpoint", https_endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if ssh_endpoint and not isinstance(ssh_endpoint, str):
            raise TypeError("Expected argument 'ssh_endpoint' to be a str")
        pulumi.set(__self__, "ssh_endpoint", ssh_endpoint)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)
        if tls_min_version and not isinstance(tls_min_version, str):
            raise TypeError("Expected argument 'tls_min_version' to be a str")
        pulumi.set(__self__, "tls_min_version", tls_min_version)

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> str:
        """
        The version of HDInsights which is used on this HDInsight Cluster.
        """
        return pulumi.get(self, "cluster_version")

    @property
    @pulumi.getter(name="componentVersions")
    def component_versions(self) -> Mapping[str, str]:
        """
        A map of versions of software used on this HDInsights Cluster.
        """
        return pulumi.get(self, "component_versions")

    @property
    @pulumi.getter(name="edgeSshEndpoint")
    def edge_ssh_endpoint(self) -> str:
        """
        The SSH Endpoint of the Edge Node for this HDInsight Cluster, if an Edge Node exists.
        """
        return pulumi.get(self, "edge_ssh_endpoint")

    @property
    @pulumi.getter
    def gateways(self) -> Sequence['outputs.GetClusterGatewayResult']:
        """
        A `gateway` block as defined below.
        """
        return pulumi.get(self, "gateways")

    @property
    @pulumi.getter(name="httpsEndpoint")
    def https_endpoint(self) -> str:
        """
        The HTTPS Endpoint for this HDInsight Cluster.
        """
        return pulumi.get(self, "https_endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of HDInsight Cluster this is, such as a Spark or Storm cluster.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region in which this HDInsight Cluster exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sshEndpoint")
    def ssh_endpoint(self) -> str:
        """
        The SSH Endpoint for this HDInsight Cluster.
        """
        return pulumi.get(self, "ssh_endpoint")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A map of tags assigned to the HDInsight Cluster.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        The SKU / Tier of this HDInsight Cluster.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="tlsMinVersion")
    def tls_min_version(self) -> str:
        """
        The minimal supported tls version.
        """
        return pulumi.get(self, "tls_min_version")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            cluster_version=self.cluster_version,
            component_versions=self.component_versions,
            edge_ssh_endpoint=self.edge_ssh_endpoint,
            gateways=self.gateways,
            https_endpoint=self.https_endpoint,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            ssh_endpoint=self.ssh_endpoint,
            tags=self.tags,
            tier=self.tier,
            tls_min_version=self.tls_min_version)


def get_cluster(name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Use this data source to access information about an existing HDInsight Cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.hdinsight.get_cluster(name="example",
        resource_group_name="example-resources")
    pulumi.export("httpsEndpoint", example.https_endpoint)
    ```


    :param str name: Specifies the name of this HDInsight Cluster.
    :param str resource_group_name: Specifies the name of the Resource Group in which this HDInsight Cluster exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:hdinsight/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        cluster_version=__ret__.cluster_version,
        component_versions=__ret__.component_versions,
        edge_ssh_endpoint=__ret__.edge_ssh_endpoint,
        gateways=__ret__.gateways,
        https_endpoint=__ret__.https_endpoint,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        resource_group_name=__ret__.resource_group_name,
        ssh_endpoint=__ret__.ssh_endpoint,
        tags=__ret__.tags,
        tier=__ret__.tier,
        tls_min_version=__ret__.tls_min_version)
