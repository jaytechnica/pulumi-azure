// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hpc

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a NFS Target within a HPC Cache.
//
// > **NOTE:**: By request of the service team the provider no longer automatically registering the `Microsoft.StorageCache` Resource Provider for this resource. To register it you can run `az provider register --namespace 'Microsoft.StorageCache'`.
type CacheNfsTarget struct {
	pulumi.CustomResourceState

	// The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
	CacheName pulumi.StringOutput `pulumi:"cacheName"`
	// The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
	NamespaceJunctions CacheNfsTargetNamespaceJunctionArrayOutput `pulumi:"namespaceJunctions"`
	// The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
	TargetHostName pulumi.StringOutput `pulumi:"targetHostName"`
	// The type of usage of the HPC Cache NFS Target.
	UsageModel pulumi.StringOutput `pulumi:"usageModel"`
}

// NewCacheNfsTarget registers a new resource with the given unique name, arguments, and options.
func NewCacheNfsTarget(ctx *pulumi.Context,
	name string, args *CacheNfsTargetArgs, opts ...pulumi.ResourceOption) (*CacheNfsTarget, error) {
	if args == nil || args.CacheName == nil {
		return nil, errors.New("missing required argument 'CacheName'")
	}
	if args == nil || args.NamespaceJunctions == nil {
		return nil, errors.New("missing required argument 'NamespaceJunctions'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.TargetHostName == nil {
		return nil, errors.New("missing required argument 'TargetHostName'")
	}
	if args == nil || args.UsageModel == nil {
		return nil, errors.New("missing required argument 'UsageModel'")
	}
	if args == nil {
		args = &CacheNfsTargetArgs{}
	}
	var resource CacheNfsTarget
	err := ctx.RegisterResource("azure:hpc/cacheNfsTarget:CacheNfsTarget", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCacheNfsTarget gets an existing CacheNfsTarget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCacheNfsTarget(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CacheNfsTargetState, opts ...pulumi.ResourceOption) (*CacheNfsTarget, error) {
	var resource CacheNfsTarget
	err := ctx.ReadResource("azure:hpc/cacheNfsTarget:CacheNfsTarget", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CacheNfsTarget resources.
type cacheNfsTargetState struct {
	// The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
	CacheName *string `pulumi:"cacheName"`
	// The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
	NamespaceJunctions []CacheNfsTargetNamespaceJunction `pulumi:"namespaceJunctions"`
	// The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
	TargetHostName *string `pulumi:"targetHostName"`
	// The type of usage of the HPC Cache NFS Target.
	UsageModel *string `pulumi:"usageModel"`
}

type CacheNfsTargetState struct {
	// The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
	CacheName pulumi.StringPtrInput
	// The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
	NamespaceJunctions CacheNfsTargetNamespaceJunctionArrayInput
	// The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringPtrInput
	// The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
	TargetHostName pulumi.StringPtrInput
	// The type of usage of the HPC Cache NFS Target.
	UsageModel pulumi.StringPtrInput
}

func (CacheNfsTargetState) ElementType() reflect.Type {
	return reflect.TypeOf((*cacheNfsTargetState)(nil)).Elem()
}

type cacheNfsTargetArgs struct {
	// The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
	CacheName string `pulumi:"cacheName"`
	// The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
	NamespaceJunctions []CacheNfsTargetNamespaceJunction `pulumi:"namespaceJunctions"`
	// The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
	TargetHostName string `pulumi:"targetHostName"`
	// The type of usage of the HPC Cache NFS Target.
	UsageModel string `pulumi:"usageModel"`
}

// The set of arguments for constructing a CacheNfsTarget resource.
type CacheNfsTargetArgs struct {
	// The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
	CacheName pulumi.StringInput
	// The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
	NamespaceJunctions CacheNfsTargetNamespaceJunctionArrayInput
	// The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringInput
	// The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
	TargetHostName pulumi.StringInput
	// The type of usage of the HPC Cache NFS Target.
	UsageModel pulumi.StringInput
}

func (CacheNfsTargetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cacheNfsTargetArgs)(nil)).Elem()
}
