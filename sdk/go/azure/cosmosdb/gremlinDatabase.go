// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cosmosdb

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Gremlin Database within a Cosmos DB Account.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/cosmosdb"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleAccount, err := cosmosdb.LookupAccount(ctx, &cosmosdb.LookupAccountArgs{
// 			Name:              "tfex-cosmosdb-account",
// 			ResourceGroupName: "tfex-cosmosdb-account-rg",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = cosmosdb.NewGremlinDatabase(ctx, "exampleGremlinDatabase", &cosmosdb.GremlinDatabaseArgs{
// 			ResourceGroupName: pulumi.String(exampleAccount.ResourceGroupName),
// 			AccountName:       pulumi.String(exampleAccount.Name),
// 			Throughput:        pulumi.Int(400),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type GremlinDatabase struct {
	pulumi.CustomResourceState

	// The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.
	AccountName       pulumi.StringOutput                       `pulumi:"accountName"`
	AutoscaleSettings GremlinDatabaseAutoscaleSettingsPtrOutput `pulumi:"autoscaleSettings"`
	// Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
	Throughput pulumi.IntOutput `pulumi:"throughput"`
}

// NewGremlinDatabase registers a new resource with the given unique name, arguments, and options.
func NewGremlinDatabase(ctx *pulumi.Context,
	name string, args *GremlinDatabaseArgs, opts ...pulumi.ResourceOption) (*GremlinDatabase, error) {
	if args == nil || args.AccountName == nil {
		return nil, errors.New("missing required argument 'AccountName'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil {
		args = &GremlinDatabaseArgs{}
	}
	var resource GremlinDatabase
	err := ctx.RegisterResource("azure:cosmosdb/gremlinDatabase:GremlinDatabase", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGremlinDatabase gets an existing GremlinDatabase resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGremlinDatabase(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GremlinDatabaseState, opts ...pulumi.ResourceOption) (*GremlinDatabase, error) {
	var resource GremlinDatabase
	err := ctx.ReadResource("azure:cosmosdb/gremlinDatabase:GremlinDatabase", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GremlinDatabase resources.
type gremlinDatabaseState struct {
	// The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.
	AccountName       *string                           `pulumi:"accountName"`
	AutoscaleSettings *GremlinDatabaseAutoscaleSettings `pulumi:"autoscaleSettings"`
	// Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
	Throughput *int `pulumi:"throughput"`
}

type GremlinDatabaseState struct {
	// The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.
	AccountName       pulumi.StringPtrInput
	AutoscaleSettings GremlinDatabaseAutoscaleSettingsPtrInput
	// Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringPtrInput
	// The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
	Throughput pulumi.IntPtrInput
}

func (GremlinDatabaseState) ElementType() reflect.Type {
	return reflect.TypeOf((*gremlinDatabaseState)(nil)).Elem()
}

type gremlinDatabaseArgs struct {
	// The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.
	AccountName       string                            `pulumi:"accountName"`
	AutoscaleSettings *GremlinDatabaseAutoscaleSettings `pulumi:"autoscaleSettings"`
	// Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
	Throughput *int `pulumi:"throughput"`
}

// The set of arguments for constructing a GremlinDatabase resource.
type GremlinDatabaseArgs struct {
	// The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.
	AccountName       pulumi.StringInput
	AutoscaleSettings GremlinDatabaseAutoscaleSettingsPtrInput
	// Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringInput
	// The throughput of the Gremlin database (RU/s). Must be set in increments of `100`. The minimum value is `400`. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.
	Throughput pulumi.IntPtrInput
}

func (GremlinDatabaseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gremlinDatabaseArgs)(nil)).Elem()
}
