// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Key Vault Certificate.
 */
export class Certifiate extends pulumi.CustomResource {
    /**
     * Get an existing Certifiate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertifiateState, opts?: pulumi.CustomResourceOptions): Certifiate {
        return new Certifiate(name, <any>state, { ...opts, id: id });
    }

    /**
     * A `certificate` block as defined below, used to Import an existing certificate.
     */
    public readonly certificate: pulumi.Output<{ contents: string, password?: string } | undefined>;
    /**
     * The raw Key Vault Certificate.
     */
    public /*out*/ readonly certificateData: pulumi.Output<string>;
    /**
     * A `certificate_policy` block as defined below.
     */
    public readonly certificatePolicy: pulumi.Output<{ issuerParameters: { name: string }, keyProperties: { exportable: boolean, keySize: number, keyType: string, reuseKey: boolean }, lifetimeActions?: { action: { actionType: string }, trigger: { daysBeforeExpiry?: number, lifetimePercentage?: number } }[], secretProperties: { contentType: string }, x509CertificateProperties: { extendedKeyUsages: string[], keyUsages: string[], subject: string, subjectAlternativeNames: { dnsNames?: string[], emails?: string[], upns?: string[] }, validityInMonths: number } }>;
    /**
     * The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The ID of the associated Key Vault Secret.
     */
    public /*out*/ readonly secretId: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any}>;
    /**
     * The X509 Thumbprint of the Key Vault Certificate returned as hex string.
     */
    public /*out*/ readonly thumbprint: pulumi.Output<string>;
    /**
     * Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.
     */
    public readonly vaultUri: pulumi.Output<string>;
    /**
     * The current version of the Key Vault Certificate.
     */
    public /*out*/ readonly version: pulumi.Output<string>;

    /**
     * Create a Certifiate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertifiateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CertifiateArgs | CertifiateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: CertifiateState = argsOrState as CertifiateState | undefined;
            inputs["certificate"] = state ? state.certificate : undefined;
            inputs["certificateData"] = state ? state.certificateData : undefined;
            inputs["certificatePolicy"] = state ? state.certificatePolicy : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["secretId"] = state ? state.secretId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["thumbprint"] = state ? state.thumbprint : undefined;
            inputs["vaultUri"] = state ? state.vaultUri : undefined;
            inputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as CertifiateArgs | undefined;
            if (!args || args.certificatePolicy === undefined) {
                throw new Error("Missing required property 'certificatePolicy'");
            }
            if (!args || args.vaultUri === undefined) {
                throw new Error("Missing required property 'vaultUri'");
            }
            inputs["certificate"] = args ? args.certificate : undefined;
            inputs["certificatePolicy"] = args ? args.certificatePolicy : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vaultUri"] = args ? args.vaultUri : undefined;
            inputs["certificateData"] = undefined /*out*/;
            inputs["secretId"] = undefined /*out*/;
            inputs["thumbprint"] = undefined /*out*/;
            inputs["version"] = undefined /*out*/;
        }
        super("azure:keyvault/certifiate:Certifiate", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Certifiate resources.
 */
export interface CertifiateState {
    /**
     * A `certificate` block as defined below, used to Import an existing certificate.
     */
    readonly certificate?: pulumi.Input<{ contents: pulumi.Input<string>, password?: pulumi.Input<string> }>;
    /**
     * The raw Key Vault Certificate.
     */
    readonly certificateData?: pulumi.Input<string>;
    /**
     * A `certificate_policy` block as defined below.
     */
    readonly certificatePolicy?: pulumi.Input<{ issuerParameters: pulumi.Input<{ name: pulumi.Input<string> }>, keyProperties: pulumi.Input<{ exportable: pulumi.Input<boolean>, keySize: pulumi.Input<number>, keyType: pulumi.Input<string>, reuseKey: pulumi.Input<boolean> }>, lifetimeActions?: pulumi.Input<pulumi.Input<{ action: pulumi.Input<{ actionType: pulumi.Input<string> }>, trigger: pulumi.Input<{ daysBeforeExpiry?: pulumi.Input<number>, lifetimePercentage?: pulumi.Input<number> }> }>[]>, secretProperties: pulumi.Input<{ contentType: pulumi.Input<string> }>, x509CertificateProperties?: pulumi.Input<{ extendedKeyUsages?: pulumi.Input<pulumi.Input<string>[]>, keyUsages: pulumi.Input<pulumi.Input<string>[]>, subject: pulumi.Input<string>, subjectAlternativeNames?: pulumi.Input<{ dnsNames?: pulumi.Input<pulumi.Input<string>[]>, emails?: pulumi.Input<pulumi.Input<string>[]>, upns?: pulumi.Input<pulumi.Input<string>[]> }>, validityInMonths: pulumi.Input<number> }> }>;
    /**
     * The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the associated Key Vault Secret.
     */
    readonly secretId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The X509 Thumbprint of the Key Vault Certificate returned as hex string.
     */
    readonly thumbprint?: pulumi.Input<string>;
    /**
     * Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.
     */
    readonly vaultUri?: pulumi.Input<string>;
    /**
     * The current version of the Key Vault Certificate.
     */
    readonly version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Certifiate resource.
 */
export interface CertifiateArgs {
    /**
     * A `certificate` block as defined below, used to Import an existing certificate.
     */
    readonly certificate?: pulumi.Input<{ contents: pulumi.Input<string>, password?: pulumi.Input<string> }>;
    /**
     * A `certificate_policy` block as defined below.
     */
    readonly certificatePolicy: pulumi.Input<{ issuerParameters: pulumi.Input<{ name: pulumi.Input<string> }>, keyProperties: pulumi.Input<{ exportable: pulumi.Input<boolean>, keySize: pulumi.Input<number>, keyType: pulumi.Input<string>, reuseKey: pulumi.Input<boolean> }>, lifetimeActions?: pulumi.Input<pulumi.Input<{ action: pulumi.Input<{ actionType: pulumi.Input<string> }>, trigger: pulumi.Input<{ daysBeforeExpiry?: pulumi.Input<number>, lifetimePercentage?: pulumi.Input<number> }> }>[]>, secretProperties: pulumi.Input<{ contentType: pulumi.Input<string> }>, x509CertificateProperties?: pulumi.Input<{ extendedKeyUsages?: pulumi.Input<pulumi.Input<string>[]>, keyUsages: pulumi.Input<pulumi.Input<string>[]>, subject: pulumi.Input<string>, subjectAlternativeNames?: pulumi.Input<{ dnsNames?: pulumi.Input<pulumi.Input<string>[]>, emails?: pulumi.Input<pulumi.Input<string>[]>, upns?: pulumi.Input<pulumi.Input<string>[]> }>, validityInMonths: pulumi.Input<number> }> }>;
    /**
     * The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.
     */
    readonly vaultUri: pulumi.Input<string>;
}
