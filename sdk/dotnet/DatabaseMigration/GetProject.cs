// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.DatabaseMigration
{
    public static class GetProject
    {
        /// <summary>
        /// Use this data source to access information about an existing Database Migration Project.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetProjectResult> InvokeAsync(GetProjectArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetProjectResult>("azure:databasemigration/getProject:getProject", args ?? new GetProjectArgs(), options.WithVersion());
    }


    public sealed class GetProjectArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the database migration project.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// Name of the resource group where resource belongs to.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// Name of the database migration service where resource belongs to.
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        public GetProjectArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetProjectResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Azure location where the resource exists.
        /// </summary>
        public readonly string Location;
        public readonly string Name;
        public readonly string ResourceGroupName;
        public readonly string ServiceName;
        /// <summary>
        /// The platform type of the migration source.
        /// </summary>
        public readonly string SourcePlatform;
        /// <summary>
        /// A mapping of tags to assigned to the resource.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Tags;
        /// <summary>
        /// The platform type of the migration target.
        /// </summary>
        public readonly string TargetPlatform;

        [OutputConstructor]
        private GetProjectResult(
            string id,

            string location,

            string name,

            string resourceGroupName,

            string serviceName,

            string sourcePlatform,

            ImmutableDictionary<string, string> tags,

            string targetPlatform)
        {
            Id = id;
            Location = location;
            Name = name;
            ResourceGroupName = resourceGroupName;
            ServiceName = serviceName;
            SourcePlatform = sourcePlatform;
            Tags = tags;
            TargetPlatform = targetPlatform;
        }
    }
}
