// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package core

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Subscription Template Deployment.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := core.NewSubscriptionTemplateDeployment(ctx, "example", &core.SubscriptionTemplateDeploymentArgs{
// 			Location:        pulumi.String("West Europe"),
// 			TemplateContent: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v", " {\n", "   \"", "$", "schema\": \"https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#\",\n", "   \"contentVersion\": \"1.0.0.0\",\n", "   \"parameters\": {},\n", "   \"variables\": {},\n", "   \"resources\": [\n", "     {\n", "       \"type\": \"Microsoft.Resources/resourceGroups\",\n", "       \"apiVersion\": \"2018-05-01\",\n", "       \"location\": \"West Europe\",\n", "       \"name\": \"some-resource-group\",\n", "       \"properties\": {}\n", "     }\n", "   ]\n", " }\n", " \n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SubscriptionTemplateDeployment struct {
	pulumi.CustomResourceState

	// The Debug Level which should be used for this Subscription Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
	DebugLevel pulumi.StringPtrOutput `pulumi:"debugLevel"`
	// The Azure Region where the Subscription Template Deployment should exist. Changing this forces a new Subscription Template Deployment to be created.
	Location pulumi.StringOutput `pulumi:"location"`
	// The name which should be used for this Subscription Template Deployment. Changing this forces a new Subscription Template Deployment to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The JSON Content of the Outputs of the ARM Template Deployment.
	OutputContent pulumi.StringOutput `pulumi:"outputContent"`
	// The contents of the ARM Template parameters file - containing a JSON list of parameters.
	ParametersContent pulumi.StringOutput `pulumi:"parametersContent"`
	// A mapping of tags which should be assigned to the Subscription Template Deployment.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The contents of the ARM Template which should be deployed into this Subscription.
	TemplateContent pulumi.StringOutput `pulumi:"templateContent"`
}

// NewSubscriptionTemplateDeployment registers a new resource with the given unique name, arguments, and options.
func NewSubscriptionTemplateDeployment(ctx *pulumi.Context,
	name string, args *SubscriptionTemplateDeploymentArgs, opts ...pulumi.ResourceOption) (*SubscriptionTemplateDeployment, error) {
	if args == nil || args.TemplateContent == nil {
		return nil, errors.New("missing required argument 'TemplateContent'")
	}
	if args == nil {
		args = &SubscriptionTemplateDeploymentArgs{}
	}
	var resource SubscriptionTemplateDeployment
	err := ctx.RegisterResource("azure:core/subscriptionTemplateDeployment:SubscriptionTemplateDeployment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSubscriptionTemplateDeployment gets an existing SubscriptionTemplateDeployment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubscriptionTemplateDeployment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SubscriptionTemplateDeploymentState, opts ...pulumi.ResourceOption) (*SubscriptionTemplateDeployment, error) {
	var resource SubscriptionTemplateDeployment
	err := ctx.ReadResource("azure:core/subscriptionTemplateDeployment:SubscriptionTemplateDeployment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SubscriptionTemplateDeployment resources.
type subscriptionTemplateDeploymentState struct {
	// The Debug Level which should be used for this Subscription Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
	DebugLevel *string `pulumi:"debugLevel"`
	// The Azure Region where the Subscription Template Deployment should exist. Changing this forces a new Subscription Template Deployment to be created.
	Location *string `pulumi:"location"`
	// The name which should be used for this Subscription Template Deployment. Changing this forces a new Subscription Template Deployment to be created.
	Name *string `pulumi:"name"`
	// The JSON Content of the Outputs of the ARM Template Deployment.
	OutputContent *string `pulumi:"outputContent"`
	// The contents of the ARM Template parameters file - containing a JSON list of parameters.
	ParametersContent *string `pulumi:"parametersContent"`
	// A mapping of tags which should be assigned to the Subscription Template Deployment.
	Tags map[string]string `pulumi:"tags"`
	// The contents of the ARM Template which should be deployed into this Subscription.
	TemplateContent *string `pulumi:"templateContent"`
}

type SubscriptionTemplateDeploymentState struct {
	// The Debug Level which should be used for this Subscription Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
	DebugLevel pulumi.StringPtrInput
	// The Azure Region where the Subscription Template Deployment should exist. Changing this forces a new Subscription Template Deployment to be created.
	Location pulumi.StringPtrInput
	// The name which should be used for this Subscription Template Deployment. Changing this forces a new Subscription Template Deployment to be created.
	Name pulumi.StringPtrInput
	// The JSON Content of the Outputs of the ARM Template Deployment.
	OutputContent pulumi.StringPtrInput
	// The contents of the ARM Template parameters file - containing a JSON list of parameters.
	ParametersContent pulumi.StringPtrInput
	// A mapping of tags which should be assigned to the Subscription Template Deployment.
	Tags pulumi.StringMapInput
	// The contents of the ARM Template which should be deployed into this Subscription.
	TemplateContent pulumi.StringPtrInput
}

func (SubscriptionTemplateDeploymentState) ElementType() reflect.Type {
	return reflect.TypeOf((*subscriptionTemplateDeploymentState)(nil)).Elem()
}

type subscriptionTemplateDeploymentArgs struct {
	// The Debug Level which should be used for this Subscription Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
	DebugLevel *string `pulumi:"debugLevel"`
	// The Azure Region where the Subscription Template Deployment should exist. Changing this forces a new Subscription Template Deployment to be created.
	Location *string `pulumi:"location"`
	// The name which should be used for this Subscription Template Deployment. Changing this forces a new Subscription Template Deployment to be created.
	Name *string `pulumi:"name"`
	// The contents of the ARM Template parameters file - containing a JSON list of parameters.
	ParametersContent *string `pulumi:"parametersContent"`
	// A mapping of tags which should be assigned to the Subscription Template Deployment.
	Tags map[string]string `pulumi:"tags"`
	// The contents of the ARM Template which should be deployed into this Subscription.
	TemplateContent string `pulumi:"templateContent"`
}

// The set of arguments for constructing a SubscriptionTemplateDeployment resource.
type SubscriptionTemplateDeploymentArgs struct {
	// The Debug Level which should be used for this Subscription Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
	DebugLevel pulumi.StringPtrInput
	// The Azure Region where the Subscription Template Deployment should exist. Changing this forces a new Subscription Template Deployment to be created.
	Location pulumi.StringPtrInput
	// The name which should be used for this Subscription Template Deployment. Changing this forces a new Subscription Template Deployment to be created.
	Name pulumi.StringPtrInput
	// The contents of the ARM Template parameters file - containing a JSON list of parameters.
	ParametersContent pulumi.StringPtrInput
	// A mapping of tags which should be assigned to the Subscription Template Deployment.
	Tags pulumi.StringMapInput
	// The contents of the ARM Template which should be deployed into this Subscription.
	TemplateContent pulumi.StringInput
}

func (SubscriptionTemplateDeploymentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*subscriptionTemplateDeploymentArgs)(nil)).Elem()
}
