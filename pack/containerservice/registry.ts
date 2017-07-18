// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class Registry extends lumi.NamedResource implements RegistryArgs {
    public readonly adminEnabled?: boolean;
    public /*out*/ readonly adminPassword: string;
    public /*out*/ readonly adminUsername: string;
    public readonly location: string;
    public /*out*/ readonly loginServer: string;
    public readonly registryName?: string;
    public readonly resourceGroupName: string;
    public readonly sku?: string;
    public readonly storageAccount: { accessKey: string, name: string }[];
    public readonly tags: {[key: string]: any};

    constructor(name: string, args: RegistryArgs) {
        super(name);
        this.adminEnabled = args.adminEnabled;
        if (lumirt.defaultIfComputed(args.location, "") === undefined) {
            throw new Error("Property argument 'location' is required, but was missing");
        }
        this.location = args.location;
        this.registryName = args.registryName;
        if (lumirt.defaultIfComputed(args.resourceGroupName, "") === undefined) {
            throw new Error("Property argument 'resourceGroupName' is required, but was missing");
        }
        this.resourceGroupName = args.resourceGroupName;
        this.sku = args.sku;
        if (lumirt.defaultIfComputed(args.storageAccount, "") === undefined) {
            throw new Error("Property argument 'storageAccount' is required, but was missing");
        }
        this.storageAccount = args.storageAccount;
        this.tags = args.tags;
    }
}

export interface RegistryArgs {
    readonly adminEnabled?: boolean;
    readonly location: string;
    readonly registryName?: string;
    readonly resourceGroupName: string;
    readonly sku?: string;
    readonly storageAccount: { accessKey: string, name: string }[];
    readonly tags?: {[key: string]: any};
}

