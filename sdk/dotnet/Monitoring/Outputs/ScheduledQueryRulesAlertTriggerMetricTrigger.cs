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
    public sealed class ScheduledQueryRulesAlertTriggerMetricTrigger
    {
        public readonly string MetricColumn;
        public readonly string MetricTriggerType;
        /// <summary>
        /// Evaluation operation for rule - 'Equal', 'GreaterThan' or 'LessThan'.
        /// </summary>
        public readonly string Operator;
        /// <summary>
        /// The threshold of the metric trigger.    Values must be between 0 and 10000 inclusive.
        /// </summary>
        public readonly double Threshold;

        [OutputConstructor]
        private ScheduledQueryRulesAlertTriggerMetricTrigger(
            string metricColumn,

            string metricTriggerType,

            string @operator,

            double threshold)
        {
            MetricColumn = metricColumn;
            MetricTriggerType = metricTriggerType;
            Operator = @operator;
            Threshold = threshold;
        }
    }
}