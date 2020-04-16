// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network.Outputs
{

    [OutputType]
    public sealed class VpnGatewayBgpSetting
    {
        /// <summary>
        /// The ASN of the BGP Speaker. Changing this forces a new resource to be created.
        /// </summary>
        public readonly int Asn;
        /// <summary>
        /// The Address which should be used for the BGP Peering.
        /// </summary>
        public readonly string? BgpPeeringAddress;
        /// <summary>
        /// The weight added to Routes learned from this BGP Speaker. Changing this forces a new resource to be created.
        /// </summary>
        public readonly int PeerWeight;

        [OutputConstructor]
        private VpnGatewayBgpSetting(
            int asn,

            string? bgpPeeringAddress,

            int peerWeight)
        {
            Asn = asn;
            BgpPeeringAddress = bgpPeeringAddress;
            PeerWeight = peerWeight;
        }
    }
}