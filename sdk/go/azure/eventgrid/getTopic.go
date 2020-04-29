// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eventgrid

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing EventGrid Topic
func LookupTopic(ctx *pulumi.Context, args *LookupTopicArgs, opts ...pulumi.InvokeOption) (*LookupTopicResult, error) {
	var rv LookupTopicResult
	err := ctx.Invoke("azure:eventgrid/getTopic:getTopic", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTopic.
type LookupTopicArgs struct {
	// The name of the EventGrid Topic resource.
	Name string `pulumi:"name"`
	// The name of the resource group in which the EventGrid Topic exists.
	ResourceGroupName string            `pulumi:"resourceGroupName"`
	Tags              map[string]string `pulumi:"tags"`
}

// A collection of values returned by getTopic.
type LookupTopicResult struct {
	// The Endpoint associated with the EventGrid Topic.
	Endpoint string `pulumi:"endpoint"`
	// The provider-assigned unique ID for this managed resource.
	Id       string `pulumi:"id"`
	Location string `pulumi:"location"`
	Name     string `pulumi:"name"`
	// The Primary Shared Access Key associated with the EventGrid Topic.
	PrimaryAccessKey  string `pulumi:"primaryAccessKey"`
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// The Secondary Shared Access Key associated with the EventGrid Topic.
	SecondaryAccessKey string            `pulumi:"secondaryAccessKey"`
	Tags               map[string]string `pulumi:"tags"`
}
