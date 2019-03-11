// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an Activity Log Alert within Azure Monitor.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const mainResourceGroup = new azure.core.ResourceGroup("main", {
 *     location: "West US",
 *     name: "example-resources",
 * });
 * const mainActionGroup = new azure.monitoring.ActionGroup("main", {
 *     name: "example-actiongroup",
 *     resourceGroupName: mainResourceGroup.name,
 *     shortName: "p0action",
 *     webhookReceivers: [{
 *         name: "callmyapi",
 *         serviceUri: "http://example.com/alert",
 *     }],
 * });
 * const toMonitor = new azure.storage.Account("to_monitor", {
 *     accountReplicationType: "GRS",
 *     accountTier: "Standard",
 *     location: mainResourceGroup.location,
 *     name: "examplesa",
 *     resourceGroupName: mainResourceGroup.name,
 * });
 * const mainActivityLogAlert = new azure.monitoring.ActivityLogAlert("main", {
 *     actions: [{
 *         actionGroupId: mainActionGroup.id,
 *         webhookProperties: {
 *             from: "terraform",
 *         },
 *     }],
 *     criteria: {
 *         category: "Recommendation",
 *         operationName: "Microsoft.Storage/storageAccounts/write",
 *         resourceId: toMonitor.id,
 *     },
 *     description: "This alert will monitor a specific storage account updates.",
 *     name: "example-activitylogalert",
 *     resourceGroupName: mainResourceGroup.name,
 *     scopes: [mainResourceGroup.id],
 * });
 * ```
 */
export class ActivityLogAlert extends pulumi.CustomResource {
    /**
     * Get an existing ActivityLogAlert resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActivityLogAlertState, opts?: pulumi.CustomResourceOptions): ActivityLogAlert {
        return new ActivityLogAlert(name, <any>state, { ...opts, id: id });
    }

    /**
     * One or more `action` blocks as defined below.
     */
    public readonly actions: pulumi.Output<{ actionGroupId: string, webhookProperties?: {[key: string]: string} }[] | undefined>;
    /**
     * A `criteria` block as defined below.
     */
    public readonly criteria: pulumi.Output<{ caller?: string, category: string, level?: string, operationName?: string, resourceGroup?: string, resourceId?: string, resourceProvider?: string, resourceType?: string, status?: string, subStatus?: string }>;
    /**
     * The description of this activity log alert.
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * Should this Activity Log Alert be enabled? Defaults to `true`.
     */
    public readonly enabled: pulumi.Output<boolean | undefined>;
    /**
     * The name of the activity log alert. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The name of the resource group in which to create the activity log alert instance.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
     */
    public readonly scopes: pulumi.Output<string[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any}>;

    /**
     * Create a ActivityLogAlert resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ActivityLogAlertArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ActivityLogAlertArgs | ActivityLogAlertState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ActivityLogAlertState = argsOrState as ActivityLogAlertState | undefined;
            inputs["actions"] = state ? state.actions : undefined;
            inputs["criteria"] = state ? state.criteria : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["scopes"] = state ? state.scopes : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as ActivityLogAlertArgs | undefined;
            if (!args || args.criteria === undefined) {
                throw new Error("Missing required property 'criteria'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.scopes === undefined) {
                throw new Error("Missing required property 'scopes'");
            }
            inputs["actions"] = args ? args.actions : undefined;
            inputs["criteria"] = args ? args.criteria : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["scopes"] = args ? args.scopes : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        super("azure:monitoring/activityLogAlert:ActivityLogAlert", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ActivityLogAlert resources.
 */
export interface ActivityLogAlertState {
    /**
     * One or more `action` blocks as defined below.
     */
    readonly actions?: pulumi.Input<pulumi.Input<{ actionGroupId: pulumi.Input<string>, webhookProperties?: pulumi.Input<{[key: string]: pulumi.Input<string>}> }>[]>;
    /**
     * A `criteria` block as defined below.
     */
    readonly criteria?: pulumi.Input<{ caller?: pulumi.Input<string>, category: pulumi.Input<string>, level?: pulumi.Input<string>, operationName?: pulumi.Input<string>, resourceGroup?: pulumi.Input<string>, resourceId?: pulumi.Input<string>, resourceProvider?: pulumi.Input<string>, resourceType?: pulumi.Input<string>, status?: pulumi.Input<string>, subStatus?: pulumi.Input<string> }>;
    /**
     * The description of this activity log alert.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Should this Activity Log Alert be enabled? Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the activity log alert. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the activity log alert instance.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
     */
    readonly scopes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a ActivityLogAlert resource.
 */
export interface ActivityLogAlertArgs {
    /**
     * One or more `action` blocks as defined below.
     */
    readonly actions?: pulumi.Input<pulumi.Input<{ actionGroupId: pulumi.Input<string>, webhookProperties?: pulumi.Input<{[key: string]: pulumi.Input<string>}> }>[]>;
    /**
     * A `criteria` block as defined below.
     */
    readonly criteria: pulumi.Input<{ caller?: pulumi.Input<string>, category: pulumi.Input<string>, level?: pulumi.Input<string>, operationName?: pulumi.Input<string>, resourceGroup?: pulumi.Input<string>, resourceId?: pulumi.Input<string>, resourceProvider?: pulumi.Input<string>, resourceType?: pulumi.Input<string>, status?: pulumi.Input<string>, subStatus?: pulumi.Input<string> }>;
    /**
     * The description of this activity log alert.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Should this Activity Log Alert be enabled? Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the activity log alert. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the activity log alert instance.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
     */
    readonly scopes: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
