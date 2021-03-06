// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package notificationhub

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Notification Hub within a Notification Hub Namespace.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/notificationhub"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
// 			Location: pulumi.String("Australia East"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleNamespace, err := notificationhub.NewNamespace(ctx, "exampleNamespace", &notificationhub.NamespaceArgs{
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			Location:          exampleResourceGroup.Location,
// 			NamespaceType:     pulumi.String("NotificationHub"),
// 			SkuName:           pulumi.String("Free"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = notificationhub.NewHub(ctx, "exampleHub", &notificationhub.HubArgs{
// 			NamespaceName:     exampleNamespace.Name,
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			Location:          exampleResourceGroup.Location,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Hub struct {
	pulumi.CustomResourceState

	// A `apnsCredential` block as defined below.
	ApnsCredential HubApnsCredentialPtrOutput `pulumi:"apnsCredential"`
	// A `gcmCredential` block as defined below.
	GcmCredential HubGcmCredentialPtrOutput `pulumi:"gcmCredential"`
	// The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.
	Location pulumi.StringOutput `pulumi:"location"`
	// The name to use for this Notification Hub. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.
	NamespaceName pulumi.StringOutput `pulumi:"namespaceName"`
	// The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewHub registers a new resource with the given unique name, arguments, and options.
func NewHub(ctx *pulumi.Context,
	name string, args *HubArgs, opts ...pulumi.ResourceOption) (*Hub, error) {
	if args == nil || args.NamespaceName == nil {
		return nil, errors.New("missing required argument 'NamespaceName'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil {
		args = &HubArgs{}
	}
	var resource Hub
	err := ctx.RegisterResource("azure:notificationhub/hub:Hub", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHub gets an existing Hub resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHub(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HubState, opts ...pulumi.ResourceOption) (*Hub, error) {
	var resource Hub
	err := ctx.ReadResource("azure:notificationhub/hub:Hub", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Hub resources.
type hubState struct {
	// A `apnsCredential` block as defined below.
	ApnsCredential *HubApnsCredential `pulumi:"apnsCredential"`
	// A `gcmCredential` block as defined below.
	GcmCredential *HubGcmCredential `pulumi:"gcmCredential"`
	// The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// The name to use for this Notification Hub. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.
	NamespaceName *string `pulumi:"namespaceName"`
	// The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

type HubState struct {
	// A `apnsCredential` block as defined below.
	ApnsCredential HubApnsCredentialPtrInput
	// A `gcmCredential` block as defined below.
	GcmCredential HubGcmCredentialPtrInput
	// The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// The name to use for this Notification Hub. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.
	NamespaceName pulumi.StringPtrInput
	// The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (HubState) ElementType() reflect.Type {
	return reflect.TypeOf((*hubState)(nil)).Elem()
}

type hubArgs struct {
	// A `apnsCredential` block as defined below.
	ApnsCredential *HubApnsCredential `pulumi:"apnsCredential"`
	// A `gcmCredential` block as defined below.
	GcmCredential *HubGcmCredential `pulumi:"gcmCredential"`
	// The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// The name to use for this Notification Hub. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.
	NamespaceName string `pulumi:"namespaceName"`
	// The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Hub resource.
type HubArgs struct {
	// A `apnsCredential` block as defined below.
	ApnsCredential HubApnsCredentialPtrInput
	// A `gcmCredential` block as defined below.
	GcmCredential HubGcmCredentialPtrInput
	// The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// The name to use for this Notification Hub. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.
	NamespaceName pulumi.StringInput
	// The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (HubArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hubArgs)(nil)).Elem()
}
