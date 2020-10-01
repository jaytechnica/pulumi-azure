# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'AssignmentIdentityArgs',
    'PolicySetDefinitionPolicyDefinitionReferenceArgs',
]

@pulumi.input_type
class AssignmentIdentityArgs:
    def __init__(__self__, *,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] principal_id: The Principal ID of this Policy Assignment if `type` is `SystemAssigned`.
        :param pulumi.Input[str] tenant_id: The Tenant ID of this Policy Assignment if `type` is `SystemAssigned`.
        :param pulumi.Input[str] type: The Managed Service Identity Type of this Policy Assignment. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), or `None` (no use of a Managed Service Identity).
        """
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Principal ID of this Policy Assignment if `type` is `SystemAssigned`.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID of this Policy Assignment if `type` is `SystemAssigned`.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The Managed Service Identity Type of this Policy Assignment. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), or `None` (no use of a Managed Service Identity).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class PolicySetDefinitionPolicyDefinitionReferenceArgs:
    def __init__(__self__, *,
                 policy_definition_id: pulumi.Input[str],
                 parameter_values: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 reference_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition or policy set definition that will be included in this policy set definition.
        :param pulumi.Input[str] parameter_values: Parameter values for the referenced policy rule. This field is a json object that allows you to assign parameters to this policy rule.
        :param pulumi.Input[Mapping[str, Any]] parameters: Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.
        :param pulumi.Input[str] reference_id: A unique ID within this policy set definition for this policy definition reference.
        """
        pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if parameter_values is not None:
            pulumi.set(__self__, "parameter_values", parameter_values)
        if parameters is not None:
            warnings.warn("Deprecated in favour of `parameter_values`", DeprecationWarning)
            pulumi.log.warn("parameters is deprecated: Deprecated in favour of `parameter_values`")
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if reference_id is not None:
            pulumi.set(__self__, "reference_id", reference_id)

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Input[str]:
        """
        The ID of the policy definition or policy set definition that will be included in this policy set definition.
        """
        return pulumi.get(self, "policy_definition_id")

    @policy_definition_id.setter
    def policy_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_definition_id", value)

    @property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[pulumi.Input[str]]:
        """
        Parameter values for the referenced policy rule. This field is a json object that allows you to assign parameters to this policy rule.
        """
        return pulumi.get(self, "parameter_values")

    @parameter_values.setter
    def parameter_values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_values", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[pulumi.Input[str]]:
        """
        A unique ID within this policy set definition for this policy definition reference.
        """
        return pulumi.get(self, "reference_id")

    @reference_id.setter
    def reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reference_id", value)


