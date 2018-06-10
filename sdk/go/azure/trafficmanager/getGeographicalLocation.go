// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package trafficmanager

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access the ID of a specified Traffic Manager Geographical Location within the Geographical Hierarchy.
func LookupeographicalLocation(ctx *pulumi.Context, args *GetGeographicalLocationArgs) error {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	_, err := ctx.Invoke("azure:trafficmanager/getGeographicalLocation:getGeographicalLocation", inputs)
	return err
}

// A collection of arguments for invoking getGeographicalLocation.
type GetGeographicalLocationArgs struct {
	// Specifies the name of the Location, for example `World`, `Europe` or `Germany`.
	Name interface{}
}