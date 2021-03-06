// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to fetch the Host Keys of an existing Function App
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const example = azure.appservice.getFunctionAppHostKeys({
 *     name: "example-function",
 *     resourceGroupName: azurerm_resource_group.example.name,
 * });
 * ```
 *
 * > **Note:** All arguments including the secret value will be stored in the raw state as plain-text, including `defaultFunctionKey` and `masterKey`. [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 */
export function getFunctionAppHostKeys(args: GetFunctionAppHostKeysArgs, opts?: pulumi.InvokeOptions): Promise<GetFunctionAppHostKeysResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azure:appservice/getFunctionAppHostKeys:getFunctionAppHostKeys", {
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

/**
 * A collection of arguments for invoking getFunctionAppHostKeys.
 */
export interface GetFunctionAppHostKeysArgs {
    /**
     * The name of the Function App.
     */
    readonly name: string;
    /**
     * The name of the Resource Group where the Function App exists.
     */
    readonly resourceGroupName: string;
}

/**
 * A collection of values returned by getFunctionAppHostKeys.
 */
export interface GetFunctionAppHostKeysResult {
    /**
     * Function App resource's default function key.
     */
    readonly defaultFunctionKey: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Function App resource's secret key
     *
     * @deprecated This property has been renamed to `primary_key` and will be removed in v3.0 of the provider in support of HashiCorp's inclusive language policy which can be found here: https://discuss.hashicorp.com/t/inclusive-language-changes
     */
    readonly masterKey: string;
    readonly name: string;
    readonly primaryKey: string;
    readonly resourceGroupName: string;
}
