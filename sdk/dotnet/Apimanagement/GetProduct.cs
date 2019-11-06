// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ApiManagement
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to access information about an existing API Management Product.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management_product.html.markdown.
        /// </summary>
        public static Task<GetProductResult> GetProduct(GetProductArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProductResult>("azure:apimanagement/getProduct:getProduct", args, options.WithVersion());
    }

    public sealed class GetProductArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Name of the API Management Service in which this Product exists.
        /// </summary>
        [Input("apiManagementName", required: true)]
        public Input<string> ApiManagementName { get; set; } = null!;

        /// <summary>
        /// The Identifier for the API Management Product.
        /// </summary>
        [Input("productId", required: true)]
        public Input<string> ProductId { get; set; } = null!;

        /// <summary>
        /// The Name of the Resource Group in which the API Management Service exists.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public GetProductArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetProductResult
    {
        public readonly string ApiManagementName;
        /// <summary>
        /// Do subscribers need to be approved prior to being able to use the Product?
        /// </summary>
        public readonly bool ApprovalRequired;
        /// <summary>
        /// The description of this Product, which may include HTML formatting tags.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The Display Name for this API Management Product.
        /// </summary>
        public readonly string DisplayName;
        public readonly string ProductId;
        /// <summary>
        /// Is this Product Published?
        /// </summary>
        public readonly bool Published;
        public readonly string ResourceGroupName;
        /// <summary>
        /// Is a Subscription required to access API's included in this Product?
        /// </summary>
        public readonly bool SubscriptionRequired;
        /// <summary>
        /// The number of subscriptions a user can have to this Product at the same time.
        /// </summary>
        public readonly int SubscriptionsLimit;
        /// <summary>
        /// Any Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.
        /// </summary>
        public readonly string Terms;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetProductResult(
            string apiManagementName,
            bool approvalRequired,
            string description,
            string displayName,
            string productId,
            bool published,
            string resourceGroupName,
            bool subscriptionRequired,
            int subscriptionsLimit,
            string terms,
            string id)
        {
            ApiManagementName = apiManagementName;
            ApprovalRequired = approvalRequired;
            Description = description;
            DisplayName = displayName;
            ProductId = productId;
            Published = published;
            ResourceGroupName = resourceGroupName;
            SubscriptionRequired = subscriptionRequired;
            SubscriptionsLimit = subscriptionsLimit;
            Terms = terms;
            Id = id;
        }
    }
}
