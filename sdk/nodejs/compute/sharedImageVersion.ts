// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Version of a Shared Image within a Shared Image Gallery.
 * 
 * > **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const existingImage = pulumi.output(azure.compute.getImage({
 *     name: "search-api",
 *     resourceGroupName: "packerimages",
 * }));
 * const existingSharedImage = pulumi.output(azure.compute.getSharedImage({
 *     galleryName: "existing_gallery",
 *     name: "existing-image",
 *     resourceGroupName: "existing-resources",
 * }));
 * const test = new azure.compute.SharedImageVersion("test", {
 *     galleryName: existingSharedImage.apply(existingSharedImage => existingSharedImage.galleryName),
 *     imageName: existingSharedImage.apply(existingSharedImage => existingSharedImage.name),
 *     location: existingSharedImage.apply(existingSharedImage => existingSharedImage.location),
 *     managedImageId: existingImage.apply(existingImage => existingImage.id),
 *     name: "0.0.1",
 *     resourceGroupName: existingSharedImage.apply(existingSharedImage => existingSharedImage.resourceGroupName),
 *     targetRegions: [{
 *         name: existingSharedImage.apply(existingSharedImage => existingSharedImage.location),
 *         regionalReplicaCount: 5,
 *     }],
 * });
 * ```
 */
export class SharedImageVersion extends pulumi.CustomResource {
    /**
     * Get an existing SharedImageVersion resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SharedImageVersionState, opts?: pulumi.CustomResourceOptions): SharedImageVersion {
        return new SharedImageVersion(name, <any>state, { ...opts, id: id });
    }

    /**
     * Should this Image Version be excluded from the `latest` filter? If set to `true` this Image Version won't be returned for the `latest` version. Defaults to `false`.
     */
    public readonly excludeFromLatest: pulumi.Output<boolean | undefined>;
    /**
     * The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.
     */
    public readonly galleryName: pulumi.Output<string>;
    /**
     * The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.
     */
    public readonly imageName: pulumi.Output<string>;
    /**
     * The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
     */
    public readonly location: pulumi.Output<string>;
    /**
     * The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.
     */
    public readonly managedImageId: pulumi.Output<string>;
    /**
     * The version number for this Image Version, such as `1.0.0`. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * A collection of tags which should be applied to this resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any}>;
    /**
     * One or more `target_region` blocks as documented below.
     */
    public readonly targetRegions: pulumi.Output<{ name: string, regionalReplicaCount: number }[]>;

    /**
     * Create a SharedImageVersion resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SharedImageVersionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SharedImageVersionArgs | SharedImageVersionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SharedImageVersionState = argsOrState as SharedImageVersionState | undefined;
            inputs["excludeFromLatest"] = state ? state.excludeFromLatest : undefined;
            inputs["galleryName"] = state ? state.galleryName : undefined;
            inputs["imageName"] = state ? state.imageName : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["managedImageId"] = state ? state.managedImageId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["targetRegions"] = state ? state.targetRegions : undefined;
        } else {
            const args = argsOrState as SharedImageVersionArgs | undefined;
            if (!args || args.galleryName === undefined) {
                throw new Error("Missing required property 'galleryName'");
            }
            if (!args || args.imageName === undefined) {
                throw new Error("Missing required property 'imageName'");
            }
            if (!args || args.location === undefined) {
                throw new Error("Missing required property 'location'");
            }
            if (!args || args.managedImageId === undefined) {
                throw new Error("Missing required property 'managedImageId'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.targetRegions === undefined) {
                throw new Error("Missing required property 'targetRegions'");
            }
            inputs["excludeFromLatest"] = args ? args.excludeFromLatest : undefined;
            inputs["galleryName"] = args ? args.galleryName : undefined;
            inputs["imageName"] = args ? args.imageName : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["managedImageId"] = args ? args.managedImageId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["targetRegions"] = args ? args.targetRegions : undefined;
        }
        super("azure:compute/sharedImageVersion:SharedImageVersion", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SharedImageVersion resources.
 */
export interface SharedImageVersionState {
    /**
     * Should this Image Version be excluded from the `latest` filter? If set to `true` this Image Version won't be returned for the `latest` version. Defaults to `false`.
     */
    readonly excludeFromLatest?: pulumi.Input<boolean>;
    /**
     * The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.
     */
    readonly galleryName?: pulumi.Input<string>;
    /**
     * The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.
     */
    readonly imageName?: pulumi.Input<string>;
    /**
     * The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.
     */
    readonly managedImageId?: pulumi.Input<string>;
    /**
     * The version number for this Image Version, such as `1.0.0`. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * A collection of tags which should be applied to this resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * One or more `target_region` blocks as documented below.
     */
    readonly targetRegions?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, regionalReplicaCount: pulumi.Input<number> }>[]>;
}

/**
 * The set of arguments for constructing a SharedImageVersion resource.
 */
export interface SharedImageVersionArgs {
    /**
     * Should this Image Version be excluded from the `latest` filter? If set to `true` this Image Version won't be returned for the `latest` version. Defaults to `false`.
     */
    readonly excludeFromLatest?: pulumi.Input<boolean>;
    /**
     * The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.
     */
    readonly galleryName: pulumi.Input<string>;
    /**
     * The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.
     */
    readonly imageName: pulumi.Input<string>;
    /**
     * The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
     */
    readonly location: pulumi.Input<string>;
    /**
     * The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.
     */
    readonly managedImageId: pulumi.Input<string>;
    /**
     * The version number for this Image Version, such as `1.0.0`. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A collection of tags which should be applied to this resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * One or more `target_region` blocks as documented below.
     */
    readonly targetRegions: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, regionalReplicaCount: pulumi.Input<number> }>[]>;
}
