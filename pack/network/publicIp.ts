// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class PublicIp extends lumi.NamedResource implements PublicIpArgs {
    public readonly domainNameLabel?: string;
    public /*out*/ readonly fqdn: string;
    public readonly idleTimeoutInMinutes?: number;
    public /*out*/ readonly ipAddress: string;
    public readonly location: string;
    public readonly publicIpName?: string;
    public readonly publicIpAddressAllocation: string;
    public readonly resourceGroupName: string;
    public readonly reverseFqdn?: string;
    public readonly tags: {[key: string]: any};

    constructor(name: string, args: PublicIpArgs) {
        super(name);
        this.domainNameLabel = args.domainNameLabel;
        this.idleTimeoutInMinutes = args.idleTimeoutInMinutes;
        if (lumirt.defaultIfComputed(args.location, "") === undefined) {
            throw new Error("Property argument 'location' is required, but was missing");
        }
        this.location = args.location;
        this.publicIpName = args.publicIpName;
        if (lumirt.defaultIfComputed(args.publicIpAddressAllocation, "") === undefined) {
            throw new Error("Property argument 'publicIpAddressAllocation' is required, but was missing");
        }
        this.publicIpAddressAllocation = args.publicIpAddressAllocation;
        if (lumirt.defaultIfComputed(args.resourceGroupName, "") === undefined) {
            throw new Error("Property argument 'resourceGroupName' is required, but was missing");
        }
        this.resourceGroupName = args.resourceGroupName;
        this.reverseFqdn = args.reverseFqdn;
        this.tags = args.tags;
    }
}

export interface PublicIpArgs {
    readonly domainNameLabel?: string;
    readonly idleTimeoutInMinutes?: number;
    readonly location: string;
    readonly publicIpName?: string;
    readonly publicIpAddressAllocation: string;
    readonly resourceGroupName: string;
    readonly reverseFqdn?: string;
    readonly tags?: {[key: string]: any};
}

