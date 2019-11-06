// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ApiManagement
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to access information about an existing API Management Service.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/api_management.html.markdown.
        /// </summary>
        public static Task<GetServiceResult> GetService(GetServiceArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetServiceResult>("azure:apimanagement/getService:getService", args, options.WithVersion());
    }

    public sealed class GetServiceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the API Management service.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The Name of the Resource Group in which the API Management Service exists.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public GetServiceArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetServiceResult
    {
        /// <summary>
        /// One or more `additional_location` blocks as defined below
        /// </summary>
        public readonly ImmutableArray<Outputs.GetServiceAdditionalLocationsResult> AdditionalLocations;
        /// <summary>
        /// Gateway URL of the API Management service in the Region.
        /// </summary>
        public readonly string GatewayRegionalUrl;
        /// <summary>
        /// The URL for the API Management Service's Gateway.
        /// </summary>
        public readonly string GatewayUrl;
        /// <summary>
        /// A `hostname_configuration` block as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetServiceHostnameConfigurationsResult> HostnameConfigurations;
        /// <summary>
        /// The location name of the additional region among Azure Data center regions.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// The URL for the Management API.
        /// </summary>
        public readonly string ManagementApiUrl;
        /// <summary>
        /// Specifies the plan's pricing tier.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The email address from which the notification will be sent.
        /// </summary>
        public readonly string NotificationSenderEmail;
        /// <summary>
        /// The URL of the Publisher Portal.
        /// </summary>
        public readonly string PortalUrl;
        /// <summary>
        /// Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
        /// </summary>
        public readonly ImmutableArray<string> PublicIpAddresses;
        /// <summary>
        /// The email of Publisher/Company of the API Management Service.
        /// </summary>
        public readonly string PublisherEmail;
        /// <summary>
        /// The name of the Publisher/Company of the API Management Service.
        /// </summary>
        public readonly string PublisherName;
        public readonly string ResourceGroupName;
        /// <summary>
        /// The SCM (Source Code Management) endpoint.
        /// </summary>
        public readonly string ScmUrl;
        /// <summary>
        /// A `sku` block as documented below.
        /// </summary>
        public readonly Outputs.GetServiceSkuResult Sku;
        public readonly string SkuName;
        /// <summary>
        /// A mapping of tags assigned to the resource.
        /// </summary>
        public readonly ImmutableDictionary<string, string> Tags;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetServiceResult(
            ImmutableArray<Outputs.GetServiceAdditionalLocationsResult> additionalLocations,
            string gatewayRegionalUrl,
            string gatewayUrl,
            ImmutableArray<Outputs.GetServiceHostnameConfigurationsResult> hostnameConfigurations,
            string location,
            string managementApiUrl,
            string name,
            string notificationSenderEmail,
            string portalUrl,
            ImmutableArray<string> publicIpAddresses,
            string publisherEmail,
            string publisherName,
            string resourceGroupName,
            string scmUrl,
            Outputs.GetServiceSkuResult sku,
            string skuName,
            ImmutableDictionary<string, string> tags,
            string id)
        {
            AdditionalLocations = additionalLocations;
            GatewayRegionalUrl = gatewayRegionalUrl;
            GatewayUrl = gatewayUrl;
            HostnameConfigurations = hostnameConfigurations;
            Location = location;
            ManagementApiUrl = managementApiUrl;
            Name = name;
            NotificationSenderEmail = notificationSenderEmail;
            PortalUrl = portalUrl;
            PublicIpAddresses = publicIpAddresses;
            PublisherEmail = publisherEmail;
            PublisherName = publisherName;
            ResourceGroupName = resourceGroupName;
            ScmUrl = scmUrl;
            Sku = sku;
            SkuName = skuName;
            Tags = tags;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetServiceAdditionalLocationsResult
    {
        /// <summary>
        /// Gateway URL of the API Management service in the Region.
        /// </summary>
        public readonly string GatewayRegionalUrl;
        /// <summary>
        /// The location name of the additional region among Azure Data center regions.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
        /// </summary>
        public readonly ImmutableArray<string> PublicIpAddresses;

        [OutputConstructor]
        private GetServiceAdditionalLocationsResult(
            string gatewayRegionalUrl,
            string location,
            ImmutableArray<string> publicIpAddresses)
        {
            GatewayRegionalUrl = gatewayRegionalUrl;
            Location = location;
            PublicIpAddresses = publicIpAddresses;
        }
    }

    [OutputType]
    public sealed class GetServiceHostnameConfigurationsManagementsResult
    {
        /// <summary>
        /// The Hostname used for the SCM URL.
        /// </summary>
        public readonly string HostName;
        /// <summary>
        /// The ID of the Key Vault Secret which contains the SSL Certificate.
        /// </summary>
        public readonly string KeyVaultId;
        /// <summary>
        /// Is Client Certificate Negotiation enabled?
        /// </summary>
        public readonly bool NegotiateClientCertificate;

        [OutputConstructor]
        private GetServiceHostnameConfigurationsManagementsResult(
            string hostName,
            string keyVaultId,
            bool negotiateClientCertificate)
        {
            HostName = hostName;
            KeyVaultId = keyVaultId;
            NegotiateClientCertificate = negotiateClientCertificate;
        }
    }

    [OutputType]
    public sealed class GetServiceHostnameConfigurationsPortalsResult
    {
        /// <summary>
        /// The Hostname used for the SCM URL.
        /// </summary>
        public readonly string HostName;
        /// <summary>
        /// The ID of the Key Vault Secret which contains the SSL Certificate.
        /// </summary>
        public readonly string KeyVaultId;
        /// <summary>
        /// Is Client Certificate Negotiation enabled?
        /// </summary>
        public readonly bool NegotiateClientCertificate;

        [OutputConstructor]
        private GetServiceHostnameConfigurationsPortalsResult(
            string hostName,
            string keyVaultId,
            bool negotiateClientCertificate)
        {
            HostName = hostName;
            KeyVaultId = keyVaultId;
            NegotiateClientCertificate = negotiateClientCertificate;
        }
    }

    [OutputType]
    public sealed class GetServiceHostnameConfigurationsProxiesResult
    {
        /// <summary>
        /// Is this the default SSL Binding?
        /// </summary>
        public readonly bool DefaultSslBinding;
        /// <summary>
        /// The Hostname used for the SCM URL.
        /// </summary>
        public readonly string HostName;
        /// <summary>
        /// The ID of the Key Vault Secret which contains the SSL Certificate.
        /// </summary>
        public readonly string KeyVaultId;
        /// <summary>
        /// Is Client Certificate Negotiation enabled?
        /// </summary>
        public readonly bool NegotiateClientCertificate;

        [OutputConstructor]
        private GetServiceHostnameConfigurationsProxiesResult(
            bool defaultSslBinding,
            string hostName,
            string keyVaultId,
            bool negotiateClientCertificate)
        {
            DefaultSslBinding = defaultSslBinding;
            HostName = hostName;
            KeyVaultId = keyVaultId;
            NegotiateClientCertificate = negotiateClientCertificate;
        }
    }

    [OutputType]
    public sealed class GetServiceHostnameConfigurationsResult
    {
        /// <summary>
        /// One or more `management` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<GetServiceHostnameConfigurationsManagementsResult> Managements;
        /// <summary>
        /// One or more `portal` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<GetServiceHostnameConfigurationsPortalsResult> Portals;
        /// <summary>
        /// One or more `proxy` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<GetServiceHostnameConfigurationsProxiesResult> Proxies;
        /// <summary>
        /// One or more `scm` blocks as documented below.
        /// </summary>
        public readonly ImmutableArray<GetServiceHostnameConfigurationsScmsResult> Scms;

        [OutputConstructor]
        private GetServiceHostnameConfigurationsResult(
            ImmutableArray<GetServiceHostnameConfigurationsManagementsResult> managements,
            ImmutableArray<GetServiceHostnameConfigurationsPortalsResult> portals,
            ImmutableArray<GetServiceHostnameConfigurationsProxiesResult> proxies,
            ImmutableArray<GetServiceHostnameConfigurationsScmsResult> scms)
        {
            Managements = managements;
            Portals = portals;
            Proxies = proxies;
            Scms = scms;
        }
    }

    [OutputType]
    public sealed class GetServiceHostnameConfigurationsScmsResult
    {
        /// <summary>
        /// The Hostname used for the SCM URL.
        /// </summary>
        public readonly string HostName;
        /// <summary>
        /// The ID of the Key Vault Secret which contains the SSL Certificate.
        /// </summary>
        public readonly string KeyVaultId;
        /// <summary>
        /// Is Client Certificate Negotiation enabled?
        /// </summary>
        public readonly bool NegotiateClientCertificate;

        [OutputConstructor]
        private GetServiceHostnameConfigurationsScmsResult(
            string hostName,
            string keyVaultId,
            bool negotiateClientCertificate)
        {
            HostName = hostName;
            KeyVaultId = keyVaultId;
            NegotiateClientCertificate = negotiateClientCertificate;
        }
    }

    [OutputType]
    public sealed class GetServiceSkuResult
    {
        /// <summary>
        /// Specifies the number of units associated with this API Management service.
        /// </summary>
        public readonly int Capacity;
        /// <summary>
        /// The name of the API Management service.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetServiceSkuResult(
            int capacity,
            string name)
        {
            Capacity = capacity;
            Name = name;
        }
    }
    }
}
