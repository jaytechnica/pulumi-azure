// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a [metric-based alert rule](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal) in Azure Monitor.
 * 
 * ## Example Usage (CPU Percentage of a virtual machine)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const test = new azure.monitoring.MetricAlertRule("test", {
 *     aggregation: "Average",
 *     description: "An alert rule to watch the metric Percentage CPU",
 *     emailAction: {
 *         customEmails: ["some.user@example.com"],
 *         sendToServiceOwners: false,
 *     },
 *     enabled: true,
 *     location: azurerm_resource_group_test.location,
 *     metricName: "Percentage CPU",
 *     name: azurerm_virtual_machine_test.name.apply(name => `${name}-cpu`),
 *     operator: "GreaterThan",
 *     period: "PT5M",
 *     resourceGroupName: azurerm_resource_group_test.name,
 *     resourceId: azurerm_virtual_machine_test.id,
 *     threshold: 75,
 *     webhookAction: {
 *         properties: {
 *             acceptance_test: "true",
 *             severity: "incredible",
 *         },
 *         serviceUri: "https://example.com/some-url",
 *     },
 * });
 * ```
 * 
 * ## Example Usage (Storage usage of a SQL Database)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const test = new azure.monitoring.MetricAlertRule("test", {
 *     aggregation: "Maximum",
 *     description: "An alert rule to watch the metric Storage",
 *     emailAction: {
 *         customEmails: ["some.user@example.com"],
 *         sendToServiceOwners: false,
 *     },
 *     enabled: true,
 *     location: azurerm_resource_group_test.location,
 *     metricName: "storage",
 *     name: azurerm_sql_database_test.name.apply(name => `${name}-storage`),
 *     operator: "GreaterThan",
 *     period: "PT10M",
 *     resourceGroupName: azurerm_resource_group_test.name,
 *     resourceId: azurerm_sql_database_test.id,
 *     threshold: 1073741824,
 *     webhookAction: {
 *         properties: {
 *             acceptance_test: "true",
 *             severity: "incredible",
 *         },
 *         serviceUri: "https://example.com/some-url",
 *     },
 * });
 * ```
 */
export class MetricAlertRule extends pulumi.CustomResource {
    /**
     * Get an existing MetricAlertRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MetricAlertRuleState, opts?: pulumi.CustomResourceOptions): MetricAlertRule {
        return new MetricAlertRule(name, <any>state, { ...opts, id: id });
    }

    /**
     * Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.
     */
    public readonly aggregation: pulumi.Output<string>;
    /**
     * A verbose description of the alert rule that will be included in the alert email.
     */
    public readonly description: pulumi.Output<string>;
    /**
     * A `email_action` block as defined below.
     */
    public readonly emailAction: pulumi.Output<{ customEmails: string[], sendToServiceOwners: boolean }>;
    /**
     * If `true`, the alert rule is enabled. Defaults to `true`.
     */
    public readonly enabled: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
     */
    public readonly location: pulumi.Output<string>;
    /**
     * The metric that defines what the rule monitors.
     */
    public readonly metricName: pulumi.Output<string>;
    /**
     * Specifies the name of the alert rule. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.
     */
    public readonly operator: pulumi.Output<string>;
    /**
     * The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.
     */
    public readonly period: pulumi.Output<string>;
    /**
     * The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * The ID of the resource monitored by the alert rule.
     */
    public readonly resourceId: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource. Changing this forces a new resource to be created.
     */
    public readonly tags: pulumi.Output<{[key: string]: any}>;
    /**
     * The threshold value that activates the alert.
     */
    public readonly threshold: pulumi.Output<number>;
    /**
     * A `webhook_action` block as defined below.
     */
    public readonly webhookAction: pulumi.Output<{ properties: {[key: string]: string}, serviceUri: string }>;

    /**
     * Create a MetricAlertRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MetricAlertRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MetricAlertRuleArgs | MetricAlertRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: MetricAlertRuleState = argsOrState as MetricAlertRuleState | undefined;
            inputs["aggregation"] = state ? state.aggregation : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["emailAction"] = state ? state.emailAction : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["metricName"] = state ? state.metricName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["operator"] = state ? state.operator : undefined;
            inputs["period"] = state ? state.period : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["resourceId"] = state ? state.resourceId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["threshold"] = state ? state.threshold : undefined;
            inputs["webhookAction"] = state ? state.webhookAction : undefined;
        } else {
            const args = argsOrState as MetricAlertRuleArgs | undefined;
            if (!args || args.aggregation === undefined) {
                throw new Error("Missing required property 'aggregation'");
            }
            if (!args || args.location === undefined) {
                throw new Error("Missing required property 'location'");
            }
            if (!args || args.metricName === undefined) {
                throw new Error("Missing required property 'metricName'");
            }
            if (!args || args.operator === undefined) {
                throw new Error("Missing required property 'operator'");
            }
            if (!args || args.period === undefined) {
                throw new Error("Missing required property 'period'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.resourceId === undefined) {
                throw new Error("Missing required property 'resourceId'");
            }
            if (!args || args.threshold === undefined) {
                throw new Error("Missing required property 'threshold'");
            }
            inputs["aggregation"] = args ? args.aggregation : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["emailAction"] = args ? args.emailAction : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["metricName"] = args ? args.metricName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["operator"] = args ? args.operator : undefined;
            inputs["period"] = args ? args.period : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["resourceId"] = args ? args.resourceId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["threshold"] = args ? args.threshold : undefined;
            inputs["webhookAction"] = args ? args.webhookAction : undefined;
        }
        super("azure:monitoring/metricAlertRule:MetricAlertRule", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MetricAlertRule resources.
 */
export interface MetricAlertRuleState {
    /**
     * Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.
     */
    readonly aggregation?: pulumi.Input<string>;
    /**
     * A verbose description of the alert rule that will be included in the alert email.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A `email_action` block as defined below.
     */
    readonly emailAction?: pulumi.Input<{ customEmails?: pulumi.Input<pulumi.Input<string>[]>, sendToServiceOwners?: pulumi.Input<boolean> }>;
    /**
     * If `true`, the alert rule is enabled. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The metric that defines what the rule monitors.
     */
    readonly metricName?: pulumi.Input<string>;
    /**
     * Specifies the name of the alert rule. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.
     */
    readonly operator?: pulumi.Input<string>;
    /**
     * The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.
     */
    readonly period?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The ID of the resource monitored by the alert rule.
     */
    readonly resourceId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource. Changing this forces a new resource to be created.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The threshold value that activates the alert.
     */
    readonly threshold?: pulumi.Input<number>;
    /**
     * A `webhook_action` block as defined below.
     */
    readonly webhookAction?: pulumi.Input<{ properties?: pulumi.Input<{[key: string]: pulumi.Input<string>}>, serviceUri: pulumi.Input<string> }>;
}

/**
 * The set of arguments for constructing a MetricAlertRule resource.
 */
export interface MetricAlertRuleArgs {
    /**
     * Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.
     */
    readonly aggregation: pulumi.Input<string>;
    /**
     * A verbose description of the alert rule that will be included in the alert email.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A `email_action` block as defined below.
     */
    readonly emailAction?: pulumi.Input<{ customEmails?: pulumi.Input<pulumi.Input<string>[]>, sendToServiceOwners?: pulumi.Input<boolean> }>;
    /**
     * If `true`, the alert rule is enabled. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
     */
    readonly location: pulumi.Input<string>;
    /**
     * The metric that defines what the rule monitors.
     */
    readonly metricName: pulumi.Input<string>;
    /**
     * Specifies the name of the alert rule. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.
     */
    readonly operator: pulumi.Input<string>;
    /**
     * The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.
     */
    readonly period: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * The ID of the resource monitored by the alert rule.
     */
    readonly resourceId: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource. Changing this forces a new resource to be created.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The threshold value that activates the alert.
     */
    readonly threshold: pulumi.Input<number>;
    /**
     * A `webhook_action` block as defined below.
     */
    readonly webhookAction?: pulumi.Input<{ properties?: pulumi.Input<{[key: string]: pulumi.Input<string>}>, serviceUri: pulumi.Input<string> }>;
}
