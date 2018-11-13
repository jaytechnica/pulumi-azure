// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manage an Application Security Group.
type ApplicationSecurityGroup struct {
	s *pulumi.ResourceState
}

// NewApplicationSecurityGroup registers a new resource with the given unique name, arguments, and options.
func NewApplicationSecurityGroup(ctx *pulumi.Context,
	name string, args *ApplicationSecurityGroupArgs, opts ...pulumi.ResourceOpt) (*ApplicationSecurityGroup, error) {
	if args == nil || args.Location == nil {
		return nil, errors.New("missing required argument 'Location'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["location"] = nil
		inputs["name"] = nil
		inputs["resourceGroupName"] = nil
		inputs["tags"] = nil
	} else {
		inputs["location"] = args.Location
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["tags"] = args.Tags
	}
	s, err := ctx.RegisterResource("azure:network/applicationSecurityGroup:ApplicationSecurityGroup", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ApplicationSecurityGroup{s: s}, nil
}

// GetApplicationSecurityGroup gets an existing ApplicationSecurityGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplicationSecurityGroup(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ApplicationSecurityGroupState, opts ...pulumi.ResourceOpt) (*ApplicationSecurityGroup, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["location"] = state.Location
		inputs["name"] = state.Name
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("azure:network/applicationSecurityGroup:ApplicationSecurityGroup", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ApplicationSecurityGroup{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ApplicationSecurityGroup) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ApplicationSecurityGroup) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
func (r *ApplicationSecurityGroup) Location() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["location"])
}

// Specifies the name of the Application Security Group. Changing this forces a new resource to be created.
func (r *ApplicationSecurityGroup) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the resource group in which to create the Application Security Group.
func (r *ApplicationSecurityGroup) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// A mapping of tags to assign to the resource.
func (r *ApplicationSecurityGroup) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering ApplicationSecurityGroup resources.
type ApplicationSecurityGroupState struct {
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location interface{}
	// Specifies the name of the Application Security Group. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the resource group in which to create the Application Security Group.
	ResourceGroupName interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a ApplicationSecurityGroup resource.
type ApplicationSecurityGroupArgs struct {
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location interface{}
	// Specifies the name of the Application Security Group. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the resource group in which to create the Application Security Group.
	ResourceGroupName interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
