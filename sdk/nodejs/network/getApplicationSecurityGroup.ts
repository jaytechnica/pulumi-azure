// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Get information about an Application Security Group.
 * 
 * -> **Note:** Application Security Groups are currently in Public Preview on an opt-in basis. [More information, including how you can register for the Preview, and which regions Application Security Groups are available in are available here](https://docs.microsoft.com/en-us/azure/virtual-network/create-network-security-group-preview)
 */
export function getApplicationSecurityGroup(args: GetApplicationSecurityGroupArgs): Promise<GetApplicationSecurityGroupResult> {
    return pulumi.runtime.invoke("azure:network/getApplicationSecurityGroup:getApplicationSecurityGroup", {
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    });
}

/**
 * A collection of arguments for invoking getApplicationSecurityGroup.
 */
export interface GetApplicationSecurityGroupArgs {
    /**
     * The name of the Application Security Group.
     */
    readonly name: pulumi.Input<string>;
    /**
     * The name of the resource group in which the Application Security Group exists.
     */
    readonly resourceGroupName: pulumi.Input<string>;
}

/**
 * A collection of values returned by getApplicationSecurityGroup.
 */
export interface GetApplicationSecurityGroupResult {
    /**
     * The supported Azure location where the Application Security Group exists.
     */
    readonly location: string;
    /**
     * A mapping of tags assigned to the resource.
     */
    readonly tags: {[key: string]: any};
}