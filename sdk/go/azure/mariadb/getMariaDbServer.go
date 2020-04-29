// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mariadb

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing MariaDB Server.
func GetMariaDbServer(ctx *pulumi.Context, args *GetMariaDbServerArgs, opts ...pulumi.InvokeOption) (*GetMariaDbServerResult, error) {
	var rv GetMariaDbServerResult
	err := ctx.Invoke("azure:mariadb/getMariaDbServer:getMariaDbServer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMariaDbServer.
type GetMariaDbServerArgs struct {
	// The name of the MariaDB Server to retrieve information about.
	Name string `pulumi:"name"`
	// The name of the resource group where the MariaDB Server exists.
	ResourceGroupName string `pulumi:"resourceGroupName"`
}

// A collection of values returned by getMariaDbServer.
type GetMariaDbServerResult struct {
	// The Administrator Login for the MariaDB Server.
	AdministratorLogin string `pulumi:"administratorLogin"`
	// The password associated with the `administratorLogin` for the MariaDB Server.
	AdministratorLoginPassword string `pulumi:"administratorLoginPassword"`
	// The FQDN of the MariaDB Server.
	Fqdn string `pulumi:"fqdn"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The Azure location where the resource exists.
	Location          string `pulumi:"location"`
	Name              string `pulumi:"name"`
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// The SKU Name for this MariaDB Server.
	SkuName string `pulumi:"skuName"`
	// The SSL being enforced on connections.
	SslEnforcement string `pulumi:"sslEnforcement"`
	// A `storageProfile` block as defined below.
	StorageProfiles []GetMariaDbServerStorageProfile `pulumi:"storageProfiles"`
	// A mapping of tags assigned to the resource.
	// ---
	Tags map[string]string `pulumi:"tags"`
	// The version of MariaDB being used.
	Version string `pulumi:"version"`
}
