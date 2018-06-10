// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package automation

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a new Automation Credential.
type Credential struct {
	s *pulumi.ResourceState
}

// NewCredential registers a new resource with the given unique name, arguments, and options.
func NewCredential(ctx *pulumi.Context,
	name string, args *CredentialArgs, opts ...pulumi.ResourceOpt) (*Credential, error) {
	if args == nil || args.AccountName == nil {
		return nil, errors.New("missing required argument 'AccountName'")
	}
	if args == nil || args.Password == nil {
		return nil, errors.New("missing required argument 'Password'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.Username == nil {
		return nil, errors.New("missing required argument 'Username'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["accountName"] = nil
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["password"] = nil
		inputs["resourceGroupName"] = nil
		inputs["username"] = nil
	} else {
		inputs["accountName"] = args.AccountName
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["password"] = args.Password
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["username"] = args.Username
	}
	s, err := ctx.RegisterResource("azure:automation/credential:Credential", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Credential{s: s}, nil
}

// GetCredential gets an existing Credential resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCredential(ctx *pulumi.Context,
	name string, id pulumi.ID, state *CredentialState, opts ...pulumi.ResourceOpt) (*Credential, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["accountName"] = state.AccountName
		inputs["description"] = state.Description
		inputs["name"] = state.Name
		inputs["password"] = state.Password
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["username"] = state.Username
	}
	s, err := ctx.ReadResource("azure:automation/credential:Credential", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Credential{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Credential) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Credential) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.
func (r *Credential) AccountName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["accountName"])
}

// The description associated with this Automation Credential.
func (r *Credential) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Specifies the name of the Credential. Changing this forces a new resource to be created.
func (r *Credential) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The password associated with this Automation Credential.
func (r *Credential) Password() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["password"])
}

// The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.
func (r *Credential) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// The username associated with this Automation Credential.
func (r *Credential) Username() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["username"])
}

// Input properties used for looking up and filtering Credential resources.
type CredentialState struct {
	// The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.
	AccountName interface{}
	// The description associated with this Automation Credential.
	Description interface{}
	// Specifies the name of the Credential. Changing this forces a new resource to be created.
	Name interface{}
	// The password associated with this Automation Credential.
	Password interface{}
	// The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// The username associated with this Automation Credential.
	Username interface{}
}

// The set of arguments for constructing a Credential resource.
type CredentialArgs struct {
	// The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.
	AccountName interface{}
	// The description associated with this Automation Credential.
	Description interface{}
	// Specifies the name of the Credential. Changing this forces a new resource to be created.
	Name interface{}
	// The password associated with this Automation Credential.
	Password interface{}
	// The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// The username associated with this Automation Credential.
	Username interface{}
}