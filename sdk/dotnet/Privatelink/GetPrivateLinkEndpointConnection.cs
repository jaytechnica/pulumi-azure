// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.PrivateLink
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to access the connection status information about an existing Private Link Endpoint.
        /// 
        /// &gt; **NOTE** Private Link is currently in Public Preview.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/private_link_endpoint_connection.html.markdown.
        /// </summary>
        public static Task<GetPrivateLinkEndpointConnectionResult> GetPrivateLinkEndpointConnection(GetPrivateLinkEndpointConnectionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPrivateLinkEndpointConnectionResult>("azure:privatelink/getPrivateLinkEndpointConnection:getPrivateLinkEndpointConnection", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetPrivateLinkEndpointConnectionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the Name of the private link endpoint.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Specifies the Name of the Resource Group within which the private link endpoint exists.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public GetPrivateLinkEndpointConnectionArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetPrivateLinkEndpointConnectionResult
    {
        /// <summary>
        /// The supported Azure location where the resource exists.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// The name of the private linke endpoint.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<Outputs.GetPrivateLinkEndpointConnectionPrivateServiceConnectionsResult> PrivateServiceConnections;
        public readonly string ResourceGroupName;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetPrivateLinkEndpointConnectionResult(
            string location,
            string name,
            ImmutableArray<Outputs.GetPrivateLinkEndpointConnectionPrivateServiceConnectionsResult> privateServiceConnections,
            string resourceGroupName,
            string id)
        {
            Location = location;
            Name = name;
            PrivateServiceConnections = privateServiceConnections;
            ResourceGroupName = resourceGroupName;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetPrivateLinkEndpointConnectionPrivateServiceConnectionsResult
    {
        /// <summary>
        /// Specifies the Name of the private link endpoint.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The private IP address associated with the private link endpoint, note that you will have a private IP address assigned to the private link endpoint even if the connection request was `Rejected`.
        /// </summary>
        public readonly string PrivateIpAddress;
        /// <summary>
        /// Possible values are as follows:
        /// Value | Meaning
        /// -- | --
        /// `Auto-Approved` | The remote resource owner has added you to the `Auto-Approved` RBAC permission list for the remote resource, all private link endpoint connection requests will be automatically `Approved`.
        /// `Deleted state` | The resource owner has `Rejected` the private link endpoint connection request and has removed your private link endpoint request from the remote resource.
        /// `request/response message` | If you submitted a manual private link endpoint connection request, while in the `Pending` status the `request_response` will display the same text from your `request_message` in the `private_service_connection` block above. If the private link endpoint connection request was `Rejected` by the owner of the remote resource, the text for the rejection will be displayed as the `request_response` text, if the private link endpoint connection request was `Approved` by the owner of the remote resource, the text for the approval will be displayed as the `request_response` text
        /// </summary>
        public readonly string RequestResponse;
        /// <summary>
        /// The current status of the private link endpoint request, possible values will be `Pending`, `Approved`, `Rejected`, or `Disconnected`.
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private GetPrivateLinkEndpointConnectionPrivateServiceConnectionsResult(
            string name,
            string privateIpAddress,
            string requestResponse,
            string status)
        {
            Name = name;
            PrivateIpAddress = privateIpAddress;
            RequestResponse = requestResponse;
            Status = status;
        }
    }
    }
}