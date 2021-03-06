// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datafactory

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Pipeline inside a Azure Data Factory.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/datafactory"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
// 			Location: pulumi.String("northeurope"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleFactory, err := datafactory.NewFactory(ctx, "exampleFactory", &datafactory.FactoryArgs{
// 			Location:          exampleResourceGroup.Location,
// 			ResourceGroupName: exampleResourceGroup.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = datafactory.NewPipeline(ctx, "examplePipeline", &datafactory.PipelineArgs{
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			DataFactoryName:   exampleFactory.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### With Activities
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/datafactory"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := datafactory.NewPipeline(ctx, "test", &datafactory.PipelineArgs{
// 			ResourceGroupName: pulumi.Any(azurerm_resource_group.Test.Name),
// 			DataFactoryName:   pulumi.Any(azurerm_data_factory.Test.Name),
// 			Variables: pulumi.StringMap{
// 				"bob": pulumi.String("item1"),
// 			},
// 			ActivitiesJson: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v", "[\n", "	{\n", "		\"name\": \"Append variable1\",\n", "		\"type\": \"AppendVariable\",\n", "		\"dependsOn\": [],\n", "		\"userProperties\": [],\n", "		\"typeProperties\": {\n", "			\"variableName\": \"bob\",\n", "			\"value\": \"something\"\n", "		}\n", "	}\n", "]\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Pipeline struct {
	pulumi.CustomResourceState

	// A JSON object that contains the activities that will be associated with the Data Factory Pipeline.
	ActivitiesJson pulumi.StringPtrOutput `pulumi:"activitiesJson"`
	// List of tags that can be used for describing the Data Factory Pipeline.
	Annotations pulumi.StringArrayOutput `pulumi:"annotations"`
	// The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.
	DataFactoryName pulumi.StringOutput `pulumi:"dataFactoryName"`
	// The description for the Data Factory Pipeline.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
	Name pulumi.StringOutput `pulumi:"name"`
	// A map of parameters to associate with the Data Factory Pipeline.
	Parameters pulumi.StringMapOutput `pulumi:"parameters"`
	// The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// A map of variables to associate with the Data Factory Pipeline.
	Variables pulumi.StringMapOutput `pulumi:"variables"`
}

// NewPipeline registers a new resource with the given unique name, arguments, and options.
func NewPipeline(ctx *pulumi.Context,
	name string, args *PipelineArgs, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	if args == nil || args.DataFactoryName == nil {
		return nil, errors.New("missing required argument 'DataFactoryName'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil {
		args = &PipelineArgs{}
	}
	var resource Pipeline
	err := ctx.RegisterResource("azure:datafactory/pipeline:Pipeline", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPipeline gets an existing Pipeline resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPipeline(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PipelineState, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	var resource Pipeline
	err := ctx.ReadResource("azure:datafactory/pipeline:Pipeline", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Pipeline resources.
type pipelineState struct {
	// A JSON object that contains the activities that will be associated with the Data Factory Pipeline.
	ActivitiesJson *string `pulumi:"activitiesJson"`
	// List of tags that can be used for describing the Data Factory Pipeline.
	Annotations []string `pulumi:"annotations"`
	// The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.
	DataFactoryName *string `pulumi:"dataFactoryName"`
	// The description for the Data Factory Pipeline.
	Description *string `pulumi:"description"`
	// Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
	Name *string `pulumi:"name"`
	// A map of parameters to associate with the Data Factory Pipeline.
	Parameters map[string]string `pulumi:"parameters"`
	// The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// A map of variables to associate with the Data Factory Pipeline.
	Variables map[string]string `pulumi:"variables"`
}

type PipelineState struct {
	// A JSON object that contains the activities that will be associated with the Data Factory Pipeline.
	ActivitiesJson pulumi.StringPtrInput
	// List of tags that can be used for describing the Data Factory Pipeline.
	Annotations pulumi.StringArrayInput
	// The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.
	DataFactoryName pulumi.StringPtrInput
	// The description for the Data Factory Pipeline.
	Description pulumi.StringPtrInput
	// Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
	Name pulumi.StringPtrInput
	// A map of parameters to associate with the Data Factory Pipeline.
	Parameters pulumi.StringMapInput
	// The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource
	ResourceGroupName pulumi.StringPtrInput
	// A map of variables to associate with the Data Factory Pipeline.
	Variables pulumi.StringMapInput
}

func (PipelineState) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineState)(nil)).Elem()
}

type pipelineArgs struct {
	// A JSON object that contains the activities that will be associated with the Data Factory Pipeline.
	ActivitiesJson *string `pulumi:"activitiesJson"`
	// List of tags that can be used for describing the Data Factory Pipeline.
	Annotations []string `pulumi:"annotations"`
	// The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.
	DataFactoryName string `pulumi:"dataFactoryName"`
	// The description for the Data Factory Pipeline.
	Description *string `pulumi:"description"`
	// Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
	Name *string `pulumi:"name"`
	// A map of parameters to associate with the Data Factory Pipeline.
	Parameters map[string]string `pulumi:"parameters"`
	// The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// A map of variables to associate with the Data Factory Pipeline.
	Variables map[string]string `pulumi:"variables"`
}

// The set of arguments for constructing a Pipeline resource.
type PipelineArgs struct {
	// A JSON object that contains the activities that will be associated with the Data Factory Pipeline.
	ActivitiesJson pulumi.StringPtrInput
	// List of tags that can be used for describing the Data Factory Pipeline.
	Annotations pulumi.StringArrayInput
	// The Data Factory name in which to associate the Pipeline with. Changing this forces a new resource.
	DataFactoryName pulumi.StringInput
	// The description for the Data Factory Pipeline.
	Description pulumi.StringPtrInput
	// Specifies the name of the Data Factory Pipeline. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
	Name pulumi.StringPtrInput
	// A map of parameters to associate with the Data Factory Pipeline.
	Parameters pulumi.StringMapInput
	// The name of the resource group in which to create the Data Factory Pipeline. Changing this forces a new resource
	ResourceGroupName pulumi.StringInput
	// A map of variables to associate with the Data Factory Pipeline.
	Variables pulumi.StringMapInput
}

func (PipelineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineArgs)(nil)).Elem()
}
