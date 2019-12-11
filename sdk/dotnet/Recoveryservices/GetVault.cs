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
        /// Use this data source to access information about an existing Recovery Services Vault.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_vault.html.markdown.
        /// </summary>
        public static Task<GetVaultResult> GetVault(GetVaultArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVaultResult>("azure:recoveryservices/getVault:getVault", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetVaultArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specifies the name of the Recovery Services Vault.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The name of the resource group in which the Recovery Services Vault resides.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        public GetVaultArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetVaultResult
    {
        /// <summary>
        /// The Azure location where the resource resides.
        /// </summary>
        public readonly string Location;
        public readonly string Name;
        public readonly string ResourceGroupName;
        /// <summary>
        /// The vault's current SKU.
        /// </summary>
        public readonly string Sku;
        /// <summary>
        /// A mapping of tags assigned to the resource.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Tags;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetVaultResult(
            string location,
            string name,
            string resourceGroupName,
            string sku,
            ImmutableDictionary<string, string> tags,
            string id)
        {
            Location = location;
            Name = name;
            ResourceGroupName = resourceGroupName;
            Sku = sku;
            Tags = tags;
            Id = id;
        }
    }
}
