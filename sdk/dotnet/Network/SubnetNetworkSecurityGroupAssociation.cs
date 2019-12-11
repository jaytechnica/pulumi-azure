// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network
{
    /// <summary>
    /// Associates a Network Security Group with a Subnet within a Virtual Network.
    /// 
    /// &gt; **NOTE:** Subnet `&lt;-&gt;` Network Security Group associations currently need to be configured on both this resource and using the `network_security_group_id` field on the `azure.network.Subnet` resource. The next major version of the AzureRM Provider (2.0) will remove the `network_security_group_id` field from the `azure.network.Subnet` resource such that this resource is used to link resources in future.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_network_security_group_association.html.markdown.
    /// </summary>
    public partial class SubnetNetworkSecurityGroupAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.
        /// </summary>
        [Output("networkSecurityGroupId")]
        public Output<string> NetworkSecurityGroupId { get; private set; } = null!;

        /// <summary>
        /// The ID of the Subnet. Changing this forces a new resource to be created.
        /// </summary>
        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;


        /// <summary>
        /// Create a SubnetNetworkSecurityGroupAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SubnetNetworkSecurityGroupAssociation(string name, SubnetNetworkSecurityGroupAssociationArgs args, CustomResourceOptions? options = null)
            : base("azure:network/subnetNetworkSecurityGroupAssociation:SubnetNetworkSecurityGroupAssociation", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private SubnetNetworkSecurityGroupAssociation(string name, Input<string> id, SubnetNetworkSecurityGroupAssociationState? state = null, CustomResourceOptions? options = null)
            : base("azure:network/subnetNetworkSecurityGroupAssociation:SubnetNetworkSecurityGroupAssociation", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SubnetNetworkSecurityGroupAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SubnetNetworkSecurityGroupAssociation Get(string name, Input<string> id, SubnetNetworkSecurityGroupAssociationState? state = null, CustomResourceOptions? options = null)
        {
            return new SubnetNetworkSecurityGroupAssociation(name, id, state, options);
        }
    }

    public sealed class SubnetNetworkSecurityGroupAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.
        /// </summary>
        [Input("networkSecurityGroupId", required: true)]
        public Input<string> NetworkSecurityGroupId { get; set; } = null!;

        /// <summary>
        /// The ID of the Subnet. Changing this forces a new resource to be created.
        /// </summary>
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        public SubnetNetworkSecurityGroupAssociationArgs()
        {
        }
    }

    public sealed class SubnetNetworkSecurityGroupAssociationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.
        /// </summary>
        [Input("networkSecurityGroupId")]
        public Input<string>? NetworkSecurityGroupId { get; set; }

        /// <summary>
        /// The ID of the Subnet. Changing this forces a new resource to be created.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public SubnetNetworkSecurityGroupAssociationState()
        {
        }
    }
}
