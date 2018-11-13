// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages the association between a Network Interface and a Load Balancer's NAT Rule.
type NetworkInterfaceNatRuleAssociation struct {
	s *pulumi.ResourceState
}

// NewNetworkInterfaceNatRuleAssociation registers a new resource with the given unique name, arguments, and options.
func NewNetworkInterfaceNatRuleAssociation(ctx *pulumi.Context,
	name string, args *NetworkInterfaceNatRuleAssociationArgs, opts ...pulumi.ResourceOpt) (*NetworkInterfaceNatRuleAssociation, error) {
	if args == nil || args.IpConfigurationName == nil {
		return nil, errors.New("missing required argument 'IpConfigurationName'")
	}
	if args == nil || args.NatRuleId == nil {
		return nil, errors.New("missing required argument 'NatRuleId'")
	}
	if args == nil || args.NetworkInterfaceId == nil {
		return nil, errors.New("missing required argument 'NetworkInterfaceId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["ipConfigurationName"] = nil
		inputs["natRuleId"] = nil
		inputs["networkInterfaceId"] = nil
	} else {
		inputs["ipConfigurationName"] = args.IpConfigurationName
		inputs["natRuleId"] = args.NatRuleId
		inputs["networkInterfaceId"] = args.NetworkInterfaceId
	}
	s, err := ctx.RegisterResource("azure:network/networkInterfaceNatRuleAssociation:NetworkInterfaceNatRuleAssociation", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NetworkInterfaceNatRuleAssociation{s: s}, nil
}

// GetNetworkInterfaceNatRuleAssociation gets an existing NetworkInterfaceNatRuleAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkInterfaceNatRuleAssociation(ctx *pulumi.Context,
	name string, id pulumi.ID, state *NetworkInterfaceNatRuleAssociationState, opts ...pulumi.ResourceOpt) (*NetworkInterfaceNatRuleAssociation, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["ipConfigurationName"] = state.IpConfigurationName
		inputs["natRuleId"] = state.NatRuleId
		inputs["networkInterfaceId"] = state.NetworkInterfaceId
	}
	s, err := ctx.ReadResource("azure:network/networkInterfaceNatRuleAssociation:NetworkInterfaceNatRuleAssociation", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NetworkInterfaceNatRuleAssociation{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *NetworkInterfaceNatRuleAssociation) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *NetworkInterfaceNatRuleAssociation) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
func (r *NetworkInterfaceNatRuleAssociation) IpConfigurationName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ipConfigurationName"])
}

// The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
func (r *NetworkInterfaceNatRuleAssociation) NatRuleId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["natRuleId"])
}

// The ID of the Network Interface. Changing this forces a new resource to be created.
func (r *NetworkInterfaceNatRuleAssociation) NetworkInterfaceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["networkInterfaceId"])
}

// Input properties used for looking up and filtering NetworkInterfaceNatRuleAssociation resources.
type NetworkInterfaceNatRuleAssociationState struct {
	// The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
	IpConfigurationName interface{}
	// The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
	NatRuleId interface{}
	// The ID of the Network Interface. Changing this forces a new resource to be created.
	NetworkInterfaceId interface{}
}

// The set of arguments for constructing a NetworkInterfaceNatRuleAssociation resource.
type NetworkInterfaceNatRuleAssociationArgs struct {
	// The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.
	IpConfigurationName interface{}
	// The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.
	NatRuleId interface{}
	// The ID of the Network Interface. Changing this forces a new resource to be created.
	NetworkInterfaceId interface{}
}
