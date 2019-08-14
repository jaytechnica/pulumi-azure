// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Traffic Manager Profile to which multiple endpoints can be attached.
// 
// ## Notes
// 
// The Traffic Manager is created with the location `global`.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_profile.html.markdown.
type TrafficManagerProfile struct {
	s *pulumi.ResourceState
}

// NewTrafficManagerProfile registers a new resource with the given unique name, arguments, and options.
func NewTrafficManagerProfile(ctx *pulumi.Context,
	name string, args *TrafficManagerProfileArgs, opts ...pulumi.ResourceOpt) (*TrafficManagerProfile, error) {
	if args == nil || args.DnsConfigs == nil {
		return nil, errors.New("missing required argument 'DnsConfigs'")
	}
	if args == nil || args.MonitorConfigs == nil {
		return nil, errors.New("missing required argument 'MonitorConfigs'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.TrafficRoutingMethod == nil {
		return nil, errors.New("missing required argument 'TrafficRoutingMethod'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["dnsConfigs"] = nil
		inputs["monitorConfigs"] = nil
		inputs["name"] = nil
		inputs["profileStatus"] = nil
		inputs["resourceGroupName"] = nil
		inputs["tags"] = nil
		inputs["trafficRoutingMethod"] = nil
	} else {
		inputs["dnsConfigs"] = args.DnsConfigs
		inputs["monitorConfigs"] = args.MonitorConfigs
		inputs["name"] = args.Name
		inputs["profileStatus"] = args.ProfileStatus
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["tags"] = args.Tags
		inputs["trafficRoutingMethod"] = args.TrafficRoutingMethod
	}
	inputs["fqdn"] = nil
	s, err := ctx.RegisterResource("azure:network/trafficManagerProfile:TrafficManagerProfile", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TrafficManagerProfile{s: s}, nil
}

// GetTrafficManagerProfile gets an existing TrafficManagerProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTrafficManagerProfile(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TrafficManagerProfileState, opts ...pulumi.ResourceOpt) (*TrafficManagerProfile, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["dnsConfigs"] = state.DnsConfigs
		inputs["fqdn"] = state.Fqdn
		inputs["monitorConfigs"] = state.MonitorConfigs
		inputs["name"] = state.Name
		inputs["profileStatus"] = state.ProfileStatus
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["tags"] = state.Tags
		inputs["trafficRoutingMethod"] = state.TrafficRoutingMethod
	}
	s, err := ctx.ReadResource("azure:network/trafficManagerProfile:TrafficManagerProfile", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TrafficManagerProfile{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *TrafficManagerProfile) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *TrafficManagerProfile) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// This block specifies the DNS configuration of the
// Profile, it supports the fields documented below.
func (r *TrafficManagerProfile) DnsConfigs() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["dnsConfigs"])
}

// The FQDN of the created Profile.
func (r *TrafficManagerProfile) Fqdn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fqdn"])
}

// This block specifies the Endpoint monitoring
// configuration for the Profile, it supports the fields documented below.
func (r *TrafficManagerProfile) MonitorConfigs() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["monitorConfigs"])
}

// The name of the virtual network. Changing this forces a
// new resource to be created.
func (r *TrafficManagerProfile) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The status of the profile, can be set to either
// `Enabled` or `Disabled`. Defaults to `Enabled`.
func (r *TrafficManagerProfile) ProfileStatus() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["profileStatus"])
}

// The name of the resource group in which to
// create the virtual network.
func (r *TrafficManagerProfile) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// A mapping of tags to assign to the resource.
func (r *TrafficManagerProfile) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Specifies the algorithm used to route traffic, possible values are:
// - `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
// - `MultiValue`- All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type ‘External’ and are specified as IPv4 or IPv6 addresses.
// - `Performance` - Traffic is routed via the User's closest Endpoint
// - `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
// - `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
// - `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
func (r *TrafficManagerProfile) TrafficRoutingMethod() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["trafficRoutingMethod"])
}

// Input properties used for looking up and filtering TrafficManagerProfile resources.
type TrafficManagerProfileState struct {
	// This block specifies the DNS configuration of the
	// Profile, it supports the fields documented below.
	DnsConfigs interface{}
	// The FQDN of the created Profile.
	Fqdn interface{}
	// This block specifies the Endpoint monitoring
	// configuration for the Profile, it supports the fields documented below.
	MonitorConfigs interface{}
	// The name of the virtual network. Changing this forces a
	// new resource to be created.
	Name interface{}
	// The status of the profile, can be set to either
	// `Enabled` or `Disabled`. Defaults to `Enabled`.
	ProfileStatus interface{}
	// The name of the resource group in which to
	// create the virtual network.
	ResourceGroupName interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// Specifies the algorithm used to route traffic, possible values are:
	// - `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
	// - `MultiValue`- All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type ‘External’ and are specified as IPv4 or IPv6 addresses.
	// - `Performance` - Traffic is routed via the User's closest Endpoint
	// - `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
	// - `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
	// - `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
	TrafficRoutingMethod interface{}
}

// The set of arguments for constructing a TrafficManagerProfile resource.
type TrafficManagerProfileArgs struct {
	// This block specifies the DNS configuration of the
	// Profile, it supports the fields documented below.
	DnsConfigs interface{}
	// This block specifies the Endpoint monitoring
	// configuration for the Profile, it supports the fields documented below.
	MonitorConfigs interface{}
	// The name of the virtual network. Changing this forces a
	// new resource to be created.
	Name interface{}
	// The status of the profile, can be set to either
	// `Enabled` or `Disabled`. Defaults to `Enabled`.
	ProfileStatus interface{}
	// The name of the resource group in which to
	// create the virtual network.
	ResourceGroupName interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// Specifies the algorithm used to route traffic, possible values are:
	// - `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
	// - `MultiValue`- All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type ‘External’ and are specified as IPv4 or IPv6 addresses.
	// - `Performance` - Traffic is routed via the User's closest Endpoint
	// - `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
	// - `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
	// - `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
	TrafficRoutingMethod interface{}
}
