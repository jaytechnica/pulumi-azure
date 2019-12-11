// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.DataFactory
{
    /// <summary>
    /// Manages a Trigger Schedule inside a Azure Data Factory.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_trigger_schedule.html.markdown.
    /// </summary>
    public partial class TriggerSchedule : Pulumi.CustomResource
    {
        /// <summary>
        /// List of tags that can be used for describing the Data Factory Schedule Trigger.
        /// </summary>
        [Output("annotations")]
        public Output<ImmutableArray<string>> Annotations { get; private set; } = null!;

        /// <summary>
        /// The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.
        /// </summary>
        [Output("dataFactoryName")]
        public Output<string> DataFactoryName { get; private set; } = null!;

        /// <summary>
        /// The time the Schedule Trigger should end. The time will be represented in UTC. 
        /// </summary>
        [Output("endTime")]
        public Output<string?> EndTime { get; private set; } = null!;

        /// <summary>
        /// The trigger freqency. Valid values include `Minute`, `Hour`, `Day`, `Week`, `Month`. Defaults to `Minute`.
        /// </summary>
        [Output("frequency")]
        public Output<string?> Frequency { get; private set; } = null!;

        /// <summary>
        /// The interval for how often the trigger occurs. This defaults to 1.
        /// </summary>
        [Output("interval")]
        public Output<int?> Interval { get; private set; } = null!;

        /// <summary>
        /// Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The Data Factory Pipeline name that the trigger will act on.
        /// </summary>
        [Output("pipelineName")]
        public Output<string> PipelineName { get; private set; } = null!;

        /// <summary>
        /// The pipeline parameters that the trigger will act upon.
        /// </summary>
        [Output("pipelineParameters")]
        public Output<ImmutableDictionary<string, string>?> PipelineParameters { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC. 
        /// </summary>
        [Output("startTime")]
        public Output<string> StartTime { get; private set; } = null!;


        /// <summary>
        /// Create a TriggerSchedule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TriggerSchedule(string name, TriggerScheduleArgs args, CustomResourceOptions? options = null)
            : base("azure:datafactory/triggerSchedule:TriggerSchedule", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private TriggerSchedule(string name, Input<string> id, TriggerScheduleState? state = null, CustomResourceOptions? options = null)
            : base("azure:datafactory/triggerSchedule:TriggerSchedule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing TriggerSchedule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TriggerSchedule Get(string name, Input<string> id, TriggerScheduleState? state = null, CustomResourceOptions? options = null)
        {
            return new TriggerSchedule(name, id, state, options);
        }
    }

    public sealed class TriggerScheduleArgs : Pulumi.ResourceArgs
    {
        [Input("annotations")]
        private InputList<string>? _annotations;

        /// <summary>
        /// List of tags that can be used for describing the Data Factory Schedule Trigger.
        /// </summary>
        public InputList<string> Annotations
        {
            get => _annotations ?? (_annotations = new InputList<string>());
            set => _annotations = value;
        }

        /// <summary>
        /// The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.
        /// </summary>
        [Input("dataFactoryName", required: true)]
        public Input<string> DataFactoryName { get; set; } = null!;

        /// <summary>
        /// The time the Schedule Trigger should end. The time will be represented in UTC. 
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// The trigger freqency. Valid values include `Minute`, `Hour`, `Day`, `Week`, `Month`. Defaults to `Minute`.
        /// </summary>
        [Input("frequency")]
        public Input<string>? Frequency { get; set; }

        /// <summary>
        /// The interval for how often the trigger occurs. This defaults to 1.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        /// <summary>
        /// Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Data Factory Pipeline name that the trigger will act on.
        /// </summary>
        [Input("pipelineName", required: true)]
        public Input<string> PipelineName { get; set; } = null!;

        [Input("pipelineParameters")]
        private InputMap<string>? _pipelineParameters;

        /// <summary>
        /// The pipeline parameters that the trigger will act upon.
        /// </summary>
        public InputMap<string> PipelineParameters
        {
            get => _pipelineParameters ?? (_pipelineParameters = new InputMap<string>());
            set => _pipelineParameters = value;
        }

        /// <summary>
        /// The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC. 
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        public TriggerScheduleArgs()
        {
        }
    }

    public sealed class TriggerScheduleState : Pulumi.ResourceArgs
    {
        [Input("annotations")]
        private InputList<string>? _annotations;

        /// <summary>
        /// List of tags that can be used for describing the Data Factory Schedule Trigger.
        /// </summary>
        public InputList<string> Annotations
        {
            get => _annotations ?? (_annotations = new InputList<string>());
            set => _annotations = value;
        }

        /// <summary>
        /// The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.
        /// </summary>
        [Input("dataFactoryName")]
        public Input<string>? DataFactoryName { get; set; }

        /// <summary>
        /// The time the Schedule Trigger should end. The time will be represented in UTC. 
        /// </summary>
        [Input("endTime")]
        public Input<string>? EndTime { get; set; }

        /// <summary>
        /// The trigger freqency. Valid values include `Minute`, `Hour`, `Day`, `Week`, `Month`. Defaults to `Minute`.
        /// </summary>
        [Input("frequency")]
        public Input<string>? Frequency { get; set; }

        /// <summary>
        /// The interval for how often the trigger occurs. This defaults to 1.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        /// <summary>
        /// Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Data Factory Pipeline name that the trigger will act on.
        /// </summary>
        [Input("pipelineName")]
        public Input<string>? PipelineName { get; set; }

        [Input("pipelineParameters")]
        private InputMap<string>? _pipelineParameters;

        /// <summary>
        /// The pipeline parameters that the trigger will act upon.
        /// </summary>
        public InputMap<string> PipelineParameters
        {
            get => _pipelineParameters ?? (_pipelineParameters = new InputMap<string>());
            set => _pipelineParameters = value;
        }

        /// <summary>
        /// The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC. 
        /// </summary>
        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        public TriggerScheduleState()
        {
        }
    }
}
