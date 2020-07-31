# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Policy(pulumi.CustomResource):
    custom_rules: pulumi.Output[list]
    """
    One or more `custom_rules` blocks as defined below.

      * `action` (`str`) - Type of action.
      * `matchConditions` (`list`) - One or more `match_conditions` blocks as defined below.
        * `matchValues` (`list`) - A list of match values.
        * `matchVariables` (`list`) - One or more `match_variables` blocks as defined below.
          * `selector` (`str`) - Describes field of the matchVariable collection
          * `variableName` (`str`) - The name of the Match Variable

        * `negationCondition` (`bool`) - Describes if this is negate condition or not
        * `operator` (`str`) - Describes operator to be matched.
        * `transforms` (`list`) - A list of transformations to do before the match is attempted.

      * `name` (`str`) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.
      * `priority` (`float`) - Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value.
      * `ruleType` (`str`) - Describes the type of rule.
    """
    location: pulumi.Output[str]
    """
    Resource location. Changing this forces a new resource to be created.
    """
    managed_rules: pulumi.Output[dict]
    """
    A `managed_rules` blocks as defined below.

      * `exclusions` (`list`) - One or more `exclusion` block defined below.
        * `matchVariable` (`str`) - The name of the Match Variable. Possible values: `RequestArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
        * `selector` (`str`) - Describes field of the matchVariable collection.
        * `selectorMatchOperator` (`str`) - Describes operator to be matched. Possible values: `Contains`, `EndsWith`, `Equals`, `EqualsAny`, `StartsWith`.

      * `managedRuleSets` (`list`) - One or more `managed_rule_set` block defined below.
        * `ruleGroupOverrides` (`list`) - One or more `rule_group_override` block defined below.
          * `disabledRules` (`list`) - One or more Rule ID's
          * `ruleGroupName` (`str`) - The name of the Rule Group

        * `type` (`str`) - The rule set type. Possible values: `Microsoft_BotManagerRuleSet` and `OWASP`.
        * `version` (`str`) - The rule set version. Possible values: `0.1`, `1.0`, `2.2.9`, `3.0` and `3.1`.
    """
    name: pulumi.Output[str]
    """
    The name of the policy. Changing this forces a new resource to be created.
    """
    policy_settings: pulumi.Output[dict]
    """
    A `policy_settings` block as defined below.

      * `enabled` (`bool`) - Describes if the policy is in enabled state or disabled state. Defaults to `Enabled`.
      * `fileUploadLimitInMb` (`float`)
      * `maxRequestBodySizeInKb` (`float`)
      * `mode` (`str`) - Describes if it is in detection mode or prevention mode at the policy level. Defaults to `Prevention`.
      * `requestBodyCheck` (`bool`) - Is Request Body Inspection enabled? Defaults to `true`.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the Web Application Firewall Policy.
    """
    def __init__(__self__, resource_name, opts=None, custom_rules=None, location=None, managed_rules=None, name=None, policy_settings=None, resource_group_name=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Azure Web Application Firewall Policy instance.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US 2")
        example_policy = azure.waf.Policy("examplePolicy",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            custom_rules=[
                {
                    "name": "Rule1",
                    "priority": 1,
                    "ruleType": "MatchRule",
                    "matchConditions": [{
                        "matchVariables": [{
                            "variableName": "RemoteAddr",
                        }],
                        "operator": "IPMatch",
                        "negationCondition": False,
                        "matchValues": [
                            "192.168.1.0/24",
                            "10.0.0.0/24",
                        ],
                    }],
                    "action": "Block",
                },
                {
                    "name": "Rule2",
                    "priority": 2,
                    "ruleType": "MatchRule",
                    "matchConditions": [
                        {
                            "matchVariables": [{
                                "variableName": "RemoteAddr",
                            }],
                            "operator": "IPMatch",
                            "negationCondition": False,
                            "matchValues": ["192.168.1.0/24"],
                        },
                        {
                            "matchVariables": [{
                                "variableName": "RequestHeaders",
                                "selector": "UserAgent",
                            }],
                            "operator": "Contains",
                            "negationCondition": False,
                            "matchValues": ["Windows"],
                        },
                    ],
                    "action": "Block",
                },
            ],
            policy_settings={
                "enabled": True,
                "mode": "Prevention",
                "requestBodyCheck": True,
                "fileUploadLimitInMb": 100,
                "maxRequestBodySizeInKb": 128,
            },
            managed_rules={
                "exclusions": [
                    {
                        "matchVariable": "RequestHeaderNames",
                        "selector": "x-company-secret-header",
                        "selectorMatchOperator": "Equals",
                    },
                    {
                        "matchVariable": "RequestCookieNames",
                        "selector": "too-tasty",
                        "selectorMatchOperator": "EndsWith",
                    },
                ],
                "managedRuleSets": [{
                    "type": "OWASP",
                    "version": "3.1",
                    "ruleGroupOverrides": [{
                        "ruleGroupName": "REQUEST-920-PROTOCOL-ENFORCEMENT",
                        "disabledRules": [
                            "920300",
                            "920440",
                        ],
                    }],
                }],
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] custom_rules: One or more `custom_rules` blocks as defined below.
        :param pulumi.Input[str] location: Resource location. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] managed_rules: A `managed_rules` blocks as defined below.
        :param pulumi.Input[str] name: The name of the policy. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] policy_settings: A `policy_settings` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the Web Application Firewall Policy.

        The **custom_rules** object supports the following:

          * `action` (`pulumi.Input[str]`) - Type of action.
          * `matchConditions` (`pulumi.Input[list]`) - One or more `match_conditions` blocks as defined below.
            * `matchValues` (`pulumi.Input[list]`) - A list of match values.
            * `matchVariables` (`pulumi.Input[list]`) - One or more `match_variables` blocks as defined below.
              * `selector` (`pulumi.Input[str]`) - Describes field of the matchVariable collection
              * `variableName` (`pulumi.Input[str]`) - The name of the Match Variable

            * `negationCondition` (`pulumi.Input[bool]`) - Describes if this is negate condition or not
            * `operator` (`pulumi.Input[str]`) - Describes operator to be matched.
            * `transforms` (`pulumi.Input[list]`) - A list of transformations to do before the match is attempted.

          * `name` (`pulumi.Input[str]`) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.
          * `priority` (`pulumi.Input[float]`) - Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value.
          * `ruleType` (`pulumi.Input[str]`) - Describes the type of rule.

        The **managed_rules** object supports the following:

          * `exclusions` (`pulumi.Input[list]`) - One or more `exclusion` block defined below.
            * `matchVariable` (`pulumi.Input[str]`) - The name of the Match Variable. Possible values: `RequestArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
            * `selector` (`pulumi.Input[str]`) - Describes field of the matchVariable collection.
            * `selectorMatchOperator` (`pulumi.Input[str]`) - Describes operator to be matched. Possible values: `Contains`, `EndsWith`, `Equals`, `EqualsAny`, `StartsWith`.

          * `managedRuleSets` (`pulumi.Input[list]`) - One or more `managed_rule_set` block defined below.
            * `ruleGroupOverrides` (`pulumi.Input[list]`) - One or more `rule_group_override` block defined below.
              * `disabledRules` (`pulumi.Input[list]`) - One or more Rule ID's
              * `ruleGroupName` (`pulumi.Input[str]`) - The name of the Rule Group

            * `type` (`pulumi.Input[str]`) - The rule set type. Possible values: `Microsoft_BotManagerRuleSet` and `OWASP`.
            * `version` (`pulumi.Input[str]`) - The rule set version. Possible values: `0.1`, `1.0`, `2.2.9`, `3.0` and `3.1`.

        The **policy_settings** object supports the following:

          * `enabled` (`pulumi.Input[bool]`) - Describes if the policy is in enabled state or disabled state. Defaults to `Enabled`.
          * `fileUploadLimitInMb` (`pulumi.Input[float]`)
          * `maxRequestBodySizeInKb` (`pulumi.Input[float]`)
          * `mode` (`pulumi.Input[str]`) - Describes if it is in detection mode or prevention mode at the policy level. Defaults to `Prevention`.
          * `requestBodyCheck` (`pulumi.Input[bool]`) - Is Request Body Inspection enabled? Defaults to `true`.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['custom_rules'] = custom_rules
            __props__['location'] = location
            if managed_rules is None:
                raise TypeError("Missing required property 'managed_rules'")
            __props__['managed_rules'] = managed_rules
            __props__['name'] = name
            __props__['policy_settings'] = policy_settings
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
        super(Policy, __self__).__init__(
            'azure:waf/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, custom_rules=None, location=None, managed_rules=None, name=None, policy_settings=None, resource_group_name=None, tags=None):
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] custom_rules: One or more `custom_rules` blocks as defined below.
        :param pulumi.Input[str] location: Resource location. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] managed_rules: A `managed_rules` blocks as defined below.
        :param pulumi.Input[str] name: The name of the policy. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] policy_settings: A `policy_settings` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the Web Application Firewall Policy.

        The **custom_rules** object supports the following:

          * `action` (`pulumi.Input[str]`) - Type of action.
          * `matchConditions` (`pulumi.Input[list]`) - One or more `match_conditions` blocks as defined below.
            * `matchValues` (`pulumi.Input[list]`) - A list of match values.
            * `matchVariables` (`pulumi.Input[list]`) - One or more `match_variables` blocks as defined below.
              * `selector` (`pulumi.Input[str]`) - Describes field of the matchVariable collection
              * `variableName` (`pulumi.Input[str]`) - The name of the Match Variable

            * `negationCondition` (`pulumi.Input[bool]`) - Describes if this is negate condition or not
            * `operator` (`pulumi.Input[str]`) - Describes operator to be matched.
            * `transforms` (`pulumi.Input[list]`) - A list of transformations to do before the match is attempted.

          * `name` (`pulumi.Input[str]`) - Gets name of the resource that is unique within a policy. This name can be used to access the resource.
          * `priority` (`pulumi.Input[float]`) - Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value.
          * `ruleType` (`pulumi.Input[str]`) - Describes the type of rule.

        The **managed_rules** object supports the following:

          * `exclusions` (`pulumi.Input[list]`) - One or more `exclusion` block defined below.
            * `matchVariable` (`pulumi.Input[str]`) - The name of the Match Variable. Possible values: `RequestArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
            * `selector` (`pulumi.Input[str]`) - Describes field of the matchVariable collection.
            * `selectorMatchOperator` (`pulumi.Input[str]`) - Describes operator to be matched. Possible values: `Contains`, `EndsWith`, `Equals`, `EqualsAny`, `StartsWith`.

          * `managedRuleSets` (`pulumi.Input[list]`) - One or more `managed_rule_set` block defined below.
            * `ruleGroupOverrides` (`pulumi.Input[list]`) - One or more `rule_group_override` block defined below.
              * `disabledRules` (`pulumi.Input[list]`) - One or more Rule ID's
              * `ruleGroupName` (`pulumi.Input[str]`) - The name of the Rule Group

            * `type` (`pulumi.Input[str]`) - The rule set type. Possible values: `Microsoft_BotManagerRuleSet` and `OWASP`.
            * `version` (`pulumi.Input[str]`) - The rule set version. Possible values: `0.1`, `1.0`, `2.2.9`, `3.0` and `3.1`.

        The **policy_settings** object supports the following:

          * `enabled` (`pulumi.Input[bool]`) - Describes if the policy is in enabled state or disabled state. Defaults to `Enabled`.
          * `fileUploadLimitInMb` (`pulumi.Input[float]`)
          * `maxRequestBodySizeInKb` (`pulumi.Input[float]`)
          * `mode` (`pulumi.Input[str]`) - Describes if it is in detection mode or prevention mode at the policy level. Defaults to `Prevention`.
          * `requestBodyCheck` (`pulumi.Input[bool]`) - Is Request Body Inspection enabled? Defaults to `true`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["custom_rules"] = custom_rules
        __props__["location"] = location
        __props__["managed_rules"] = managed_rules
        __props__["name"] = name
        __props__["policy_settings"] = policy_settings
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        return Policy(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
