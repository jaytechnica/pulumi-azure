// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class SqlServer extends lumi.NamedResource implements SqlServerArgs {
    public readonly administratorLogin: string;
    public readonly administratorLoginPassword: string;
    public /*out*/ readonly fullyQualifiedDomainName: string;
    public readonly location: string;
    public readonly sqlServerName?: string;
    public readonly resourceGroupName: string;
    public readonly tags: {[key: string]: any};
    public readonly version: string;

    constructor(name: string, args: SqlServerArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.administratorLogin, "") === undefined) {
            throw new Error("Property argument 'administratorLogin' is required, but was missing");
        }
        this.administratorLogin = args.administratorLogin;
        if (lumirt.defaultIfComputed(args.administratorLoginPassword, "") === undefined) {
            throw new Error("Property argument 'administratorLoginPassword' is required, but was missing");
        }
        this.administratorLoginPassword = args.administratorLoginPassword;
        if (lumirt.defaultIfComputed(args.location, "") === undefined) {
            throw new Error("Property argument 'location' is required, but was missing");
        }
        this.location = args.location;
        this.sqlServerName = args.sqlServerName;
        if (lumirt.defaultIfComputed(args.resourceGroupName, "") === undefined) {
            throw new Error("Property argument 'resourceGroupName' is required, but was missing");
        }
        this.resourceGroupName = args.resourceGroupName;
        this.tags = args.tags;
        if (lumirt.defaultIfComputed(args.version, "") === undefined) {
            throw new Error("Property argument 'version' is required, but was missing");
        }
        this.version = args.version;
    }
}

export interface SqlServerArgs {
    readonly administratorLogin: string;
    readonly administratorLoginPassword: string;
    readonly location: string;
    readonly sqlServerName?: string;
    readonly resourceGroupName: string;
    readonly tags?: {[key: string]: any};
    readonly version: string;
}
