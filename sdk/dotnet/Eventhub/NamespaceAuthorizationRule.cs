// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.EventHub
{
    /// <summary>
    /// Manages a ServiceBus Namespace authorization Rule within a ServiceBus.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_namespace_authorization_rule_legacy.html.markdown.
    /// </summary>
    public partial class NamespaceAuthorizationRule : Pulumi.CustomResource
    {
        /// <summary>
        /// Grants listen access to this this Authorization Rule. Defaults to `false`.
        /// </summary>
        [Output("listen")]
        public Output<bool?> Listen { get; private set; } = null!;

        /// <summary>
        /// Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        /// </summary>
        [Output("manage")]
        public Output<bool?> Manage { get; private set; } = null!;

        /// <summary>
        /// Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.
        /// </summary>
        [Output("namespaceName")]
        public Output<string> NamespaceName { get; private set; } = null!;

        /// <summary>
        /// The Primary Connection String for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Output("primaryConnectionString")]
        public Output<string> PrimaryConnectionString { get; private set; } = null!;

        /// <summary>
        /// The Primary Key for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Output("primaryKey")]
        public Output<string> PrimaryKey { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The Secondary Connection String for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Output("secondaryConnectionString")]
        public Output<string> SecondaryConnectionString { get; private set; } = null!;

        /// <summary>
        /// The Secondary Key for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Output("secondaryKey")]
        public Output<string> SecondaryKey { get; private set; } = null!;

        /// <summary>
        /// Grants send access to this this Authorization Rule. Defaults to `false`.
        /// </summary>
        [Output("send")]
        public Output<bool?> Send { get; private set; } = null!;


        /// <summary>
        /// Create a NamespaceAuthorizationRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NamespaceAuthorizationRule(string name, NamespaceAuthorizationRuleArgs args, CustomResourceOptions? options = null)
            : base("azure:eventhub/namespaceAuthorizationRule:NamespaceAuthorizationRule", name, args, MakeResourceOptions(options, ""))
        {
        }

        private NamespaceAuthorizationRule(string name, Input<string> id, NamespaceAuthorizationRuleState? state = null, CustomResourceOptions? options = null)
            : base("azure:eventhub/namespaceAuthorizationRule:NamespaceAuthorizationRule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing NamespaceAuthorizationRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NamespaceAuthorizationRule Get(string name, Input<string> id, NamespaceAuthorizationRuleState? state = null, CustomResourceOptions? options = null)
        {
            return new NamespaceAuthorizationRule(name, id, state, options);
        }
    }

    public sealed class NamespaceAuthorizationRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Grants listen access to this this Authorization Rule. Defaults to `false`.
        /// </summary>
        [Input("listen")]
        public Input<bool>? Listen { get; set; }

        /// <summary>
        /// Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        /// </summary>
        [Input("manage")]
        public Input<bool>? Manage { get; set; }

        /// <summary>
        /// Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.
        /// </summary>
        [Input("namespaceName", required: true)]
        public Input<string> NamespaceName { get; set; } = null!;

        /// <summary>
        /// The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// Grants send access to this this Authorization Rule. Defaults to `false`.
        /// </summary>
        [Input("send")]
        public Input<bool>? Send { get; set; }

        public NamespaceAuthorizationRuleArgs()
        {
        }
    }

    public sealed class NamespaceAuthorizationRuleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Grants listen access to this this Authorization Rule. Defaults to `false`.
        /// </summary>
        [Input("listen")]
        public Input<bool>? Listen { get; set; }

        /// <summary>
        /// Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        /// </summary>
        [Input("manage")]
        public Input<bool>? Manage { get; set; }

        /// <summary>
        /// Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.
        /// </summary>
        [Input("namespaceName")]
        public Input<string>? NamespaceName { get; set; }

        /// <summary>
        /// The Primary Connection String for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Input("primaryConnectionString")]
        public Input<string>? PrimaryConnectionString { get; set; }

        /// <summary>
        /// The Primary Key for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Input("primaryKey")]
        public Input<string>? PrimaryKey { get; set; }

        /// <summary>
        /// The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The Secondary Connection String for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Input("secondaryConnectionString")]
        public Input<string>? SecondaryConnectionString { get; set; }

        /// <summary>
        /// The Secondary Key for the ServiceBus Namespace authorization Rule.
        /// </summary>
        [Input("secondaryKey")]
        public Input<string>? SecondaryKey { get; set; }

        /// <summary>
        /// Grants send access to this this Authorization Rule. Defaults to `false`.
        /// </summary>
        [Input("send")]
        public Input<bool>? Send { get; set; }

        public NamespaceAuthorizationRuleState()
        {
        }
    }
}
