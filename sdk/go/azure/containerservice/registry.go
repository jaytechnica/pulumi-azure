// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package containerservice

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages an Azure Container Registry.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry.html.markdown.
type Registry struct {
	pulumi.CustomResourceState

	// Specifies whether the admin user is enabled. Defaults to `false`.
	AdminEnabled pulumi.BoolPtrOutput `pulumi:"adminEnabled"`
	// The Password associated with the Container Registry Admin account - if the admin account is enabled.
	AdminPassword pulumi.StringOutput `pulumi:"adminPassword"`
	// The Username associated with the Container Registry Admin account - if the admin account is enabled.
	AdminUsername pulumi.StringOutput `pulumi:"adminUsername"`
	// A list of Azure locations where the container registry should be geo-replicated.
	GeoreplicationLocations pulumi.StringArrayOutput `pulumi:"georeplicationLocations"`
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location pulumi.StringOutput `pulumi:"location"`
	// The URL that can be used to log into the container registry.
	LoginServer pulumi.StringOutput `pulumi:"loginServer"`
	// Specifies the name of the Container Registry. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// A `networkRuleSet` block as documented below.
	NetworkRuleSet RegistryNetworkRuleSetOutput `pulumi:"networkRuleSet"`
	// The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// The SKU name of the container registry. Possible values are  `Basic`, `Standard` and `Premium`. `Classic` (which was previously `Basic`) is supported only for existing resources.
	Sku pulumi.StringPtrOutput `pulumi:"sku"`
	// The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.
	StorageAccountId pulumi.StringPtrOutput `pulumi:"storageAccountId"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewRegistry registers a new resource with the given unique name, arguments, and options.
func NewRegistry(ctx *pulumi.Context,
	name string, args *RegistryArgs, opts ...pulumi.ResourceOption) (*Registry, error) {
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil {
		args = &RegistryArgs{}
	}
	var resource Registry
	err := ctx.RegisterResource("azure:containerservice/registry:Registry", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegistry gets an existing Registry resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegistry(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegistryState, opts ...pulumi.ResourceOption) (*Registry, error) {
	var resource Registry
	err := ctx.ReadResource("azure:containerservice/registry:Registry", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Registry resources.
type registryState struct {
	// Specifies whether the admin user is enabled. Defaults to `false`.
	AdminEnabled *bool `pulumi:"adminEnabled"`
	// The Password associated with the Container Registry Admin account - if the admin account is enabled.
	AdminPassword *string `pulumi:"adminPassword"`
	// The Username associated with the Container Registry Admin account - if the admin account is enabled.
	AdminUsername *string `pulumi:"adminUsername"`
	// A list of Azure locations where the container registry should be geo-replicated.
	GeoreplicationLocations []string `pulumi:"georeplicationLocations"`
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// The URL that can be used to log into the container registry.
	LoginServer *string `pulumi:"loginServer"`
	// Specifies the name of the Container Registry. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// A `networkRuleSet` block as documented below.
	NetworkRuleSet *RegistryNetworkRuleSet `pulumi:"networkRuleSet"`
	// The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// The SKU name of the container registry. Possible values are  `Basic`, `Standard` and `Premium`. `Classic` (which was previously `Basic`) is supported only for existing resources.
	Sku *string `pulumi:"sku"`
	// The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.
	StorageAccountId *string `pulumi:"storageAccountId"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

type RegistryState struct {
	// Specifies whether the admin user is enabled. Defaults to `false`.
	AdminEnabled pulumi.BoolPtrInput
	// The Password associated with the Container Registry Admin account - if the admin account is enabled.
	AdminPassword pulumi.StringPtrInput
	// The Username associated with the Container Registry Admin account - if the admin account is enabled.
	AdminUsername pulumi.StringPtrInput
	// A list of Azure locations where the container registry should be geo-replicated.
	GeoreplicationLocations pulumi.StringArrayInput
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// The URL that can be used to log into the container registry.
	LoginServer pulumi.StringPtrInput
	// Specifies the name of the Container Registry. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// A `networkRuleSet` block as documented below.
	NetworkRuleSet RegistryNetworkRuleSetPtrInput
	// The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringPtrInput
	// The SKU name of the container registry. Possible values are  `Basic`, `Standard` and `Premium`. `Classic` (which was previously `Basic`) is supported only for existing resources.
	Sku pulumi.StringPtrInput
	// The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.
	StorageAccountId pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (RegistryState) ElementType() reflect.Type {
	return reflect.TypeOf((*registryState)(nil)).Elem()
}

type registryArgs struct {
	// Specifies whether the admin user is enabled. Defaults to `false`.
	AdminEnabled *bool `pulumi:"adminEnabled"`
	// A list of Azure locations where the container registry should be geo-replicated.
	GeoreplicationLocations []string `pulumi:"georeplicationLocations"`
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// Specifies the name of the Container Registry. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// A `networkRuleSet` block as documented below.
	NetworkRuleSet *RegistryNetworkRuleSet `pulumi:"networkRuleSet"`
	// The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// The SKU name of the container registry. Possible values are  `Basic`, `Standard` and `Premium`. `Classic` (which was previously `Basic`) is supported only for existing resources.
	Sku *string `pulumi:"sku"`
	// The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.
	StorageAccountId *string `pulumi:"storageAccountId"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Registry resource.
type RegistryArgs struct {
	// Specifies whether the admin user is enabled. Defaults to `false`.
	AdminEnabled pulumi.BoolPtrInput
	// A list of Azure locations where the container registry should be geo-replicated.
	GeoreplicationLocations pulumi.StringArrayInput
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// Specifies the name of the Container Registry. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// A `networkRuleSet` block as documented below.
	NetworkRuleSet RegistryNetworkRuleSetPtrInput
	// The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringInput
	// The SKU name of the container registry. Possible values are  `Basic`, `Standard` and `Premium`. `Classic` (which was previously `Basic`) is supported only for existing resources.
	Sku pulumi.StringPtrInput
	// The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.
	StorageAccountId pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (RegistryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*registryArgs)(nil)).Elem()
}

