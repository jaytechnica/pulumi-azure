// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package securitycenter

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages the Data Access Settings for Azure Security Center.
//
// > **NOTE:** This resource requires the `Owner` permission on the Subscription.
//
// > **NOTE:** Deletion of this resource does not change or reset the data access settings
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/securitycenter"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := securitycenter.NewSetting(ctx, "example", &securitycenter.SettingArgs{
// 			Enabled:     pulumi.Bool(true),
// 			SettingName: pulumi.String("MCAS"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Setting struct {
	pulumi.CustomResourceState

	// Boolean flag to enable/disable data access.
	Enabled pulumi.BoolOutput `pulumi:"enabled"`
	// The setting to manage. Possible values are `MCAS` and `WDATP`.
	SettingName pulumi.StringOutput `pulumi:"settingName"`
}

// NewSetting registers a new resource with the given unique name, arguments, and options.
func NewSetting(ctx *pulumi.Context,
	name string, args *SettingArgs, opts ...pulumi.ResourceOption) (*Setting, error) {
	if args == nil || args.Enabled == nil {
		return nil, errors.New("missing required argument 'Enabled'")
	}
	if args == nil || args.SettingName == nil {
		return nil, errors.New("missing required argument 'SettingName'")
	}
	if args == nil {
		args = &SettingArgs{}
	}
	var resource Setting
	err := ctx.RegisterResource("azure:securitycenter/setting:Setting", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSetting gets an existing Setting resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSetting(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SettingState, opts ...pulumi.ResourceOption) (*Setting, error) {
	var resource Setting
	err := ctx.ReadResource("azure:securitycenter/setting:Setting", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Setting resources.
type settingState struct {
	// Boolean flag to enable/disable data access.
	Enabled *bool `pulumi:"enabled"`
	// The setting to manage. Possible values are `MCAS` and `WDATP`.
	SettingName *string `pulumi:"settingName"`
}

type SettingState struct {
	// Boolean flag to enable/disable data access.
	Enabled pulumi.BoolPtrInput
	// The setting to manage. Possible values are `MCAS` and `WDATP`.
	SettingName pulumi.StringPtrInput
}

func (SettingState) ElementType() reflect.Type {
	return reflect.TypeOf((*settingState)(nil)).Elem()
}

type settingArgs struct {
	// Boolean flag to enable/disable data access.
	Enabled bool `pulumi:"enabled"`
	// The setting to manage. Possible values are `MCAS` and `WDATP`.
	SettingName string `pulumi:"settingName"`
}

// The set of arguments for constructing a Setting resource.
type SettingArgs struct {
	// Boolean flag to enable/disable data access.
	Enabled pulumi.BoolInput
	// The setting to manage. Possible values are `MCAS` and `WDATP`.
	SettingName pulumi.StringInput
}

func (SettingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*settingArgs)(nil)).Elem()
}
