// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manage an Azure Storage File Share.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "westus",
 *     name: "azuretest",
 * });
 * const testAccount = new azure.storage.Account("test", {
 *     accountReplicationType: "LRS",
 *     accountTier: "Standard",
 *     location: "westus",
 *     name: "azureteststorage",
 *     resourceGroupName: testResourceGroup.name,
 * });
 * const testshare = new azure.storage.Share("testshare", {
 *     name: "sharename",
 *     quota: 50,
 *     resourceGroupName: testResourceGroup.name,
 *     storageAccountName: testAccount.name,
 * });
 * ```
 */
export class Share extends pulumi.CustomResource {
    /**
     * Get an existing Share resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareState, opts?: pulumi.CustomResourceOptions): Share {
        return new Share(name, <any>state, { ...opts, id: id });
    }

    /**
     * The name of the share. Must be unique within the storage account where the share is located.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.
     */
    public readonly quota: pulumi.Output<number | undefined>;
    /**
     * The name of the resource group in which to
     * create the share. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * Specifies the storage account in which to create the share.
     * Changing this forces a new resource to be created.
     */
    public readonly storageAccountName: pulumi.Output<string>;
    /**
     * The URL of the share
     */
    public /*out*/ readonly url: pulumi.Output<string>;

    /**
     * Create a Share resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ShareArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ShareArgs | ShareState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ShareState = argsOrState as ShareState | undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["quota"] = state ? state.quota : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["storageAccountName"] = state ? state.storageAccountName : undefined;
            inputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as ShareArgs | undefined;
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.storageAccountName === undefined) {
                throw new Error("Missing required property 'storageAccountName'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["quota"] = args ? args.quota : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["storageAccountName"] = args ? args.storageAccountName : undefined;
            inputs["url"] = undefined /*out*/;
        }
        super("azure:storage/share:Share", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Share resources.
 */
export interface ShareState {
    /**
     * The name of the share. Must be unique within the storage account where the share is located.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.
     */
    readonly quota?: pulumi.Input<number>;
    /**
     * The name of the resource group in which to
     * create the share. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Specifies the storage account in which to create the share.
     * Changing this forces a new resource to be created.
     */
    readonly storageAccountName?: pulumi.Input<string>;
    /**
     * The URL of the share
     */
    readonly url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Share resource.
 */
export interface ShareArgs {
    /**
     * The name of the share. Must be unique within the storage account where the share is located.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.
     */
    readonly quota?: pulumi.Input<number>;
    /**
     * The name of the resource group in which to
     * create the share. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Specifies the storage account in which to create the share.
     * Changing this forces a new resource to be created.
     */
    readonly storageAccountName: pulumi.Input<string>;
}
