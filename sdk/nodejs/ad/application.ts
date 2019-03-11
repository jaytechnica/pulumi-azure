// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an Application within Azure Active Directory.
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
 * const test = new azure.ad.Application("test", {
 *     availableToOtherTenants: false,
 *     homepage: "https://homepage",
 *     identifierUris: ["https://uri"],
 *     name: "example",
 *     oauth2AllowImplicitFlow: true,
 *     replyUrls: ["https://replyurl"],
 * });
 * ```
 */
export class Application extends pulumi.CustomResource {
    /**
     * Get an existing Application resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationState, opts?: pulumi.CustomResourceOptions): Application {
        return new Application(name, <any>state, { ...opts, id: id });
    }

    /**
     * The Application ID.
     */
    public /*out*/ readonly applicationId: pulumi.Output<string>;
    /**
     * Is this Azure AD Application available to other tenants? Defaults to `false`.
     */
    public readonly availableToOtherTenants: pulumi.Output<boolean | undefined>;
    /**
     * The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.
     */
    public readonly homepage: pulumi.Output<string>;
    /**
     * A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
     */
    public readonly identifierUris: pulumi.Output<string[]>;
    /**
     * The display name for the application.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
     */
    public readonly oauth2AllowImplicitFlow: pulumi.Output<boolean | undefined>;
    /**
     * A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
     */
    public readonly replyUrls: pulumi.Output<string[]>;

    /**
     * Create a Application resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationArgs | ApplicationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ApplicationState = argsOrState as ApplicationState | undefined;
            inputs["applicationId"] = state ? state.applicationId : undefined;
            inputs["availableToOtherTenants"] = state ? state.availableToOtherTenants : undefined;
            inputs["homepage"] = state ? state.homepage : undefined;
            inputs["identifierUris"] = state ? state.identifierUris : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["oauth2AllowImplicitFlow"] = state ? state.oauth2AllowImplicitFlow : undefined;
            inputs["replyUrls"] = state ? state.replyUrls : undefined;
        } else {
            const args = argsOrState as ApplicationArgs | undefined;
            inputs["availableToOtherTenants"] = args ? args.availableToOtherTenants : undefined;
            inputs["homepage"] = args ? args.homepage : undefined;
            inputs["identifierUris"] = args ? args.identifierUris : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["oauth2AllowImplicitFlow"] = args ? args.oauth2AllowImplicitFlow : undefined;
            inputs["replyUrls"] = args ? args.replyUrls : undefined;
            inputs["applicationId"] = undefined /*out*/;
        }
        super("azure:ad/application:Application", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Application resources.
 */
export interface ApplicationState {
    /**
     * The Application ID.
     */
    readonly applicationId?: pulumi.Input<string>;
    /**
     * Is this Azure AD Application available to other tenants? Defaults to `false`.
     */
    readonly availableToOtherTenants?: pulumi.Input<boolean>;
    /**
     * The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.
     */
    readonly homepage?: pulumi.Input<string>;
    /**
     * A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
     */
    readonly identifierUris?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The display name for the application.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
     */
    readonly oauth2AllowImplicitFlow?: pulumi.Input<boolean>;
    /**
     * A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
     */
    readonly replyUrls?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Application resource.
 */
export interface ApplicationArgs {
    /**
     * Is this Azure AD Application available to other tenants? Defaults to `false`.
     */
    readonly availableToOtherTenants?: pulumi.Input<boolean>;
    /**
     * The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.
     */
    readonly homepage?: pulumi.Input<string>;
    /**
     * A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.
     */
    readonly identifierUris?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The display name for the application.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.
     */
    readonly oauth2AllowImplicitFlow?: pulumi.Input<boolean>;
    /**
     * A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.
     */
    readonly replyUrls?: pulumi.Input<pulumi.Input<string>[]>;
}
