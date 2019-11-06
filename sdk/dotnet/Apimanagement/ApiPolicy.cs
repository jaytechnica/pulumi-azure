// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ApiManagement
{
    /// <summary>
    /// Manages an API Management API Policy
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_policy.html.markdown.
    /// </summary>
    public partial class ApiPolicy : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the API Management Service. Changing this forces a new resource to be created.
        /// </summary>
        [Output("apiManagementName")]
        public Output<string> ApiManagementName { get; private set; } = null!;

        /// <summary>
        /// The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.
        /// </summary>
        [Output("apiName")]
        public Output<string> ApiName { get; private set; } = null!;

        /// <summary>
        /// The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        [Output("xmlContent")]
        public Output<string> XmlContent { get; private set; } = null!;

        /// <summary>
        /// A link to a Policy XML Document, which must be publicly available.
        /// </summary>
        [Output("xmlLink")]
        public Output<string?> XmlLink { get; private set; } = null!;


        /// <summary>
        /// Create a ApiPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApiPolicy(string name, ApiPolicyArgs args, CustomResourceOptions? options = null)
            : base("azure:apimanagement/apiPolicy:ApiPolicy", name, args, MakeResourceOptions(options, ""))
        {
        }

        private ApiPolicy(string name, Input<string> id, ApiPolicyState? state = null, CustomResourceOptions? options = null)
            : base("azure:apimanagement/apiPolicy:ApiPolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApiPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApiPolicy Get(string name, Input<string> id, ApiPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new ApiPolicy(name, id, state, options);
        }
    }

    public sealed class ApiPolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the API Management Service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("apiManagementName", required: true)]
        public Input<string> ApiManagementName { get; set; } = null!;

        /// <summary>
        /// The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("apiName", required: true)]
        public Input<string> ApiName { get; set; } = null!;

        /// <summary>
        /// The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        [Input("xmlContent")]
        public Input<string>? XmlContent { get; set; }

        /// <summary>
        /// A link to a Policy XML Document, which must be publicly available.
        /// </summary>
        [Input("xmlLink")]
        public Input<string>? XmlLink { get; set; }

        public ApiPolicyArgs()
        {
        }
    }

    public sealed class ApiPolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the API Management Service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("apiManagementName")]
        public Input<string>? ApiManagementName { get; set; }

        /// <summary>
        /// The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("apiName")]
        public Input<string>? ApiName { get; set; }

        /// <summary>
        /// The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        [Input("xmlContent")]
        public Input<string>? XmlContent { get; set; }

        /// <summary>
        /// A link to a Policy XML Document, which must be publicly available.
        /// </summary>
        [Input("xmlLink")]
        public Input<string>? XmlLink { get; set; }

        public ApiPolicyState()
        {
        }
    }
}
