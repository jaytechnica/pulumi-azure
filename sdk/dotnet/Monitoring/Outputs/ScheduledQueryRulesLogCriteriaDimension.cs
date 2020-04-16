// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Monitoring.Outputs
{

    [OutputType]
    public sealed class ScheduledQueryRulesLogCriteriaDimension
    {
        /// <summary>
        /// Name of the dimension.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Operator for dimension values, - 'Include'.
        /// </summary>
        public readonly string? Operator;
        /// <summary>
        /// List of dimension values.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private ScheduledQueryRulesLogCriteriaDimension(
            string name,

            string? @operator,

            ImmutableArray<string> values)
        {
            Name = name;
            Operator = @operator;
            Values = values;
        }
    }
}