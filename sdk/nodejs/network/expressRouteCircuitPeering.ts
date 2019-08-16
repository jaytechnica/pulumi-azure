// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages an ExpressRoute Circuit Peering.
 * 
 * ## Example Usage (Creating a Microsoft Peering)
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West US",
 *     name: "exprtTest",
 * });
 * const testExpressRouteCircuit = new azure.network.ExpressRouteCircuit("test", {
 *     allowClassicOperations: false,
 *     bandwidthInMbps: 50,
 *     location: testResourceGroup.location,
 *     name: "expressRoute1",
 *     peeringLocation: "Silicon Valley",
 *     resourceGroupName: testResourceGroup.name,
 *     serviceProviderName: "Equinix",
 *     sku: {
 *         family: "MeteredData",
 *         tier: "Standard",
 *     },
 *     tags: {
 *         environment: "Production",
 *     },
 * });
 * const testExpressRouteCircuitPeering = new azure.network.ExpressRouteCircuitPeering("test", {
 *     expressRouteCircuitName: testExpressRouteCircuit.name,
 *     microsoftPeeringConfig: {
 *         advertisedPublicPrefixes: ["123.1.0.0/24"],
 *     },
 *     peerAsn: 100,
 *     peeringType: "MicrosoftPeering",
 *     primaryPeerAddressPrefix: "123.0.0.0/30",
 *     resourceGroupName: testResourceGroup.name,
 *     secondaryPeerAddressPrefix: "123.0.0.4/30",
 *     vlanId: 300,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit_peering.html.markdown.
 */
export class ExpressRouteCircuitPeering extends pulumi.CustomResource {
    /**
     * Get an existing ExpressRouteCircuitPeering resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExpressRouteCircuitPeeringState, opts?: pulumi.CustomResourceOptions): ExpressRouteCircuitPeering {
        return new ExpressRouteCircuitPeering(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:network/expressRouteCircuitPeering:ExpressRouteCircuitPeering';

    /**
     * Returns true if the given object is an instance of ExpressRouteCircuitPeering.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ExpressRouteCircuitPeering {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ExpressRouteCircuitPeering.__pulumiType;
    }

    /**
     * The ASN used by Azure.
     */
    public /*out*/ readonly azureAsn!: pulumi.Output<number>;
    /**
     * The name of the ExpressRoute Circuit in which to create the Peering.
     */
    public readonly expressRouteCircuitName!: pulumi.Output<string>;
    /**
     * A `microsoftPeeringConfig` block as defined below. Required when `peeringType` is set to `MicrosoftPeering`.
     */
    public readonly microsoftPeeringConfig!: pulumi.Output<outputs.network.ExpressRouteCircuitPeeringMicrosoftPeeringConfig | undefined>;
    /**
     * The Either a 16-bit or a 32-bit ASN. Can either be public or private..
     */
    public readonly peerAsn!: pulumi.Output<number>;
    /**
     * The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.
     */
    public readonly peeringType!: pulumi.Output<string>;
    /**
     * The Primary Port used by Azure for this Peering.
     */
    public /*out*/ readonly primaryAzurePort!: pulumi.Output<string>;
    /**
     * A `/30` subnet for the primary link.
     */
    public readonly primaryPeerAddressPrefix!: pulumi.Output<string>;
    /**
     * The name of the resource group in which to
     * create the Express Route Circuit Peering. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * The Secondary Port used by Azure for this Peering.
     */
    public /*out*/ readonly secondaryAzurePort!: pulumi.Output<string>;
    /**
     * A `/30` subnet for the secondary link.
     */
    public readonly secondaryPeerAddressPrefix!: pulumi.Output<string>;
    /**
     * The shared key. Can be a maximum of 25 characters.
     */
    public readonly sharedKey!: pulumi.Output<string | undefined>;
    /**
     * A valid VLAN ID to establish this peering on.
     */
    public readonly vlanId!: pulumi.Output<number>;

    /**
     * Create a ExpressRouteCircuitPeering resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ExpressRouteCircuitPeeringArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ExpressRouteCircuitPeeringArgs | ExpressRouteCircuitPeeringState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ExpressRouteCircuitPeeringState | undefined;
            inputs["azureAsn"] = state ? state.azureAsn : undefined;
            inputs["expressRouteCircuitName"] = state ? state.expressRouteCircuitName : undefined;
            inputs["microsoftPeeringConfig"] = state ? state.microsoftPeeringConfig : undefined;
            inputs["peerAsn"] = state ? state.peerAsn : undefined;
            inputs["peeringType"] = state ? state.peeringType : undefined;
            inputs["primaryAzurePort"] = state ? state.primaryAzurePort : undefined;
            inputs["primaryPeerAddressPrefix"] = state ? state.primaryPeerAddressPrefix : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["secondaryAzurePort"] = state ? state.secondaryAzurePort : undefined;
            inputs["secondaryPeerAddressPrefix"] = state ? state.secondaryPeerAddressPrefix : undefined;
            inputs["sharedKey"] = state ? state.sharedKey : undefined;
            inputs["vlanId"] = state ? state.vlanId : undefined;
        } else {
            const args = argsOrState as ExpressRouteCircuitPeeringArgs | undefined;
            if (!args || args.expressRouteCircuitName === undefined) {
                throw new Error("Missing required property 'expressRouteCircuitName'");
            }
            if (!args || args.peeringType === undefined) {
                throw new Error("Missing required property 'peeringType'");
            }
            if (!args || args.primaryPeerAddressPrefix === undefined) {
                throw new Error("Missing required property 'primaryPeerAddressPrefix'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.secondaryPeerAddressPrefix === undefined) {
                throw new Error("Missing required property 'secondaryPeerAddressPrefix'");
            }
            if (!args || args.vlanId === undefined) {
                throw new Error("Missing required property 'vlanId'");
            }
            inputs["expressRouteCircuitName"] = args ? args.expressRouteCircuitName : undefined;
            inputs["microsoftPeeringConfig"] = args ? args.microsoftPeeringConfig : undefined;
            inputs["peerAsn"] = args ? args.peerAsn : undefined;
            inputs["peeringType"] = args ? args.peeringType : undefined;
            inputs["primaryPeerAddressPrefix"] = args ? args.primaryPeerAddressPrefix : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["secondaryPeerAddressPrefix"] = args ? args.secondaryPeerAddressPrefix : undefined;
            inputs["sharedKey"] = args ? args.sharedKey : undefined;
            inputs["vlanId"] = args ? args.vlanId : undefined;
            inputs["azureAsn"] = undefined /*out*/;
            inputs["primaryAzurePort"] = undefined /*out*/;
            inputs["secondaryAzurePort"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ExpressRouteCircuitPeering.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ExpressRouteCircuitPeering resources.
 */
export interface ExpressRouteCircuitPeeringState {
    /**
     * The ASN used by Azure.
     */
    readonly azureAsn?: pulumi.Input<number>;
    /**
     * The name of the ExpressRoute Circuit in which to create the Peering.
     */
    readonly expressRouteCircuitName?: pulumi.Input<string>;
    /**
     * A `microsoftPeeringConfig` block as defined below. Required when `peeringType` is set to `MicrosoftPeering`.
     */
    readonly microsoftPeeringConfig?: pulumi.Input<inputs.network.ExpressRouteCircuitPeeringMicrosoftPeeringConfig>;
    /**
     * The Either a 16-bit or a 32-bit ASN. Can either be public or private..
     */
    readonly peerAsn?: pulumi.Input<number>;
    /**
     * The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.
     */
    readonly peeringType?: pulumi.Input<string>;
    /**
     * The Primary Port used by Azure for this Peering.
     */
    readonly primaryAzurePort?: pulumi.Input<string>;
    /**
     * A `/30` subnet for the primary link.
     */
    readonly primaryPeerAddressPrefix?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to
     * create the Express Route Circuit Peering. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The Secondary Port used by Azure for this Peering.
     */
    readonly secondaryAzurePort?: pulumi.Input<string>;
    /**
     * A `/30` subnet for the secondary link.
     */
    readonly secondaryPeerAddressPrefix?: pulumi.Input<string>;
    /**
     * The shared key. Can be a maximum of 25 characters.
     */
    readonly sharedKey?: pulumi.Input<string>;
    /**
     * A valid VLAN ID to establish this peering on.
     */
    readonly vlanId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a ExpressRouteCircuitPeering resource.
 */
export interface ExpressRouteCircuitPeeringArgs {
    /**
     * The name of the ExpressRoute Circuit in which to create the Peering.
     */
    readonly expressRouteCircuitName: pulumi.Input<string>;
    /**
     * A `microsoftPeeringConfig` block as defined below. Required when `peeringType` is set to `MicrosoftPeering`.
     */
    readonly microsoftPeeringConfig?: pulumi.Input<inputs.network.ExpressRouteCircuitPeeringMicrosoftPeeringConfig>;
    /**
     * The Either a 16-bit or a 32-bit ASN. Can either be public or private..
     */
    readonly peerAsn?: pulumi.Input<number>;
    /**
     * The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.
     */
    readonly peeringType: pulumi.Input<string>;
    /**
     * A `/30` subnet for the primary link.
     */
    readonly primaryPeerAddressPrefix: pulumi.Input<string>;
    /**
     * The name of the resource group in which to
     * create the Express Route Circuit Peering. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A `/30` subnet for the secondary link.
     */
    readonly secondaryPeerAddressPrefix: pulumi.Input<string>;
    /**
     * The shared key. Can be a maximum of 25 characters.
     */
    readonly sharedKey?: pulumi.Input<string>;
    /**
     * A valid VLAN ID to establish this peering on.
     */
    readonly vlanId: pulumi.Input<number>;
}
