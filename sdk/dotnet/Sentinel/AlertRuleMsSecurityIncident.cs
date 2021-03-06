// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Sentinel
{
    /// <summary>
    /// Manages a Sentinel MS Security Incident Alert Rule.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Azure = Pulumi.Azure;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleResourceGroup = new Azure.Core.ResourceGroup("exampleResourceGroup", new Azure.Core.ResourceGroupArgs
    ///         {
    ///             Location = "West Europe",
    ///         });
    ///         var exampleAnalyticsWorkspace = new Azure.OperationalInsights.AnalyticsWorkspace("exampleAnalyticsWorkspace", new Azure.OperationalInsights.AnalyticsWorkspaceArgs
    ///         {
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             Sku = "pergb2018",
    ///         });
    ///         var exampleAlertRuleMsSecurityIncident = new Azure.Sentinel.AlertRuleMsSecurityIncident("exampleAlertRuleMsSecurityIncident", new Azure.Sentinel.AlertRuleMsSecurityIncidentArgs
    ///         {
    ///             LogAnalyticsWorkspaceId = exampleAnalyticsWorkspace.Id,
    ///             ProductFilter = "Microsoft Cloud App Security",
    ///             DisplayName = "example rule",
    ///             SeverityFilters = 
    ///             {
    ///                 "High",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class AlertRuleMsSecurityIncident : Pulumi.CustomResource
    {
        /// <summary>
        /// The description of this Sentinel MS Security Incident Alert Rule.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The friendly name of this Sentinel MS Security Incident Alert Rule.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Only create incidents when the alert display name contain text from this list, leave empty to apply no filter.
        /// </summary>
        [Output("displayNameFilters")]
        public Output<ImmutableArray<string>> DisplayNameFilters { get; private set; } = null!;

        /// <summary>
        /// Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to `true`.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        /// </summary>
        [Output("logAnalyticsWorkspaceId")]
        public Output<string> LogAnalyticsWorkspaceId { get; private set; } = null!;

        /// <summary>
        /// The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The Microsoft Security Service from where the alert will be generated. Possible values are `Azure Active Directory Identity Protection`, `Azure Advanced Threat Protection`, `Azure Security Center`, `Azure Security Center for IoT` and `Microsoft Cloud App Security`.
        /// </summary>
        [Output("productFilter")]
        public Output<string> ProductFilter { get; private set; } = null!;

        /// <summary>
        /// Only create incidents from alerts when alert severity level is contained in this list. Possible values are `High`, `Medium`, `Low` and `Informational`.
        /// </summary>
        [Output("severityFilters")]
        public Output<ImmutableArray<string>> SeverityFilters { get; private set; } = null!;

        [Output("textWhitelists")]
        public Output<ImmutableArray<string>> TextWhitelists { get; private set; } = null!;


        /// <summary>
        /// Create a AlertRuleMsSecurityIncident resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AlertRuleMsSecurityIncident(string name, AlertRuleMsSecurityIncidentArgs args, CustomResourceOptions? options = null)
            : base("azure:sentinel/alertRuleMsSecurityIncident:AlertRuleMsSecurityIncident", name, args ?? new AlertRuleMsSecurityIncidentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AlertRuleMsSecurityIncident(string name, Input<string> id, AlertRuleMsSecurityIncidentState? state = null, CustomResourceOptions? options = null)
            : base("azure:sentinel/alertRuleMsSecurityIncident:AlertRuleMsSecurityIncident", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AlertRuleMsSecurityIncident resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AlertRuleMsSecurityIncident Get(string name, Input<string> id, AlertRuleMsSecurityIncidentState? state = null, CustomResourceOptions? options = null)
        {
            return new AlertRuleMsSecurityIncident(name, id, state, options);
        }
    }

    public sealed class AlertRuleMsSecurityIncidentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of this Sentinel MS Security Incident Alert Rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The friendly name of this Sentinel MS Security Incident Alert Rule.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        [Input("displayNameFilters")]
        private InputList<string>? _displayNameFilters;

        /// <summary>
        /// Only create incidents when the alert display name contain text from this list, leave empty to apply no filter.
        /// </summary>
        public InputList<string> DisplayNameFilters
        {
            get => _displayNameFilters ?? (_displayNameFilters = new InputList<string>());
            set => _displayNameFilters = value;
        }

        /// <summary>
        /// Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        /// </summary>
        [Input("logAnalyticsWorkspaceId", required: true)]
        public Input<string> LogAnalyticsWorkspaceId { get; set; } = null!;

        /// <summary>
        /// The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Microsoft Security Service from where the alert will be generated. Possible values are `Azure Active Directory Identity Protection`, `Azure Advanced Threat Protection`, `Azure Security Center`, `Azure Security Center for IoT` and `Microsoft Cloud App Security`.
        /// </summary>
        [Input("productFilter", required: true)]
        public Input<string> ProductFilter { get; set; } = null!;

        [Input("severityFilters", required: true)]
        private InputList<string>? _severityFilters;

        /// <summary>
        /// Only create incidents from alerts when alert severity level is contained in this list. Possible values are `High`, `Medium`, `Low` and `Informational`.
        /// </summary>
        public InputList<string> SeverityFilters
        {
            get => _severityFilters ?? (_severityFilters = new InputList<string>());
            set => _severityFilters = value;
        }

        [Input("textWhitelists")]
        private InputList<string>? _textWhitelists;
        [Obsolete(@"this property has been renamed to display_name_filter to better match the SDK & API")]
        public InputList<string> TextWhitelists
        {
            get => _textWhitelists ?? (_textWhitelists = new InputList<string>());
            set => _textWhitelists = value;
        }

        public AlertRuleMsSecurityIncidentArgs()
        {
        }
    }

    public sealed class AlertRuleMsSecurityIncidentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of this Sentinel MS Security Incident Alert Rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The friendly name of this Sentinel MS Security Incident Alert Rule.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("displayNameFilters")]
        private InputList<string>? _displayNameFilters;

        /// <summary>
        /// Only create incidents when the alert display name contain text from this list, leave empty to apply no filter.
        /// </summary>
        public InputList<string> DisplayNameFilters
        {
            get => _displayNameFilters ?? (_displayNameFilters = new InputList<string>());
            set => _displayNameFilters = value;
        }

        /// <summary>
        /// Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        /// </summary>
        [Input("logAnalyticsWorkspaceId")]
        public Input<string>? LogAnalyticsWorkspaceId { get; set; }

        /// <summary>
        /// The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Microsoft Security Service from where the alert will be generated. Possible values are `Azure Active Directory Identity Protection`, `Azure Advanced Threat Protection`, `Azure Security Center`, `Azure Security Center for IoT` and `Microsoft Cloud App Security`.
        /// </summary>
        [Input("productFilter")]
        public Input<string>? ProductFilter { get; set; }

        [Input("severityFilters")]
        private InputList<string>? _severityFilters;

        /// <summary>
        /// Only create incidents from alerts when alert severity level is contained in this list. Possible values are `High`, `Medium`, `Low` and `Informational`.
        /// </summary>
        public InputList<string> SeverityFilters
        {
            get => _severityFilters ?? (_severityFilters = new InputList<string>());
            set => _severityFilters = value;
        }

        [Input("textWhitelists")]
        private InputList<string>? _textWhitelists;
        [Obsolete(@"this property has been renamed to display_name_filter to better match the SDK & API")]
        public InputList<string> TextWhitelists
        {
            get => _textWhitelists ?? (_textWhitelists = new InputList<string>());
            set => _textWhitelists = value;
        }

        public AlertRuleMsSecurityIncidentState()
        {
        }
    }
}
