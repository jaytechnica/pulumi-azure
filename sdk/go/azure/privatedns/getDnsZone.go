// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package privatedns

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Private DNS Zone.
func GetDnsZone(ctx *pulumi.Context, args *GetDnsZoneArgs, opts ...pulumi.InvokeOption) (*GetDnsZoneResult, error) {
	var rv GetDnsZoneResult
	err := ctx.Invoke("azure:privatedns/getDnsZone:getDnsZone", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDnsZone.
type GetDnsZoneArgs struct {
	// The name of the Private DNS Zone.
	Name string `pulumi:"name"`
	// The Name of the Resource Group where the Private DNS Zone exists.
	// If the Name of the Resource Group is not provided, the first Private DNS Zone from the list of Private
	// DNS Zones in your subscription that matches `name` will be returned.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
}

// A collection of values returned by getDnsZone.
type GetDnsZoneResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Maximum number of recordsets that can be created in this Private Zone.
	MaxNumberOfRecordSets int `pulumi:"maxNumberOfRecordSets"`
	// Maximum number of Virtual Networks that can be linked to this Private Zone.
	MaxNumberOfVirtualNetworkLinks int `pulumi:"maxNumberOfVirtualNetworkLinks"`
	// Maximum number of Virtual Networks that can be linked to this Private Zone with registration enabled.
	MaxNumberOfVirtualNetworkLinksWithRegistration int    `pulumi:"maxNumberOfVirtualNetworkLinksWithRegistration"`
	Name                                           string `pulumi:"name"`
	// The number of recordsets currently in the zone.
	NumberOfRecordSets int    `pulumi:"numberOfRecordSets"`
	ResourceGroupName  string `pulumi:"resourceGroupName"`
	// A mapping of tags for the zone.
	Tags map[string]string `pulumi:"tags"`
}