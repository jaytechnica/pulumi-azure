// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.AD
{
    public static partial class Invokes
    {
        /// <summary>
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/azuread_service_principal.html.markdown.
        /// </summary>
        public static Task<GetServicePrincipalResult> GetServicePrincipal(GetServicePrincipalArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetServicePrincipalResult>("azure:ad/getServicePrincipal:getServicePrincipal", args, options.WithVersion());
    }

    public sealed class GetServicePrincipalArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Azure AD Application for which to create a Service Principal.
        /// </summary>
        [Input("applicationId")]
        public Input<string>? ApplicationId { get; set; }

        /// <summary>
        /// The Display Name of the Azure AD Application associated with this Service Principal.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The ID of the Azure AD Service Principal.
        /// </summary>
        [Input("objectId")]
        public Input<string>? ObjectId { get; set; }

        public GetServicePrincipalArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetServicePrincipalResult
    {
        public readonly string ApplicationId;
        public readonly string DisplayName;
        public readonly string ObjectId;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetServicePrincipalResult(
            string applicationId,
            string displayName,
            string objectId,
            string id)
        {
            ApplicationId = applicationId;
            DisplayName = displayName;
            ObjectId = objectId;
            Id = id;
        }
    }
}
