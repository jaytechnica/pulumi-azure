// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apimanagement

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an API Management Microsoft Identity Provider.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/apimanagement"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
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
// 		exampleService, err := apimanagement.NewService(ctx, "exampleService", &apimanagement.ServiceArgs{
// 			Location:          exampleResourceGroup.Location,
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			PublisherName:     pulumi.String("My Company"),
// 			PublisherEmail:    pulumi.String("company@mycompany.io"),
// 			SkuName:           pulumi.String("Developer_1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = apimanagement.NewIdentityProviderMicrosoft(ctx, "exampleIdentityProviderMicrosoft", &apimanagement.IdentityProviderMicrosoftArgs{
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			ApiManagementName: exampleService.Name,
// 			ClientId:          pulumi.String("00000000-0000-0000-0000-000000000000"),
// 			ClientSecret:      pulumi.String("00000000000000000000000000000000"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type IdentityProviderMicrosoft struct {
	pulumi.CustomResourceState

	// The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.
	ApiManagementName pulumi.StringOutput `pulumi:"apiManagementName"`
	// Client Id of the Azure AD Application.
	ClientId pulumi.StringOutput `pulumi:"clientId"`
	// Client secret of the Azure AD Application.
	ClientSecret pulumi.StringOutput `pulumi:"clientSecret"`
	// The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
}

// NewIdentityProviderMicrosoft registers a new resource with the given unique name, arguments, and options.
func NewIdentityProviderMicrosoft(ctx *pulumi.Context,
	name string, args *IdentityProviderMicrosoftArgs, opts ...pulumi.ResourceOption) (*IdentityProviderMicrosoft, error) {
	if args == nil || args.ApiManagementName == nil {
		return nil, errors.New("missing required argument 'ApiManagementName'")
	}
	if args == nil || args.ClientId == nil {
		return nil, errors.New("missing required argument 'ClientId'")
	}
	if args == nil || args.ClientSecret == nil {
		return nil, errors.New("missing required argument 'ClientSecret'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil {
		args = &IdentityProviderMicrosoftArgs{}
	}
	var resource IdentityProviderMicrosoft
	err := ctx.RegisterResource("azure:apimanagement/identityProviderMicrosoft:IdentityProviderMicrosoft", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIdentityProviderMicrosoft gets an existing IdentityProviderMicrosoft resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIdentityProviderMicrosoft(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IdentityProviderMicrosoftState, opts ...pulumi.ResourceOption) (*IdentityProviderMicrosoft, error) {
	var resource IdentityProviderMicrosoft
	err := ctx.ReadResource("azure:apimanagement/identityProviderMicrosoft:IdentityProviderMicrosoft", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IdentityProviderMicrosoft resources.
type identityProviderMicrosoftState struct {
	// The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.
	ApiManagementName *string `pulumi:"apiManagementName"`
	// Client Id of the Azure AD Application.
	ClientId *string `pulumi:"clientId"`
	// Client secret of the Azure AD Application.
	ClientSecret *string `pulumi:"clientSecret"`
	// The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
}

type IdentityProviderMicrosoftState struct {
	// The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.
	ApiManagementName pulumi.StringPtrInput
	// Client Id of the Azure AD Application.
	ClientId pulumi.StringPtrInput
	// Client secret of the Azure AD Application.
	ClientSecret pulumi.StringPtrInput
	// The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringPtrInput
}

func (IdentityProviderMicrosoftState) ElementType() reflect.Type {
	return reflect.TypeOf((*identityProviderMicrosoftState)(nil)).Elem()
}

type identityProviderMicrosoftArgs struct {
	// The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.
	ApiManagementName string `pulumi:"apiManagementName"`
	// Client Id of the Azure AD Application.
	ClientId string `pulumi:"clientId"`
	// Client secret of the Azure AD Application.
	ClientSecret string `pulumi:"clientSecret"`
	// The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
}

// The set of arguments for constructing a IdentityProviderMicrosoft resource.
type IdentityProviderMicrosoftArgs struct {
	// The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.
	ApiManagementName pulumi.StringInput
	// Client Id of the Azure AD Application.
	ClientId pulumi.StringInput
	// Client secret of the Azure AD Application.
	ClientSecret pulumi.StringInput
	// The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringInput
}

func (IdentityProviderMicrosoftArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*identityProviderMicrosoftArgs)(nil)).Elem()
}
