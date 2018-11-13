// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ad

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Service Principal associated with an Application within Azure Active Directory.
// 
// -> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
type ServicePrincipal struct {
	s *pulumi.ResourceState
}

// NewServicePrincipal registers a new resource with the given unique name, arguments, and options.
func NewServicePrincipal(ctx *pulumi.Context,
	name string, args *ServicePrincipalArgs, opts ...pulumi.ResourceOpt) (*ServicePrincipal, error) {
	if args == nil || args.ApplicationId == nil {
		return nil, errors.New("missing required argument 'ApplicationId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["applicationId"] = nil
	} else {
		inputs["applicationId"] = args.ApplicationId
	}
	inputs["displayName"] = nil
	s, err := ctx.RegisterResource("azure:ad/servicePrincipal:ServicePrincipal", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ServicePrincipal{s: s}, nil
}

// GetServicePrincipal gets an existing ServicePrincipal resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServicePrincipal(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ServicePrincipalState, opts ...pulumi.ResourceOpt) (*ServicePrincipal, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["applicationId"] = state.ApplicationId
		inputs["displayName"] = state.DisplayName
	}
	s, err := ctx.ReadResource("azure:ad/servicePrincipal:ServicePrincipal", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ServicePrincipal{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ServicePrincipal) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ServicePrincipal) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ID of the Azure AD Application for which to create a Service Principal.
func (r *ServicePrincipal) ApplicationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["applicationId"])
}

// The Display Name of the Azure Active Directory Application associated with this Service Principal.
func (r *ServicePrincipal) DisplayName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["displayName"])
}

// Input properties used for looking up and filtering ServicePrincipal resources.
type ServicePrincipalState struct {
	// The ID of the Azure AD Application for which to create a Service Principal.
	ApplicationId interface{}
	// The Display Name of the Azure Active Directory Application associated with this Service Principal.
	DisplayName interface{}
}

// The set of arguments for constructing a ServicePrincipal resource.
type ServicePrincipalArgs struct {
	// The ID of the Azure AD Application for which to create a Service Principal.
	ApplicationId interface{}
}
