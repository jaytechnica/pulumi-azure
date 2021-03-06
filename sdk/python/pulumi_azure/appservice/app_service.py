# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['AppService']


class AppService(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_service_plan_id: Optional[pulumi.Input[str]] = None,
                 app_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 auth_settings: Optional[pulumi.Input[pulumi.InputType['AppServiceAuthSettingsArgs']]] = None,
                 backup: Optional[pulumi.Input[pulumi.InputType['AppServiceBackupArgs']]] = None,
                 client_affinity_enabled: Optional[pulumi.Input[bool]] = None,
                 client_cert_enabled: Optional[pulumi.Input[bool]] = None,
                 connection_strings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceConnectionStringArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 https_only: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['AppServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[pulumi.InputType['AppServiceLogsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_config: Optional[pulumi.Input[pulumi.InputType['AppServiceSiteConfigArgs']]] = None,
                 source_control: Optional[pulumi.Input[pulumi.InputType['AppServiceSourceControlArgs']]] = None,
                 storage_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceStorageAccountArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an App Service (within an App Service Plan).

        > **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `appservice.AppService` resource will be overwritten when promoting a Slot using the `appservice.ActiveSlot` resource.

        ## Example Usage

        This example provisions a Windows App Service.

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.appservice.PlanSkuArgs(
                tier="Standard",
                size="S1",
            ))
        example_app_service = azure.appservice.AppService("exampleAppService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id,
            site_config=azure.appservice.AppServiceSiteConfigArgs(
                dotnet_framework_version="v4.0",
                scm_type="LocalGit",
            ),
            app_settings={
                "SOME_KEY": "some-value",
            },
            connection_strings=[azure.appservice.AppServiceConnectionStringArgs(
                name="Database",
                type="SQLServer",
                value="Server=some-server.mydomain.com;Integrated Security=SSPI",
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_plan_id: The ID of the App Service Plan within which to create this App Service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[pulumi.InputType['AppServiceAuthSettingsArgs']] auth_settings: A `auth_settings` block as defined below.
        :param pulumi.Input[pulumi.InputType['AppServiceBackupArgs']] backup: A `backup` block as defined below.
        :param pulumi.Input[bool] client_affinity_enabled: Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
        :param pulumi.Input[bool] client_cert_enabled: Does the App Service require client certificates for incoming requests? Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceConnectionStringArgs']]]] connection_strings: One or more `connection_string` blocks as defined below.
        :param pulumi.Input[bool] enabled: Is the App Service Enabled?
        :param pulumi.Input[bool] https_only: Can the App Service only be accessed via HTTPS? Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['AppServiceIdentityArgs']] identity: A Managed Service Identity block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AppServiceLogsArgs']] logs: A `logs` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of the App Service. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the App Service.
        :param pulumi.Input[pulumi.InputType['AppServiceSiteConfigArgs']] site_config: A `site_config` block as defined below.
        :param pulumi.Input[pulumi.InputType['AppServiceSourceControlArgs']] source_control: A Source Control block as defined below
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceStorageAccountArgs']]]] storage_accounts: One or more `storage_account` blocks as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if app_service_plan_id is None:
                raise TypeError("Missing required property 'app_service_plan_id'")
            __props__['app_service_plan_id'] = app_service_plan_id
            __props__['app_settings'] = app_settings
            __props__['auth_settings'] = auth_settings
            __props__['backup'] = backup
            __props__['client_affinity_enabled'] = client_affinity_enabled
            __props__['client_cert_enabled'] = client_cert_enabled
            __props__['connection_strings'] = connection_strings
            __props__['enabled'] = enabled
            __props__['https_only'] = https_only
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['logs'] = logs
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['site_config'] = site_config
            __props__['source_control'] = source_control
            __props__['storage_accounts'] = storage_accounts
            __props__['tags'] = tags
            __props__['default_site_hostname'] = None
            __props__['outbound_ip_addresses'] = None
            __props__['possible_outbound_ip_addresses'] = None
            __props__['site_credentials'] = None
        super(AppService, __self__).__init__(
            'azure:appservice/appService:AppService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_service_plan_id: Optional[pulumi.Input[str]] = None,
            app_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            auth_settings: Optional[pulumi.Input[pulumi.InputType['AppServiceAuthSettingsArgs']]] = None,
            backup: Optional[pulumi.Input[pulumi.InputType['AppServiceBackupArgs']]] = None,
            client_affinity_enabled: Optional[pulumi.Input[bool]] = None,
            client_cert_enabled: Optional[pulumi.Input[bool]] = None,
            connection_strings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceConnectionStringArgs']]]]] = None,
            default_site_hostname: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            https_only: Optional[pulumi.Input[bool]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['AppServiceIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            logs: Optional[pulumi.Input[pulumi.InputType['AppServiceLogsArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            outbound_ip_addresses: Optional[pulumi.Input[str]] = None,
            possible_outbound_ip_addresses: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            site_config: Optional[pulumi.Input[pulumi.InputType['AppServiceSiteConfigArgs']]] = None,
            site_credentials: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceSiteCredentialArgs']]]]] = None,
            source_control: Optional[pulumi.Input[pulumi.InputType['AppServiceSourceControlArgs']]] = None,
            storage_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceStorageAccountArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'AppService':
        """
        Get an existing AppService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_plan_id: The ID of the App Service Plan within which to create this App Service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[pulumi.InputType['AppServiceAuthSettingsArgs']] auth_settings: A `auth_settings` block as defined below.
        :param pulumi.Input[pulumi.InputType['AppServiceBackupArgs']] backup: A `backup` block as defined below.
        :param pulumi.Input[bool] client_affinity_enabled: Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
        :param pulumi.Input[bool] client_cert_enabled: Does the App Service require client certificates for incoming requests? Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceConnectionStringArgs']]]] connection_strings: One or more `connection_string` blocks as defined below.
        :param pulumi.Input[str] default_site_hostname: The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
        :param pulumi.Input[bool] enabled: Is the App Service Enabled?
        :param pulumi.Input[bool] https_only: Can the App Service only be accessed via HTTPS? Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['AppServiceIdentityArgs']] identity: A Managed Service Identity block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['AppServiceLogsArgs']] logs: A `logs` block as defined below.
        :param pulumi.Input[str] name: Specifies the name of the App Service. Changing this forces a new resource to be created.
        :param pulumi.Input[str] outbound_ip_addresses: A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
        :param pulumi.Input[str] possible_outbound_ip_addresses: A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the App Service.
        :param pulumi.Input[pulumi.InputType['AppServiceSiteConfigArgs']] site_config: A `site_config` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceSiteCredentialArgs']]]] site_credentials: A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
        :param pulumi.Input[pulumi.InputType['AppServiceSourceControlArgs']] source_control: A Source Control block as defined below
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppServiceStorageAccountArgs']]]] storage_accounts: One or more `storage_account` blocks as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_service_plan_id"] = app_service_plan_id
        __props__["app_settings"] = app_settings
        __props__["auth_settings"] = auth_settings
        __props__["backup"] = backup
        __props__["client_affinity_enabled"] = client_affinity_enabled
        __props__["client_cert_enabled"] = client_cert_enabled
        __props__["connection_strings"] = connection_strings
        __props__["default_site_hostname"] = default_site_hostname
        __props__["enabled"] = enabled
        __props__["https_only"] = https_only
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["logs"] = logs
        __props__["name"] = name
        __props__["outbound_ip_addresses"] = outbound_ip_addresses
        __props__["possible_outbound_ip_addresses"] = possible_outbound_ip_addresses
        __props__["resource_group_name"] = resource_group_name
        __props__["site_config"] = site_config
        __props__["site_credentials"] = site_credentials
        __props__["source_control"] = source_control
        __props__["storage_accounts"] = storage_accounts
        __props__["tags"] = tags
        return AppService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appServicePlanId")
    def app_service_plan_id(self) -> pulumi.Output[str]:
        """
        The ID of the App Service Plan within which to create this App Service.
        """
        return pulumi.get(self, "app_service_plan_id")

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A key-value pair of App Settings.
        """
        return pulumi.get(self, "app_settings")

    @property
    @pulumi.getter(name="authSettings")
    def auth_settings(self) -> pulumi.Output['outputs.AppServiceAuthSettings']:
        """
        A `auth_settings` block as defined below.
        """
        return pulumi.get(self, "auth_settings")

    @property
    @pulumi.getter
    def backup(self) -> pulumi.Output[Optional['outputs.AppServiceBackup']]:
        """
        A `backup` block as defined below.
        """
        return pulumi.get(self, "backup")

    @property
    @pulumi.getter(name="clientAffinityEnabled")
    def client_affinity_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
        """
        return pulumi.get(self, "client_affinity_enabled")

    @property
    @pulumi.getter(name="clientCertEnabled")
    def client_cert_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Does the App Service require client certificates for incoming requests? Defaults to `false`.
        """
        return pulumi.get(self, "client_cert_enabled")

    @property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(self) -> pulumi.Output[Sequence['outputs.AppServiceConnectionString']]:
        """
        One or more `connection_string` blocks as defined below.
        """
        return pulumi.get(self, "connection_strings")

    @property
    @pulumi.getter(name="defaultSiteHostname")
    def default_site_hostname(self) -> pulumi.Output[str]:
        """
        The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
        """
        return pulumi.get(self, "default_site_hostname")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Is the App Service Enabled?
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="httpsOnly")
    def https_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Can the App Service only be accessed via HTTPS? Defaults to `false`.
        """
        return pulumi.get(self, "https_only")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.AppServiceIdentity']:
        """
        A Managed Service Identity block as defined below.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def logs(self) -> pulumi.Output['outputs.AppServiceLogs']:
        """
        A `logs` block as defined below.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the App Service. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> pulumi.Output[str]:
        """
        A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
        """
        return pulumi.get(self, "outbound_ip_addresses")

    @property
    @pulumi.getter(name="possibleOutboundIpAddresses")
    def possible_outbound_ip_addresses(self) -> pulumi.Output[str]:
        """
        A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
        """
        return pulumi.get(self, "possible_outbound_ip_addresses")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the App Service.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="siteConfig")
    def site_config(self) -> pulumi.Output['outputs.AppServiceSiteConfig']:
        """
        A `site_config` block as defined below.
        """
        return pulumi.get(self, "site_config")

    @property
    @pulumi.getter(name="siteCredentials")
    def site_credentials(self) -> pulumi.Output[Sequence['outputs.AppServiceSiteCredential']]:
        """
        A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
        """
        return pulumi.get(self, "site_credentials")

    @property
    @pulumi.getter(name="sourceControl")
    def source_control(self) -> pulumi.Output['outputs.AppServiceSourceControl']:
        """
        A Source Control block as defined below
        """
        return pulumi.get(self, "source_control")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> pulumi.Output[Sequence['outputs.AppServiceStorageAccount']]:
        """
        One or more `storage_account` blocks as defined below.
        """
        return pulumi.get(self, "storage_accounts")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

