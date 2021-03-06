// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a Key Vault Certificate.
 *
 * ## Example Usage
 * ### Generating A New Certificate)
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const current = azure.core.getClientConfig({});
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West Europe"});
 * const exampleKeyVault = new azure.keyvault.KeyVault("exampleKeyVault", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 *     tenantId: current.then(current => current.tenantId),
 *     skuName: "standard",
 *     accessPolicies: [{
 *         tenantId: current.then(current => current.tenantId),
 *         objectId: current.then(current => current.objectId),
 *         certificatePermissions: [
 *             "create",
 *             "delete",
 *             "deleteissuers",
 *             "get",
 *             "getissuers",
 *             "import",
 *             "list",
 *             "listissuers",
 *             "managecontacts",
 *             "manageissuers",
 *             "setissuers",
 *             "update",
 *         ],
 *         keyPermissions: [
 *             "backup",
 *             "create",
 *             "decrypt",
 *             "delete",
 *             "encrypt",
 *             "get",
 *             "import",
 *             "list",
 *             "purge",
 *             "recover",
 *             "restore",
 *             "sign",
 *             "unwrapKey",
 *             "update",
 *             "verify",
 *             "wrapKey",
 *         ],
 *         secretPermissions: [
 *             "backup",
 *             "delete",
 *             "get",
 *             "list",
 *             "purge",
 *             "recover",
 *             "restore",
 *             "set",
 *         ],
 *     }],
 *     tags: {
 *         environment: "Production",
 *     },
 * });
 * const exampleCertificate = new azure.keyvault.Certificate("exampleCertificate", {
 *     keyVaultId: exampleKeyVault.id,
 *     certificatePolicy: {
 *         issuerParameters: {
 *             name: "Self",
 *         },
 *         keyProperties: {
 *             exportable: true,
 *             keySize: 2048,
 *             keyType: "RSA",
 *             reuseKey: true,
 *         },
 *         lifetimeActions: [{
 *             action: {
 *                 actionType: "AutoRenew",
 *             },
 *             trigger: {
 *                 daysBeforeExpiry: 30,
 *             },
 *         }],
 *         secretProperties: {
 *             contentType: "application/x-pkcs12",
 *         },
 *         x509CertificateProperties: {
 *             extendedKeyUsages: ["1.3.6.1.5.5.7.3.1"],
 *             keyUsages: [
 *                 "cRLSign",
 *                 "dataEncipherment",
 *                 "digitalSignature",
 *                 "keyAgreement",
 *                 "keyCertSign",
 *                 "keyEncipherment",
 *             ],
 *             subjectAlternativeNames: {
 *                 dnsNames: [
 *                     "internal.contoso.com",
 *                     "domain.hello.world",
 *                 ],
 *             },
 *             subject: "CN=hello-world",
 *             validityInMonths: 12,
 *         },
 *     },
 * });
 * ```
 */
export class Certificate extends pulumi.CustomResource {
    /**
     * Get an existing Certificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateState, opts?: pulumi.CustomResourceOptions): Certificate {
        return new Certificate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:keyvault/certificate:Certificate';

    /**
     * Returns true if the given object is an instance of Certificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Certificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Certificate.__pulumiType;
    }

    /**
     * A `certificate` block as defined below, used to Import an existing certificate.
     */
    public readonly certificate!: pulumi.Output<outputs.keyvault.CertificateCertificate | undefined>;
    /**
     * A `certificateAttribute` block as defined below.
     */
    public /*out*/ readonly certificateAttributes!: pulumi.Output<outputs.keyvault.CertificateCertificateAttribute[]>;
    /**
     * The raw Key Vault Certificate data represented as a hexadecimal string.
     */
    public /*out*/ readonly certificateData!: pulumi.Output<string>;
    /**
     * A `certificatePolicy` block as defined below.
     */
    public readonly certificatePolicy!: pulumi.Output<outputs.keyvault.CertificateCertificatePolicy>;
    /**
     * The ID of the Key Vault where the Certificate should be created.
     */
    public readonly keyVaultId!: pulumi.Output<string>;
    /**
     * Specifies the name of the Key Vault Certificate. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the associated Key Vault Secret.
     */
    public /*out*/ readonly secretId!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The X509 Thumbprint of the Key Vault Certificate represented as a hexadecimal string.
     */
    public /*out*/ readonly thumbprint!: pulumi.Output<string>;
    /**
     * The current version of the Key Vault Certificate.
     */
    public /*out*/ readonly version!: pulumi.Output<string>;

    /**
     * Create a Certificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertificateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CertificateArgs | CertificateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as CertificateState | undefined;
            inputs["certificate"] = state ? state.certificate : undefined;
            inputs["certificateAttributes"] = state ? state.certificateAttributes : undefined;
            inputs["certificateData"] = state ? state.certificateData : undefined;
            inputs["certificatePolicy"] = state ? state.certificatePolicy : undefined;
            inputs["keyVaultId"] = state ? state.keyVaultId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["secretId"] = state ? state.secretId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["thumbprint"] = state ? state.thumbprint : undefined;
            inputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as CertificateArgs | undefined;
            if (!args || args.certificatePolicy === undefined) {
                throw new Error("Missing required property 'certificatePolicy'");
            }
            if (!args || args.keyVaultId === undefined) {
                throw new Error("Missing required property 'keyVaultId'");
            }
            inputs["certificate"] = args ? args.certificate : undefined;
            inputs["certificatePolicy"] = args ? args.certificatePolicy : undefined;
            inputs["keyVaultId"] = args ? args.keyVaultId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["certificateAttributes"] = undefined /*out*/;
            inputs["certificateData"] = undefined /*out*/;
            inputs["secretId"] = undefined /*out*/;
            inputs["thumbprint"] = undefined /*out*/;
            inputs["version"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        const aliasOpts = { aliases: [{ type: "azure:keyvault/certifiate:Certifiate" }] };
        opts = opts ? pulumi.mergeOptions(opts, aliasOpts) : aliasOpts;
        super(Certificate.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Certificate resources.
 */
export interface CertificateState {
    /**
     * A `certificate` block as defined below, used to Import an existing certificate.
     */
    readonly certificate?: pulumi.Input<inputs.keyvault.CertificateCertificate>;
    /**
     * A `certificateAttribute` block as defined below.
     */
    readonly certificateAttributes?: pulumi.Input<pulumi.Input<inputs.keyvault.CertificateCertificateAttribute>[]>;
    /**
     * The raw Key Vault Certificate data represented as a hexadecimal string.
     */
    readonly certificateData?: pulumi.Input<string>;
    /**
     * A `certificatePolicy` block as defined below.
     */
    readonly certificatePolicy?: pulumi.Input<inputs.keyvault.CertificateCertificatePolicy>;
    /**
     * The ID of the Key Vault where the Certificate should be created.
     */
    readonly keyVaultId?: pulumi.Input<string>;
    /**
     * Specifies the name of the Key Vault Certificate. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the associated Key Vault Secret.
     */
    readonly secretId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The X509 Thumbprint of the Key Vault Certificate represented as a hexadecimal string.
     */
    readonly thumbprint?: pulumi.Input<string>;
    /**
     * The current version of the Key Vault Certificate.
     */
    readonly version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Certificate resource.
 */
export interface CertificateArgs {
    /**
     * A `certificate` block as defined below, used to Import an existing certificate.
     */
    readonly certificate?: pulumi.Input<inputs.keyvault.CertificateCertificate>;
    /**
     * A `certificatePolicy` block as defined below.
     */
    readonly certificatePolicy: pulumi.Input<inputs.keyvault.CertificateCertificatePolicy>;
    /**
     * The ID of the Key Vault where the Certificate should be created.
     */
    readonly keyVaultId: pulumi.Input<string>;
    /**
     * Specifies the name of the Key Vault Certificate. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
