// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class BackendAddressPool extends lumi.NamedResource implements BackendAddressPoolArgs {
    public /*out*/ readonly backendIpConfigurations: string[];
    public /*out*/ readonly loadBalancingRules: string[];
    public readonly loadbalancerId: string;
    public readonly location?: string;
    public readonly backendAddressPoolName?: string;
    public readonly resourceGroupName: string;

    constructor(name: string, args: BackendAddressPoolArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.loadbalancerId, "") === undefined) {
            throw new Error("Property argument 'loadbalancerId' is required, but was missing");
        }
        this.loadbalancerId = args.loadbalancerId;
        this.location = args.location;
        this.backendAddressPoolName = args.backendAddressPoolName;
        if (lumirt.defaultIfComputed(args.resourceGroupName, "") === undefined) {
            throw new Error("Property argument 'resourceGroupName' is required, but was missing");
        }
        this.resourceGroupName = args.resourceGroupName;
    }
}

export interface BackendAddressPoolArgs {
    readonly loadbalancerId: string;
    readonly location?: string;
    readonly backendAddressPoolName?: string;
    readonly resourceGroupName: string;
}

