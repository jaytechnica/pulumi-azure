# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, certificate_data=None, certificate_policies=None, id=None, key_vault_id=None, name=None, secret_id=None, tags=None, thumbprint=None, version=None):
        if certificate_data and not isinstance(certificate_data, str):
            raise TypeError("Expected argument 'certificate_data' to be a str")
        __self__.certificate_data = certificate_data
        if certificate_policies and not isinstance(certificate_policies, list):
            raise TypeError("Expected argument 'certificate_policies' to be a list")
        __self__.certificate_policies = certificate_policies
        """
        A `certificate_policy` block as defined below.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if key_vault_id and not isinstance(key_vault_id, str):
            raise TypeError("Expected argument 'key_vault_id' to be a str")
        __self__.key_vault_id = key_vault_id
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the Certificate Issuer.
        """
        if secret_id and not isinstance(secret_id, str):
            raise TypeError("Expected argument 'secret_id' to be a str")
        __self__.secret_id = secret_id
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        __self__.thumbprint = thumbprint
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        __self__.version = version
class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            certificate_data=self.certificate_data,
            certificate_policies=self.certificate_policies,
            id=self.id,
            key_vault_id=self.key_vault_id,
            name=self.name,
            secret_id=self.secret_id,
            tags=self.tags,
            thumbprint=self.thumbprint,
            version=self.version)

def get_certificate(key_vault_id=None,name=None,version=None,opts=None):
    """
    Use this data source to access information about an existing Key Vault Certificate.

    > **Note:** All arguments including the secret value will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

    ## Example Usage



    ```python
    import pulumi
    import pulumi_azure as azure

    example_key_vault = azure.keyvault.get_key_vault(name="examplekv",
        resource_group_name="some-resource-group")
    example_certificate = azure.keyvault.get_certificate(name="secret-sauce",
        key_vault_id=example_key_vault.id)
    pulumi.export("certificateThumbprint", example_certificate.thumbprint)
    ```



    :param str key_vault_id: Specifies the ID of the Key Vault instance where the Secret resides, available on the `keyvault.KeyVault` Data Source / Resource.
    :param str name: Specifies the name of the Key Vault Secret.
    :param str version: Specifies the version of the certificate to look up.  (Defaults to latest) 
    """
    __args__ = dict()


    __args__['keyVaultId'] = key_vault_id
    __args__['name'] = name
    __args__['version'] = version
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:keyvault/getCertificate:getCertificate', __args__, opts=opts).value

    return AwaitableGetCertificateResult(
        certificate_data=__ret__.get('certificateData'),
        certificate_policies=__ret__.get('certificatePolicies'),
        id=__ret__.get('id'),
        key_vault_id=__ret__.get('keyVaultId'),
        name=__ret__.get('name'),
        secret_id=__ret__.get('secretId'),
        tags=__ret__.get('tags'),
        thumbprint=__ret__.get('thumbprint'),
        version=__ret__.get('version'))
