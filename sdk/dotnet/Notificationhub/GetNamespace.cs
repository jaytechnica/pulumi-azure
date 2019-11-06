// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.NotificationHub
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to access information about an existing Notification Hub Namespace.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/notification_hub_namespace.html.markdown.
        /// </summary>
        public static Task<GetNamespaceResult> GetNamespace(GetNamespaceArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNamespaceResult>("azure:notificationhub/getNamespace:getNamespace", args, options.WithVersion());
    }

    public sealed class GetNamespaceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the Name of the Notification Hub Namespace.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Specifies the Name of the Resource Group within which the Notification Hub exists.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public GetNamespaceArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetNamespaceResult
    {
        /// <summary>
        /// Is this Notification Hub Namespace enabled?
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The Azure Region in which this Notification Hub Namespace exists.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// (Required) The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard.`
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The Type of Namespace, such as `Messaging` or `NotificationHub`.
        /// </summary>
        public readonly string NamespaceType;
        public readonly string ResourceGroupName;
        public readonly string ServicebusEndpoint;
        /// <summary>
        /// A `sku` block as defined below.
        /// </summary>
        public readonly Outputs.GetNamespaceSkuResult Sku;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetNamespaceResult(
            bool enabled,
            string location,
            string name,
            string namespaceType,
            string resourceGroupName,
            string servicebusEndpoint,
            Outputs.GetNamespaceSkuResult sku,
            string id)
        {
            Enabled = enabled;
            Location = location;
            Name = name;
            NamespaceType = namespaceType;
            ResourceGroupName = resourceGroupName;
            ServicebusEndpoint = servicebusEndpoint;
            Sku = sku;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetNamespaceSkuResult
    {
        /// <summary>
        /// Specifies the Name of the Notification Hub Namespace.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetNamespaceSkuResult(string name)
        {
            Name = name;
        }
    }
    }
}
