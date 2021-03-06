// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datashare

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Data Share Data Lake Gen2 Dataset.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/authorization"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/datashare"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/storage"
// 	"github.com/pulumi/pulumi-azuread/sdk/v2/go/azuread"
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
// 		exampleAccount, err := datashare.NewAccount(ctx, "exampleAccount", &datashare.AccountArgs{
// 			Location:          exampleResourceGroup.Location,
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			Identity: &datashare.AccountIdentityArgs{
// 				Type: pulumi.String("SystemAssigned"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleShare, err := datashare.NewShare(ctx, "exampleShare", &datashare.ShareArgs{
// 			AccountId: exampleAccount.ID(),
// 			Kind:      pulumi.String("CopyBased"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = storage.NewAccount(ctx, "exampleStorage_accountAccount", &storage.AccountArgs{
// 			ResourceGroupName:      exampleResourceGroup.Name,
// 			Location:               exampleResourceGroup.Location,
// 			AccountKind:            pulumi.String("BlobStorage"),
// 			AccountTier:            pulumi.String("Standard"),
// 			AccountReplicationType: pulumi.String("LRS"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleDataLakeGen2Filesystem, err := storage.NewDataLakeGen2Filesystem(ctx, "exampleDataLakeGen2Filesystem", &storage.DataLakeGen2FilesystemArgs{
// 			StorageAccountId: pulumi.String(exampleStorage / accountAccount.Id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleAssignment, err := authorization.NewAssignment(ctx, "exampleAssignment", &authorization.AssignmentArgs{
// 			Scope:              pulumi.String(exampleStorage / accountAccount.Id),
// 			RoleDefinitionName: pulumi.String("Storage Blob Data Reader"),
// 			PrincipalId: exampleServicePrincipal.ApplyT(func(exampleServicePrincipal azuread.LookupServicePrincipalResult) (string, error) {
// 				return exampleServicePrincipal.ObjectId, nil
// 			}).(pulumi.StringOutput),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = datashare.NewDatasetDataLakeGen2(ctx, "exampleDatasetDataLakeGen2", &datashare.DatasetDataLakeGen2Args{
// 			ShareId:          exampleShare.ID(),
// 			StorageAccountId: pulumi.String(exampleStorage / accountAccount.Id),
// 			FileSystemName:   exampleDataLakeGen2Filesystem.Name,
// 			FilePath:         pulumi.String("myfile.txt"),
// 		}, pulumi.DependsOn([]pulumi.Resource{
// 			exampleAssignment,
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type DatasetDataLakeGen2 struct {
	pulumi.CustomResourceState

	// The name of the Data Share Dataset.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// The path of the file in the data lake file system to be shared with the receiver. Conflicts with `folderPath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FilePath pulumi.StringPtrOutput `pulumi:"filePath"`
	// The name of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FileSystemName pulumi.StringOutput `pulumi:"fileSystemName"`
	// The folder path in the data lake file system to be shared with the receiver. Conflicts with `filePath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FolderPath pulumi.StringPtrOutput `pulumi:"folderPath"`
	// The name which should be used for this Data Share Data Lake Gen2 Dataset. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The resource ID of the Data Share where this Data Share Data Lake Gen2 Dataset should be created. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	ShareId pulumi.StringOutput `pulumi:"shareId"`
	// The resource id of the storage account of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	StorageAccountId pulumi.StringOutput `pulumi:"storageAccountId"`
}

// NewDatasetDataLakeGen2 registers a new resource with the given unique name, arguments, and options.
func NewDatasetDataLakeGen2(ctx *pulumi.Context,
	name string, args *DatasetDataLakeGen2Args, opts ...pulumi.ResourceOption) (*DatasetDataLakeGen2, error) {
	if args == nil || args.FileSystemName == nil {
		return nil, errors.New("missing required argument 'FileSystemName'")
	}
	if args == nil || args.ShareId == nil {
		return nil, errors.New("missing required argument 'ShareId'")
	}
	if args == nil || args.StorageAccountId == nil {
		return nil, errors.New("missing required argument 'StorageAccountId'")
	}
	if args == nil {
		args = &DatasetDataLakeGen2Args{}
	}
	var resource DatasetDataLakeGen2
	err := ctx.RegisterResource("azure:datashare/datasetDataLakeGen2:DatasetDataLakeGen2", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatasetDataLakeGen2 gets an existing DatasetDataLakeGen2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatasetDataLakeGen2(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatasetDataLakeGen2State, opts ...pulumi.ResourceOption) (*DatasetDataLakeGen2, error) {
	var resource DatasetDataLakeGen2
	err := ctx.ReadResource("azure:datashare/datasetDataLakeGen2:DatasetDataLakeGen2", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DatasetDataLakeGen2 resources.
type datasetDataLakeGen2State struct {
	// The name of the Data Share Dataset.
	DisplayName *string `pulumi:"displayName"`
	// The path of the file in the data lake file system to be shared with the receiver. Conflicts with `folderPath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FilePath *string `pulumi:"filePath"`
	// The name of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FileSystemName *string `pulumi:"fileSystemName"`
	// The folder path in the data lake file system to be shared with the receiver. Conflicts with `filePath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FolderPath *string `pulumi:"folderPath"`
	// The name which should be used for this Data Share Data Lake Gen2 Dataset. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	Name *string `pulumi:"name"`
	// The resource ID of the Data Share where this Data Share Data Lake Gen2 Dataset should be created. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	ShareId *string `pulumi:"shareId"`
	// The resource id of the storage account of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	StorageAccountId *string `pulumi:"storageAccountId"`
}

type DatasetDataLakeGen2State struct {
	// The name of the Data Share Dataset.
	DisplayName pulumi.StringPtrInput
	// The path of the file in the data lake file system to be shared with the receiver. Conflicts with `folderPath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FilePath pulumi.StringPtrInput
	// The name of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FileSystemName pulumi.StringPtrInput
	// The folder path in the data lake file system to be shared with the receiver. Conflicts with `filePath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FolderPath pulumi.StringPtrInput
	// The name which should be used for this Data Share Data Lake Gen2 Dataset. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	Name pulumi.StringPtrInput
	// The resource ID of the Data Share where this Data Share Data Lake Gen2 Dataset should be created. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	ShareId pulumi.StringPtrInput
	// The resource id of the storage account of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	StorageAccountId pulumi.StringPtrInput
}

func (DatasetDataLakeGen2State) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetDataLakeGen2State)(nil)).Elem()
}

type datasetDataLakeGen2Args struct {
	// The path of the file in the data lake file system to be shared with the receiver. Conflicts with `folderPath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FilePath *string `pulumi:"filePath"`
	// The name of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FileSystemName string `pulumi:"fileSystemName"`
	// The folder path in the data lake file system to be shared with the receiver. Conflicts with `filePath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FolderPath *string `pulumi:"folderPath"`
	// The name which should be used for this Data Share Data Lake Gen2 Dataset. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	Name *string `pulumi:"name"`
	// The resource ID of the Data Share where this Data Share Data Lake Gen2 Dataset should be created. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	ShareId string `pulumi:"shareId"`
	// The resource id of the storage account of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	StorageAccountId string `pulumi:"storageAccountId"`
}

// The set of arguments for constructing a DatasetDataLakeGen2 resource.
type DatasetDataLakeGen2Args struct {
	// The path of the file in the data lake file system to be shared with the receiver. Conflicts with `folderPath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FilePath pulumi.StringPtrInput
	// The name of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FileSystemName pulumi.StringInput
	// The folder path in the data lake file system to be shared with the receiver. Conflicts with `filePath` Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	FolderPath pulumi.StringPtrInput
	// The name which should be used for this Data Share Data Lake Gen2 Dataset. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	Name pulumi.StringPtrInput
	// The resource ID of the Data Share where this Data Share Data Lake Gen2 Dataset should be created. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	ShareId pulumi.StringInput
	// The resource id of the storage account of the data lake file system to be shared with the receiver. Changing this forces a new Data Share Data Lake Gen2 Dataset to be created.
	StorageAccountId pulumi.StringInput
}

func (DatasetDataLakeGen2Args) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetDataLakeGen2Args)(nil)).Elem()
}
