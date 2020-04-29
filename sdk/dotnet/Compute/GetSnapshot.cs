// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Compute
{
    public static class GetSnapshot
    {
        /// <summary>
        /// Use this data source to access information about an existing Snapshot.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSnapshotResult> InvokeAsync(GetSnapshotArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSnapshotResult>("azure:compute/getSnapshot:getSnapshot", args ?? new GetSnapshotArgs(), options.WithVersion());
    }


    public sealed class GetSnapshotArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specifies the name of the Snapshot.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// Specifies the name of the resource group the Snapshot is located in.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        public GetSnapshotArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSnapshotResult
    {
        public readonly string CreationOption;
        /// <summary>
        /// The size of the Snapshotted Disk in GB.
        /// </summary>
        public readonly int DiskSizeGb;
        public readonly ImmutableArray<Outputs.GetSnapshotEncryptionSettingResult> EncryptionSettings;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string OsType;
        public readonly string ResourceGroupName;
        /// <summary>
        /// The reference to an existing snapshot.
        /// </summary>
        public readonly string SourceResourceId;
        /// <summary>
        /// The URI to a Managed or Unmanaged Disk.
        /// </summary>
        public readonly string SourceUri;
        /// <summary>
        /// The ID of an storage account.
        /// </summary>
        public readonly string StorageAccountId;
        public readonly string TimeCreated;

        [OutputConstructor]
        private GetSnapshotResult(
            string creationOption,

            int diskSizeGb,

            ImmutableArray<Outputs.GetSnapshotEncryptionSettingResult> encryptionSettings,

            string id,

            string name,

            string osType,

            string resourceGroupName,

            string sourceResourceId,

            string sourceUri,

            string storageAccountId,

            string timeCreated)
        {
            CreationOption = creationOption;
            DiskSizeGb = diskSizeGb;
            EncryptionSettings = encryptionSettings;
            Id = id;
            Name = name;
            OsType = osType;
            ResourceGroupName = resourceGroupName;
            SourceResourceId = sourceResourceId;
            SourceUri = sourceUri;
            StorageAccountId = storageAccountId;
            TimeCreated = timeCreated;
        }
    }
}
