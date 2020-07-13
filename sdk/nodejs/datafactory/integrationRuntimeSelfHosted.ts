// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a Data Factory Self-host Integration Runtime.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "eastus"});
 * const exampleFactory = new azure.datafactory.Factory("exampleFactory", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 * });
 * const exampleIntegrationRuntimeSelfHosted = new azure.datafactory.IntegrationRuntimeSelfHosted("exampleIntegrationRuntimeSelfHosted", {
 *     resourceGroupName: "example",
 *     dataFactoryName: "example",
 * });
 * ```
 */
export class IntegrationRuntimeSelfHosted extends pulumi.CustomResource {
    /**
     * Get an existing IntegrationRuntimeSelfHosted resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IntegrationRuntimeSelfHostedState, opts?: pulumi.CustomResourceOptions): IntegrationRuntimeSelfHosted {
        return new IntegrationRuntimeSelfHosted(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:datafactory/integrationRuntimeSelfHosted:IntegrationRuntimeSelfHosted';

    /**
     * Returns true if the given object is an instance of IntegrationRuntimeSelfHosted.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IntegrationRuntimeSelfHosted {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IntegrationRuntimeSelfHosted.__pulumiType;
    }

    /**
     * The primary integration runtime authentication key.
     */
    public /*out*/ readonly authKey1!: pulumi.Output<string>;
    /**
     * The secondary integration runtime authentication key.
     */
    public /*out*/ readonly authKey2!: pulumi.Output<string>;
    /**
     * Changing this forces a new Data Factory to be created.
     */
    public readonly dataFactoryName!: pulumi.Output<string>;
    /**
     * Integration runtime description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name which should be used for this Data Factory. Changing this forces a new Data Factory to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A `rbacAuthorization` block as defined below.
     */
    public readonly rbacAuthorizations!: pulumi.Output<outputs.datafactory.IntegrationRuntimeSelfHostedRbacAuthorization[] | undefined>;
    /**
     * The name of the Resource Group where the Data Factory should exist. Changing this forces a new Data Factory to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;

    /**
     * Create a IntegrationRuntimeSelfHosted resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IntegrationRuntimeSelfHostedArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IntegrationRuntimeSelfHostedArgs | IntegrationRuntimeSelfHostedState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IntegrationRuntimeSelfHostedState | undefined;
            inputs["authKey1"] = state ? state.authKey1 : undefined;
            inputs["authKey2"] = state ? state.authKey2 : undefined;
            inputs["dataFactoryName"] = state ? state.dataFactoryName : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["rbacAuthorizations"] = state ? state.rbacAuthorizations : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
        } else {
            const args = argsOrState as IntegrationRuntimeSelfHostedArgs | undefined;
            if (!args || args.dataFactoryName === undefined) {
                throw new Error("Missing required property 'dataFactoryName'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            inputs["dataFactoryName"] = args ? args.dataFactoryName : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["rbacAuthorizations"] = args ? args.rbacAuthorizations : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["authKey1"] = undefined /*out*/;
            inputs["authKey2"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(IntegrationRuntimeSelfHosted.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IntegrationRuntimeSelfHosted resources.
 */
export interface IntegrationRuntimeSelfHostedState {
    /**
     * The primary integration runtime authentication key.
     */
    readonly authKey1?: pulumi.Input<string>;
    /**
     * The secondary integration runtime authentication key.
     */
    readonly authKey2?: pulumi.Input<string>;
    /**
     * Changing this forces a new Data Factory to be created.
     */
    readonly dataFactoryName?: pulumi.Input<string>;
    /**
     * Integration runtime description.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name which should be used for this Data Factory. Changing this forces a new Data Factory to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A `rbacAuthorization` block as defined below.
     */
    readonly rbacAuthorizations?: pulumi.Input<pulumi.Input<inputs.datafactory.IntegrationRuntimeSelfHostedRbacAuthorization>[]>;
    /**
     * The name of the Resource Group where the Data Factory should exist. Changing this forces a new Data Factory to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IntegrationRuntimeSelfHosted resource.
 */
export interface IntegrationRuntimeSelfHostedArgs {
    /**
     * Changing this forces a new Data Factory to be created.
     */
    readonly dataFactoryName: pulumi.Input<string>;
    /**
     * Integration runtime description.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name which should be used for this Data Factory. Changing this forces a new Data Factory to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A `rbacAuthorization` block as defined below.
     */
    readonly rbacAuthorizations?: pulumi.Input<pulumi.Input<inputs.datafactory.IntegrationRuntimeSelfHostedRbacAuthorization>[]>;
    /**
     * The name of the Resource Group where the Data Factory should exist. Changing this forces a new Data Factory to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
}