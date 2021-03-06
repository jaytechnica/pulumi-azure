// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network
{
    /// <summary>
    /// Manages a Network Connection Monitor.
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
    ///         var exampleResourceGroup = Output.Create(Azure.Core.GetResourceGroup.InvokeAsync(new Azure.Core.GetResourceGroupArgs
    ///         {
    ///             Name = "example-resources",
    ///         }));
    ///         var exampleNetworkWatcher = new Azure.Network.NetworkWatcher("exampleNetworkWatcher", new Azure.Network.NetworkWatcherArgs
    ///         {
    ///             Location = exampleResourceGroup.Apply(exampleResourceGroup =&gt; exampleResourceGroup.Location),
    ///             ResourceGroupName = exampleResourceGroup.Apply(exampleResourceGroup =&gt; exampleResourceGroup.Name),
    ///         });
    ///         var srcVirtualMachine = exampleResourceGroup.Apply(exampleResourceGroup =&gt; Output.Create(Azure.Compute.GetVirtualMachine.InvokeAsync(new Azure.Compute.GetVirtualMachineArgs
    ///         {
    ///             Name = "example-vm",
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///         })));
    ///         var srcExtension = new Azure.Compute.Extension("srcExtension", new Azure.Compute.ExtensionArgs
    ///         {
    ///             VirtualMachineId = srcVirtualMachine.Apply(srcVirtualMachine =&gt; srcVirtualMachine.Id),
    ///             Publisher = "Microsoft.Azure.NetworkWatcher",
    ///             Type = "NetworkWatcherAgentLinux",
    ///             TypeHandlerVersion = "1.4",
    ///             AutoUpgradeMinorVersion = true,
    ///         });
    ///         var exampleNetworkConnectionMonitor = new Azure.Network.NetworkConnectionMonitor("exampleNetworkConnectionMonitor", new Azure.Network.NetworkConnectionMonitorArgs
    ///         {
    ///             NetworkWatcherName = exampleNetworkWatcher.Name,
    ///             ResourceGroupName = exampleResourceGroup.Apply(exampleResourceGroup =&gt; exampleResourceGroup.Name),
    ///             Location = exampleNetworkWatcher.Location,
    ///             AutoStart = false,
    ///             IntervalInSeconds = 30,
    ///             Source = new Azure.Network.Inputs.NetworkConnectionMonitorSourceArgs
    ///             {
    ///                 VirtualMachineId = srcVirtualMachine.Apply(srcVirtualMachine =&gt; srcVirtualMachine.Id),
    ///                 Port = 20020,
    ///             },
    ///             Destination = new Azure.Network.Inputs.NetworkConnectionMonitorDestinationArgs
    ///             {
    ///                 Address = "mycompany.io",
    ///                 Port = 443,
    ///             },
    ///             Tags = 
    ///             {
    ///                 { "foo", "bar" },
    ///             },
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 srcExtension,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class NetworkConnectionMonitor : Pulumi.CustomResource
    {
        /// <summary>
        /// Will the connection monitor start automatically once created? Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Output("autoStart")]
        public Output<bool?> AutoStart { get; private set; } = null!;

        /// <summary>
        /// A `destination` block as defined below.
        /// </summary>
        [Output("destination")]
        public Output<Outputs.NetworkConnectionMonitorDestination> Destination { get; private set; } = null!;

        /// <summary>
        /// Monitoring interval in seconds.
        /// </summary>
        [Output("intervalInSeconds")]
        public Output<int?> IntervalInSeconds { get; private set; } = null!;

        /// <summary>
        /// The Azure Region where the Network Connection Monitor should exist. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name which should be used for this Network Connection Monitor. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the Network Watcher. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Output("networkWatcherName")]
        public Output<string> NetworkWatcherName { get; private set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the Network Connection Monitor should exist. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// A `source` block as defined below.
        /// </summary>
        [Output("source")]
        public Output<Outputs.NetworkConnectionMonitorSource> Source { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags which should be assigned to the Network Connection Monitor.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkConnectionMonitor resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkConnectionMonitor(string name, NetworkConnectionMonitorArgs args, CustomResourceOptions? options = null)
            : base("azure:network/networkConnectionMonitor:NetworkConnectionMonitor", name, args ?? new NetworkConnectionMonitorArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkConnectionMonitor(string name, Input<string> id, NetworkConnectionMonitorState? state = null, CustomResourceOptions? options = null)
            : base("azure:network/networkConnectionMonitor:NetworkConnectionMonitor", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing NetworkConnectionMonitor resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkConnectionMonitor Get(string name, Input<string> id, NetworkConnectionMonitorState? state = null, CustomResourceOptions? options = null)
        {
            return new NetworkConnectionMonitor(name, id, state, options);
        }
    }

    public sealed class NetworkConnectionMonitorArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Will the connection monitor start automatically once created? Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("autoStart")]
        public Input<bool>? AutoStart { get; set; }

        /// <summary>
        /// A `destination` block as defined below.
        /// </summary>
        [Input("destination", required: true)]
        public Input<Inputs.NetworkConnectionMonitorDestinationArgs> Destination { get; set; } = null!;

        /// <summary>
        /// Monitoring interval in seconds.
        /// </summary>
        [Input("intervalInSeconds")]
        public Input<int>? IntervalInSeconds { get; set; }

        /// <summary>
        /// The Azure Region where the Network Connection Monitor should exist. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name which should be used for this Network Connection Monitor. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Network Watcher. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("networkWatcherName", required: true)]
        public Input<string> NetworkWatcherName { get; set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the Network Connection Monitor should exist. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// A `source` block as defined below.
        /// </summary>
        [Input("source", required: true)]
        public Input<Inputs.NetworkConnectionMonitorSourceArgs> Source { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags which should be assigned to the Network Connection Monitor.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public NetworkConnectionMonitorArgs()
        {
        }
    }

    public sealed class NetworkConnectionMonitorState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Will the connection monitor start automatically once created? Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("autoStart")]
        public Input<bool>? AutoStart { get; set; }

        /// <summary>
        /// A `destination` block as defined below.
        /// </summary>
        [Input("destination")]
        public Input<Inputs.NetworkConnectionMonitorDestinationGetArgs>? Destination { get; set; }

        /// <summary>
        /// Monitoring interval in seconds.
        /// </summary>
        [Input("intervalInSeconds")]
        public Input<int>? IntervalInSeconds { get; set; }

        /// <summary>
        /// The Azure Region where the Network Connection Monitor should exist. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name which should be used for this Network Connection Monitor. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Network Watcher. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("networkWatcherName")]
        public Input<string>? NetworkWatcherName { get; set; }

        /// <summary>
        /// The name of the Resource Group where the Network Connection Monitor should exist. Changing this forces a new Network Connection Monitor to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// A `source` block as defined below.
        /// </summary>
        [Input("source")]
        public Input<Inputs.NetworkConnectionMonitorSourceGetArgs>? Source { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags which should be assigned to the Network Connection Monitor.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public NetworkConnectionMonitorState()
        {
        }
    }
}
