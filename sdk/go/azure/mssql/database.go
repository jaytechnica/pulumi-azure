// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mssql

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a MS SQL Database.
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
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/sql"
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
// 		exampleAccount, err := storage.NewAccount(ctx, "exampleAccount", &storage.AccountArgs{
// 			ResourceGroupName:      exampleResourceGroup.Name,
// 			Location:               exampleResourceGroup.Location,
// 			AccountTier:            pulumi.String("Standard"),
// 			AccountReplicationType: pulumi.String("LRS"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleSqlServer, err := sql.NewSqlServer(ctx, "exampleSqlServer", &sql.SqlServerArgs{
// 			ResourceGroupName:          exampleResourceGroup.Name,
// 			Location:                   exampleResourceGroup.Location,
// 			Version:                    pulumi.String("12.0"),
// 			AdministratorLogin:         pulumi.String("4dm1n157r470r"),
// 			AdministratorLoginPassword: pulumi.String("4-v3ry-53cr37-p455w0rd"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = mssql.NewDatabase(ctx, "test", &mssql.DatabaseArgs{
// 			ServerId:      exampleSqlServer.ID(),
// 			Collation:     pulumi.String("SQL_Latin1_General_CP1_CI_AS"),
// 			LicenseType:   pulumi.String("LicenseIncluded"),
// 			MaxSizeGb:     pulumi.Int(4),
// 			ReadScale:     pulumi.Bool(true),
// 			SkuName:       pulumi.String("BC_Gen5_2"),
// 			ZoneRedundant: pulumi.Bool(true),
// 			ExtendedAuditingPolicy: &mssql.DatabaseExtendedAuditingPolicyArgs{
// 				StorageEndpoint:                    exampleAccount.PrimaryBlobEndpoint,
// 				StorageAccountAccessKey:            exampleAccount.PrimaryAccessKey,
// 				StorageAccountAccessKeyIsSecondary: pulumi.Bool(true),
// 				RetentionInDays:                    pulumi.Int(6),
// 			},
// 			Tags: pulumi.StringMap{
// 				"foo": pulumi.String("bar"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Database struct {
	pulumi.CustomResourceState

	// Time in minutes after which database is automatically paused. A value of `-1` means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.
	AutoPauseDelayInMinutes pulumi.IntOutput `pulumi:"autoPauseDelayInMinutes"`
	// Specifies the collation of the database. Changing this forces a new resource to be created.
	Collation pulumi.StringOutput `pulumi:"collation"`
	// The create mode of the database. Possible values are `Copy`, `Default`, `OnlineSecondary`, `PointInTimeRestore`, `Restore`, `RestoreExternalBackup`, `RestoreExternalBackupSecondary`, `RestoreLongTermRetentionBackup` and `Secondary`.
	CreateMode pulumi.StringOutput `pulumi:"createMode"`
	// The id of the source database to be referred to create the new database. This should only be used for databases with `createMode` values that use another database as reference. Changing this forces a new resource to be created.
	CreationSourceDatabaseId pulumi.StringOutput `pulumi:"creationSourceDatabaseId"`
	// Specifies the ID of the elastic pool containing this database.
	ElasticPoolId pulumi.StringPtrOutput `pulumi:"elasticPoolId"`
	// A `extendedAuditingPolicy` block as defined below.
	//
	// Deprecated: the `extended_auditing_policy` block has been moved to `azurerm_mssql_server_extended_auditing_policy` and `azurerm_mssql_database_extended_auditing_policy`. This block will be removed in version 3.0 of the provider.
	ExtendedAuditingPolicy DatabaseExtendedAuditingPolicyTypeOutput `pulumi:"extendedAuditingPolicy"`
	// Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
	LicenseType pulumi.StringOutput `pulumi:"licenseType"`
	// The max size of the database in gigabytes.
	MaxSizeGb pulumi.IntOutput `pulumi:"maxSizeGb"`
	// Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.
	MinCapacity pulumi.Float64Output `pulumi:"minCapacity"`
	// The name of the Ms SQL Database. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.
	ReadReplicaCount pulumi.IntOutput `pulumi:"readReplicaCount"`
	// If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
	ReadScale pulumi.BoolOutput `pulumi:"readScale"`
	// Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for `createMode`= `PointInTimeRestore`  databases.
	RestorePointInTime pulumi.StringOutput `pulumi:"restorePointInTime"`
	// Specifies the name of the sample schema to apply when creating this database. Possible value is `AdventureWorksLT`.
	SampleName pulumi.StringOutput `pulumi:"sampleName"`
	// The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.
	ServerId pulumi.StringOutput `pulumi:"serverId"`
	// Specifies the name of the sku used by the database. Only changing this from tier `Hyperscale` to another tier will force a new resource to be created. For example, `GP_S_Gen5_2`,`HS_Gen4_1`,`BC_Gen5_2`, `ElasticPool`, `Basic`,`S0`, `P2` ,`DW100c`, `DS100`.
	SkuName pulumi.StringOutput `pulumi:"skuName"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// Threat detection policy configuration. The `threatDetectionPolicy` block supports fields documented below.
	ThreatDetectionPolicy DatabaseThreatDetectionPolicyOutput `pulumi:"threatDetectionPolicy"`
	// Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.
	ZoneRedundant pulumi.BoolOutput `pulumi:"zoneRedundant"`
}

// NewDatabase registers a new resource with the given unique name, arguments, and options.
func NewDatabase(ctx *pulumi.Context,
	name string, args *DatabaseArgs, opts ...pulumi.ResourceOption) (*Database, error) {
	if args == nil || args.ServerId == nil {
		return nil, errors.New("missing required argument 'ServerId'")
	}
	if args == nil {
		args = &DatabaseArgs{}
	}
	var resource Database
	err := ctx.RegisterResource("azure:mssql/database:Database", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatabase gets an existing Database resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabase(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatabaseState, opts ...pulumi.ResourceOption) (*Database, error) {
	var resource Database
	err := ctx.ReadResource("azure:mssql/database:Database", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Database resources.
type databaseState struct {
	// Time in minutes after which database is automatically paused. A value of `-1` means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.
	AutoPauseDelayInMinutes *int `pulumi:"autoPauseDelayInMinutes"`
	// Specifies the collation of the database. Changing this forces a new resource to be created.
	Collation *string `pulumi:"collation"`
	// The create mode of the database. Possible values are `Copy`, `Default`, `OnlineSecondary`, `PointInTimeRestore`, `Restore`, `RestoreExternalBackup`, `RestoreExternalBackupSecondary`, `RestoreLongTermRetentionBackup` and `Secondary`.
	CreateMode *string `pulumi:"createMode"`
	// The id of the source database to be referred to create the new database. This should only be used for databases with `createMode` values that use another database as reference. Changing this forces a new resource to be created.
	CreationSourceDatabaseId *string `pulumi:"creationSourceDatabaseId"`
	// Specifies the ID of the elastic pool containing this database.
	ElasticPoolId *string `pulumi:"elasticPoolId"`
	// A `extendedAuditingPolicy` block as defined below.
	//
	// Deprecated: the `extended_auditing_policy` block has been moved to `azurerm_mssql_server_extended_auditing_policy` and `azurerm_mssql_database_extended_auditing_policy`. This block will be removed in version 3.0 of the provider.
	ExtendedAuditingPolicy *DatabaseExtendedAuditingPolicyType `pulumi:"extendedAuditingPolicy"`
	// Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
	LicenseType *string `pulumi:"licenseType"`
	// The max size of the database in gigabytes.
	MaxSizeGb *int `pulumi:"maxSizeGb"`
	// Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.
	MinCapacity *float64 `pulumi:"minCapacity"`
	// The name of the Ms SQL Database. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.
	ReadReplicaCount *int `pulumi:"readReplicaCount"`
	// If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
	ReadScale *bool `pulumi:"readScale"`
	// Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for `createMode`= `PointInTimeRestore`  databases.
	RestorePointInTime *string `pulumi:"restorePointInTime"`
	// Specifies the name of the sample schema to apply when creating this database. Possible value is `AdventureWorksLT`.
	SampleName *string `pulumi:"sampleName"`
	// The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.
	ServerId *string `pulumi:"serverId"`
	// Specifies the name of the sku used by the database. Only changing this from tier `Hyperscale` to another tier will force a new resource to be created. For example, `GP_S_Gen5_2`,`HS_Gen4_1`,`BC_Gen5_2`, `ElasticPool`, `Basic`,`S0`, `P2` ,`DW100c`, `DS100`.
	SkuName *string `pulumi:"skuName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// Threat detection policy configuration. The `threatDetectionPolicy` block supports fields documented below.
	ThreatDetectionPolicy *DatabaseThreatDetectionPolicy `pulumi:"threatDetectionPolicy"`
	// Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.
	ZoneRedundant *bool `pulumi:"zoneRedundant"`
}

type DatabaseState struct {
	// Time in minutes after which database is automatically paused. A value of `-1` means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.
	AutoPauseDelayInMinutes pulumi.IntPtrInput
	// Specifies the collation of the database. Changing this forces a new resource to be created.
	Collation pulumi.StringPtrInput
	// The create mode of the database. Possible values are `Copy`, `Default`, `OnlineSecondary`, `PointInTimeRestore`, `Restore`, `RestoreExternalBackup`, `RestoreExternalBackupSecondary`, `RestoreLongTermRetentionBackup` and `Secondary`.
	CreateMode pulumi.StringPtrInput
	// The id of the source database to be referred to create the new database. This should only be used for databases with `createMode` values that use another database as reference. Changing this forces a new resource to be created.
	CreationSourceDatabaseId pulumi.StringPtrInput
	// Specifies the ID of the elastic pool containing this database.
	ElasticPoolId pulumi.StringPtrInput
	// A `extendedAuditingPolicy` block as defined below.
	//
	// Deprecated: the `extended_auditing_policy` block has been moved to `azurerm_mssql_server_extended_auditing_policy` and `azurerm_mssql_database_extended_auditing_policy`. This block will be removed in version 3.0 of the provider.
	ExtendedAuditingPolicy DatabaseExtendedAuditingPolicyTypePtrInput
	// Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
	LicenseType pulumi.StringPtrInput
	// The max size of the database in gigabytes.
	MaxSizeGb pulumi.IntPtrInput
	// Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.
	MinCapacity pulumi.Float64PtrInput
	// The name of the Ms SQL Database. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.
	ReadReplicaCount pulumi.IntPtrInput
	// If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
	ReadScale pulumi.BoolPtrInput
	// Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for `createMode`= `PointInTimeRestore`  databases.
	RestorePointInTime pulumi.StringPtrInput
	// Specifies the name of the sample schema to apply when creating this database. Possible value is `AdventureWorksLT`.
	SampleName pulumi.StringPtrInput
	// The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.
	ServerId pulumi.StringPtrInput
	// Specifies the name of the sku used by the database. Only changing this from tier `Hyperscale` to another tier will force a new resource to be created. For example, `GP_S_Gen5_2`,`HS_Gen4_1`,`BC_Gen5_2`, `ElasticPool`, `Basic`,`S0`, `P2` ,`DW100c`, `DS100`.
	SkuName pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// Threat detection policy configuration. The `threatDetectionPolicy` block supports fields documented below.
	ThreatDetectionPolicy DatabaseThreatDetectionPolicyPtrInput
	// Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.
	ZoneRedundant pulumi.BoolPtrInput
}

func (DatabaseState) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseState)(nil)).Elem()
}

type databaseArgs struct {
	// Time in minutes after which database is automatically paused. A value of `-1` means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.
	AutoPauseDelayInMinutes *int `pulumi:"autoPauseDelayInMinutes"`
	// Specifies the collation of the database. Changing this forces a new resource to be created.
	Collation *string `pulumi:"collation"`
	// The create mode of the database. Possible values are `Copy`, `Default`, `OnlineSecondary`, `PointInTimeRestore`, `Restore`, `RestoreExternalBackup`, `RestoreExternalBackupSecondary`, `RestoreLongTermRetentionBackup` and `Secondary`.
	CreateMode *string `pulumi:"createMode"`
	// The id of the source database to be referred to create the new database. This should only be used for databases with `createMode` values that use another database as reference. Changing this forces a new resource to be created.
	CreationSourceDatabaseId *string `pulumi:"creationSourceDatabaseId"`
	// Specifies the ID of the elastic pool containing this database.
	ElasticPoolId *string `pulumi:"elasticPoolId"`
	// A `extendedAuditingPolicy` block as defined below.
	//
	// Deprecated: the `extended_auditing_policy` block has been moved to `azurerm_mssql_server_extended_auditing_policy` and `azurerm_mssql_database_extended_auditing_policy`. This block will be removed in version 3.0 of the provider.
	ExtendedAuditingPolicy *DatabaseExtendedAuditingPolicyType `pulumi:"extendedAuditingPolicy"`
	// Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
	LicenseType *string `pulumi:"licenseType"`
	// The max size of the database in gigabytes.
	MaxSizeGb *int `pulumi:"maxSizeGb"`
	// Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.
	MinCapacity *float64 `pulumi:"minCapacity"`
	// The name of the Ms SQL Database. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.
	ReadReplicaCount *int `pulumi:"readReplicaCount"`
	// If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
	ReadScale *bool `pulumi:"readScale"`
	// Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for `createMode`= `PointInTimeRestore`  databases.
	RestorePointInTime *string `pulumi:"restorePointInTime"`
	// Specifies the name of the sample schema to apply when creating this database. Possible value is `AdventureWorksLT`.
	SampleName *string `pulumi:"sampleName"`
	// The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.
	ServerId string `pulumi:"serverId"`
	// Specifies the name of the sku used by the database. Only changing this from tier `Hyperscale` to another tier will force a new resource to be created. For example, `GP_S_Gen5_2`,`HS_Gen4_1`,`BC_Gen5_2`, `ElasticPool`, `Basic`,`S0`, `P2` ,`DW100c`, `DS100`.
	SkuName *string `pulumi:"skuName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// Threat detection policy configuration. The `threatDetectionPolicy` block supports fields documented below.
	ThreatDetectionPolicy *DatabaseThreatDetectionPolicy `pulumi:"threatDetectionPolicy"`
	// Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.
	ZoneRedundant *bool `pulumi:"zoneRedundant"`
}

// The set of arguments for constructing a Database resource.
type DatabaseArgs struct {
	// Time in minutes after which database is automatically paused. A value of `-1` means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.
	AutoPauseDelayInMinutes pulumi.IntPtrInput
	// Specifies the collation of the database. Changing this forces a new resource to be created.
	Collation pulumi.StringPtrInput
	// The create mode of the database. Possible values are `Copy`, `Default`, `OnlineSecondary`, `PointInTimeRestore`, `Restore`, `RestoreExternalBackup`, `RestoreExternalBackupSecondary`, `RestoreLongTermRetentionBackup` and `Secondary`.
	CreateMode pulumi.StringPtrInput
	// The id of the source database to be referred to create the new database. This should only be used for databases with `createMode` values that use another database as reference. Changing this forces a new resource to be created.
	CreationSourceDatabaseId pulumi.StringPtrInput
	// Specifies the ID of the elastic pool containing this database.
	ElasticPoolId pulumi.StringPtrInput
	// A `extendedAuditingPolicy` block as defined below.
	//
	// Deprecated: the `extended_auditing_policy` block has been moved to `azurerm_mssql_server_extended_auditing_policy` and `azurerm_mssql_database_extended_auditing_policy`. This block will be removed in version 3.0 of the provider.
	ExtendedAuditingPolicy DatabaseExtendedAuditingPolicyTypePtrInput
	// Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.
	LicenseType pulumi.StringPtrInput
	// The max size of the database in gigabytes.
	MaxSizeGb pulumi.IntPtrInput
	// Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.
	MinCapacity pulumi.Float64PtrInput
	// The name of the Ms SQL Database. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.
	ReadReplicaCount pulumi.IntPtrInput
	// If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
	ReadScale pulumi.BoolPtrInput
	// Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for `createMode`= `PointInTimeRestore`  databases.
	RestorePointInTime pulumi.StringPtrInput
	// Specifies the name of the sample schema to apply when creating this database. Possible value is `AdventureWorksLT`.
	SampleName pulumi.StringPtrInput
	// The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.
	ServerId pulumi.StringInput
	// Specifies the name of the sku used by the database. Only changing this from tier `Hyperscale` to another tier will force a new resource to be created. For example, `GP_S_Gen5_2`,`HS_Gen4_1`,`BC_Gen5_2`, `ElasticPool`, `Basic`,`S0`, `P2` ,`DW100c`, `DS100`.
	SkuName pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// Threat detection policy configuration. The `threatDetectionPolicy` block supports fields documented below.
	ThreatDetectionPolicy DatabaseThreatDetectionPolicyPtrInput
	// Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.
	ZoneRedundant pulumi.BoolPtrInput
}

func (DatabaseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseArgs)(nil)).Elem()
}
