// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.SiteRecovery
{
    /// <summary>
    /// Manages a VM replicated using Azure Site Recovery (Azure to Azure only). A replicated VM keeps a copiously updated image of the VM in another region in order to be able to start the VM in that region in case of a disaster.
    /// </summary>
    public partial class ReplicatedVM : Pulumi.CustomResource
    {
        /// <summary>
        /// One or more `managed_disk` block.
        /// </summary>
        [Output("managedDisks")]
        public Output<ImmutableArray<Outputs.ReplicatedVMManagedDisk>> ManagedDisks { get; private set; } = null!;

        /// <summary>
        /// The name of the network mapping.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// One or more `network_interface` block.
        /// </summary>
        [Output("networkInterfaces")]
        public Output<ImmutableArray<Outputs.ReplicatedVMNetworkInterface>> NetworkInterfaces { get; private set; } = null!;

        [Output("recoveryReplicationPolicyId")]
        public Output<string> RecoveryReplicationPolicyId { get; private set; } = null!;

        /// <summary>
        /// The name of the vault that should be updated.
        /// </summary>
        [Output("recoveryVaultName")]
        public Output<string> RecoveryVaultName { get; private set; } = null!;

        /// <summary>
        /// Name of the resource group where the vault that should be updated is located.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// Name of fabric that should contains this replication.
        /// </summary>
        [Output("sourceRecoveryFabricName")]
        public Output<string> SourceRecoveryFabricName { get; private set; } = null!;

        /// <summary>
        /// Name of the protection container to use.
        /// </summary>
        [Output("sourceRecoveryProtectionContainerName")]
        public Output<string> SourceRecoveryProtectionContainerName { get; private set; } = null!;

        /// <summary>
        /// Id of the VM to replicate
        /// </summary>
        [Output("sourceVmId")]
        public Output<string> SourceVmId { get; private set; } = null!;

        /// <summary>
        /// Id of availability set that the new VM should belong to when a failover is done.
        /// </summary>
        [Output("targetAvailabilitySetId")]
        public Output<string?> TargetAvailabilitySetId { get; private set; } = null!;

        /// <summary>
        /// Network to use when a failover is done (recommended to set if any network_interface is configured for failover).
        /// </summary>
        [Output("targetNetworkId")]
        public Output<string> TargetNetworkId { get; private set; } = null!;

        /// <summary>
        /// Id of fabric where the VM replication should be handled when a failover is done.
        /// </summary>
        [Output("targetRecoveryFabricId")]
        public Output<string> TargetRecoveryFabricId { get; private set; } = null!;

        /// <summary>
        /// Id of protection container where the VM replication should be created when a failover is done.
        /// </summary>
        [Output("targetRecoveryProtectionContainerId")]
        public Output<string> TargetRecoveryProtectionContainerId { get; private set; } = null!;

        /// <summary>
        /// Id of resource group where the VM should be created when a failover is done.
        /// </summary>
        [Output("targetResourceGroupId")]
        public Output<string> TargetResourceGroupId { get; private set; } = null!;


        /// <summary>
        /// Create a ReplicatedVM resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReplicatedVM(string name, ReplicatedVMArgs args, CustomResourceOptions? options = null)
            : base("azure:siterecovery/replicatedVM:ReplicatedVM", name, args ?? new ReplicatedVMArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReplicatedVM(string name, Input<string> id, ReplicatedVMState? state = null, CustomResourceOptions? options = null)
            : base("azure:siterecovery/replicatedVM:ReplicatedVM", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ReplicatedVM resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReplicatedVM Get(string name, Input<string> id, ReplicatedVMState? state = null, CustomResourceOptions? options = null)
        {
            return new ReplicatedVM(name, id, state, options);
        }
    }

    public sealed class ReplicatedVMArgs : Pulumi.ResourceArgs
    {
        [Input("managedDisks")]
        private InputList<Inputs.ReplicatedVMManagedDiskArgs>? _managedDisks;

        /// <summary>
        /// One or more `managed_disk` block.
        /// </summary>
        public InputList<Inputs.ReplicatedVMManagedDiskArgs> ManagedDisks
        {
            get => _managedDisks ?? (_managedDisks = new InputList<Inputs.ReplicatedVMManagedDiskArgs>());
            set => _managedDisks = value;
        }

        /// <summary>
        /// The name of the network mapping.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.ReplicatedVMNetworkInterfaceArgs>? _networkInterfaces;

        /// <summary>
        /// One or more `network_interface` block.
        /// </summary>
        public InputList<Inputs.ReplicatedVMNetworkInterfaceArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.ReplicatedVMNetworkInterfaceArgs>());
            set => _networkInterfaces = value;
        }

        [Input("recoveryReplicationPolicyId", required: true)]
        public Input<string> RecoveryReplicationPolicyId { get; set; } = null!;

        /// <summary>
        /// The name of the vault that should be updated.
        /// </summary>
        [Input("recoveryVaultName", required: true)]
        public Input<string> RecoveryVaultName { get; set; } = null!;

        /// <summary>
        /// Name of the resource group where the vault that should be updated is located.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// Name of fabric that should contains this replication.
        /// </summary>
        [Input("sourceRecoveryFabricName", required: true)]
        public Input<string> SourceRecoveryFabricName { get; set; } = null!;

        /// <summary>
        /// Name of the protection container to use.
        /// </summary>
        [Input("sourceRecoveryProtectionContainerName", required: true)]
        public Input<string> SourceRecoveryProtectionContainerName { get; set; } = null!;

        /// <summary>
        /// Id of the VM to replicate
        /// </summary>
        [Input("sourceVmId", required: true)]
        public Input<string> SourceVmId { get; set; } = null!;

        /// <summary>
        /// Id of availability set that the new VM should belong to when a failover is done.
        /// </summary>
        [Input("targetAvailabilitySetId")]
        public Input<string>? TargetAvailabilitySetId { get; set; }

        /// <summary>
        /// Network to use when a failover is done (recommended to set if any network_interface is configured for failover).
        /// </summary>
        [Input("targetNetworkId")]
        public Input<string>? TargetNetworkId { get; set; }

        /// <summary>
        /// Id of fabric where the VM replication should be handled when a failover is done.
        /// </summary>
        [Input("targetRecoveryFabricId", required: true)]
        public Input<string> TargetRecoveryFabricId { get; set; } = null!;

        /// <summary>
        /// Id of protection container where the VM replication should be created when a failover is done.
        /// </summary>
        [Input("targetRecoveryProtectionContainerId", required: true)]
        public Input<string> TargetRecoveryProtectionContainerId { get; set; } = null!;

        /// <summary>
        /// Id of resource group where the VM should be created when a failover is done.
        /// </summary>
        [Input("targetResourceGroupId", required: true)]
        public Input<string> TargetResourceGroupId { get; set; } = null!;

        public ReplicatedVMArgs()
        {
        }
    }

    public sealed class ReplicatedVMState : Pulumi.ResourceArgs
    {
        [Input("managedDisks")]
        private InputList<Inputs.ReplicatedVMManagedDiskGetArgs>? _managedDisks;

        /// <summary>
        /// One or more `managed_disk` block.
        /// </summary>
        public InputList<Inputs.ReplicatedVMManagedDiskGetArgs> ManagedDisks
        {
            get => _managedDisks ?? (_managedDisks = new InputList<Inputs.ReplicatedVMManagedDiskGetArgs>());
            set => _managedDisks = value;
        }

        /// <summary>
        /// The name of the network mapping.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.ReplicatedVMNetworkInterfaceGetArgs>? _networkInterfaces;

        /// <summary>
        /// One or more `network_interface` block.
        /// </summary>
        public InputList<Inputs.ReplicatedVMNetworkInterfaceGetArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.ReplicatedVMNetworkInterfaceGetArgs>());
            set => _networkInterfaces = value;
        }

        [Input("recoveryReplicationPolicyId")]
        public Input<string>? RecoveryReplicationPolicyId { get; set; }

        /// <summary>
        /// The name of the vault that should be updated.
        /// </summary>
        [Input("recoveryVaultName")]
        public Input<string>? RecoveryVaultName { get; set; }

        /// <summary>
        /// Name of the resource group where the vault that should be updated is located.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// Name of fabric that should contains this replication.
        /// </summary>
        [Input("sourceRecoveryFabricName")]
        public Input<string>? SourceRecoveryFabricName { get; set; }

        /// <summary>
        /// Name of the protection container to use.
        /// </summary>
        [Input("sourceRecoveryProtectionContainerName")]
        public Input<string>? SourceRecoveryProtectionContainerName { get; set; }

        /// <summary>
        /// Id of the VM to replicate
        /// </summary>
        [Input("sourceVmId")]
        public Input<string>? SourceVmId { get; set; }

        /// <summary>
        /// Id of availability set that the new VM should belong to when a failover is done.
        /// </summary>
        [Input("targetAvailabilitySetId")]
        public Input<string>? TargetAvailabilitySetId { get; set; }

        /// <summary>
        /// Network to use when a failover is done (recommended to set if any network_interface is configured for failover).
        /// </summary>
        [Input("targetNetworkId")]
        public Input<string>? TargetNetworkId { get; set; }

        /// <summary>
        /// Id of fabric where the VM replication should be handled when a failover is done.
        /// </summary>
        [Input("targetRecoveryFabricId")]
        public Input<string>? TargetRecoveryFabricId { get; set; }

        /// <summary>
        /// Id of protection container where the VM replication should be created when a failover is done.
        /// </summary>
        [Input("targetRecoveryProtectionContainerId")]
        public Input<string>? TargetRecoveryProtectionContainerId { get; set; }

        /// <summary>
        /// Id of resource group where the VM should be created when a failover is done.
        /// </summary>
        [Input("targetResourceGroupId")]
        public Input<string>? TargetResourceGroupId { get; set; }

        public ReplicatedVMState()
        {
        }
    }
}
