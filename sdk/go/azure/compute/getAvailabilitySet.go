// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access information about an existing Availability Set.
func LookupAvailabilitySet(ctx *pulumi.Context, args *GetAvailabilitySetArgs) (*GetAvailabilitySetResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
	}
	outputs, err := ctx.Invoke("azure:compute/getAvailabilitySet:getAvailabilitySet", inputs)
	if err != nil {
		return nil, err
	}
	return &GetAvailabilitySetResult{
		Location: outputs["location"],
		Managed: outputs["managed"],
		PlatformFaultDomainCount: outputs["platformFaultDomainCount"],
		PlatformUpdateDomainCount: outputs["platformUpdateDomainCount"],
		Tags: outputs["tags"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getAvailabilitySet.
type GetAvailabilitySetArgs struct {
	// The name of the Availability Set.
	Name interface{}
	// The name of the resource group in which the Availability Set exists.
	ResourceGroupName interface{}
}

// A collection of values returned by getAvailabilitySet.
type GetAvailabilitySetResult struct {
	// The supported Azure location where the Availability Set exists.
	Location interface{}
	// Whether the availability set is managed or not.
	Managed interface{}
	// The number of fault domains that are used.
	PlatformFaultDomainCount interface{}
	// The number of update domains that are used.
	PlatformUpdateDomainCount interface{}
	// A mapping of tags assigned to the resource.
	Tags interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
