// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.OperationalInsights
{
    /// <summary>
    /// Links a Log Analytics (formally Operational Insights) Workspace to another resource. The (currently) only linkable service is an Azure Automation Account.
    /// 
    /// &gt; **NOTE:** This resource has been deprecated in favour of the `azure.loganalytics.LinkedService` resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/log_analytics_workspace_linked_service.html.markdown.
    /// </summary>
    public partial class AnalyticsWorkspaceLinkedService : Pulumi.CustomResource
    {
        /// <summary>
        /// Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in `workspace_name`. Currently it defaults to and only supports `automation` as a value. Changing this forces a new resource to be created.
        /// </summary>
        [Output("linkedServiceName")]
        public Output<string?> LinkedServiceName { get; private set; } = null!;

        /// <summary>
        /// A `linked_service_properties` block as defined below.
        /// </summary>
        [Output("linkedServiceProperties")]
        public Output<Outputs.AnalyticsWorkspaceLinkedServiceLinkedServiceProperties> LinkedServiceProperties { get; private set; } = null!;

        /// <summary>
        /// The automatically generated name of the Linked Service. This cannot be specified. The format is always `&lt;workspace_name&gt;/&lt;linked_service_name&gt;` e.g. `workspace1/Automation`
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level `resource_id` field and will be removed in v2.0 of the AzureRM Provider.
        /// </summary>
        [Output("resourceId")]
        public Output<string> ResourceId { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>> Tags { get; private set; } = null!;

        /// <summary>
        /// Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.
        /// </summary>
        [Output("workspaceName")]
        public Output<string> WorkspaceName { get; private set; } = null!;


        /// <summary>
        /// Create a AnalyticsWorkspaceLinkedService resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AnalyticsWorkspaceLinkedService(string name, AnalyticsWorkspaceLinkedServiceArgs args, CustomResourceOptions? options = null)
            : base("azure:operationalinsights/analyticsWorkspaceLinkedService:AnalyticsWorkspaceLinkedService", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private AnalyticsWorkspaceLinkedService(string name, Input<string> id, AnalyticsWorkspaceLinkedServiceState? state = null, CustomResourceOptions? options = null)
            : base("azure:operationalinsights/analyticsWorkspaceLinkedService:AnalyticsWorkspaceLinkedService", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AnalyticsWorkspaceLinkedService resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AnalyticsWorkspaceLinkedService Get(string name, Input<string> id, AnalyticsWorkspaceLinkedServiceState? state = null, CustomResourceOptions? options = null)
        {
            return new AnalyticsWorkspaceLinkedService(name, id, state, options);
        }
    }

    public sealed class AnalyticsWorkspaceLinkedServiceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in `workspace_name`. Currently it defaults to and only supports `automation` as a value. Changing this forces a new resource to be created.
        /// </summary>
        [Input("linkedServiceName")]
        public Input<string>? LinkedServiceName { get; set; }

        /// <summary>
        /// A `linked_service_properties` block as defined below.
        /// </summary>
        [Input("linkedServiceProperties")]
        public Input<Inputs.AnalyticsWorkspaceLinkedServiceLinkedServicePropertiesArgs>? LinkedServiceProperties { get; set; }

        /// <summary>
        /// The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level `resource_id` field and will be removed in v2.0 of the AzureRM Provider.
        /// </summary>
        [Input("resourceId")]
        public Input<string>? ResourceId { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.
        /// </summary>
        [Input("workspaceName", required: true)]
        public Input<string> WorkspaceName { get; set; } = null!;

        public AnalyticsWorkspaceLinkedServiceArgs()
        {
        }
    }

    public sealed class AnalyticsWorkspaceLinkedServiceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in `workspace_name`. Currently it defaults to and only supports `automation` as a value. Changing this forces a new resource to be created.
        /// </summary>
        [Input("linkedServiceName")]
        public Input<string>? LinkedServiceName { get; set; }

        /// <summary>
        /// A `linked_service_properties` block as defined below.
        /// </summary>
        [Input("linkedServiceProperties")]
        public Input<Inputs.AnalyticsWorkspaceLinkedServiceLinkedServicePropertiesGetArgs>? LinkedServiceProperties { get; set; }

        /// <summary>
        /// The automatically generated name of the Linked Service. This cannot be specified. The format is always `&lt;workspace_name&gt;/&lt;linked_service_name&gt;` e.g. `workspace1/Automation`
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level `resource_id` field and will be removed in v2.0 of the AzureRM Provider.
        /// </summary>
        [Input("resourceId")]
        public Input<string>? ResourceId { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.
        /// </summary>
        [Input("workspaceName")]
        public Input<string>? WorkspaceName { get; set; }

        public AnalyticsWorkspaceLinkedServiceState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class AnalyticsWorkspaceLinkedServiceLinkedServicePropertiesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level `resource_id` field and will be removed in v2.0 of the AzureRM Provider.
        /// </summary>
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        public AnalyticsWorkspaceLinkedServiceLinkedServicePropertiesArgs()
        {
        }
    }

    public sealed class AnalyticsWorkspaceLinkedServiceLinkedServicePropertiesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level `resource_id` field and will be removed in v2.0 of the AzureRM Provider.
        /// </summary>
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        public AnalyticsWorkspaceLinkedServiceLinkedServicePropertiesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class AnalyticsWorkspaceLinkedServiceLinkedServiceProperties
    {
        /// <summary>
        /// The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level `resource_id` field and will be removed in v2.0 of the AzureRM Provider.
        /// </summary>
        public readonly string ResourceId;

        [OutputConstructor]
        private AnalyticsWorkspaceLinkedServiceLinkedServiceProperties(string resourceId)
        {
            ResourceId = resourceId;
        }
    }
    }
}
