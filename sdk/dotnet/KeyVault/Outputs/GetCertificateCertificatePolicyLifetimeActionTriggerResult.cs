// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.KeyVault.Outputs
{

    [OutputType]
    public sealed class GetCertificateCertificatePolicyLifetimeActionTriggerResult
    {
        /// <summary>
        /// The number of days before the Certificate expires that the action associated with this Trigger should run.
        /// </summary>
        public readonly int DaysBeforeExpiry;
        /// <summary>
        /// The percentage at which during the Certificates Lifetime the action associated with this Trigger should run.
        /// </summary>
        public readonly int LifetimePercentage;

        [OutputConstructor]
        private GetCertificateCertificatePolicyLifetimeActionTriggerResult(
            int daysBeforeExpiry,

            int lifetimePercentage)
        {
            DaysBeforeExpiry = daysBeforeExpiry;
            LifetimePercentage = lifetimePercentage;
        }
    }
}
