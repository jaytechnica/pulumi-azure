// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datashare

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Data Share Kusto Cluster Dataset.
type DatasetKustoCluster struct {
	pulumi.CustomResourceState

	// The name of the Data Share Dataset.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	KustoClusterId pulumi.StringOutput `pulumi:"kustoClusterId"`
	// The location of the Kusto Cluster.
	KustoClusterLocation pulumi.StringOutput `pulumi:"kustoClusterLocation"`
	// The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	ShareId pulumi.StringOutput `pulumi:"shareId"`
}

// NewDatasetKustoCluster registers a new resource with the given unique name, arguments, and options.
func NewDatasetKustoCluster(ctx *pulumi.Context,
	name string, args *DatasetKustoClusterArgs, opts ...pulumi.ResourceOption) (*DatasetKustoCluster, error) {
	if args == nil || args.KustoClusterId == nil {
		return nil, errors.New("missing required argument 'KustoClusterId'")
	}
	if args == nil || args.ShareId == nil {
		return nil, errors.New("missing required argument 'ShareId'")
	}
	if args == nil {
		args = &DatasetKustoClusterArgs{}
	}
	var resource DatasetKustoCluster
	err := ctx.RegisterResource("azure:datashare/datasetKustoCluster:DatasetKustoCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatasetKustoCluster gets an existing DatasetKustoCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatasetKustoCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatasetKustoClusterState, opts ...pulumi.ResourceOption) (*DatasetKustoCluster, error) {
	var resource DatasetKustoCluster
	err := ctx.ReadResource("azure:datashare/datasetKustoCluster:DatasetKustoCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DatasetKustoCluster resources.
type datasetKustoClusterState struct {
	// The name of the Data Share Dataset.
	DisplayName *string `pulumi:"displayName"`
	// The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	KustoClusterId *string `pulumi:"kustoClusterId"`
	// The location of the Kusto Cluster.
	KustoClusterLocation *string `pulumi:"kustoClusterLocation"`
	// The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	Name *string `pulumi:"name"`
	// The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	ShareId *string `pulumi:"shareId"`
}

type DatasetKustoClusterState struct {
	// The name of the Data Share Dataset.
	DisplayName pulumi.StringPtrInput
	// The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	KustoClusterId pulumi.StringPtrInput
	// The location of the Kusto Cluster.
	KustoClusterLocation pulumi.StringPtrInput
	// The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	Name pulumi.StringPtrInput
	// The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	ShareId pulumi.StringPtrInput
}

func (DatasetKustoClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetKustoClusterState)(nil)).Elem()
}

type datasetKustoClusterArgs struct {
	// The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	KustoClusterId string `pulumi:"kustoClusterId"`
	// The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	Name *string `pulumi:"name"`
	// The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	ShareId string `pulumi:"shareId"`
}

// The set of arguments for constructing a DatasetKustoCluster resource.
type DatasetKustoClusterArgs struct {
	// The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	KustoClusterId pulumi.StringInput
	// The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	Name pulumi.StringPtrInput
	// The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
	ShareId pulumi.StringInput
}

func (DatasetKustoClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*datasetKustoClusterArgs)(nil)).Elem()
}