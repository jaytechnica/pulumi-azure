// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apimanagement

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages an API Management User Assignment to a Group.
type GroupUser struct {
	s *pulumi.ResourceState
}

// NewGroupUser registers a new resource with the given unique name, arguments, and options.
func NewGroupUser(ctx *pulumi.Context,
	name string, args *GroupUserArgs, opts ...pulumi.ResourceOpt) (*GroupUser, error) {
	if args == nil || args.ApiManagementName == nil {
		return nil, errors.New("missing required argument 'ApiManagementName'")
	}
	if args == nil || args.GroupName == nil {
		return nil, errors.New("missing required argument 'GroupName'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.UserId == nil {
		return nil, errors.New("missing required argument 'UserId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["apiManagementName"] = nil
		inputs["groupName"] = nil
		inputs["resourceGroupName"] = nil
		inputs["userId"] = nil
	} else {
		inputs["apiManagementName"] = args.ApiManagementName
		inputs["groupName"] = args.GroupName
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["userId"] = args.UserId
	}
	s, err := ctx.RegisterResource("azure:apimanagement/groupUser:GroupUser", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GroupUser{s: s}, nil
}

// GetGroupUser gets an existing GroupUser resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroupUser(ctx *pulumi.Context,
	name string, id pulumi.ID, state *GroupUserState, opts ...pulumi.ResourceOpt) (*GroupUser, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["apiManagementName"] = state.ApiManagementName
		inputs["groupName"] = state.GroupName
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["userId"] = state.UserId
	}
	s, err := ctx.ReadResource("azure:apimanagement/groupUser:GroupUser", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GroupUser{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *GroupUser) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *GroupUser) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name of the API Management Service. Changing this forces a new resource to be created.
func (r *GroupUser) ApiManagementName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["apiManagementName"])
}

// The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.
func (r *GroupUser) GroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["groupName"])
}

// The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
func (r *GroupUser) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.
func (r *GroupUser) UserId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["userId"])
}

// Input properties used for looking up and filtering GroupUser resources.
type GroupUserState struct {
	// The name of the API Management Service. Changing this forces a new resource to be created.
	ApiManagementName interface{}
	// The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.
	GroupName interface{}
	// The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.
	UserId interface{}
}

// The set of arguments for constructing a GroupUser resource.
type GroupUserArgs struct {
	// The name of the API Management Service. Changing this forces a new resource to be created.
	ApiManagementName interface{}
	// The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.
	GroupName interface{}
	// The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.
	UserId interface{}
}
