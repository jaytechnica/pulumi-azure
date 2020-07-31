// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Waf.Inputs
{

    public sealed class PolicyManagedRulesExclusionGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Match Variable. Possible values: `RequestArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
        /// </summary>
        [Input("matchVariable", required: true)]
        public Input<string> MatchVariable { get; set; } = null!;

        /// <summary>
        /// Describes field of the matchVariable collection.
        /// </summary>
        [Input("selector", required: true)]
        public Input<string> Selector { get; set; } = null!;

        /// <summary>
        /// Describes operator to be matched. Possible values: `Contains`, `EndsWith`, `Equals`, `EqualsAny`, `StartsWith`.
        /// </summary>
        [Input("selectorMatchOperator", required: true)]
        public Input<string> SelectorMatchOperator { get; set; } = null!;

        public PolicyManagedRulesExclusionGetArgs()
        {
        }
    }
}
