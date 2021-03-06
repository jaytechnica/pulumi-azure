# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'CacheNfsTargetNamespaceJunction',
]

@pulumi.output_type
class CacheNfsTargetNamespaceJunction(dict):
    def __init__(__self__, *,
                 namespace_path: str,
                 nfs_export: str,
                 target_path: Optional[str] = None):
        """
        :param str namespace_path: The client-facing file path of this NFS target within the HPC Cache NFS Target.
        :param str nfs_export: The NFS export of this NFS target within the HPC Cache NFS Target.
        :param str target_path: The relative subdirectory path from the `nfs_export` to map to the `namespace_path`. Defaults to `""`, in which case the whole `nfs_export` is exported.
        """
        pulumi.set(__self__, "namespace_path", namespace_path)
        pulumi.set(__self__, "nfs_export", nfs_export)
        if target_path is not None:
            pulumi.set(__self__, "target_path", target_path)

    @property
    @pulumi.getter(name="namespacePath")
    def namespace_path(self) -> str:
        """
        The client-facing file path of this NFS target within the HPC Cache NFS Target.
        """
        return pulumi.get(self, "namespace_path")

    @property
    @pulumi.getter(name="nfsExport")
    def nfs_export(self) -> str:
        """
        The NFS export of this NFS target within the HPC Cache NFS Target.
        """
        return pulumi.get(self, "nfs_export")

    @property
    @pulumi.getter(name="targetPath")
    def target_path(self) -> Optional[str]:
        """
        The relative subdirectory path from the `nfs_export` to map to the `namespace_path`. Defaults to `""`, in which case the whole `nfs_export` is exported.
        """
        return pulumi.get(self, "target_path")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


