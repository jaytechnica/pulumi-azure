// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appservice

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing App Service.
func LookupAppService(ctx *pulumi.Context, args *LookupAppServiceArgs, opts ...pulumi.InvokeOption) (*LookupAppServiceResult, error) {
	var rv LookupAppServiceResult
	err := ctx.Invoke("azure:appservice/getAppService:getAppService", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAppService.
type LookupAppServiceArgs struct {
	// The name of the App Service.
	Name string `pulumi:"name"`
	// The Name of the Resource Group where the App Service exists.
	ResourceGroupName string `pulumi:"resourceGroupName"`
}

// A collection of values returned by getAppService.
type LookupAppServiceResult struct {
	// The ID of the App Service Plan within which the App Service exists.
	AppServicePlanId string `pulumi:"appServicePlanId"`
	// A key-value pair of App Settings for the App Service.
	AppSettings map[string]string `pulumi:"appSettings"`
	// Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?
	ClientAffinityEnabled bool `pulumi:"clientAffinityEnabled"`
	// Does the App Service require client certificates for incoming requests?
	ClientCertEnabled bool `pulumi:"clientCertEnabled"`
	// An `connectionString` block as defined below.
	ConnectionStrings []GetAppServiceConnectionString `pulumi:"connectionStrings"`
	// The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
	DefaultSiteHostname string `pulumi:"defaultSiteHostname"`
	// Is the App Service Enabled?
	Enabled bool `pulumi:"enabled"`
	// Can the App Service only be accessed via HTTPS?
	HttpsOnly bool `pulumi:"httpsOnly"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The Azure location where the App Service exists.
	Location string `pulumi:"location"`
	// The name of the Connection String.
	Name string `pulumi:"name"`
	// A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
	OutboundIpAddresses string `pulumi:"outboundIpAddresses"`
	// A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outboundIpAddresses`.
	PossibleOutboundIpAddresses string `pulumi:"possibleOutboundIpAddresses"`
	ResourceGroupName           string `pulumi:"resourceGroupName"`
	// A `siteConfig` block as defined below.
	SiteConfigs     []GetAppServiceSiteConfig     `pulumi:"siteConfigs"`
	SiteCredentials []GetAppServiceSiteCredential `pulumi:"siteCredentials"`
	SourceControls  []GetAppServiceSourceControl  `pulumi:"sourceControls"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}
