// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.
 * 
 * > **NOTE:** This resource has been deprecated in favour of the `azurerm_monitor_autoscale_setting` resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West US",
 *     name: "autoscalingTest",
 * });
 * const testScaleSet = new azure.compute.ScaleSet("test", {});
 * const testSetting = new azure.autoscale.Setting("test", {
 *     location: testResourceGroup.location,
 *     name: "myAutoscaleSetting",
 *     notification: {
 *         email: {
 *             customEmails: ["admin@contoso.com"],
 *             sendToSubscriptionAdministrator: true,
 *             sendToSubscriptionCoAdministrator: true,
 *         },
 *     },
 *     profiles: [{
 *         capacity: {
 *             default: 1,
 *             maximum: 10,
 *             minimum: 1,
 *         },
 *         name: "defaultProfile",
 *         rules: [
 *             {
 *                 metricTrigger: {
 *                     metricName: "Percentage CPU",
 *                     metricResourceId: testScaleSet.id,
 *                     operator: "GreaterThan",
 *                     statistic: "Average",
 *                     threshold: 75,
 *                     timeAggregation: "Average",
 *                     timeGrain: "PT1M",
 *                     timeWindow: "PT5M",
 *                 },
 *                 scaleAction: {
 *                     cooldown: "PT1M",
 *                     direction: "Increase",
 *                     type: "ChangeCount",
 *                     value: 1,
 *                 },
 *             },
 *             {
 *                 metricTrigger: {
 *                     metricName: "Percentage CPU",
 *                     metricResourceId: testScaleSet.id,
 *                     operator: "LessThan",
 *                     statistic: "Average",
 *                     threshold: 25,
 *                     timeAggregation: "Average",
 *                     timeGrain: "PT1M",
 *                     timeWindow: "PT5M",
 *                 },
 *                 scaleAction: {
 *                     cooldown: "PT1M",
 *                     direction: "Decrease",
 *                     type: "ChangeCount",
 *                     value: 1,
 *                 },
 *             },
 *         ],
 *     }],
 *     resourceGroupName: testResourceGroup.name,
 *     targetResourceId: testScaleSet.id,
 * });
 * ```
 * 
 * ## Example Usage (repeating on weekends)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West US",
 *     name: "autoscalingTest",
 * });
 * const testScaleSet = new azure.compute.ScaleSet("test", {});
 * const testSetting = new azure.autoscale.Setting("test", {
 *     location: testResourceGroup.location,
 *     name: "myAutoscaleSetting",
 *     notification: {
 *         email: {
 *             customEmails: ["admin@contoso.com"],
 *             sendToSubscriptionAdministrator: true,
 *             sendToSubscriptionCoAdministrator: true,
 *         },
 *     },
 *     profiles: [{
 *         capacity: {
 *             default: 1,
 *             maximum: 10,
 *             minimum: 1,
 *         },
 *         name: "Weekends",
 *         recurrence: {
 *             days: [
 *                 "Saturday",
 *                 "Sunday",
 *             ],
 *             frequency: "Week",
 *             hours: 12,
 *             minutes: 0,
 *             timezone: "Pacific Standard Time",
 *         },
 *         rules: [
 *             {
 *                 metricTrigger: {
 *                     metricName: "Percentage CPU",
 *                     metricResourceId: testScaleSet.id,
 *                     operator: "GreaterThan",
 *                     statistic: "Average",
 *                     threshold: 90,
 *                     timeAggregation: "Average",
 *                     timeGrain: "PT1M",
 *                     timeWindow: "PT5M",
 *                 },
 *                 scaleAction: {
 *                     cooldown: "PT1M",
 *                     direction: "Increase",
 *                     type: "ChangeCount",
 *                     value: 2,
 *                 },
 *             },
 *             {
 *                 metricTrigger: {
 *                     metricName: "Percentage CPU",
 *                     metricResourceId: testScaleSet.id,
 *                     operator: "LessThan",
 *                     statistic: "Average",
 *                     threshold: 10,
 *                     timeAggregation: "Average",
 *                     timeGrain: "PT1M",
 *                     timeWindow: "PT5M",
 *                 },
 *                 scaleAction: {
 *                     cooldown: "PT1M",
 *                     direction: "Decrease",
 *                     type: "ChangeCount",
 *                     value: 2,
 *                 },
 *             },
 *         ],
 *     }],
 *     resourceGroupName: testResourceGroup.name,
 *     targetResourceId: testScaleSet.id,
 * });
 * ```
 * 
 * ## Example Usage (for fixed dates)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West US",
 *     name: "autoscalingTest",
 * });
 * const testScaleSet = new azure.compute.ScaleSet("test", {});
 * const testSetting = new azure.autoscale.Setting("test", {
 *     enabled: true,
 *     location: testResourceGroup.location,
 *     name: "myAutoscaleSetting",
 *     notification: {
 *         email: {
 *             customEmails: ["admin@contoso.com"],
 *             sendToSubscriptionAdministrator: true,
 *             sendToSubscriptionCoAdministrator: true,
 *         },
 *     },
 *     profiles: [{
 *         capacity: {
 *             default: 1,
 *             maximum: 10,
 *             minimum: 1,
 *         },
 *         fixedDate: {
 *             end: "2020-07-31T23:59:59Z",
 *             start: "2020-07-01T00:00:00Z",
 *             timezone: "Pacific Standard Time",
 *         },
 *         name: "forJuly",
 *         rules: [
 *             {
 *                 metricTrigger: {
 *                     metricName: "Percentage CPU",
 *                     metricResourceId: testScaleSet.id,
 *                     operator: "GreaterThan",
 *                     statistic: "Average",
 *                     threshold: 90,
 *                     timeAggregation: "Average",
 *                     timeGrain: "PT1M",
 *                     timeWindow: "PT5M",
 *                 },
 *                 scaleAction: {
 *                     cooldown: "PT1M",
 *                     direction: "Increase",
 *                     type: "ChangeCount",
 *                     value: 2,
 *                 },
 *             },
 *             {
 *                 metricTrigger: {
 *                     metricName: "Percentage CPU",
 *                     metricResourceId: testScaleSet.id,
 *                     operator: "LessThan",
 *                     statistic: "Average",
 *                     threshold: 10,
 *                     timeAggregation: "Average",
 *                     timeGrain: "PT1M",
 *                     timeWindow: "PT5M",
 *                 },
 *                 scaleAction: {
 *                     cooldown: "PT1M",
 *                     direction: "Decrease",
 *                     type: "ChangeCount",
 *                     value: 2,
 *                 },
 *             },
 *         ],
 *     }],
 *     resourceGroupName: testResourceGroup.name,
 *     targetResourceId: testScaleSet.id,
 * });
 * ```
 */
export class Setting extends pulumi.CustomResource {
    /**
     * Get an existing Setting resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SettingState, opts?: pulumi.CustomResourceOptions): Setting {
        return new Setting(name, <any>state, { ...opts, id: id });
    }

    /**
     * Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
     */
    public readonly enabled: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
     */
    public readonly location: pulumi.Output<string>;
    /**
     * The name of the AutoScale Setting. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Specifies a `notification` block as defined below.
     */
    public readonly notification: pulumi.Output<{ email?: { customEmails?: string[], sendToSubscriptionAdministrator?: boolean, sendToSubscriptionCoAdministrator?: boolean }, webhooks?: { properties?: {[key: string]: any}, serviceUri: string }[] } | undefined>;
    /**
     * Specifies one or more (up to 20) `profile` blocks as defined below.
     */
    public readonly profiles: pulumi.Output<{ capacity: { default: number, maximum: number, minimum: number }, fixedDate?: { end: string, start: string, timezone?: string }, name: string, recurrence?: { days: string[], hours: number, minutes: number, timezone?: string }, rules?: { metricTrigger: { metricName: string, metricResourceId: string, operator: string, statistic: string, threshold: number, timeAggregation: string, timeGrain: string, timeWindow: string }, scaleAction: { cooldown: string, direction: string, type: string, value: number } }[] }[]>;
    /**
     * The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any}>;
    /**
     * Specifies the resource ID of the resource that the autoscale setting should be added to.
     */
    public readonly targetResourceId: pulumi.Output<string>;

    /**
     * Create a Setting resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SettingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SettingArgs | SettingState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SettingState = argsOrState as SettingState | undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["notification"] = state ? state.notification : undefined;
            inputs["profiles"] = state ? state.profiles : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["targetResourceId"] = state ? state.targetResourceId : undefined;
        } else {
            const args = argsOrState as SettingArgs | undefined;
            if (!args || args.location === undefined) {
                throw new Error("Missing required property 'location'");
            }
            if (!args || args.profiles === undefined) {
                throw new Error("Missing required property 'profiles'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.targetResourceId === undefined) {
                throw new Error("Missing required property 'targetResourceId'");
            }
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["notification"] = args ? args.notification : undefined;
            inputs["profiles"] = args ? args.profiles : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["targetResourceId"] = args ? args.targetResourceId : undefined;
        }
        super("azure:autoscale/setting:Setting", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Setting resources.
 */
export interface SettingState {
    /**
     * Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The name of the AutoScale Setting. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies a `notification` block as defined below.
     */
    readonly notification?: pulumi.Input<{ email?: pulumi.Input<{ customEmails?: pulumi.Input<pulumi.Input<string>[]>, sendToSubscriptionAdministrator?: pulumi.Input<boolean>, sendToSubscriptionCoAdministrator?: pulumi.Input<boolean> }>, webhooks?: pulumi.Input<pulumi.Input<{ properties?: pulumi.Input<{[key: string]: any}>, serviceUri: pulumi.Input<string> }>[]> }>;
    /**
     * Specifies one or more (up to 20) `profile` blocks as defined below.
     */
    readonly profiles?: pulumi.Input<pulumi.Input<{ capacity: pulumi.Input<{ default: pulumi.Input<number>, maximum: pulumi.Input<number>, minimum: pulumi.Input<number> }>, fixedDate?: pulumi.Input<{ end: pulumi.Input<string>, start: pulumi.Input<string>, timezone?: pulumi.Input<string> }>, name: pulumi.Input<string>, recurrence?: pulumi.Input<{ days: pulumi.Input<pulumi.Input<string>[]>, hours: pulumi.Input<number>, minutes: pulumi.Input<number>, timezone?: pulumi.Input<string> }>, rules?: pulumi.Input<pulumi.Input<{ metricTrigger: pulumi.Input<{ metricName: pulumi.Input<string>, metricResourceId: pulumi.Input<string>, operator: pulumi.Input<string>, statistic: pulumi.Input<string>, threshold: pulumi.Input<number>, timeAggregation: pulumi.Input<string>, timeGrain: pulumi.Input<string>, timeWindow: pulumi.Input<string> }>, scaleAction: pulumi.Input<{ cooldown: pulumi.Input<string>, direction: pulumi.Input<string>, type: pulumi.Input<string>, value: pulumi.Input<number> }> }>[]> }>[]>;
    /**
     * The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Specifies the resource ID of the resource that the autoscale setting should be added to.
     */
    readonly targetResourceId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Setting resource.
 */
export interface SettingArgs {
    /**
     * Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
     */
    readonly location: pulumi.Input<string>;
    /**
     * The name of the AutoScale Setting. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies a `notification` block as defined below.
     */
    readonly notification?: pulumi.Input<{ email?: pulumi.Input<{ customEmails?: pulumi.Input<pulumi.Input<string>[]>, sendToSubscriptionAdministrator?: pulumi.Input<boolean>, sendToSubscriptionCoAdministrator?: pulumi.Input<boolean> }>, webhooks?: pulumi.Input<pulumi.Input<{ properties?: pulumi.Input<{[key: string]: any}>, serviceUri: pulumi.Input<string> }>[]> }>;
    /**
     * Specifies one or more (up to 20) `profile` blocks as defined below.
     */
    readonly profiles: pulumi.Input<pulumi.Input<{ capacity: pulumi.Input<{ default: pulumi.Input<number>, maximum: pulumi.Input<number>, minimum: pulumi.Input<number> }>, fixedDate?: pulumi.Input<{ end: pulumi.Input<string>, start: pulumi.Input<string>, timezone?: pulumi.Input<string> }>, name: pulumi.Input<string>, recurrence?: pulumi.Input<{ days: pulumi.Input<pulumi.Input<string>[]>, hours: pulumi.Input<number>, minutes: pulumi.Input<number>, timezone?: pulumi.Input<string> }>, rules?: pulumi.Input<pulumi.Input<{ metricTrigger: pulumi.Input<{ metricName: pulumi.Input<string>, metricResourceId: pulumi.Input<string>, operator: pulumi.Input<string>, statistic: pulumi.Input<string>, threshold: pulumi.Input<number>, timeAggregation: pulumi.Input<string>, timeGrain: pulumi.Input<string>, timeWindow: pulumi.Input<string> }>, scaleAction: pulumi.Input<{ cooldown: pulumi.Input<string>, direction: pulumi.Input<string>, type: pulumi.Input<string>, value: pulumi.Input<number> }> }>[]> }>[]>;
    /**
     * The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Specifies the resource ID of the resource that the autoscale setting should be added to.
     */
    readonly targetResourceId: pulumi.Input<string>;
}
