// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Storage.Inputs
{

    public sealed class ShareAclAccessPolicyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The time at which this Access Policy should be valid until, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        /// </summary>
        [Input("expiry", required: true)]
        public Input<string> Expiry { get; set; } = null!;

        /// <summary>
        /// The permissions which should be associated with this Shared Identifier. Possible value is combination of `d` (delete), `l` (list), `r` (read) and `w` (write).
        /// </summary>
        [Input("permissions", required: true)]
        public Input<string> Permissions { get; set; } = null!;

        /// <summary>
        /// The time at which this Access Policy should be valid from, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        /// </summary>
        [Input("start", required: true)]
        public Input<string> Start { get; set; } = null!;

        public ShareAclAccessPolicyGetArgs()
        {
        }
    }
}
