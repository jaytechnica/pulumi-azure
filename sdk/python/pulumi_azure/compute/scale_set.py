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

__all__ = ['ScaleSet']


class ScaleSet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automatic_os_upgrade: Optional[pulumi.Input[bool]] = None,
                 boot_diagnostics: Optional[pulumi.Input[pulumi.InputType['ScaleSetBootDiagnosticsArgs']]] = None,
                 eviction_policy: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetExtensionArgs']]]]] = None,
                 health_probe_id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ScaleSetIdentityArgs']]] = None,
                 license_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetNetworkProfileArgs']]]]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['ScaleSetOsProfileArgs']]] = None,
                 os_profile_linux_config: Optional[pulumi.Input[pulumi.InputType['ScaleSetOsProfileLinuxConfigArgs']]] = None,
                 os_profile_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetOsProfileSecretArgs']]]]] = None,
                 os_profile_windows_config: Optional[pulumi.Input[pulumi.InputType['ScaleSetOsProfileWindowsConfigArgs']]] = None,
                 overprovision: Optional[pulumi.Input[bool]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['ScaleSetPlanArgs']]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 proximity_placement_group_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rolling_upgrade_policy: Optional[pulumi.Input[pulumi.InputType['ScaleSetRollingUpgradePolicyArgs']]] = None,
                 single_placement_group: Optional[pulumi.Input[bool]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ScaleSetSkuArgs']]] = None,
                 storage_profile_data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileDataDiskArgs']]]]] = None,
                 storage_profile_image_reference: Optional[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileImageReferenceArgs']]] = None,
                 storage_profile_os_disk: Optional[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileOsDiskArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 upgrade_policy_mode: Optional[pulumi.Input[str]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a virtual machine scale set.

        ## Disclaimers

        > **Note:** The `compute.ScaleSet` resource has been superseded by the `compute.LinuxVirtualMachineScaleSet` and `compute.WindowsVirtualMachineScaleSet` resources. The existing `compute.ScaleSet` resource will continue to be available throughout the 2.x releases however is in a feature-frozen state to maintain compatibility - new functionality will instead be added to the `compute.LinuxVirtualMachineScaleSet` and `compute.WindowsVirtualMachineScaleSet` resources.

        ## Example Usage
        ### With Managed Disks (Recommended)

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US 2")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.2.0/24"])
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            allocation_method="Static",
            domain_name_label=example_resource_group.name,
            tags={
                "environment": "staging",
            })
        example_load_balancer = azure.lb.LoadBalancer("exampleLoadBalancer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            frontend_ip_configurations=[azure.lb.LoadBalancerFrontendIpConfigurationArgs(
                name="PublicIPAddress",
                public_ip_address_id=example_public_ip.id,
            )])
        bpepool = azure.lb.BackendAddressPool("bpepool",
            resource_group_name=example_resource_group.name,
            loadbalancer_id=example_load_balancer.id)
        lbnatpool = azure.lb.NatPool("lbnatpool",
            resource_group_name=example_resource_group.name,
            loadbalancer_id=example_load_balancer.id,
            protocol="Tcp",
            frontend_port_start=50000,
            frontend_port_end=50119,
            backend_port=22,
            frontend_ip_configuration_name="PublicIPAddress")
        example_probe = azure.lb.Probe("exampleProbe",
            resource_group_name=example_resource_group.name,
            loadbalancer_id=example_load_balancer.id,
            protocol="Http",
            request_path="/health",
            port=8080)
        example_scale_set = azure.compute.ScaleSet("exampleScaleSet",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            automatic_os_upgrade=True,
            upgrade_policy_mode="Rolling",
            rolling_upgrade_policy=azure.compute.ScaleSetRollingUpgradePolicyArgs(
                max_batch_instance_percent=20,
                max_unhealthy_instance_percent=20,
                max_unhealthy_upgraded_instance_percent=5,
                pause_time_between_batches="PT0S",
            ),
            health_probe_id=example_probe.id,
            sku=azure.compute.ScaleSetSkuArgs(
                name="Standard_F2",
                tier="Standard",
                capacity=2,
            ),
            storage_profile_image_reference=azure.compute.ScaleSetStorageProfileImageReferenceArgs(
                publisher="Canonical",
                offer="UbuntuServer",
                sku="16.04-LTS",
                version="latest",
            ),
            storage_profile_os_disk=azure.compute.ScaleSetStorageProfileOsDiskArgs(
                name="",
                caching="ReadWrite",
                create_option="FromImage",
                managed_disk_type="Standard_LRS",
            ),
            storage_profile_data_disks=[azure.compute.ScaleSetStorageProfileDataDiskArgs(
                lun=0,
                caching="ReadWrite",
                create_option="Empty",
                disk_size_gb=10,
            )],
            os_profile=azure.compute.ScaleSetOsProfileArgs(
                computer_name_prefix="testvm",
                admin_username="myadmin",
            ),
            os_profile_linux_config=azure.compute.ScaleSetOsProfileLinuxConfigArgs(
                disable_password_authentication=True,
                ssh_keys=[azure.compute.ScaleSetOsProfileLinuxConfigSshKeyArgs(
                    path="/home/myadmin/.ssh/authorized_keys",
                    key_data=(lambda path: open(path).read())("~/.ssh/demo_key.pub"),
                )],
            ),
            network_profiles=[azure.compute.ScaleSetNetworkProfileArgs(
                name="mynetworkprofile",
                primary=True,
                ip_configurations=[{
                    "name": "TestIPConfiguration",
                    "primary": True,
                    "subnet_id": example_subnet.id,
                    "loadBalancerBackendAddressPoolIds": [bpepool.id],
                    "loadBalancerInboundNatRulesIds": [lbnatpool.id],
                }],
            )],
            tags={
                "environment": "staging",
            })
        ```
        ### With Unmanaged Disks

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location="West US",
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.2.0/24"])
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location="westus",
            account_tier="Standard",
            account_replication_type="LRS",
            tags={
                "environment": "staging",
            })
        example_container = azure.storage.Container("exampleContainer",
            storage_account_name=example_account.name,
            container_access_type="private")
        example_scale_set = azure.compute.ScaleSet("exampleScaleSet",
            location="West US",
            resource_group_name=example_resource_group.name,
            upgrade_policy_mode="Manual",
            sku=azure.compute.ScaleSetSkuArgs(
                name="Standard_F2",
                tier="Standard",
                capacity=2,
            ),
            os_profile=azure.compute.ScaleSetOsProfileArgs(
                computer_name_prefix="testvm",
                admin_username="myadmin",
            ),
            os_profile_linux_config=azure.compute.ScaleSetOsProfileLinuxConfigArgs(
                disable_password_authentication=True,
                ssh_keys=[azure.compute.ScaleSetOsProfileLinuxConfigSshKeyArgs(
                    path="/home/myadmin/.ssh/authorized_keys",
                    key_data=(lambda path: open(path).read())("~/.ssh/demo_key.pub"),
                )],
            ),
            network_profiles=[azure.compute.ScaleSetNetworkProfileArgs(
                name="TestNetworkProfile",
                primary=True,
                ip_configurations=[{
                    "name": "TestIPConfiguration",
                    "primary": True,
                    "subnet_id": example_subnet.id,
                }],
            )],
            storage_profile_os_disk=azure.compute.ScaleSetStorageProfileOsDiskArgs(
                name="osDiskProfile",
                caching="ReadWrite",
                create_option="FromImage",
                vhd_containers=[pulumi.Output.all(example_account.primary_blob_endpoint, example_container.name).apply(lambda primary_blob_endpoint, name: f"{primary_blob_endpoint}{name}")],
            ),
            storage_profile_image_reference=azure.compute.ScaleSetStorageProfileImageReferenceArgs(
                publisher="Canonical",
                offer="UbuntuServer",
                sku="16.04-LTS",
                version="latest",
            ))
        ```
        ## Example of storage_profile_image_reference with id

        ```python
        import pulumi
        import pulumi_azure as azure

        example_image = azure.compute.Image("exampleImage")
        # ...
        example_scale_set = azure.compute.ScaleSet("exampleScaleSet", storage_profile_image_reference=azure.compute.ScaleSetStorageProfileImageReferenceArgs(
            id=example_image.id,
        ))
        # ...
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] automatic_os_upgrade: Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when `upgrade_policy_mode` is set to `Rolling`. Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['ScaleSetBootDiagnosticsArgs']] boot_diagnostics: A boot diagnostics profile block as referenced below.
        :param pulumi.Input[str] eviction_policy: Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are `Deallocate` and `Delete`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetExtensionArgs']]]] extensions: Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.
        :param pulumi.Input[str] health_probe_id: Specifies the identifier for the load balancer health probe. Required when using `Rolling` as your `upgrade_policy_mode`.
        :param pulumi.Input[str] license_type: Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the virtual machine scale set resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetNetworkProfileArgs']]]] network_profiles: A collection of network profile block as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetOsProfileArgs']] os_profile: A Virtual Machine OS Profile block as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetOsProfileLinuxConfigArgs']] os_profile_linux_config: A Linux config block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetOsProfileSecretArgs']]]] os_profile_secrets: A collection of Secret blocks as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetOsProfileWindowsConfigArgs']] os_profile_windows_config: A Windows config block as documented below.
        :param pulumi.Input[bool] overprovision: Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.
        :param pulumi.Input[pulumi.InputType['ScaleSetPlanArgs']] plan: A plan block as documented below.
        :param pulumi.Input[str] priority: Specifies the priority for the Virtual Machines in the Scale Set. Defaults to `Regular`. Possible values are `Low` and `Regular`.
        :param pulumi.Input[str] proximity_placement_group_id: The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ScaleSetRollingUpgradePolicyArgs']] rolling_upgrade_policy: A `rolling_upgrade_policy` block as defined below. This is only applicable when the `upgrade_policy_mode` is `Rolling`.
        :param pulumi.Input[bool] single_placement_group: Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.
        :param pulumi.Input[pulumi.InputType['ScaleSetSkuArgs']] sku: A sku block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileDataDiskArgs']]]] storage_profile_data_disks: A storage profile data disk block as documented below
        :param pulumi.Input[pulumi.InputType['ScaleSetStorageProfileImageReferenceArgs']] storage_profile_image_reference: A storage profile image reference block as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetStorageProfileOsDiskArgs']] storage_profile_os_disk: A storage profile os disk block as documented below
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] upgrade_policy_mode: Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Rolling`, `Manual`, or `Automatic`. When choosing `Rolling`, you will need to set a health probe.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A collection of availability zones to spread the Virtual Machines over.
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

            __props__['automatic_os_upgrade'] = automatic_os_upgrade
            __props__['boot_diagnostics'] = boot_diagnostics
            __props__['eviction_policy'] = eviction_policy
            __props__['extensions'] = extensions
            __props__['health_probe_id'] = health_probe_id
            __props__['identity'] = identity
            __props__['license_type'] = license_type
            __props__['location'] = location
            __props__['name'] = name
            if network_profiles is None:
                raise TypeError("Missing required property 'network_profiles'")
            __props__['network_profiles'] = network_profiles
            if os_profile is None:
                raise TypeError("Missing required property 'os_profile'")
            __props__['os_profile'] = os_profile
            __props__['os_profile_linux_config'] = os_profile_linux_config
            __props__['os_profile_secrets'] = os_profile_secrets
            __props__['os_profile_windows_config'] = os_profile_windows_config
            __props__['overprovision'] = overprovision
            __props__['plan'] = plan
            __props__['priority'] = priority
            __props__['proximity_placement_group_id'] = proximity_placement_group_id
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['rolling_upgrade_policy'] = rolling_upgrade_policy
            __props__['single_placement_group'] = single_placement_group
            if sku is None:
                raise TypeError("Missing required property 'sku'")
            __props__['sku'] = sku
            __props__['storage_profile_data_disks'] = storage_profile_data_disks
            __props__['storage_profile_image_reference'] = storage_profile_image_reference
            if storage_profile_os_disk is None:
                raise TypeError("Missing required property 'storage_profile_os_disk'")
            __props__['storage_profile_os_disk'] = storage_profile_os_disk
            __props__['tags'] = tags
            if upgrade_policy_mode is None:
                raise TypeError("Missing required property 'upgrade_policy_mode'")
            __props__['upgrade_policy_mode'] = upgrade_policy_mode
            __props__['zones'] = zones
        super(ScaleSet, __self__).__init__(
            'azure:compute/scaleSet:ScaleSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automatic_os_upgrade: Optional[pulumi.Input[bool]] = None,
            boot_diagnostics: Optional[pulumi.Input[pulumi.InputType['ScaleSetBootDiagnosticsArgs']]] = None,
            eviction_policy: Optional[pulumi.Input[str]] = None,
            extensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetExtensionArgs']]]]] = None,
            health_probe_id: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['ScaleSetIdentityArgs']]] = None,
            license_type: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_profiles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetNetworkProfileArgs']]]]] = None,
            os_profile: Optional[pulumi.Input[pulumi.InputType['ScaleSetOsProfileArgs']]] = None,
            os_profile_linux_config: Optional[pulumi.Input[pulumi.InputType['ScaleSetOsProfileLinuxConfigArgs']]] = None,
            os_profile_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetOsProfileSecretArgs']]]]] = None,
            os_profile_windows_config: Optional[pulumi.Input[pulumi.InputType['ScaleSetOsProfileWindowsConfigArgs']]] = None,
            overprovision: Optional[pulumi.Input[bool]] = None,
            plan: Optional[pulumi.Input[pulumi.InputType['ScaleSetPlanArgs']]] = None,
            priority: Optional[pulumi.Input[str]] = None,
            proximity_placement_group_id: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            rolling_upgrade_policy: Optional[pulumi.Input[pulumi.InputType['ScaleSetRollingUpgradePolicyArgs']]] = None,
            single_placement_group: Optional[pulumi.Input[bool]] = None,
            sku: Optional[pulumi.Input[pulumi.InputType['ScaleSetSkuArgs']]] = None,
            storage_profile_data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileDataDiskArgs']]]]] = None,
            storage_profile_image_reference: Optional[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileImageReferenceArgs']]] = None,
            storage_profile_os_disk: Optional[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileOsDiskArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            upgrade_policy_mode: Optional[pulumi.Input[str]] = None,
            zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ScaleSet':
        """
        Get an existing ScaleSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] automatic_os_upgrade: Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when `upgrade_policy_mode` is set to `Rolling`. Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['ScaleSetBootDiagnosticsArgs']] boot_diagnostics: A boot diagnostics profile block as referenced below.
        :param pulumi.Input[str] eviction_policy: Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are `Deallocate` and `Delete`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetExtensionArgs']]]] extensions: Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.
        :param pulumi.Input[str] health_probe_id: Specifies the identifier for the load balancer health probe. Required when using `Rolling` as your `upgrade_policy_mode`.
        :param pulumi.Input[str] license_type: Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the virtual machine scale set resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetNetworkProfileArgs']]]] network_profiles: A collection of network profile block as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetOsProfileArgs']] os_profile: A Virtual Machine OS Profile block as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetOsProfileLinuxConfigArgs']] os_profile_linux_config: A Linux config block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetOsProfileSecretArgs']]]] os_profile_secrets: A collection of Secret blocks as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetOsProfileWindowsConfigArgs']] os_profile_windows_config: A Windows config block as documented below.
        :param pulumi.Input[bool] overprovision: Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.
        :param pulumi.Input[pulumi.InputType['ScaleSetPlanArgs']] plan: A plan block as documented below.
        :param pulumi.Input[str] priority: Specifies the priority for the Virtual Machines in the Scale Set. Defaults to `Regular`. Possible values are `Low` and `Regular`.
        :param pulumi.Input[str] proximity_placement_group_id: The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ScaleSetRollingUpgradePolicyArgs']] rolling_upgrade_policy: A `rolling_upgrade_policy` block as defined below. This is only applicable when the `upgrade_policy_mode` is `Rolling`.
        :param pulumi.Input[bool] single_placement_group: Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.
        :param pulumi.Input[pulumi.InputType['ScaleSetSkuArgs']] sku: A sku block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScaleSetStorageProfileDataDiskArgs']]]] storage_profile_data_disks: A storage profile data disk block as documented below
        :param pulumi.Input[pulumi.InputType['ScaleSetStorageProfileImageReferenceArgs']] storage_profile_image_reference: A storage profile image reference block as documented below.
        :param pulumi.Input[pulumi.InputType['ScaleSetStorageProfileOsDiskArgs']] storage_profile_os_disk: A storage profile os disk block as documented below
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] upgrade_policy_mode: Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Rolling`, `Manual`, or `Automatic`. When choosing `Rolling`, you will need to set a health probe.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A collection of availability zones to spread the Virtual Machines over.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["automatic_os_upgrade"] = automatic_os_upgrade
        __props__["boot_diagnostics"] = boot_diagnostics
        __props__["eviction_policy"] = eviction_policy
        __props__["extensions"] = extensions
        __props__["health_probe_id"] = health_probe_id
        __props__["identity"] = identity
        __props__["license_type"] = license_type
        __props__["location"] = location
        __props__["name"] = name
        __props__["network_profiles"] = network_profiles
        __props__["os_profile"] = os_profile
        __props__["os_profile_linux_config"] = os_profile_linux_config
        __props__["os_profile_secrets"] = os_profile_secrets
        __props__["os_profile_windows_config"] = os_profile_windows_config
        __props__["overprovision"] = overprovision
        __props__["plan"] = plan
        __props__["priority"] = priority
        __props__["proximity_placement_group_id"] = proximity_placement_group_id
        __props__["resource_group_name"] = resource_group_name
        __props__["rolling_upgrade_policy"] = rolling_upgrade_policy
        __props__["single_placement_group"] = single_placement_group
        __props__["sku"] = sku
        __props__["storage_profile_data_disks"] = storage_profile_data_disks
        __props__["storage_profile_image_reference"] = storage_profile_image_reference
        __props__["storage_profile_os_disk"] = storage_profile_os_disk
        __props__["tags"] = tags
        __props__["upgrade_policy_mode"] = upgrade_policy_mode
        __props__["zones"] = zones
        return ScaleSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automaticOsUpgrade")
    def automatic_os_upgrade(self) -> pulumi.Output[Optional[bool]]:
        """
        Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when `upgrade_policy_mode` is set to `Rolling`. Defaults to `false`.
        """
        return pulumi.get(self, "automatic_os_upgrade")

    @property
    @pulumi.getter(name="bootDiagnostics")
    def boot_diagnostics(self) -> pulumi.Output[Optional['outputs.ScaleSetBootDiagnostics']]:
        """
        A boot diagnostics profile block as referenced below.
        """
        return pulumi.get(self, "boot_diagnostics")

    @property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are `Deallocate` and `Delete`.
        """
        return pulumi.get(self, "eviction_policy")

    @property
    @pulumi.getter
    def extensions(self) -> pulumi.Output[Optional[Sequence['outputs.ScaleSetExtension']]]:
        """
        Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.
        """
        return pulumi.get(self, "extensions")

    @property
    @pulumi.getter(name="healthProbeId")
    def health_probe_id(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the identifier for the load balancer health probe. Required when using `Rolling` as your `upgrade_policy_mode`.
        """
        return pulumi.get(self, "health_probe_id")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.ScaleSetIdentity']:
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[str]:
        """
        Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the virtual machine scale set resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfiles")
    def network_profiles(self) -> pulumi.Output[Sequence['outputs.ScaleSetNetworkProfile']]:
        """
        A collection of network profile block as documented below.
        """
        return pulumi.get(self, "network_profiles")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output['outputs.ScaleSetOsProfile']:
        """
        A Virtual Machine OS Profile block as documented below.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="osProfileLinuxConfig")
    def os_profile_linux_config(self) -> pulumi.Output['outputs.ScaleSetOsProfileLinuxConfig']:
        """
        A Linux config block as documented below.
        """
        return pulumi.get(self, "os_profile_linux_config")

    @property
    @pulumi.getter(name="osProfileSecrets")
    def os_profile_secrets(self) -> pulumi.Output[Optional[Sequence['outputs.ScaleSetOsProfileSecret']]]:
        """
        A collection of Secret blocks as documented below.
        """
        return pulumi.get(self, "os_profile_secrets")

    @property
    @pulumi.getter(name="osProfileWindowsConfig")
    def os_profile_windows_config(self) -> pulumi.Output[Optional['outputs.ScaleSetOsProfileWindowsConfig']]:
        """
        A Windows config block as documented below.
        """
        return pulumi.get(self, "os_profile_windows_config")

    @property
    @pulumi.getter
    def overprovision(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.
        """
        return pulumi.get(self, "overprovision")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional['outputs.ScaleSetPlan']]:
        """
        A plan block as documented below.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the priority for the Virtual Machines in the Scale Set. Defaults to `Regular`. Possible values are `Low` and `Regular`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="proximityPlacementGroupId")
    def proximity_placement_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created
        """
        return pulumi.get(self, "proximity_placement_group_id")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="rollingUpgradePolicy")
    def rolling_upgrade_policy(self) -> pulumi.Output[Optional['outputs.ScaleSetRollingUpgradePolicy']]:
        """
        A `rolling_upgrade_policy` block as defined below. This is only applicable when the `upgrade_policy_mode` is `Rolling`.
        """
        return pulumi.get(self, "rolling_upgrade_policy")

    @property
    @pulumi.getter(name="singlePlacementGroup")
    def single_placement_group(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.
        """
        return pulumi.get(self, "single_placement_group")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.ScaleSetSku']:
        """
        A sku block as documented below.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageProfileDataDisks")
    def storage_profile_data_disks(self) -> pulumi.Output[Optional[Sequence['outputs.ScaleSetStorageProfileDataDisk']]]:
        """
        A storage profile data disk block as documented below
        """
        return pulumi.get(self, "storage_profile_data_disks")

    @property
    @pulumi.getter(name="storageProfileImageReference")
    def storage_profile_image_reference(self) -> pulumi.Output['outputs.ScaleSetStorageProfileImageReference']:
        """
        A storage profile image reference block as documented below.
        """
        return pulumi.get(self, "storage_profile_image_reference")

    @property
    @pulumi.getter(name="storageProfileOsDisk")
    def storage_profile_os_disk(self) -> pulumi.Output['outputs.ScaleSetStorageProfileOsDisk']:
        """
        A storage profile os disk block as documented below
        """
        return pulumi.get(self, "storage_profile_os_disk")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="upgradePolicyMode")
    def upgrade_policy_mode(self) -> pulumi.Output[str]:
        """
        Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Rolling`, `Manual`, or `Automatic`. When choosing `Rolling`, you will need to set a health probe.
        """
        return pulumi.get(self, "upgrade_policy_mode")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A collection of availability zones to spread the Virtual Machines over.
        """
        return pulumi.get(self, "zones")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

