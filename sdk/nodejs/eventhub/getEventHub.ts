// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about an existing EventHub.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const example = azure.eventhub.getEventHub({
 *     name: "search-eventhub",
 *     resourceGroupName: "search-service",
 *     namespaceName: "search-eventhubns",
 * });
 * export const eventhubId = example.then(example => example.id);
 * ```
 */
export function getEventHub(args: GetEventHubArgs, opts?: pulumi.InvokeOptions): Promise<GetEventHubResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azure:eventhub/getEventHub:getEventHub", {
        "name": args.name,
        "namespaceName": args.namespaceName,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

/**
 * A collection of arguments for invoking getEventHub.
 */
export interface GetEventHubArgs {
    /**
     * The name of this EventHub.
     */
    readonly name: string;
    /**
     * The name of the EventHub Namespace where the EventHub exists.
     */
    readonly namespaceName: string;
    /**
     * The name of the Resource Group where the EventHub exists.
     */
    readonly resourceGroupName: string;
}

/**
 * A collection of values returned by getEventHub.
 */
export interface GetEventHubResult {
    readonly name: string;
    readonly namespaceName: string;
    /**
     * The number of partitions in the EventHub.
     */
    readonly partitionCount: number;
    /**
     * The identifiers for the partitions of this EventHub.
     */
    readonly partitionIds: string[];
    readonly resourceGroupName: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
