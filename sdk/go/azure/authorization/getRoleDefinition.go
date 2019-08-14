// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package authorization

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to access information about an existing Role Definition.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/role_definition.html.markdown.
func LookupRoleDefinition(ctx *pulumi.Context, args *GetRoleDefinitionArgs) (*GetRoleDefinitionResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["roleDefinitionId"] = args.RoleDefinitionId
		inputs["scope"] = args.Scope
	}
	outputs, err := ctx.Invoke("azure:authorization/getRoleDefinition:getRoleDefinition", inputs)
	if err != nil {
		return nil, err
	}
	return &GetRoleDefinitionResult{
		AssignableScopes: outputs["assignableScopes"],
		Description: outputs["description"],
		Name: outputs["name"],
		Permissions: outputs["permissions"],
		RoleDefinitionId: outputs["roleDefinitionId"],
		Scope: outputs["scope"],
		Type: outputs["type"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getRoleDefinition.
type GetRoleDefinitionArgs struct {
	// Specifies the Name of either a built-in or custom Role Definition.
	Name interface{}
	// Specifies the ID of the Role Definition as a UUID/GUID.
	RoleDefinitionId interface{}
	// Specifies the Scope at which the Custom Role Definition exists.
	Scope interface{}
}

// A collection of values returned by getRoleDefinition.
type GetRoleDefinitionResult struct {
	// One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
	AssignableScopes interface{}
	// the Description of the built-in Role.
	Description interface{}
	Name interface{}
	// a `permissions` block as documented below.
	Permissions interface{}
	RoleDefinitionId interface{}
	Scope interface{}
	// the Type of the Role.
	Type interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
