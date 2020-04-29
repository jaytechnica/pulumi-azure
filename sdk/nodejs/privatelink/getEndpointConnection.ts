// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to access the connection status information about an existing Private Endpoint Connection.
 * 
 * > **NOTE** Private Endpoint is currently in Public Preview.
 * 
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/private_endpoint_connection.html.markdown.
 */
export function getEndpointConnection(args: GetEndpointConnectionArgs, opts?: pulumi.InvokeOptions): Promise<GetEndpointConnectionResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azure:privatelink/getEndpointConnection:getEndpointConnection", {
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

/**
 * A collection of arguments for invoking getEndpointConnection.
 */
export interface GetEndpointConnectionArgs {
    /**
     * Specifies the Name of the private endpoint.
     */
    readonly name: string;
    /**
     * Specifies the Name of the Resource Group within which the private endpoint exists.
     */
    readonly resourceGroupName: string;
}

/**
 * A collection of values returned by getEndpointConnection.
 */
export interface GetEndpointConnectionResult {
    /**
     * The supported Azure location where the resource exists.
     */
    readonly location: string;
    /**
     * The name of the private endpoint.
     */
    readonly name: string;
    readonly privateServiceConnections: outputs.privatelink.GetEndpointConnectionPrivateServiceConnection[];
    readonly resourceGroupName: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
