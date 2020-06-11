// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.EventGrid.Outputs
{

    [OutputType]
    public sealed class EventSubscriptionWebhookEndpoint
    {
        /// <summary>
        /// The Azure Active Directory Application ID or URI to get the access token that will be included as the bearer token in delivery requests.
        /// </summary>
        public readonly string? ActiveDirectoryAppIdOrUri;
        /// <summary>
        /// The Azure Active Directory Tenant ID to get the access token that will be included as the bearer token in delivery requests.
        /// </summary>
        public readonly string? ActiveDirectoryTenantId;
        /// <summary>
        /// The base url of the webhook where the Event Subscription will receive events.
        /// </summary>
        public readonly string? BaseUrl;
        /// <summary>
        /// Maximum number of events per batch.
        /// </summary>
        public readonly int? MaxEventsPerBatch;
        /// <summary>
        /// Preferred batch size in Kilobytes.
        /// </summary>
        public readonly int? PreferredBatchSizeInKilobytes;
        /// <summary>
        /// Specifies the url of the webhook where the Event Subscription will receive events.
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private EventSubscriptionWebhookEndpoint(
            string? activeDirectoryAppIdOrUri,

            string? activeDirectoryTenantId,

            string? baseUrl,

            int? maxEventsPerBatch,

            int? preferredBatchSizeInKilobytes,

            string url)
        {
            ActiveDirectoryAppIdOrUri = activeDirectoryAppIdOrUri;
            ActiveDirectoryTenantId = activeDirectoryTenantId;
            BaseUrl = baseUrl;
            MaxEventsPerBatch = maxEventsPerBatch;
            PreferredBatchSizeInKilobytes = preferredBatchSizeInKilobytes;
            Url = url;
        }
    }
}
