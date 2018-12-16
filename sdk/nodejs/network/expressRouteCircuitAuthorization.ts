// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an ExpressRoute Circuit Authorization.
 */
export class ExpressRouteCircuitAuthorization extends pulumi.CustomResource {
    /**
     * Get an existing ExpressRouteCircuitAuthorization resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExpressRouteCircuitAuthorizationState, opts?: pulumi.CustomResourceOptions): ExpressRouteCircuitAuthorization {
        return new ExpressRouteCircuitAuthorization(name, <any>state, { ...opts, id: id });
    }

    /**
     * The Authorization Key.
     */
    public /*out*/ readonly authorizationKey: pulumi.Output<string>;
    /**
     * The authorization use status.
     */
    public /*out*/ readonly authorizationUseStatus: pulumi.Output<string>;
    /**
     * The name of the Express Route Circuit in which to create the Authorization.
     */
    public readonly expressRouteCircuitName: pulumi.Output<string>;
    /**
     * The name of the ExpressRoute circuit. Changing this forces a
     * new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The name of the resource group in which to
     * create the ExpressRoute circuit. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;

    /**
     * Create a ExpressRouteCircuitAuthorization resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ExpressRouteCircuitAuthorizationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ExpressRouteCircuitAuthorizationArgs | ExpressRouteCircuitAuthorizationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ExpressRouteCircuitAuthorizationState = argsOrState as ExpressRouteCircuitAuthorizationState | undefined;
            inputs["authorizationKey"] = state ? state.authorizationKey : undefined;
            inputs["authorizationUseStatus"] = state ? state.authorizationUseStatus : undefined;
            inputs["expressRouteCircuitName"] = state ? state.expressRouteCircuitName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
        } else {
            const args = argsOrState as ExpressRouteCircuitAuthorizationArgs | undefined;
            if (!args || args.expressRouteCircuitName === undefined) {
                throw new Error("Missing required property 'expressRouteCircuitName'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            inputs["expressRouteCircuitName"] = args ? args.expressRouteCircuitName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["authorizationKey"] = undefined /*out*/;
            inputs["authorizationUseStatus"] = undefined /*out*/;
        }
        super("azure:network/expressRouteCircuitAuthorization:ExpressRouteCircuitAuthorization", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ExpressRouteCircuitAuthorization resources.
 */
export interface ExpressRouteCircuitAuthorizationState {
    /**
     * The Authorization Key.
     */
    readonly authorizationKey?: pulumi.Input<string>;
    /**
     * The authorization use status.
     */
    readonly authorizationUseStatus?: pulumi.Input<string>;
    /**
     * The name of the Express Route Circuit in which to create the Authorization.
     */
    readonly expressRouteCircuitName?: pulumi.Input<string>;
    /**
     * The name of the ExpressRoute circuit. Changing this forces a
     * new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to
     * create the ExpressRoute circuit. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ExpressRouteCircuitAuthorization resource.
 */
export interface ExpressRouteCircuitAuthorizationArgs {
    /**
     * The name of the Express Route Circuit in which to create the Authorization.
     */
    readonly expressRouteCircuitName: pulumi.Input<string>;
    /**
     * The name of the ExpressRoute circuit. Changing this forces a
     * new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to
     * create the ExpressRoute circuit. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
}
