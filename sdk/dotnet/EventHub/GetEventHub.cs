// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.EventHub
{
    public static class GetEventHub
    {
        /// <summary>
        /// Use this data source to access information about an existing EventHub.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetEventHubResult> InvokeAsync(GetEventHubArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetEventHubResult>("azure:eventhub/getEventHub:getEventHub", args ?? new GetEventHubArgs(), options.WithVersion());
    }


    public sealed class GetEventHubArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of this EventHub.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The name of the EventHub Namespace where the EventHub exists.
        /// </summary>
        [Input("namespaceName", required: true)]
        public string NamespaceName { get; set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the EventHub exists.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        public GetEventHubArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetEventHubResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        public readonly string NamespaceName;
        /// <summary>
        /// The number of partitions in the EventHub.
        /// </summary>
        public readonly int PartitionCount;
        /// <summary>
        /// The identifiers for the partitions of this EventHub.
        /// </summary>
        public readonly ImmutableArray<string> PartitionIds;
        public readonly string ResourceGroupName;

        [OutputConstructor]
        private GetEventHubResult(
            string id,

            string name,

            string namespaceName,

            int partitionCount,

            ImmutableArray<string> partitionIds,

            string resourceGroupName)
        {
            Id = id;
            Name = name;
            NamespaceName = namespaceName;
            PartitionCount = partitionCount;
            PartitionIds = partitionIds;
            ResourceGroupName = resourceGroupName;
        }
    }
}
