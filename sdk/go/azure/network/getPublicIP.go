// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Public IP Address.
func GetPublicIP(ctx *pulumi.Context, args *GetPublicIPArgs, opts ...pulumi.InvokeOption) (*GetPublicIPResult, error) {
	var rv GetPublicIPResult
	err := ctx.Invoke("azure:network/getPublicIP:getPublicIP", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPublicIP.
type GetPublicIPArgs struct {
	// Specifies the name of the public IP address.
	Name string `pulumi:"name"`
	// Specifies the name of the resource group.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// A mapping of tags to assigned to the resource.
	Tags  map[string]string `pulumi:"tags"`
	Zones []string          `pulumi:"zones"`
}

// A collection of values returned by getPublicIP.
type GetPublicIPResult struct {
	AllocationMethod string `pulumi:"allocationMethod"`
	// The label for the Domain Name.
	DomainNameLabel string `pulumi:"domainNameLabel"`
	// Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone.
	Fqdn string `pulumi:"fqdn"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Specifies the timeout for the TCP idle connection.
	IdleTimeoutInMinutes int `pulumi:"idleTimeoutInMinutes"`
	// The IP address value that was allocated.
	IpAddress string `pulumi:"ipAddress"`
	// The IP version being used, for example `IPv4` or `IPv6`.
	IpVersion         string `pulumi:"ipVersion"`
	Location          string `pulumi:"location"`
	Name              string `pulumi:"name"`
	ResourceGroupName string `pulumi:"resourceGroupName"`
	ReverseFqdn       string `pulumi:"reverseFqdn"`
	Sku               string `pulumi:"sku"`
	// A mapping of tags to assigned to the resource.
	Tags  map[string]string `pulumi:"tags"`
	Zones []string          `pulumi:"zones"`
}
