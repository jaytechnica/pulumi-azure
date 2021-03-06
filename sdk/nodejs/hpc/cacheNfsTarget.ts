// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a NFS Target within a HPC Cache.
 *
 * > **NOTE:**: By request of the service team the provider no longer automatically registering the `Microsoft.StorageCache` Resource Provider for this resource. To register it you can run `az provider register --namespace 'Microsoft.StorageCache'`.
 */
export class CacheNfsTarget extends pulumi.CustomResource {
    /**
     * Get an existing CacheNfsTarget resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CacheNfsTargetState, opts?: pulumi.CustomResourceOptions): CacheNfsTarget {
        return new CacheNfsTarget(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:hpc/cacheNfsTarget:CacheNfsTarget';

    /**
     * Returns true if the given object is an instance of CacheNfsTarget.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CacheNfsTarget {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CacheNfsTarget.__pulumiType;
    }

    /**
     * The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
     */
    public readonly cacheName!: pulumi.Output<string>;
    /**
     * The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
     */
    public readonly namespaceJunctions!: pulumi.Output<outputs.hpc.CacheNfsTargetNamespaceJunction[]>;
    /**
     * The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
     */
    public readonly targetHostName!: pulumi.Output<string>;
    /**
     * The type of usage of the HPC Cache NFS Target.
     */
    public readonly usageModel!: pulumi.Output<string>;

    /**
     * Create a CacheNfsTarget resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CacheNfsTargetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CacheNfsTargetArgs | CacheNfsTargetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as CacheNfsTargetState | undefined;
            inputs["cacheName"] = state ? state.cacheName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["namespaceJunctions"] = state ? state.namespaceJunctions : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["targetHostName"] = state ? state.targetHostName : undefined;
            inputs["usageModel"] = state ? state.usageModel : undefined;
        } else {
            const args = argsOrState as CacheNfsTargetArgs | undefined;
            if (!args || args.cacheName === undefined) {
                throw new Error("Missing required property 'cacheName'");
            }
            if (!args || args.namespaceJunctions === undefined) {
                throw new Error("Missing required property 'namespaceJunctions'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.targetHostName === undefined) {
                throw new Error("Missing required property 'targetHostName'");
            }
            if (!args || args.usageModel === undefined) {
                throw new Error("Missing required property 'usageModel'");
            }
            inputs["cacheName"] = args ? args.cacheName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["namespaceJunctions"] = args ? args.namespaceJunctions : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["targetHostName"] = args ? args.targetHostName : undefined;
            inputs["usageModel"] = args ? args.usageModel : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(CacheNfsTarget.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CacheNfsTarget resources.
 */
export interface CacheNfsTargetState {
    /**
     * The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
     */
    readonly cacheName?: pulumi.Input<string>;
    /**
     * The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
     */
    readonly namespaceJunctions?: pulumi.Input<pulumi.Input<inputs.hpc.CacheNfsTargetNamespaceJunction>[]>;
    /**
     * The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
     */
    readonly targetHostName?: pulumi.Input<string>;
    /**
     * The type of usage of the HPC Cache NFS Target.
     */
    readonly usageModel?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CacheNfsTarget resource.
 */
export interface CacheNfsTargetArgs {
    /**
     * The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.
     */
    readonly cacheName: pulumi.Input<string>;
    /**
     * The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Can be specified multiple times to define multiple `namespaceJunction`. Each `namespaceJuntion` block supports fields documented below.
     */
    readonly namespaceJunctions: pulumi.Input<pulumi.Input<inputs.hpc.CacheNfsTargetNamespaceJunction>[]>;
    /**
     * The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.
     */
    readonly targetHostName: pulumi.Input<string>;
    /**
     * The type of usage of the HPC Cache NFS Target.
     */
    readonly usageModel: pulumi.Input<string>;
}
