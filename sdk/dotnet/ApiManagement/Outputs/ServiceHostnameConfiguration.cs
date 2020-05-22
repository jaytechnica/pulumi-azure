// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ApiManagement.Outputs
{

    [OutputType]
    public sealed class ServiceHostnameConfiguration
    {
        /// <summary>
        /// One or more `developer_portal` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ServiceHostnameConfigurationDeveloperPortal> DeveloperPortals;
        /// <summary>
        /// One or more `management` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ServiceHostnameConfigurationManagement> Managements;
        /// <summary>
        /// One or more `portal` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ServiceHostnameConfigurationPortal> Portals;
        /// <summary>
        /// One or more `proxy` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ServiceHostnameConfigurationProxy> Proxies;
        /// <summary>
        /// One or more `scm` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<Outputs.ServiceHostnameConfigurationScm> Scms;

        [OutputConstructor]
        private ServiceHostnameConfiguration(
            ImmutableArray<Outputs.ServiceHostnameConfigurationDeveloperPortal> developerPortals,

            ImmutableArray<Outputs.ServiceHostnameConfigurationManagement> managements,

            ImmutableArray<Outputs.ServiceHostnameConfigurationPortal> portals,

            ImmutableArray<Outputs.ServiceHostnameConfigurationProxy> proxies,

            ImmutableArray<Outputs.ServiceHostnameConfigurationScm> scms)
        {
            DeveloperPortals = developerPortals;
            Managements = managements;
            Portals = portals;
            Proxies = proxies;
            Scms = scms;
        }
    }
}
