// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manage a virtual machine scale set.
// 
// ~> **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
type ScaleSet struct {
	s *pulumi.ResourceState
}

// NewScaleSet registers a new resource with the given unique name, arguments, and options.
func NewScaleSet(ctx *pulumi.Context,
	name string, args *ScaleSetArgs, opts ...pulumi.ResourceOpt) (*ScaleSet, error) {
	if args == nil || args.Location == nil {
		return nil, errors.New("missing required argument 'Location'")
	}
	if args == nil || args.NetworkProfiles == nil {
		return nil, errors.New("missing required argument 'NetworkProfiles'")
	}
	if args == nil || args.OsProfile == nil {
		return nil, errors.New("missing required argument 'OsProfile'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.Sku == nil {
		return nil, errors.New("missing required argument 'Sku'")
	}
	if args == nil || args.StorageProfileOsDisk == nil {
		return nil, errors.New("missing required argument 'StorageProfileOsDisk'")
	}
	if args == nil || args.UpgradePolicyMode == nil {
		return nil, errors.New("missing required argument 'UpgradePolicyMode'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bootDiagnostics"] = nil
		inputs["extensions"] = nil
		inputs["identity"] = nil
		inputs["licenseType"] = nil
		inputs["location"] = nil
		inputs["name"] = nil
		inputs["networkProfiles"] = nil
		inputs["osProfile"] = nil
		inputs["osProfileLinuxConfig"] = nil
		inputs["osProfileSecrets"] = nil
		inputs["osProfileWindowsConfig"] = nil
		inputs["overprovision"] = nil
		inputs["plan"] = nil
		inputs["priority"] = nil
		inputs["resourceGroupName"] = nil
		inputs["singlePlacementGroup"] = nil
		inputs["sku"] = nil
		inputs["storageProfileDataDisks"] = nil
		inputs["storageProfileImageReference"] = nil
		inputs["storageProfileOsDisk"] = nil
		inputs["tags"] = nil
		inputs["upgradePolicyMode"] = nil
		inputs["zones"] = nil
	} else {
		inputs["bootDiagnostics"] = args.BootDiagnostics
		inputs["extensions"] = args.Extensions
		inputs["identity"] = args.Identity
		inputs["licenseType"] = args.LicenseType
		inputs["location"] = args.Location
		inputs["name"] = args.Name
		inputs["networkProfiles"] = args.NetworkProfiles
		inputs["osProfile"] = args.OsProfile
		inputs["osProfileLinuxConfig"] = args.OsProfileLinuxConfig
		inputs["osProfileSecrets"] = args.OsProfileSecrets
		inputs["osProfileWindowsConfig"] = args.OsProfileWindowsConfig
		inputs["overprovision"] = args.Overprovision
		inputs["plan"] = args.Plan
		inputs["priority"] = args.Priority
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["singlePlacementGroup"] = args.SinglePlacementGroup
		inputs["sku"] = args.Sku
		inputs["storageProfileDataDisks"] = args.StorageProfileDataDisks
		inputs["storageProfileImageReference"] = args.StorageProfileImageReference
		inputs["storageProfileOsDisk"] = args.StorageProfileOsDisk
		inputs["tags"] = args.Tags
		inputs["upgradePolicyMode"] = args.UpgradePolicyMode
		inputs["zones"] = args.Zones
	}
	s, err := ctx.RegisterResource("azure:compute/scaleSet:ScaleSet", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ScaleSet{s: s}, nil
}

// GetScaleSet gets an existing ScaleSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetScaleSet(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ScaleSetState, opts ...pulumi.ResourceOpt) (*ScaleSet, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bootDiagnostics"] = state.BootDiagnostics
		inputs["extensions"] = state.Extensions
		inputs["identity"] = state.Identity
		inputs["licenseType"] = state.LicenseType
		inputs["location"] = state.Location
		inputs["name"] = state.Name
		inputs["networkProfiles"] = state.NetworkProfiles
		inputs["osProfile"] = state.OsProfile
		inputs["osProfileLinuxConfig"] = state.OsProfileLinuxConfig
		inputs["osProfileSecrets"] = state.OsProfileSecrets
		inputs["osProfileWindowsConfig"] = state.OsProfileWindowsConfig
		inputs["overprovision"] = state.Overprovision
		inputs["plan"] = state.Plan
		inputs["priority"] = state.Priority
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["singlePlacementGroup"] = state.SinglePlacementGroup
		inputs["sku"] = state.Sku
		inputs["storageProfileDataDisks"] = state.StorageProfileDataDisks
		inputs["storageProfileImageReference"] = state.StorageProfileImageReference
		inputs["storageProfileOsDisk"] = state.StorageProfileOsDisk
		inputs["tags"] = state.Tags
		inputs["upgradePolicyMode"] = state.UpgradePolicyMode
		inputs["zones"] = state.Zones
	}
	s, err := ctx.ReadResource("azure:compute/scaleSet:ScaleSet", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ScaleSet{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ScaleSet) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ScaleSet) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// A boot diagnostics profile block as referenced below.
func (r *ScaleSet) BootDiagnostics() *pulumi.Output {
	return r.s.State["bootDiagnostics"]
}

// Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.
func (r *ScaleSet) Extensions() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["extensions"])
}

func (r *ScaleSet) Identity() *pulumi.Output {
	return r.s.State["identity"]
}

// Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.
func (r *ScaleSet) LicenseType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["licenseType"])
}

// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
func (r *ScaleSet) Location() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["location"])
}

// Specifies the name of the image from the marketplace.
func (r *ScaleSet) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// A collection of network profile block as documented below.
func (r *ScaleSet) NetworkProfiles() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["networkProfiles"])
}

// A Virtual Machine OS Profile block as documented below.
func (r *ScaleSet) OsProfile() *pulumi.Output {
	return r.s.State["osProfile"]
}

// A Linux config block as documented below.
func (r *ScaleSet) OsProfileLinuxConfig() *pulumi.Output {
	return r.s.State["osProfileLinuxConfig"]
}

// A collection of Secret blocks as documented below.
func (r *ScaleSet) OsProfileSecrets() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["osProfileSecrets"])
}

// A Windows config block as documented below.
func (r *ScaleSet) OsProfileWindowsConfig() *pulumi.Output {
	return r.s.State["osProfileWindowsConfig"]
}

// Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.
func (r *ScaleSet) Overprovision() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["overprovision"])
}

// A plan block as documented below.
func (r *ScaleSet) Plan() *pulumi.Output {
	return r.s.State["plan"]
}

// Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.
func (r *ScaleSet) Priority() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["priority"])
}

// The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.
func (r *ScaleSet) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Defaults to `true`. Changing this forces a
// new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.
func (r *ScaleSet) SinglePlacementGroup() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["singlePlacementGroup"])
}

// Specifies the SKU of the image used to create the virtual machines.
func (r *ScaleSet) Sku() *pulumi.Output {
	return r.s.State["sku"]
}

// A storage profile data disk block as documented below
func (r *ScaleSet) StorageProfileDataDisks() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["storageProfileDataDisks"])
}

// A storage profile image reference block as documented below.
func (r *ScaleSet) StorageProfileImageReference() *pulumi.Output {
	return r.s.State["storageProfileImageReference"]
}

// A storage profile os disk block as documented below
func (r *ScaleSet) StorageProfileOsDisk() *pulumi.Output {
	return r.s.State["storageProfileOsDisk"]
}

// A mapping of tags to assign to the resource.
func (r *ScaleSet) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.
func (r *ScaleSet) UpgradePolicyMode() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["upgradePolicyMode"])
}

// A collection of availability zones to spread the Virtual Machines over.
func (r *ScaleSet) Zones() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["zones"])
}

// Input properties used for looking up and filtering ScaleSet resources.
type ScaleSetState struct {
	// A boot diagnostics profile block as referenced below.
	BootDiagnostics interface{}
	// Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.
	Extensions interface{}
	Identity interface{}
	// Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.
	LicenseType interface{}
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location interface{}
	// Specifies the name of the image from the marketplace.
	Name interface{}
	// A collection of network profile block as documented below.
	NetworkProfiles interface{}
	// A Virtual Machine OS Profile block as documented below.
	OsProfile interface{}
	// A Linux config block as documented below.
	OsProfileLinuxConfig interface{}
	// A collection of Secret blocks as documented below.
	OsProfileSecrets interface{}
	// A Windows config block as documented below.
	OsProfileWindowsConfig interface{}
	// Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.
	Overprovision interface{}
	// A plan block as documented below.
	Plan interface{}
	// Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.
	Priority interface{}
	// The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Defaults to `true`. Changing this forces a
	// new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.
	SinglePlacementGroup interface{}
	// Specifies the SKU of the image used to create the virtual machines.
	Sku interface{}
	// A storage profile data disk block as documented below
	StorageProfileDataDisks interface{}
	// A storage profile image reference block as documented below.
	StorageProfileImageReference interface{}
	// A storage profile os disk block as documented below
	StorageProfileOsDisk interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.
	UpgradePolicyMode interface{}
	// A collection of availability zones to spread the Virtual Machines over.
	Zones interface{}
}

// The set of arguments for constructing a ScaleSet resource.
type ScaleSetArgs struct {
	// A boot diagnostics profile block as referenced below.
	BootDiagnostics interface{}
	// Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.
	Extensions interface{}
	Identity interface{}
	// Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.
	LicenseType interface{}
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location interface{}
	// Specifies the name of the image from the marketplace.
	Name interface{}
	// A collection of network profile block as documented below.
	NetworkProfiles interface{}
	// A Virtual Machine OS Profile block as documented below.
	OsProfile interface{}
	// A Linux config block as documented below.
	OsProfileLinuxConfig interface{}
	// A collection of Secret blocks as documented below.
	OsProfileSecrets interface{}
	// A Windows config block as documented below.
	OsProfileWindowsConfig interface{}
	// Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.
	Overprovision interface{}
	// A plan block as documented below.
	Plan interface{}
	// Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.
	Priority interface{}
	// The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Defaults to `true`. Changing this forces a
	// new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.
	SinglePlacementGroup interface{}
	// Specifies the SKU of the image used to create the virtual machines.
	Sku interface{}
	// A storage profile data disk block as documented below
	StorageProfileDataDisks interface{}
	// A storage profile image reference block as documented below.
	StorageProfileImageReference interface{}
	// A storage profile os disk block as documented below
	StorageProfileOsDisk interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.
	UpgradePolicyMode interface{}
	// A collection of availability zones to spread the Virtual Machines over.
	Zones interface{}
}
