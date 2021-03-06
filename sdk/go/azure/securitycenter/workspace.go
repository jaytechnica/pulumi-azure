// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package securitycenter

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages the subscription's Security Center Workspace.
//
// > **NOTE:** Owner access permission is required.
//
// > **NOTE:** The subscription's pricing model can not be `Free` for this to have any affect.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/operationalinsights"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/securitycenter"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
// 			Location: pulumi.String("westus"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleAnalyticsWorkspace, err := operationalinsights.NewAnalyticsWorkspace(ctx, "exampleAnalyticsWorkspace", &operationalinsights.AnalyticsWorkspaceArgs{
// 			Location:          exampleResourceGroup.Location,
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			Sku:               pulumi.String("PerGB2018"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = securitycenter.NewWorkspace(ctx, "exampleWorkspace", &securitycenter.WorkspaceArgs{
// 			Scope:       pulumi.String("/subscriptions/00000000-0000-0000-0000-000000000000"),
// 			WorkspaceId: exampleAnalyticsWorkspace.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Workspace struct {
	pulumi.CustomResourceState

	// The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.
	Scope pulumi.StringOutput `pulumi:"scope"`
	// The ID of the Log Analytics Workspace to save the data in.
	WorkspaceId pulumi.StringOutput `pulumi:"workspaceId"`
}

// NewWorkspace registers a new resource with the given unique name, arguments, and options.
func NewWorkspace(ctx *pulumi.Context,
	name string, args *WorkspaceArgs, opts ...pulumi.ResourceOption) (*Workspace, error) {
	if args == nil || args.Scope == nil {
		return nil, errors.New("missing required argument 'Scope'")
	}
	if args == nil || args.WorkspaceId == nil {
		return nil, errors.New("missing required argument 'WorkspaceId'")
	}
	if args == nil {
		args = &WorkspaceArgs{}
	}
	var resource Workspace
	err := ctx.RegisterResource("azure:securitycenter/workspace:Workspace", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWorkspace gets an existing Workspace resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWorkspace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WorkspaceState, opts ...pulumi.ResourceOption) (*Workspace, error) {
	var resource Workspace
	err := ctx.ReadResource("azure:securitycenter/workspace:Workspace", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Workspace resources.
type workspaceState struct {
	// The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.
	Scope *string `pulumi:"scope"`
	// The ID of the Log Analytics Workspace to save the data in.
	WorkspaceId *string `pulumi:"workspaceId"`
}

type WorkspaceState struct {
	// The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.
	Scope pulumi.StringPtrInput
	// The ID of the Log Analytics Workspace to save the data in.
	WorkspaceId pulumi.StringPtrInput
}

func (WorkspaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceState)(nil)).Elem()
}

type workspaceArgs struct {
	// The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.
	Scope string `pulumi:"scope"`
	// The ID of the Log Analytics Workspace to save the data in.
	WorkspaceId string `pulumi:"workspaceId"`
}

// The set of arguments for constructing a Workspace resource.
type WorkspaceArgs struct {
	// The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.
	Scope pulumi.StringInput
	// The ID of the Log Analytics Workspace to save the data in.
	WorkspaceId pulumi.StringInput
}

func (WorkspaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceArgs)(nil)).Elem()
}
