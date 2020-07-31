// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Hsm.Inputs
{

    public sealed class ModuleNetworkProfileArgs : Pulumi.ResourceArgs
    {
        [Input("networkInterfacePrivateIpAddresses", required: true)]
        private InputList<string>? _networkInterfacePrivateIpAddresses;

        /// <summary>
        /// The private IPv4 address of the network interface. Changing this forces a new Dedicated Hardware Security Module to be created.
        /// </summary>
        public InputList<string> NetworkInterfacePrivateIpAddresses
        {
            get => _networkInterfacePrivateIpAddresses ?? (_networkInterfacePrivateIpAddresses = new InputList<string>());
            set => _networkInterfacePrivateIpAddresses = value;
        }

        /// <summary>
        /// The ID of the subnet. Changing this forces a new Dedicated Hardware Security Module to be created.
        /// </summary>
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        public ModuleNetworkProfileArgs()
        {
        }
    }
}
