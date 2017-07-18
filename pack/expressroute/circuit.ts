// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class Circuit extends lumi.NamedResource implements CircuitArgs {
    public readonly allowClassicOperations?: boolean;
    public readonly bandwidthInMbps: number;
    public readonly location: string;
    public readonly circuitName?: string;
    public readonly peeringLocation: string;
    public readonly resourceGroupName: string;
    public /*out*/ readonly serviceKey: string;
    public readonly serviceProviderName: string;
    public /*out*/ readonly serviceProviderProvisioningState: string;
    public readonly sku: { family: string, tier: string }[];
    public readonly tags: {[key: string]: any};

    constructor(name: string, args: CircuitArgs) {
        super(name);
        this.allowClassicOperations = args.allowClassicOperations;
        if (lumirt.defaultIfComputed(args.bandwidthInMbps, "") === undefined) {
            throw new Error("Property argument 'bandwidthInMbps' is required, but was missing");
        }
        this.bandwidthInMbps = args.bandwidthInMbps;
        if (lumirt.defaultIfComputed(args.location, "") === undefined) {
            throw new Error("Property argument 'location' is required, but was missing");
        }
        this.location = args.location;
        this.circuitName = args.circuitName;
        if (lumirt.defaultIfComputed(args.peeringLocation, "") === undefined) {
            throw new Error("Property argument 'peeringLocation' is required, but was missing");
        }
        this.peeringLocation = args.peeringLocation;
        if (lumirt.defaultIfComputed(args.resourceGroupName, "") === undefined) {
            throw new Error("Property argument 'resourceGroupName' is required, but was missing");
        }
        this.resourceGroupName = args.resourceGroupName;
        if (lumirt.defaultIfComputed(args.serviceProviderName, "") === undefined) {
            throw new Error("Property argument 'serviceProviderName' is required, but was missing");
        }
        this.serviceProviderName = args.serviceProviderName;
        if (lumirt.defaultIfComputed(args.sku, "") === undefined) {
            throw new Error("Property argument 'sku' is required, but was missing");
        }
        this.sku = args.sku;
        this.tags = args.tags;
    }
}

export interface CircuitArgs {
    readonly allowClassicOperations?: boolean;
    readonly bandwidthInMbps: number;
    readonly location: string;
    readonly circuitName?: string;
    readonly peeringLocation: string;
    readonly resourceGroupName: string;
    readonly serviceProviderName: string;
    readonly sku: { family: string, tier: string }[];
    readonly tags?: {[key: string]: any};
}

