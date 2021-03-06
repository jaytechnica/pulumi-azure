// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ApiManagement
{
    /// <summary>
    /// Manages a API Management Service API Diagnostics Logs.
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
    ///         var exampleInsights = new Azure.AppInsights.Insights("exampleInsights", new Azure.AppInsights.InsightsArgs
    ///         {
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             ApplicationType = "web",
    ///         });
    ///         var exampleService = new Azure.ApiManagement.Service("exampleService", new Azure.ApiManagement.ServiceArgs
    ///         {
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             PublisherName = "My Company",
    ///             PublisherEmail = "company@terraform.io",
    ///             SkuName = "Developer_1",
    ///         });
    ///         var exampleApi = new Azure.ApiManagement.Api("exampleApi", new Azure.ApiManagement.ApiArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             ApiManagementName = exampleService.Name,
    ///             Revision = "1",
    ///             DisplayName = "Example API",
    ///             Path = "example",
    ///             Protocols = 
    ///             {
    ///                 "https",
    ///             },
    ///             Import = new Azure.ApiManagement.Inputs.ApiImportArgs
    ///             {
    ///                 ContentFormat = "swagger-link-json",
    ///                 ContentValue = "http://conferenceapi.azurewebsites.net/?format=json",
    ///             },
    ///         });
    ///         var exampleLogger = new Azure.ApiManagement.Logger("exampleLogger", new Azure.ApiManagement.LoggerArgs
    ///         {
    ///             ApiManagementName = exampleService.Name,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             ApplicationInsights = new Azure.ApiManagement.Inputs.LoggerApplicationInsightsArgs
    ///             {
    ///                 InstrumentationKey = exampleInsights.InstrumentationKey,
    ///             },
    ///         });
    ///         var exampleApiDiagnostic = new Azure.ApiManagement.ApiDiagnostic("exampleApiDiagnostic", new Azure.ApiManagement.ApiDiagnosticArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             ApiManagementName = exampleService.Name,
    ///             ApiName = exampleApi.Name,
    ///             ApiManagementLoggerId = exampleLogger.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class ApiDiagnostic : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID (name) of the Diagnostics Logger.
        /// </summary>
        [Output("apiManagementLoggerId")]
        public Output<string> ApiManagementLoggerId { get; private set; } = null!;

        /// <summary>
        /// The name of the API Management Service instance. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Output("apiManagementName")]
        public Output<string> ApiManagementName { get; private set; } = null!;

        /// <summary>
        /// The name of the API on which to configure the Diagnostics Logs. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Output("apiName")]
        public Output<string> ApiName { get; private set; } = null!;

        /// <summary>
        /// Identifier of the Diagnostics Logs. Possible values are `applicationinsights` and `azuremonitor`. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Output("identifier")]
        public Output<string> Identifier { get; private set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the API Management Service API Diagnostics Logs should exist. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;


        /// <summary>
        /// Create a ApiDiagnostic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApiDiagnostic(string name, ApiDiagnosticArgs args, CustomResourceOptions? options = null)
            : base("azure:apimanagement/apiDiagnostic:ApiDiagnostic", name, args ?? new ApiDiagnosticArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApiDiagnostic(string name, Input<string> id, ApiDiagnosticState? state = null, CustomResourceOptions? options = null)
            : base("azure:apimanagement/apiDiagnostic:ApiDiagnostic", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApiDiagnostic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApiDiagnostic Get(string name, Input<string> id, ApiDiagnosticState? state = null, CustomResourceOptions? options = null)
        {
            return new ApiDiagnostic(name, id, state, options);
        }
    }

    public sealed class ApiDiagnosticArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID (name) of the Diagnostics Logger.
        /// </summary>
        [Input("apiManagementLoggerId", required: true)]
        public Input<string> ApiManagementLoggerId { get; set; } = null!;

        /// <summary>
        /// The name of the API Management Service instance. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("apiManagementName", required: true)]
        public Input<string> ApiManagementName { get; set; } = null!;

        /// <summary>
        /// The name of the API on which to configure the Diagnostics Logs. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("apiName", required: true)]
        public Input<string> ApiName { get; set; } = null!;

        /// <summary>
        /// Identifier of the Diagnostics Logs. Possible values are `applicationinsights` and `azuremonitor`. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("identifier", required: true)]
        public Input<string> Identifier { get; set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the API Management Service API Diagnostics Logs should exist. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public ApiDiagnosticArgs()
        {
        }
    }

    public sealed class ApiDiagnosticState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID (name) of the Diagnostics Logger.
        /// </summary>
        [Input("apiManagementLoggerId")]
        public Input<string>? ApiManagementLoggerId { get; set; }

        /// <summary>
        /// The name of the API Management Service instance. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("apiManagementName")]
        public Input<string>? ApiManagementName { get; set; }

        /// <summary>
        /// The name of the API on which to configure the Diagnostics Logs. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("apiName")]
        public Input<string>? ApiName { get; set; }

        /// <summary>
        /// Identifier of the Diagnostics Logs. Possible values are `applicationinsights` and `azuremonitor`. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("identifier")]
        public Input<string>? Identifier { get; set; }

        /// <summary>
        /// The name of the Resource Group where the API Management Service API Diagnostics Logs should exist. Changing this forces a new API Management Service API Diagnostics Logs to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        public ApiDiagnosticState()
        {
        }
    }
}
