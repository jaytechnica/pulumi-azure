// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class Blob extends lumi.NamedResource implements BlobArgs {
    public readonly attempts?: number;
    public readonly blobName?: string;
    public readonly parallelism?: number;
    public readonly resourceGroupName: string;
    public readonly size?: number;
    public readonly source?: string;
    public readonly sourceUri?: string;
    public readonly storageAccountName: string;
    public readonly storageContainerName: string;
    public readonly type?: string;
    public /*out*/ readonly url: string;

    constructor(name: string, args: BlobArgs) {
        super(name);
        this.attempts = args.attempts;
        this.blobName = args.blobName;
        this.parallelism = args.parallelism;
        if (lumirt.defaultIfComputed(args.resourceGroupName, "") === undefined) {
            throw new Error("Property argument 'resourceGroupName' is required, but was missing");
        }
        this.resourceGroupName = args.resourceGroupName;
        this.size = args.size;
        this.source = args.source;
        this.sourceUri = args.sourceUri;
        if (lumirt.defaultIfComputed(args.storageAccountName, "") === undefined) {
            throw new Error("Property argument 'storageAccountName' is required, but was missing");
        }
        this.storageAccountName = args.storageAccountName;
        if (lumirt.defaultIfComputed(args.storageContainerName, "") === undefined) {
            throw new Error("Property argument 'storageContainerName' is required, but was missing");
        }
        this.storageContainerName = args.storageContainerName;
        this.type = args.type;
    }
}

export interface BlobArgs {
    readonly attempts?: number;
    readonly blobName?: string;
    readonly parallelism?: number;
    readonly resourceGroupName: string;
    readonly size?: number;
    readonly source?: string;
    readonly sourceUri?: string;
    readonly storageAccountName: string;
    readonly storageContainerName: string;
    readonly type?: string;
}
