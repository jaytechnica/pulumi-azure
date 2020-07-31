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
    /// Manages an Azure Firewall.
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
    ///             Location = "North Europe",
    ///         });
    ///         var exampleVirtualNetwork = new Azure.Network.VirtualNetwork("exampleVirtualNetwork", new Azure.Network.VirtualNetworkArgs
    ///         {
    ///             AddressSpaces = 
    ///             {
    ///                 "10.0.0.0/16",
    ///             },
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///         });
    ///         var exampleSubnet = new Azure.Network.Subnet("exampleSubnet", new Azure.Network.SubnetArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             VirtualNetworkName = exampleVirtualNetwork.Name,
    ///             AddressPrefix = "10.0.1.0/24",
    ///         });
    ///         var examplePublicIp = new Azure.Network.PublicIp("examplePublicIp", new Azure.Network.PublicIpArgs
    ///         {
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             AllocationMethod = "Static",
    ///             Sku = "Standard",
    ///         });
    ///         var exampleFirewall = new Azure.Network.Firewall("exampleFirewall", new Azure.Network.FirewallArgs
    ///         {
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             IpConfigurations = 
    ///             {
    ///                 new Azure.Network.Inputs.FirewallIpConfigurationArgs
    ///                 {
    ///                     Name = "configuration",
    ///                     SubnetId = exampleSubnet.Id,
    ///                     PublicIpAddressId = examplePublicIp.Id,
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Firewall : Pulumi.CustomResource
    {
        /// <summary>
        /// A `ip_configuration` block as documented below.
        /// </summary>
        [Output("ipConfigurations")]
        public Output<ImmutableArray<Outputs.FirewallIpConfiguration>> IpConfigurations { get; private set; } = null!;

        /// <summary>
        /// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Specifies the name of the Firewall. Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The operation mode for threat intelligence-based filtering. Possible values are: `Off`, `Alert` and `Deny`. Defaults to `Alert`
        /// </summary>
        [Output("threatIntelMode")]
        public Output<string?> ThreatIntelMode { get; private set; } = null!;

        /// <summary>
        /// Specifies the availability zones in which the Azure Firewall should be created. Changing this forces a new resource to be created.
        /// </summary>
        [Output("zones")]
        public Output<ImmutableArray<string>> Zones { get; private set; } = null!;


        /// <summary>
        /// Create a Firewall resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Firewall(string name, FirewallArgs args, CustomResourceOptions? options = null)
            : base("azure:network/firewall:Firewall", name, args ?? new FirewallArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Firewall(string name, Input<string> id, FirewallState? state = null, CustomResourceOptions? options = null)
            : base("azure:network/firewall:Firewall", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Firewall resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Firewall Get(string name, Input<string> id, FirewallState? state = null, CustomResourceOptions? options = null)
        {
            return new Firewall(name, id, state, options);
        }
    }

    public sealed class FirewallArgs : Pulumi.ResourceArgs
    {
        [Input("ipConfigurations", required: true)]
        private InputList<Inputs.FirewallIpConfigurationArgs>? _ipConfigurations;

        /// <summary>
        /// A `ip_configuration` block as documented below.
        /// </summary>
        public InputList<Inputs.FirewallIpConfigurationArgs> IpConfigurations
        {
            get => _ipConfigurations ?? (_ipConfigurations = new InputList<Inputs.FirewallIpConfigurationArgs>());
            set => _ipConfigurations = value;
        }

        /// <summary>
        /// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Specifies the name of the Firewall. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The operation mode for threat intelligence-based filtering. Possible values are: `Off`, `Alert` and `Deny`. Defaults to `Alert`
        /// </summary>
        [Input("threatIntelMode")]
        public Input<string>? ThreatIntelMode { get; set; }

        [Input("zones")]
        private InputList<string>? _zones;

        /// <summary>
        /// Specifies the availability zones in which the Azure Firewall should be created. Changing this forces a new resource to be created.
        /// </summary>
        public InputList<string> Zones
        {
            get => _zones ?? (_zones = new InputList<string>());
            set => _zones = value;
        }

        public FirewallArgs()
        {
        }
    }

    public sealed class FirewallState : Pulumi.ResourceArgs
    {
        [Input("ipConfigurations")]
        private InputList<Inputs.FirewallIpConfigurationGetArgs>? _ipConfigurations;

        /// <summary>
        /// A `ip_configuration` block as documented below.
        /// </summary>
        public InputList<Inputs.FirewallIpConfigurationGetArgs> IpConfigurations
        {
            get => _ipConfigurations ?? (_ipConfigurations = new InputList<Inputs.FirewallIpConfigurationGetArgs>());
            set => _ipConfigurations = value;
        }

        /// <summary>
        /// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Specifies the name of the Firewall. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The operation mode for threat intelligence-based filtering. Possible values are: `Off`, `Alert` and `Deny`. Defaults to `Alert`
        /// </summary>
        [Input("threatIntelMode")]
        public Input<string>? ThreatIntelMode { get; set; }

        [Input("zones")]
        private InputList<string>? _zones;

        /// <summary>
        /// Specifies the availability zones in which the Azure Firewall should be created. Changing this forces a new resource to be created.
        /// </summary>
        public InputList<string> Zones
        {
            get => _zones ?? (_zones = new InputList<string>());
            set => _zones = value;
        }

        public FirewallState()
        {
        }
    }
}
