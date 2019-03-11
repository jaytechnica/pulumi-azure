// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an API Management User Assignment to a Group.
 * 
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const exampleUser = pulumi.output(azure.apimanagement.getUser({
 *     apiManagementName: "example-apim",
 *     resourceGroupName: "search-service",
 *     userId: "my-user",
 * }));
 * const exampleGroupUser = new azure.apimanagement.GroupUser("example", {
 *     apiManagementName: exampleUser.apply(exampleUser => exampleUser.apiManagementName),
 *     groupName: "example-group",
 *     resourceGroupName: exampleUser.apply(exampleUser => exampleUser.resourceGroupName),
 *     userId: exampleUser.apply(exampleUser => exampleUser.id),
 * });
 * ```
 */
export class GroupUser extends pulumi.CustomResource {
    /**
     * Get an existing GroupUser resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupUserState, opts?: pulumi.CustomResourceOptions): GroupUser {
        return new GroupUser(name, <any>state, { ...opts, id: id });
    }

    /**
     * The name of the API Management Service. Changing this forces a new resource to be created.
     */
    public readonly apiManagementName: pulumi.Output<string>;
    /**
     * The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.
     */
    public readonly groupName: pulumi.Output<string>;
    /**
     * The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.
     */
    public readonly userId: pulumi.Output<string>;

    /**
     * Create a GroupUser resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupUserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupUserArgs | GroupUserState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: GroupUserState = argsOrState as GroupUserState | undefined;
            inputs["apiManagementName"] = state ? state.apiManagementName : undefined;
            inputs["groupName"] = state ? state.groupName : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["userId"] = state ? state.userId : undefined;
        } else {
            const args = argsOrState as GroupUserArgs | undefined;
            if (!args || args.apiManagementName === undefined) {
                throw new Error("Missing required property 'apiManagementName'");
            }
            if (!args || args.groupName === undefined) {
                throw new Error("Missing required property 'groupName'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.userId === undefined) {
                throw new Error("Missing required property 'userId'");
            }
            inputs["apiManagementName"] = args ? args.apiManagementName : undefined;
            inputs["groupName"] = args ? args.groupName : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["userId"] = args ? args.userId : undefined;
        }
        super("azure:apimanagement/groupUser:GroupUser", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GroupUser resources.
 */
export interface GroupUserState {
    /**
     * The name of the API Management Service. Changing this forces a new resource to be created.
     */
    readonly apiManagementName?: pulumi.Input<string>;
    /**
     * The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.
     */
    readonly groupName?: pulumi.Input<string>;
    /**
     * The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.
     */
    readonly userId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GroupUser resource.
 */
export interface GroupUserArgs {
    /**
     * The name of the API Management Service. Changing this forces a new resource to be created.
     */
    readonly apiManagementName: pulumi.Input<string>;
    /**
     * The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.
     */
    readonly groupName: pulumi.Input<string>;
    /**
     * The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.
     */
    readonly userId: pulumi.Input<string>;
}
