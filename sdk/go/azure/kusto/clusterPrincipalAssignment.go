// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kusto

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Kusto Cluster Principal Assignment.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/kusto"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		current, err := core.GetClientConfig(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		rg, err := core.NewResourceGroup(ctx, "rg", &core.ResourceGroupArgs{
// 			Location: pulumi.String("East US"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleCluster, err := kusto.NewCluster(ctx, "exampleCluster", &kusto.ClusterArgs{
// 			Location:          rg.Location,
// 			ResourceGroupName: rg.Name,
// 			Sku: &kusto.ClusterSkuArgs{
// 				Name:     pulumi.String("Standard_D13_v2"),
// 				Capacity: pulumi.Int(2),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = kusto.NewClusterPrincipalAssignment(ctx, "exampleClusterPrincipalAssignment", &kusto.ClusterPrincipalAssignmentArgs{
// 			ResourceGroupName: rg.Name,
// 			ClusterName:       exampleCluster.Name,
// 			TenantId:          pulumi.String(current.TenantId),
// 			PrincipalId:       pulumi.String(current.ClientId),
// 			PrincipalType:     pulumi.String("App"),
// 			Role:              pulumi.String("AllDatabasesAdmin"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type ClusterPrincipalAssignment struct {
	pulumi.CustomResourceState

	// The name of the cluster in which to create the resource. Changing this forces a new resource to be created.
	ClusterName pulumi.StringOutput `pulumi:"clusterName"`
	Name        pulumi.StringOutput `pulumi:"name"`
	// The object id of the principal. Changing this forces a new resource to be created.
	PrincipalId pulumi.StringOutput `pulumi:"principalId"`
	// The name of the principal.
	PrincipalName pulumi.StringOutput `pulumi:"principalName"`
	// The type of the principal. Valid values include `App`, `Group`, `User`. Changing this forces a new resource to be created.
	PrincipalType pulumi.StringOutput `pulumi:"principalType"`
	// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// The cluster role assigned to the principal. Valid values include `AllDatabasesAdmin` and `AllDatabasesViewer`. Changing this forces a new resource to be created.
	Role pulumi.StringOutput `pulumi:"role"`
	// The tenant id in which the principal resides. Changing this forces a new resource to be created.
	TenantId pulumi.StringOutput `pulumi:"tenantId"`
	// The name of the tenant.
	TenantName pulumi.StringOutput `pulumi:"tenantName"`
}

// NewClusterPrincipalAssignment registers a new resource with the given unique name, arguments, and options.
func NewClusterPrincipalAssignment(ctx *pulumi.Context,
	name string, args *ClusterPrincipalAssignmentArgs, opts ...pulumi.ResourceOption) (*ClusterPrincipalAssignment, error) {
	if args == nil || args.ClusterName == nil {
		return nil, errors.New("missing required argument 'ClusterName'")
	}
	if args == nil || args.PrincipalId == nil {
		return nil, errors.New("missing required argument 'PrincipalId'")
	}
	if args == nil || args.PrincipalType == nil {
		return nil, errors.New("missing required argument 'PrincipalType'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	if args == nil || args.TenantId == nil {
		return nil, errors.New("missing required argument 'TenantId'")
	}
	if args == nil {
		args = &ClusterPrincipalAssignmentArgs{}
	}
	var resource ClusterPrincipalAssignment
	err := ctx.RegisterResource("azure:kusto/clusterPrincipalAssignment:ClusterPrincipalAssignment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetClusterPrincipalAssignment gets an existing ClusterPrincipalAssignment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetClusterPrincipalAssignment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterPrincipalAssignmentState, opts ...pulumi.ResourceOption) (*ClusterPrincipalAssignment, error) {
	var resource ClusterPrincipalAssignment
	err := ctx.ReadResource("azure:kusto/clusterPrincipalAssignment:ClusterPrincipalAssignment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ClusterPrincipalAssignment resources.
type clusterPrincipalAssignmentState struct {
	// The name of the cluster in which to create the resource. Changing this forces a new resource to be created.
	ClusterName *string `pulumi:"clusterName"`
	Name        *string `pulumi:"name"`
	// The object id of the principal. Changing this forces a new resource to be created.
	PrincipalId *string `pulumi:"principalId"`
	// The name of the principal.
	PrincipalName *string `pulumi:"principalName"`
	// The type of the principal. Valid values include `App`, `Group`, `User`. Changing this forces a new resource to be created.
	PrincipalType *string `pulumi:"principalType"`
	// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// The cluster role assigned to the principal. Valid values include `AllDatabasesAdmin` and `AllDatabasesViewer`. Changing this forces a new resource to be created.
	Role *string `pulumi:"role"`
	// The tenant id in which the principal resides. Changing this forces a new resource to be created.
	TenantId *string `pulumi:"tenantId"`
	// The name of the tenant.
	TenantName *string `pulumi:"tenantName"`
}

type ClusterPrincipalAssignmentState struct {
	// The name of the cluster in which to create the resource. Changing this forces a new resource to be created.
	ClusterName pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	// The object id of the principal. Changing this forces a new resource to be created.
	PrincipalId pulumi.StringPtrInput
	// The name of the principal.
	PrincipalName pulumi.StringPtrInput
	// The type of the principal. Valid values include `App`, `Group`, `User`. Changing this forces a new resource to be created.
	PrincipalType pulumi.StringPtrInput
	// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringPtrInput
	// The cluster role assigned to the principal. Valid values include `AllDatabasesAdmin` and `AllDatabasesViewer`. Changing this forces a new resource to be created.
	Role pulumi.StringPtrInput
	// The tenant id in which the principal resides. Changing this forces a new resource to be created.
	TenantId pulumi.StringPtrInput
	// The name of the tenant.
	TenantName pulumi.StringPtrInput
}

func (ClusterPrincipalAssignmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterPrincipalAssignmentState)(nil)).Elem()
}

type clusterPrincipalAssignmentArgs struct {
	// The name of the cluster in which to create the resource. Changing this forces a new resource to be created.
	ClusterName string  `pulumi:"clusterName"`
	Name        *string `pulumi:"name"`
	// The object id of the principal. Changing this forces a new resource to be created.
	PrincipalId string `pulumi:"principalId"`
	// The type of the principal. Valid values include `App`, `Group`, `User`. Changing this forces a new resource to be created.
	PrincipalType string `pulumi:"principalType"`
	// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// The cluster role assigned to the principal. Valid values include `AllDatabasesAdmin` and `AllDatabasesViewer`. Changing this forces a new resource to be created.
	Role string `pulumi:"role"`
	// The tenant id in which the principal resides. Changing this forces a new resource to be created.
	TenantId string `pulumi:"tenantId"`
}

// The set of arguments for constructing a ClusterPrincipalAssignment resource.
type ClusterPrincipalAssignmentArgs struct {
	// The name of the cluster in which to create the resource. Changing this forces a new resource to be created.
	ClusterName pulumi.StringInput
	Name        pulumi.StringPtrInput
	// The object id of the principal. Changing this forces a new resource to be created.
	PrincipalId pulumi.StringInput
	// The type of the principal. Valid values include `App`, `Group`, `User`. Changing this forces a new resource to be created.
	PrincipalType pulumi.StringInput
	// The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringInput
	// The cluster role assigned to the principal. Valid values include `AllDatabasesAdmin` and `AllDatabasesViewer`. Changing this forces a new resource to be created.
	Role pulumi.StringInput
	// The tenant id in which the principal resides. Changing this forces a new resource to be created.
	TenantId pulumi.StringInput
}

func (ClusterPrincipalAssignmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterPrincipalAssignmentArgs)(nil)).Elem()
}
