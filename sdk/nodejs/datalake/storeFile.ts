// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manage a Azure Data Lake Store File.
 * 
 * > **Note:** If you want to change the data in the remote file without changing the `local_file_path`, then 
 * taint the resource so the `azurerm_data_lake_store_file` gets recreated with the new data.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const exampleResourceGroup = new azure.core.ResourceGroup("example", {
 *     location: "northeurope",
 *     name: "example",
 * });
 * const exampleStore = new azure.datalake.Store("example", {
 *     location: exampleResourceGroup.location,
 *     name: "consumptiondatalake",
 *     resourceGroupName: exampleResourceGroup.name,
 * });
 * const exampleStoreFile = new azure.datalake.StoreFile("example", {
 *     localFilePath: "/path/to/local/file",
 *     remoteFilePath: "/path/created/for/remote/file",
 *     resourceGroupName: exampleResourceGroup.name,
 * });
 * ```
 */
export class StoreFile extends pulumi.CustomResource {
    /**
     * Get an existing StoreFile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StoreFileState, opts?: pulumi.CustomResourceOptions): StoreFile {
        return new StoreFile(name, <any>state, { ...opts, id: id });
    }

    /**
     * Specifies the name of the Data Lake Store for which the File should created.
     */
    public readonly accountName: pulumi.Output<string>;
    /**
     * The path to the local file to be added to the Data Lake Store.
     */
    public readonly localFilePath: pulumi.Output<string>;
    /**
     * The path created for the file on the Data Lake Store.
     */
    public readonly remoteFilePath: pulumi.Output<string>;

    /**
     * Create a StoreFile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StoreFileArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StoreFileArgs | StoreFileState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: StoreFileState = argsOrState as StoreFileState | undefined;
            inputs["accountName"] = state ? state.accountName : undefined;
            inputs["localFilePath"] = state ? state.localFilePath : undefined;
            inputs["remoteFilePath"] = state ? state.remoteFilePath : undefined;
        } else {
            const args = argsOrState as StoreFileArgs | undefined;
            if (!args || args.accountName === undefined) {
                throw new Error("Missing required property 'accountName'");
            }
            if (!args || args.localFilePath === undefined) {
                throw new Error("Missing required property 'localFilePath'");
            }
            if (!args || args.remoteFilePath === undefined) {
                throw new Error("Missing required property 'remoteFilePath'");
            }
            inputs["accountName"] = args ? args.accountName : undefined;
            inputs["localFilePath"] = args ? args.localFilePath : undefined;
            inputs["remoteFilePath"] = args ? args.remoteFilePath : undefined;
        }
        super("azure:datalake/storeFile:StoreFile", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering StoreFile resources.
 */
export interface StoreFileState {
    /**
     * Specifies the name of the Data Lake Store for which the File should created.
     */
    readonly accountName?: pulumi.Input<string>;
    /**
     * The path to the local file to be added to the Data Lake Store.
     */
    readonly localFilePath?: pulumi.Input<string>;
    /**
     * The path created for the file on the Data Lake Store.
     */
    readonly remoteFilePath?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a StoreFile resource.
 */
export interface StoreFileArgs {
    /**
     * Specifies the name of the Data Lake Store for which the File should created.
     */
    readonly accountName: pulumi.Input<string>;
    /**
     * The path to the local file to be added to the Data Lake Store.
     */
    readonly localFilePath: pulumi.Input<string>;
    /**
     * The path created for the file on the Data Lake Store.
     */
    readonly remoteFilePath: pulumi.Input<string>;
}
