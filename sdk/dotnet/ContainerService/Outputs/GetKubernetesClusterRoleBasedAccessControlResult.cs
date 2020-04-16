// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ContainerService.Outputs
{

    [OutputType]
    public sealed class GetKubernetesClusterRoleBasedAccessControlResult
    {
        /// <summary>
        /// A `azure_active_directory` block as documented above.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetKubernetesClusterRoleBasedAccessControlAzureActiveDirectoryResult> AzureActiveDirectories;
        /// <summary>
        /// Is Role Based Access Control enabled?
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private GetKubernetesClusterRoleBasedAccessControlResult(
            ImmutableArray<Outputs.GetKubernetesClusterRoleBasedAccessControlAzureActiveDirectoryResult> azureActiveDirectories,

            bool enabled)
        {
            AzureActiveDirectories = azureActiveDirectories;
            Enabled = enabled;
        }
    }
}