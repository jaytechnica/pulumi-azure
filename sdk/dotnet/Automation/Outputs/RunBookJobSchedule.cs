// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Automation.Outputs
{

    [OutputType]
    public sealed class RunBookJobSchedule
    {
        public readonly string? JobScheduleId;
        public readonly ImmutableDictionary<string, string>? Parameters;
        public readonly string? RunOn;
        public readonly string ScheduleName;

        [OutputConstructor]
        private RunBookJobSchedule(
            string? jobScheduleId,

            ImmutableDictionary<string, string>? parameters,

            string? runOn,

            string scheduleName)
        {
            JobScheduleId = jobScheduleId;
            Parameters = parameters;
            RunOn = runOn;
            ScheduleName = scheduleName;
        }
    }
}
