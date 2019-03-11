// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Firewall Rule for a MySQL Server
 * 
 * ## Example Usage (Single IP Address)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testServer = new azure.mysql.Server("test", {});
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West Europe",
 *     name: "api-rg-pro",
 * });
 * const testFirewallRule = new azure.mysql.FirewallRule("test", {
 *     endIpAddress: "40.112.8.12",
 *     name: "office",
 *     resourceGroupName: testResourceGroup.name,
 *     serverName: testServer.name,
 *     startIpAddress: "40.112.8.12",
 * });
 * ```
 * 
 * ## Example Usage (IP Range)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testServer = new azure.mysql.Server("test", {});
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West Europe",
 *     name: "api-rg-pro",
 * });
 * const testFirewallRule = new azure.mysql.FirewallRule("test", {
 *     endIpAddress: "40.112.255.255",
 *     name: "office",
 *     resourceGroupName: testResourceGroup.name,
 *     serverName: testServer.name,
 *     startIpAddress: "40.112.0.0",
 * });
 * ```
 */
export class FirewallRule extends pulumi.CustomResource {
    /**
     * Get an existing FirewallRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallRuleState, opts?: pulumi.CustomResourceOptions): FirewallRule {
        return new FirewallRule(name, <any>state, { ...opts, id: id });
    }

    /**
     * Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.
     */
    public readonly endIpAddress: pulumi.Output<string>;
    /**
     * Specifies the name of the MySQL Firewall Rule. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * Specifies the name of the MySQL Server. Changing this forces a new resource to be created.
     */
    public readonly serverName: pulumi.Output<string>;
    /**
     * Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.
     */
    public readonly startIpAddress: pulumi.Output<string>;

    /**
     * Create a FirewallRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FirewallRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FirewallRuleArgs | FirewallRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: FirewallRuleState = argsOrState as FirewallRuleState | undefined;
            inputs["endIpAddress"] = state ? state.endIpAddress : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["serverName"] = state ? state.serverName : undefined;
            inputs["startIpAddress"] = state ? state.startIpAddress : undefined;
        } else {
            const args = argsOrState as FirewallRuleArgs | undefined;
            if (!args || args.endIpAddress === undefined) {
                throw new Error("Missing required property 'endIpAddress'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.serverName === undefined) {
                throw new Error("Missing required property 'serverName'");
            }
            if (!args || args.startIpAddress === undefined) {
                throw new Error("Missing required property 'startIpAddress'");
            }
            inputs["endIpAddress"] = args ? args.endIpAddress : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["serverName"] = args ? args.serverName : undefined;
            inputs["startIpAddress"] = args ? args.startIpAddress : undefined;
        }
        super("azure:mysql/firewallRule:FirewallRule", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FirewallRule resources.
 */
export interface FirewallRuleState {
    /**
     * Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.
     */
    readonly endIpAddress?: pulumi.Input<string>;
    /**
     * Specifies the name of the MySQL Firewall Rule. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Specifies the name of the MySQL Server. Changing this forces a new resource to be created.
     */
    readonly serverName?: pulumi.Input<string>;
    /**
     * Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.
     */
    readonly startIpAddress?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FirewallRule resource.
 */
export interface FirewallRuleArgs {
    /**
     * Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.
     */
    readonly endIpAddress: pulumi.Input<string>;
    /**
     * Specifies the name of the MySQL Firewall Rule. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Specifies the name of the MySQL Server. Changing this forces a new resource to be created.
     */
    readonly serverName: pulumi.Input<string>;
    /**
     * Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.
     */
    readonly startIpAddress: pulumi.Input<string>;
}
