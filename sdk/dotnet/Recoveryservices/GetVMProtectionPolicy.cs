// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.RecoveryServices
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to access information about an existing Recovery Services VM Protection Policy.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_protection_policy_vm.html.markdown.
        /// </summary>
        public static Task<GetVMProtectionPolicyResult> GetVMProtectionPolicy(GetVMProtectionPolicyArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVMProtectionPolicyResult>("azure:recoveryservices/getVMProtectionPolicy:getVMProtectionPolicy", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetVMProtectionPolicyArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specifies the name of the Recovery Services VM Protection Policy.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// Specifies the name of the Recovery Services Vault.
        /// </summary>
        [Input("recoveryVaultName", required: true)]
        public string RecoveryVaultName { get; set; } = null!;

        /// <summary>
        /// The name of the resource group in which the Recovery Services VM Protection Policy resides.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        public GetVMProtectionPolicyArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetVMProtectionPolicyResult
    {
        public readonly string Name;
        public readonly string RecoveryVaultName;
        public readonly string ResourceGroupName;
        /// <summary>
        /// A mapping of tags assigned to the resource.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Tags;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetVMProtectionPolicyResult(
            string name,
            string recoveryVaultName,
            string resourceGroupName,
            ImmutableDictionary<string, string> tags,
            string id)
        {
            Name = name;
            RecoveryVaultName = recoveryVaultName;
            ResourceGroupName = resourceGroupName;
            Tags = tags;
            Id = id;
        }
    }
}
