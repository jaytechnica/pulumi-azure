// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package proximity

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Proximity Placement Group.
func LookupPlacementGroup(ctx *pulumi.Context, args *LookupPlacementGroupArgs, opts ...pulumi.InvokeOption) (*LookupPlacementGroupResult, error) {
	var rv LookupPlacementGroupResult
	err := ctx.Invoke("azure:proximity/getPlacementGroup:getPlacementGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPlacementGroup.
type LookupPlacementGroupArgs struct {
	// The name of the Proximity Placement Group.
	Name string `pulumi:"name"`
	// The name of the resource group in which the Proximity Placement Group exists.
	ResourceGroupName string `pulumi:"resourceGroupName"`
}

// A collection of values returned by getPlacementGroup.
type LookupPlacementGroupResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id                string            `pulumi:"id"`
	Location          string            `pulumi:"location"`
	Name              string            `pulumi:"name"`
	ResourceGroupName string            `pulumi:"resourceGroupName"`
	Tags              map[string]string `pulumi:"tags"`
}
