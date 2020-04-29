// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package privatelink

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access endpoint connection information about an existing Private Link Service.
//
// > **NOTE** Private Link is currently in Public Preview.
func GetServiceEndpointConnections(ctx *pulumi.Context, args *GetServiceEndpointConnectionsArgs, opts ...pulumi.InvokeOption) (*GetServiceEndpointConnectionsResult, error) {
	var rv GetServiceEndpointConnectionsResult
	err := ctx.Invoke("azure:privatelink/getServiceEndpointConnections:getServiceEndpointConnections", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getServiceEndpointConnections.
type GetServiceEndpointConnectionsArgs struct {
	// The name of the resource group in which the private link service resides.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// The resource ID of the private link service.
	ServiceId string `pulumi:"serviceId"`
}

// A collection of values returned by getServiceEndpointConnections.
type GetServiceEndpointConnectionsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id                         string                                                   `pulumi:"id"`
	Location                   string                                                   `pulumi:"location"`
	PrivateEndpointConnections []GetServiceEndpointConnectionsPrivateEndpointConnection `pulumi:"privateEndpointConnections"`
	ResourceGroupName          string                                                   `pulumi:"resourceGroupName"`
	ServiceId                  string                                                   `pulumi:"serviceId"`
	// The name of the private link service.
	ServiceName string `pulumi:"serviceName"`
}
