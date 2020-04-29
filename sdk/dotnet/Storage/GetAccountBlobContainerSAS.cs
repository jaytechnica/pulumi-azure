// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Storage
{
    public static class GetAccountBlobContainerSAS
    {
        /// <summary>
        /// Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Storage Account Blob Container.
        /// 
        /// Shared access signatures allow fine-grained, ephemeral access control to various aspects of an Azure Storage Account Blob Container.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetAccountBlobContainerSASResult> InvokeAsync(GetAccountBlobContainerSASArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAccountBlobContainerSASResult>("azure:storage/getAccountBlobContainerSAS:getAccountBlobContainerSAS", args ?? new GetAccountBlobContainerSASArgs(), options.WithVersion());
    }


    public sealed class GetAccountBlobContainerSASArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The `Cache-Control` response header that is sent when this SAS token is used.
        /// </summary>
        [Input("cacheControl")]
        public string? CacheControl { get; set; }

        /// <summary>
        /// The connection string for the storage account to which this SAS applies. Typically directly from the `primary_connection_string` attribute of an `azure.storage.Account` resource.
        /// </summary>
        [Input("connectionString", required: true)]
        public string ConnectionString { get; set; } = null!;

        /// <summary>
        /// Name of the container.
        /// </summary>
        [Input("containerName", required: true)]
        public string ContainerName { get; set; } = null!;

        /// <summary>
        /// The `Content-Disposition` response header that is sent when this SAS token is used.
        /// </summary>
        [Input("contentDisposition")]
        public string? ContentDisposition { get; set; }

        /// <summary>
        /// The `Content-Encoding` response header that is sent when this SAS token is used.
        /// </summary>
        [Input("contentEncoding")]
        public string? ContentEncoding { get; set; }

        /// <summary>
        /// The `Content-Language` response header that is sent when this SAS token is used.
        /// </summary>
        [Input("contentLanguage")]
        public string? ContentLanguage { get; set; }

        /// <summary>
        /// The `Content-Type` response header that is sent when this SAS token is used.
        /// </summary>
        [Input("contentType")]
        public string? ContentType { get; set; }

        /// <summary>
        /// The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
        /// </summary>
        [Input("expiry", required: true)]
        public string Expiry { get; set; } = null!;

        /// <summary>
        /// Only permit `https` access. If `false`, both `http` and `https` are permitted. Defaults to `true`.
        /// </summary>
        [Input("httpsOnly")]
        public bool? HttpsOnly { get; set; }

        /// <summary>
        /// Single ipv4 address or range (connected with a dash) of ipv4 addresses.
        /// </summary>
        [Input("ipAddress")]
        public string? IpAddress { get; set; }

        /// <summary>
        /// A `permissions` block as defined below.
        /// </summary>
        [Input("permissions", required: true)]
        public Inputs.GetAccountBlobContainerSASPermissionsArgs Permissions { get; set; } = null!;

        /// <summary>
        /// The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.
        /// </summary>
        [Input("start", required: true)]
        public string Start { get; set; } = null!;

        public GetAccountBlobContainerSASArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetAccountBlobContainerSASResult
    {
        public readonly string? CacheControl;
        public readonly string ConnectionString;
        public readonly string ContainerName;
        public readonly string? ContentDisposition;
        public readonly string? ContentEncoding;
        public readonly string? ContentLanguage;
        public readonly string? ContentType;
        public readonly string Expiry;
        public readonly bool? HttpsOnly;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? IpAddress;
        public readonly Outputs.GetAccountBlobContainerSASPermissionsResult Permissions;
        /// <summary>
        /// The computed Blob Container Shared Access Signature (SAS).
        /// </summary>
        public readonly string Sas;
        public readonly string Start;

        [OutputConstructor]
        private GetAccountBlobContainerSASResult(
            string? cacheControl,

            string connectionString,

            string containerName,

            string? contentDisposition,

            string? contentEncoding,

            string? contentLanguage,

            string? contentType,

            string expiry,

            bool? httpsOnly,

            string id,

            string? ipAddress,

            Outputs.GetAccountBlobContainerSASPermissionsResult permissions,

            string sas,

            string start)
        {
            CacheControl = cacheControl;
            ConnectionString = connectionString;
            ContainerName = containerName;
            ContentDisposition = contentDisposition;
            ContentEncoding = contentEncoding;
            ContentLanguage = contentLanguage;
            ContentType = contentType;
            Expiry = expiry;
            HttpsOnly = httpsOnly;
            Id = id;
            IpAddress = ipAddress;
            Permissions = permissions;
            Sas = sas;
            Start = start;
        }
    }
}
