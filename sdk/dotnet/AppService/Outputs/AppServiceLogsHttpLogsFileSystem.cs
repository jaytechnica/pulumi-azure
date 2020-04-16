// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.AppService.Outputs
{

    [OutputType]
    public sealed class AppServiceLogsHttpLogsFileSystem
    {
        /// <summary>
        /// The number of days to retain logs for.
        /// </summary>
        public readonly int RetentionInDays;
        /// <summary>
        /// The maximum size in megabytes that http log files can use before being removed.
        /// </summary>
        public readonly int RetentionInMb;

        [OutputConstructor]
        private AppServiceLogsHttpLogsFileSystem(
            int retentionInDays,

            int retentionInMb)
        {
            RetentionInDays = retentionInDays;
            RetentionInMb = retentionInMb;
        }
    }
}