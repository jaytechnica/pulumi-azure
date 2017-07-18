// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class CNameRecord extends lumi.NamedResource implements CNameRecordArgs {
    public readonly cNameRecordName?: string;
    public readonly record: string;
    public readonly resourceGroupName: string;
    public readonly tags: {[key: string]: any};
    public readonly ttl: number;
    public readonly zoneName: string;

    constructor(name: string, args: CNameRecordArgs) {
        super(name);
        this.cNameRecordName = args.cNameRecordName;
        if (lumirt.defaultIfComputed(args.record, "") === undefined) {
            throw new Error("Property argument 'record' is required, but was missing");
        }
        this.record = args.record;
        if (lumirt.defaultIfComputed(args.resourceGroupName, "") === undefined) {
            throw new Error("Property argument 'resourceGroupName' is required, but was missing");
        }
        this.resourceGroupName = args.resourceGroupName;
        this.tags = args.tags;
        if (lumirt.defaultIfComputed(args.ttl, "") === undefined) {
            throw new Error("Property argument 'ttl' is required, but was missing");
        }
        this.ttl = args.ttl;
        if (lumirt.defaultIfComputed(args.zoneName, "") === undefined) {
            throw new Error("Property argument 'zoneName' is required, but was missing");
        }
        this.zoneName = args.zoneName;
    }
}

export interface CNameRecordArgs {
    readonly cNameRecordName?: string;
    readonly record: string;
    readonly resourceGroupName: string;
    readonly tags?: {[key: string]: any};
    readonly ttl: number;
    readonly zoneName: string;
}

