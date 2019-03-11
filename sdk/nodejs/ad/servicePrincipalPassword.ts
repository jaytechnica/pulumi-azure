// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Password associated with a Service Principal within Azure Active Directory.
 * 
 * > **NOTE:** The Azure Active Directory resources have been split out into [a new AzureAD Provider](http://terraform.io/docs/providers/azuread/index.html) - as such the AzureAD resources within the AzureRM Provider are deprecated and will be removed in the next major version (2.0). Information on how to migrate from the existing resources to the new AzureAD Provider can be found here.
 * 
 * > **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testApplication = new azure.ad.Application("test", {
 *     availableToOtherTenants: false,
 *     homepage: "http://homepage",
 *     identifierUris: ["http://uri"],
 *     name: "example",
 *     oauth2AllowImplicitFlow: true,
 *     replyUrls: ["http://replyurl"],
 * });
 * const testServicePrincipal = new azure.ad.ServicePrincipal("test", {
 *     applicationId: testApplication.applicationId,
 * });
 * const testServicePrincipalPassword = new azure.ad.ServicePrincipalPassword("test", {
 *     endDate: "2020-01-01T01:02:03Z",
 *     servicePrincipalId: testServicePrincipal.id,
 *     value: "VT=uSgbTanZhyz@%nL9Hpd+Tfay_MRV#",
 * });
 * ```
 */
export class ServicePrincipalPassword extends pulumi.CustomResource {
    /**
     * Get an existing ServicePrincipalPassword resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServicePrincipalPasswordState, opts?: pulumi.CustomResourceOptions): ServicePrincipalPassword {
        return new ServicePrincipalPassword(name, <any>state, { ...opts, id: id });
    }

    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    public readonly endDate: pulumi.Output<string>;
    /**
     * A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    public readonly keyId: pulumi.Output<string>;
    /**
     * The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
     */
    public readonly servicePrincipalId: pulumi.Output<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    public readonly startDate: pulumi.Output<string>;
    /**
     * The Password for this Service Principal.
     */
    public readonly value: pulumi.Output<string>;

    /**
     * Create a ServicePrincipalPassword resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServicePrincipalPasswordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServicePrincipalPasswordArgs | ServicePrincipalPasswordState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ServicePrincipalPasswordState = argsOrState as ServicePrincipalPasswordState | undefined;
            inputs["endDate"] = state ? state.endDate : undefined;
            inputs["keyId"] = state ? state.keyId : undefined;
            inputs["servicePrincipalId"] = state ? state.servicePrincipalId : undefined;
            inputs["startDate"] = state ? state.startDate : undefined;
            inputs["value"] = state ? state.value : undefined;
        } else {
            const args = argsOrState as ServicePrincipalPasswordArgs | undefined;
            if (!args || args.endDate === undefined) {
                throw new Error("Missing required property 'endDate'");
            }
            if (!args || args.servicePrincipalId === undefined) {
                throw new Error("Missing required property 'servicePrincipalId'");
            }
            if (!args || args.value === undefined) {
                throw new Error("Missing required property 'value'");
            }
            inputs["endDate"] = args ? args.endDate : undefined;
            inputs["keyId"] = args ? args.keyId : undefined;
            inputs["servicePrincipalId"] = args ? args.servicePrincipalId : undefined;
            inputs["startDate"] = args ? args.startDate : undefined;
            inputs["value"] = args ? args.value : undefined;
        }
        super("azure:ad/servicePrincipalPassword:ServicePrincipalPassword", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ServicePrincipalPassword resources.
 */
export interface ServicePrincipalPasswordState {
    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
     */
    readonly servicePrincipalId?: pulumi.Input<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The Password for this Service Principal.
     */
    readonly value?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ServicePrincipalPassword resource.
 */
export interface ServicePrincipalPasswordArgs {
    /**
     * The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.
     */
    readonly endDate: pulumi.Input<string>;
    /**
     * A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.
     */
    readonly servicePrincipalId: pulumi.Input<string>;
    /**
     * The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * The Password for this Service Principal.
     */
    readonly value: pulumi.Input<string>;
}
