// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Authorization
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to access information about an existing User Assigned Identity.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/user_assigned_identity.html.markdown.
        /// </summary>
        public static Task<GetUserAssignedIdentityResult> GetUserAssignedIdentity(GetUserAssignedIdentityArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetUserAssignedIdentityResult>("azure:authorization/getUserAssignedIdentity:getUserAssignedIdentity", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetUserAssignedIdentityArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the User Assigned Identity.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The name of the Resource Group in which the User Assigned Identity exists.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        public GetUserAssignedIdentityArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetUserAssignedIdentityResult
    {
        /// <summary>
        /// The Client ID of the User Assigned Identity.
        /// </summary>
        public readonly string ClientId;
        /// <summary>
        /// The Azure location where the User Assigned Identity exists.
        /// </summary>
        public readonly string Location;
        public readonly string Name;
        /// <summary>
        /// The Service Principal ID of the User Assigned Identity.
        /// </summary>
        public readonly string PrincipalId;
        public readonly string ResourceGroupName;
        /// <summary>
        /// A mapping of tags assigned to the User Assigned Identity.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Tags;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetUserAssignedIdentityResult(
            string clientId,
            string location,
            string name,
            string principalId,
            string resourceGroupName,
            ImmutableDictionary<string, string> tags,
            string id)
        {
            ClientId = clientId;
            Location = location;
            Name = name;
            PrincipalId = principalId;
            ResourceGroupName = resourceGroupName;
            Tags = tags;
            Id = id;
        }
    }
}
