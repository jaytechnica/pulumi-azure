// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages an AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.
 * 
 * > **NOTE:** This resource has been deprecated in favour of the `azure.monitoring.AutoscaleSetting` resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.
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
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/autoscale_setting.html.markdown.
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

    /** @internal */
    public static readonly __pulumiType = 'azure:autoscale/setting:Setting';

    /**
     * Returns true if the given object is an instance of Setting.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Setting {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Setting.__pulumiType;
    }

    /**
     * Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * The name of the AutoScale Setting. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies a `notification` block as defined below.
     */
    public readonly notification!: pulumi.Output<outputs.autoscale.SettingNotification | undefined>;
    /**
     * Specifies one or more (up to 20) `profile` blocks as defined below.
     */
    public readonly profiles!: pulumi.Output<outputs.autoscale.SettingProfile[]>;
    /**
     * The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any}>;
    /**
     * Specifies the resource ID of the resource that the autoscale setting should be added to.
     */
    public readonly targetResourceId!: pulumi.Output<string>;

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
            const state = argsOrState as SettingState | undefined;
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
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Setting.__pulumiType, name, inputs, opts);
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
    readonly notification?: pulumi.Input<inputs.autoscale.SettingNotification>;
    /**
     * Specifies one or more (up to 20) `profile` blocks as defined below.
     */
    readonly profiles?: pulumi.Input<pulumi.Input<inputs.autoscale.SettingProfile>[]>;
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
    readonly location?: pulumi.Input<string>;
    /**
     * The name of the AutoScale Setting. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies a `notification` block as defined below.
     */
    readonly notification?: pulumi.Input<inputs.autoscale.SettingNotification>;
    /**
     * Specifies one or more (up to 20) `profile` blocks as defined below.
     */
    readonly profiles: pulumi.Input<pulumi.Input<inputs.autoscale.SettingProfile>[]>;
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
