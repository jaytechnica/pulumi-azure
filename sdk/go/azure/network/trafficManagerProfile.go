// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Traffic Manager Profile to which multiple endpoints can be attached.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network"
// 	"github.com/pulumi/pulumi-random/sdk/v2/go/random"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		server, err := random.NewRandomId(ctx, "server", &random.RandomIdArgs{
// 			Keepers: pulumi.Float64Map{
// 				"azi_id": pulumi.Float64(1),
// 			},
// 			ByteLength: pulumi.Int(8),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
// 			Location: pulumi.String("West US"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = network.NewTrafficManagerProfile(ctx, "exampleTrafficManagerProfile", &network.TrafficManagerProfileArgs{
// 			ResourceGroupName:    exampleResourceGroup.Name,
// 			TrafficRoutingMethod: pulumi.String("Weighted"),
// 			DnsConfig: &network.TrafficManagerProfileDnsConfigArgs{
// 				RelativeName: server.Hex,
// 				Ttl:          pulumi.Int(100),
// 			},
// 			MonitorConfig: &network.TrafficManagerProfileMonitorConfigArgs{
// 				Protocol:                  pulumi.String("http"),
// 				Port:                      pulumi.Int(80),
// 				Path:                      pulumi.String("/"),
// 				IntervalInSeconds:         pulumi.Int(30),
// 				TimeoutInSeconds:          pulumi.Int(9),
// 				ToleratedNumberOfFailures: pulumi.Int(3),
// 			},
// 			Tags: pulumi.StringMap{
// 				"environment": pulumi.String("Production"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type TrafficManagerProfile struct {
	pulumi.CustomResourceState

	// This block specifies the DNS configuration of the Profile, it supports the fields documented below.
	DnsConfig TrafficManagerProfileDnsConfigOutput `pulumi:"dnsConfig"`
	// The FQDN of the created Profile.
	Fqdn pulumi.StringOutput `pulumi:"fqdn"`
	// This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.
	MonitorConfig TrafficManagerProfileMonitorConfigOutput `pulumi:"monitorConfig"`
	// The name of the Traffic Manager profile. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
	ProfileStatus pulumi.StringOutput `pulumi:"profileStatus"`
	// The name of the resource group in which to create the Traffic Manager profile.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// Specifies the algorithm used to route traffic, possible values are:
	TrafficRoutingMethod pulumi.StringOutput `pulumi:"trafficRoutingMethod"`
}

// NewTrafficManagerProfile registers a new resource with the given unique name, arguments, and options.
func NewTrafficManagerProfile(ctx *pulumi.Context,
	name string, args *TrafficManagerProfileArgs, opts ...pulumi.ResourceOption) (*TrafficManagerProfile, error) {
	if args == nil || args.DnsConfig == nil {
		return nil, errors.New("missing required argument 'DnsConfig'")
	}
	if args == nil || args.MonitorConfig == nil {
		return nil, errors.New("missing required argument 'MonitorConfig'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.TrafficRoutingMethod == nil {
		return nil, errors.New("missing required argument 'TrafficRoutingMethod'")
	}
	if args == nil {
		args = &TrafficManagerProfileArgs{}
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("azure:trafficmanager/profile:Profile"),
		},
	})
	opts = append(opts, aliases)
	var resource TrafficManagerProfile
	err := ctx.RegisterResource("azure:network/trafficManagerProfile:TrafficManagerProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTrafficManagerProfile gets an existing TrafficManagerProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTrafficManagerProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TrafficManagerProfileState, opts ...pulumi.ResourceOption) (*TrafficManagerProfile, error) {
	var resource TrafficManagerProfile
	err := ctx.ReadResource("azure:network/trafficManagerProfile:TrafficManagerProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TrafficManagerProfile resources.
type trafficManagerProfileState struct {
	// This block specifies the DNS configuration of the Profile, it supports the fields documented below.
	DnsConfig *TrafficManagerProfileDnsConfig `pulumi:"dnsConfig"`
	// The FQDN of the created Profile.
	Fqdn *string `pulumi:"fqdn"`
	// This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.
	MonitorConfig *TrafficManagerProfileMonitorConfig `pulumi:"monitorConfig"`
	// The name of the Traffic Manager profile. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
	ProfileStatus *string `pulumi:"profileStatus"`
	// The name of the resource group in which to create the Traffic Manager profile.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// Specifies the algorithm used to route traffic, possible values are:
	TrafficRoutingMethod *string `pulumi:"trafficRoutingMethod"`
}

type TrafficManagerProfileState struct {
	// This block specifies the DNS configuration of the Profile, it supports the fields documented below.
	DnsConfig TrafficManagerProfileDnsConfigPtrInput
	// The FQDN of the created Profile.
	Fqdn pulumi.StringPtrInput
	// This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.
	MonitorConfig TrafficManagerProfileMonitorConfigPtrInput
	// The name of the Traffic Manager profile. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
	ProfileStatus pulumi.StringPtrInput
	// The name of the resource group in which to create the Traffic Manager profile.
	ResourceGroupName pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// Specifies the algorithm used to route traffic, possible values are:
	TrafficRoutingMethod pulumi.StringPtrInput
}

func (TrafficManagerProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*trafficManagerProfileState)(nil)).Elem()
}

type trafficManagerProfileArgs struct {
	// This block specifies the DNS configuration of the Profile, it supports the fields documented below.
	DnsConfig TrafficManagerProfileDnsConfig `pulumi:"dnsConfig"`
	// This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.
	MonitorConfig TrafficManagerProfileMonitorConfig `pulumi:"monitorConfig"`
	// The name of the Traffic Manager profile. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
	ProfileStatus *string `pulumi:"profileStatus"`
	// The name of the resource group in which to create the Traffic Manager profile.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// Specifies the algorithm used to route traffic, possible values are:
	TrafficRoutingMethod string `pulumi:"trafficRoutingMethod"`
}

// The set of arguments for constructing a TrafficManagerProfile resource.
type TrafficManagerProfileArgs struct {
	// This block specifies the DNS configuration of the Profile, it supports the fields documented below.
	DnsConfig TrafficManagerProfileDnsConfigInput
	// This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.
	MonitorConfig TrafficManagerProfileMonitorConfigInput
	// The name of the Traffic Manager profile. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
	ProfileStatus pulumi.StringPtrInput
	// The name of the resource group in which to create the Traffic Manager profile.
	ResourceGroupName pulumi.StringInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// Specifies the algorithm used to route traffic, possible values are:
	TrafficRoutingMethod pulumi.StringInput
}

func (TrafficManagerProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*trafficManagerProfileArgs)(nil)).Elem()
}
