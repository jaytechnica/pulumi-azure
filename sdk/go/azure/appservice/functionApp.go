// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appservice

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Function App.
type FunctionApp struct {
	s *pulumi.ResourceState
}

// NewFunctionApp registers a new resource with the given unique name, arguments, and options.
func NewFunctionApp(ctx *pulumi.Context,
	name string, args *FunctionAppArgs, opts ...pulumi.ResourceOpt) (*FunctionApp, error) {
	if args == nil || args.AppServicePlanId == nil {
		return nil, errors.New("missing required argument 'AppServicePlanId'")
	}
	if args == nil || args.Location == nil {
		return nil, errors.New("missing required argument 'Location'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.StorageConnectionString == nil {
		return nil, errors.New("missing required argument 'StorageConnectionString'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["appServicePlanId"] = nil
		inputs["appSettings"] = nil
		inputs["clientAffinityEnabled"] = nil
		inputs["connectionStrings"] = nil
		inputs["enableBuiltinLogging"] = nil
		inputs["enabled"] = nil
		inputs["httpsOnly"] = nil
		inputs["identity"] = nil
		inputs["location"] = nil
		inputs["name"] = nil
		inputs["resourceGroupName"] = nil
		inputs["siteConfig"] = nil
		inputs["storageConnectionString"] = nil
		inputs["tags"] = nil
		inputs["version"] = nil
	} else {
		inputs["appServicePlanId"] = args.AppServicePlanId
		inputs["appSettings"] = args.AppSettings
		inputs["clientAffinityEnabled"] = args.ClientAffinityEnabled
		inputs["connectionStrings"] = args.ConnectionStrings
		inputs["enableBuiltinLogging"] = args.EnableBuiltinLogging
		inputs["enabled"] = args.Enabled
		inputs["httpsOnly"] = args.HttpsOnly
		inputs["identity"] = args.Identity
		inputs["location"] = args.Location
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["siteConfig"] = args.SiteConfig
		inputs["storageConnectionString"] = args.StorageConnectionString
		inputs["tags"] = args.Tags
		inputs["version"] = args.Version
	}
	inputs["defaultHostname"] = nil
	inputs["kind"] = nil
	inputs["outboundIpAddresses"] = nil
	inputs["possibleOutboundIpAddresses"] = nil
	inputs["siteCredential"] = nil
	s, err := ctx.RegisterResource("azure:appservice/functionApp:FunctionApp", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FunctionApp{s: s}, nil
}

// GetFunctionApp gets an existing FunctionApp resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFunctionApp(ctx *pulumi.Context,
	name string, id pulumi.ID, state *FunctionAppState, opts ...pulumi.ResourceOpt) (*FunctionApp, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["appServicePlanId"] = state.AppServicePlanId
		inputs["appSettings"] = state.AppSettings
		inputs["clientAffinityEnabled"] = state.ClientAffinityEnabled
		inputs["connectionStrings"] = state.ConnectionStrings
		inputs["defaultHostname"] = state.DefaultHostname
		inputs["enableBuiltinLogging"] = state.EnableBuiltinLogging
		inputs["enabled"] = state.Enabled
		inputs["httpsOnly"] = state.HttpsOnly
		inputs["identity"] = state.Identity
		inputs["kind"] = state.Kind
		inputs["location"] = state.Location
		inputs["name"] = state.Name
		inputs["outboundIpAddresses"] = state.OutboundIpAddresses
		inputs["possibleOutboundIpAddresses"] = state.PossibleOutboundIpAddresses
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["siteConfig"] = state.SiteConfig
		inputs["siteCredential"] = state.SiteCredential
		inputs["storageConnectionString"] = state.StorageConnectionString
		inputs["tags"] = state.Tags
		inputs["version"] = state.Version
	}
	s, err := ctx.ReadResource("azure:appservice/functionApp:FunctionApp", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FunctionApp{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *FunctionApp) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *FunctionApp) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.
func (r *FunctionApp) AppServicePlanId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["appServicePlanId"])
}

// A key-value pair of App Settings.
func (r *FunctionApp) AppSettings() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["appSettings"])
}

// Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?
func (r *FunctionApp) ClientAffinityEnabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["clientAffinityEnabled"])
}

// An `connection_string` block as defined below.
func (r *FunctionApp) ConnectionStrings() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["connectionStrings"])
}

// The default hostname associated with the Function App - such as `mysite.azurewebsites.net`
func (r *FunctionApp) DefaultHostname() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultHostname"])
}

// Should the built-in logging of this Function App be enabled? Defaults to `true`.
func (r *FunctionApp) EnableBuiltinLogging() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enableBuiltinLogging"])
}

// Is the Function App enabled?
func (r *FunctionApp) Enabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enabled"])
}

// Can the Function App only be accessed via HTTPS? Defaults to `false`.
func (r *FunctionApp) HttpsOnly() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["httpsOnly"])
}

// An `identity` block as defined below.
func (r *FunctionApp) Identity() *pulumi.Output {
	return r.s.State["identity"]
}

// The Function App kind - such as `functionapp,linux,container`
func (r *FunctionApp) Kind() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kind"])
}

// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
func (r *FunctionApp) Location() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["location"])
}

// The name of the Connection String.
func (r *FunctionApp) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
func (r *FunctionApp) OutboundIpAddresses() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["outboundIpAddresses"])
}

// A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
func (r *FunctionApp) PossibleOutboundIpAddresses() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["possibleOutboundIpAddresses"])
}

// The name of the resource group in which to create the Function App.
func (r *FunctionApp) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// A `site_config` object as defined below.
func (r *FunctionApp) SiteConfig() *pulumi.Output {
	return r.s.State["siteConfig"]
}

// A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
func (r *FunctionApp) SiteCredential() *pulumi.Output {
	return r.s.State["siteCredential"]
}

// The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).
func (r *FunctionApp) StorageConnectionString() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["storageConnectionString"])
}

// A mapping of tags to assign to the resource.
func (r *FunctionApp) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// The runtime version associated with the Function App. Defaults to `~1`.
func (r *FunctionApp) Version() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["version"])
}

// Input properties used for looking up and filtering FunctionApp resources.
type FunctionAppState struct {
	// The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.
	AppServicePlanId interface{}
	// A key-value pair of App Settings.
	AppSettings interface{}
	// Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?
	ClientAffinityEnabled interface{}
	// An `connection_string` block as defined below.
	ConnectionStrings interface{}
	// The default hostname associated with the Function App - such as `mysite.azurewebsites.net`
	DefaultHostname interface{}
	// Should the built-in logging of this Function App be enabled? Defaults to `true`.
	EnableBuiltinLogging interface{}
	// Is the Function App enabled?
	Enabled interface{}
	// Can the Function App only be accessed via HTTPS? Defaults to `false`.
	HttpsOnly interface{}
	// An `identity` block as defined below.
	Identity interface{}
	// The Function App kind - such as `functionapp,linux,container`
	Kind interface{}
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location interface{}
	// The name of the Connection String.
	Name interface{}
	// A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
	OutboundIpAddresses interface{}
	// A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
	PossibleOutboundIpAddresses interface{}
	// The name of the resource group in which to create the Function App.
	ResourceGroupName interface{}
	// A `site_config` object as defined below.
	SiteConfig interface{}
	// A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
	SiteCredential interface{}
	// The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).
	StorageConnectionString interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// The runtime version associated with the Function App. Defaults to `~1`.
	Version interface{}
}

// The set of arguments for constructing a FunctionApp resource.
type FunctionAppArgs struct {
	// The ID of the App Service Plan within which to create this Function App. Changing this forces a new resource to be created.
	AppServicePlanId interface{}
	// A key-value pair of App Settings.
	AppSettings interface{}
	// Should the Function App send session affinity cookies, which route client requests in the same session to the same instance?
	ClientAffinityEnabled interface{}
	// An `connection_string` block as defined below.
	ConnectionStrings interface{}
	// Should the built-in logging of this Function App be enabled? Defaults to `true`.
	EnableBuiltinLogging interface{}
	// Is the Function App enabled?
	Enabled interface{}
	// Can the Function App only be accessed via HTTPS? Defaults to `false`.
	HttpsOnly interface{}
	// An `identity` block as defined below.
	Identity interface{}
	// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
	Location interface{}
	// The name of the Connection String.
	Name interface{}
	// The name of the resource group in which to create the Function App.
	ResourceGroupName interface{}
	// A `site_config` object as defined below.
	SiteConfig interface{}
	// The connection string of the backend storage account which will be used by this Function App (such as the dashboard, logs).
	StorageConnectionString interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// The runtime version associated with the Function App. Defaults to `~1`.
	Version interface{}
}
