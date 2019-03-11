// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Enables you to manage DNS AAAA Records within Azure DNS.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West US",
 *     name: "acceptanceTestResourceGroup1",
 * });
 * const testZone = new azure.dns.Zone("test", {
 *     name: "mydomain.com",
 *     resourceGroupName: testResourceGroup.name,
 * });
 * const testAaaaRecord = new azure.dns.AaaaRecord("test", {
 *     name: "test",
 *     records: ["2607:f8b0:4009:1803::1005"],
 *     resourceGroupName: testResourceGroup.name,
 *     ttl: 300,
 *     zoneName: testZone.name,
 * });
 * ```
 */
export class AaaaRecord extends pulumi.CustomResource {
    /**
     * Get an existing AaaaRecord resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AaaaRecordState, opts?: pulumi.CustomResourceOptions): AaaaRecord {
        return new AaaaRecord(name, <any>state, { ...opts, id: id });
    }

    /**
     * The name of the DNS AAAA Record.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * List of IPv6 Addresses.
     */
    public readonly records: pulumi.Output<string[]>;
    /**
     * Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any}>;
    public readonly ttl: pulumi.Output<number>;
    /**
     * Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
     */
    public readonly zoneName: pulumi.Output<string>;

    /**
     * Create a AaaaRecord resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AaaaRecordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AaaaRecordArgs | AaaaRecordState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: AaaaRecordState = argsOrState as AaaaRecordState | undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["records"] = state ? state.records : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["ttl"] = state ? state.ttl : undefined;
            inputs["zoneName"] = state ? state.zoneName : undefined;
        } else {
            const args = argsOrState as AaaaRecordArgs | undefined;
            if (!args || args.records === undefined) {
                throw new Error("Missing required property 'records'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.ttl === undefined) {
                throw new Error("Missing required property 'ttl'");
            }
            if (!args || args.zoneName === undefined) {
                throw new Error("Missing required property 'zoneName'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["records"] = args ? args.records : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["ttl"] = args ? args.ttl : undefined;
            inputs["zoneName"] = args ? args.zoneName : undefined;
        }
        super("azure:dns/aaaaRecord:AaaaRecord", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AaaaRecord resources.
 */
export interface AaaaRecordState {
    /**
     * The name of the DNS AAAA Record.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * List of IPv6 Addresses.
     */
    readonly records?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    readonly ttl?: pulumi.Input<number>;
    /**
     * Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
     */
    readonly zoneName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AaaaRecord resource.
 */
export interface AaaaRecordArgs {
    /**
     * The name of the DNS AAAA Record.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * List of IPv6 Addresses.
     */
    readonly records: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    readonly ttl: pulumi.Input<number>;
    /**
     * Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
     */
    readonly zoneName: pulumi.Input<string>;
}
