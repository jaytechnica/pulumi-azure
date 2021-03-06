// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mssql

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Ms Sql Database Extended Auditing Policy.
//
// > **NOTE:** The Database Extended Auditing Policy Can be set inline here as well as with the mssqlDatabaseExtendedAuditingPolicy resource resource. You can only use one or the other and using both will cause a conflict.
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
// 		exampleDatabase, err := mssql.NewDatabase(ctx, "exampleDatabase", &mssql.DatabaseArgs{
// 			ServerId: exampleServer.ID(),
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
// 		_, err = mssql.NewDatabaseExtendedAuditingPolicy(ctx, "exampleDatabaseExtendedAuditingPolicy", &mssql.DatabaseExtendedAuditingPolicyArgs{
// 			DatabaseId:                         exampleDatabase.ID(),
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
type DatabaseExtendedAuditingPolicy struct {
	pulumi.CustomResourceState

	// The ID of the sql database to set the extended auditing policy. Changing this forces a new resource to be created.
	DatabaseId pulumi.StringOutput `pulumi:"databaseId"`
	// The number of days to retain logs for in the storage account.
	RetentionInDays pulumi.IntPtrOutput `pulumi:"retentionInDays"`
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey pulumi.StringPtrOutput `pulumi:"storageAccountAccessKey"`
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary pulumi.BoolPtrOutput `pulumi:"storageAccountAccessKeyIsSecondary"`
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint pulumi.StringOutput `pulumi:"storageEndpoint"`
}

// NewDatabaseExtendedAuditingPolicy registers a new resource with the given unique name, arguments, and options.
func NewDatabaseExtendedAuditingPolicy(ctx *pulumi.Context,
	name string, args *DatabaseExtendedAuditingPolicyArgs, opts ...pulumi.ResourceOption) (*DatabaseExtendedAuditingPolicy, error) {
	if args == nil || args.DatabaseId == nil {
		return nil, errors.New("missing required argument 'DatabaseId'")
	}
	if args == nil || args.StorageEndpoint == nil {
		return nil, errors.New("missing required argument 'StorageEndpoint'")
	}
	if args == nil {
		args = &DatabaseExtendedAuditingPolicyArgs{}
	}
	var resource DatabaseExtendedAuditingPolicy
	err := ctx.RegisterResource("azure:mssql/databaseExtendedAuditingPolicy:DatabaseExtendedAuditingPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatabaseExtendedAuditingPolicy gets an existing DatabaseExtendedAuditingPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabaseExtendedAuditingPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatabaseExtendedAuditingPolicyState, opts ...pulumi.ResourceOption) (*DatabaseExtendedAuditingPolicy, error) {
	var resource DatabaseExtendedAuditingPolicy
	err := ctx.ReadResource("azure:mssql/databaseExtendedAuditingPolicy:DatabaseExtendedAuditingPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DatabaseExtendedAuditingPolicy resources.
type databaseExtendedAuditingPolicyState struct {
	// The ID of the sql database to set the extended auditing policy. Changing this forces a new resource to be created.
	DatabaseId *string `pulumi:"databaseId"`
	// The number of days to retain logs for in the storage account.
	RetentionInDays *int `pulumi:"retentionInDays"`
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey *string `pulumi:"storageAccountAccessKey"`
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary *bool `pulumi:"storageAccountAccessKeyIsSecondary"`
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint *string `pulumi:"storageEndpoint"`
}

type DatabaseExtendedAuditingPolicyState struct {
	// The ID of the sql database to set the extended auditing policy. Changing this forces a new resource to be created.
	DatabaseId pulumi.StringPtrInput
	// The number of days to retain logs for in the storage account.
	RetentionInDays pulumi.IntPtrInput
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey pulumi.StringPtrInput
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary pulumi.BoolPtrInput
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint pulumi.StringPtrInput
}

func (DatabaseExtendedAuditingPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseExtendedAuditingPolicyState)(nil)).Elem()
}

type databaseExtendedAuditingPolicyArgs struct {
	// The ID of the sql database to set the extended auditing policy. Changing this forces a new resource to be created.
	DatabaseId string `pulumi:"databaseId"`
	// The number of days to retain logs for in the storage account.
	RetentionInDays *int `pulumi:"retentionInDays"`
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey *string `pulumi:"storageAccountAccessKey"`
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary *bool `pulumi:"storageAccountAccessKeyIsSecondary"`
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint string `pulumi:"storageEndpoint"`
}

// The set of arguments for constructing a DatabaseExtendedAuditingPolicy resource.
type DatabaseExtendedAuditingPolicyArgs struct {
	// The ID of the sql database to set the extended auditing policy. Changing this forces a new resource to be created.
	DatabaseId pulumi.StringInput
	// The number of days to retain logs for in the storage account.
	RetentionInDays pulumi.IntPtrInput
	// The access key to use for the auditing storage account.
	StorageAccountAccessKey pulumi.StringPtrInput
	// Is `storageAccountAccessKey` value the storage's secondary key?
	StorageAccountAccessKeyIsSecondary pulumi.BoolPtrInput
	// The blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all extended auditing logs.
	StorageEndpoint pulumi.StringInput
}

func (DatabaseExtendedAuditingPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseExtendedAuditingPolicyArgs)(nil)).Elem()
}
