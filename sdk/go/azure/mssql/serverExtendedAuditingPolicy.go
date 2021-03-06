// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mssql

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Ms Sql Server Extended Auditing Policy.
//
// > **NOTE:** The Server Extended Auditing Policy Can be set inline here as well as with the mssqlServerExtendedAuditingPolicy resource resource. You can only use one or the other and using both will cause a conflict.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/mssql"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/storage"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
// 			Location: pulumi.String("West Europe"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleServer, err := mssql.NewServer(ctx, "exampleServer", &mssql.ServerArgs{
// 			ResourceGroupName:          exampleResourceGroup.Name,
// 			Location:                   exampleResourceGroup.Location,
// 			Version:                    pulumi.String("12.0"),
// 			AdministratorLogin:         pulumi.String("missadministrator"),
// 			AdministratorLoginPassword: pulumi.String("AdminPassword123!"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleAccount, err := storage.NewAccount(ctx, "exampleAccount", &storage.AccountArgs{
// 			ResourceGroupName:      exampleResourceGroup.Name,
// 			Location:               exampleResourceGroup.Location,
// 			AccountTier:            pulumi.String("Standard"),
// 			AccountReplicationType: pulumi.String("LRS"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = mssql.NewServerExtendedAuditingPolicy(ctx, "exampleServerExtendedAuditingPolicy", &mssql.ServerExtendedAuditingPolicyArgs{
// 			ServerId:                           exampleServer.ID(),
// 			StorageEndpoint:                    exampleAccount.PrimaryBlobEndpoint,
// 			StorageAccountAccessKey:            exampleAccount.PrimaryAccessKey,
// 			StorageAccountAccessKeyIsSecondary: pulumi.Bool(false),
// 			RetentionInDays:                    pulumi.Int(6),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type ServerExtendedAuditingPolicy struct {
	pulumi.CustomResourceState

	// The number of days to retain logs for in the storage account.
	RetentionInDays pulumi.IntPtrOutput `pulumi:"retentionInDays"`
	// The ID of the sql server to set the extended auditing policy. Changing this forces a new resource to be created.
	ServerId pulumi.StringOutput `pulumi:"serverId"`
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey pulumi.StringPtrOutput `pulumi:"storageAccountAccessKey"`
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary pulumi.BoolPtrOutput `pulumi:"storageAccountAccessKeyIsSecondary"`
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint pulumi.StringOutput `pulumi:"storageEndpoint"`
}

// NewServerExtendedAuditingPolicy registers a new resource with the given unique name, arguments, and options.
func NewServerExtendedAuditingPolicy(ctx *pulumi.Context,
	name string, args *ServerExtendedAuditingPolicyArgs, opts ...pulumi.ResourceOption) (*ServerExtendedAuditingPolicy, error) {
	if args == nil || args.ServerId == nil {
		return nil, errors.New("missing required argument 'ServerId'")
	}
	if args == nil || args.StorageEndpoint == nil {
		return nil, errors.New("missing required argument 'StorageEndpoint'")
	}
	if args == nil {
		args = &ServerExtendedAuditingPolicyArgs{}
	}
	var resource ServerExtendedAuditingPolicy
	err := ctx.RegisterResource("azure:mssql/serverExtendedAuditingPolicy:ServerExtendedAuditingPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServerExtendedAuditingPolicy gets an existing ServerExtendedAuditingPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServerExtendedAuditingPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServerExtendedAuditingPolicyState, opts ...pulumi.ResourceOption) (*ServerExtendedAuditingPolicy, error) {
	var resource ServerExtendedAuditingPolicy
	err := ctx.ReadResource("azure:mssql/serverExtendedAuditingPolicy:ServerExtendedAuditingPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServerExtendedAuditingPolicy resources.
type serverExtendedAuditingPolicyState struct {
	// The number of days to retain logs for in the storage account.
	RetentionInDays *int `pulumi:"retentionInDays"`
	// The ID of the sql server to set the extended auditing policy. Changing this forces a new resource to be created.
	ServerId *string `pulumi:"serverId"`
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey *string `pulumi:"storageAccountAccessKey"`
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary *bool `pulumi:"storageAccountAccessKeyIsSecondary"`
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint *string `pulumi:"storageEndpoint"`
}

type ServerExtendedAuditingPolicyState struct {
	// The number of days to retain logs for in the storage account.
	RetentionInDays pulumi.IntPtrInput
	// The ID of the sql server to set the extended auditing policy. Changing this forces a new resource to be created.
	ServerId pulumi.StringPtrInput
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey pulumi.StringPtrInput
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary pulumi.BoolPtrInput
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint pulumi.StringPtrInput
}

func (ServerExtendedAuditingPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*serverExtendedAuditingPolicyState)(nil)).Elem()
}

type serverExtendedAuditingPolicyArgs struct {
	// The number of days to retain logs for in the storage account.
	RetentionInDays *int `pulumi:"retentionInDays"`
	// The ID of the sql server to set the extended auditing policy. Changing this forces a new resource to be created.
	ServerId string `pulumi:"serverId"`
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey *string `pulumi:"storageAccountAccessKey"`
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary *bool `pulumi:"storageAccountAccessKeyIsSecondary"`
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint string `pulumi:"storageEndpoint"`
}

// The set of arguments for constructing a ServerExtendedAuditingPolicy resource.
type ServerExtendedAuditingPolicyArgs struct {
	// The number of days to retain logs for in the storage account.
	RetentionInDays pulumi.IntPtrInput
	// The ID of the sql server to set the extended auditing policy. Changing this forces a new resource to be created.
	ServerId pulumi.StringInput
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey pulumi.StringPtrInput
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary pulumi.BoolPtrInput
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint pulumi.StringInput
}

func (ServerExtendedAuditingPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serverExtendedAuditingPolicyArgs)(nil)).Elem()
}
