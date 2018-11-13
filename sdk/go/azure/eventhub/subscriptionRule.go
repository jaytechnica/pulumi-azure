// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eventhub

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manage a ServiceBus Subscription Rule.
type SubscriptionRule struct {
	s *pulumi.ResourceState
}

// NewSubscriptionRule registers a new resource with the given unique name, arguments, and options.
func NewSubscriptionRule(ctx *pulumi.Context,
	name string, args *SubscriptionRuleArgs, opts ...pulumi.ResourceOpt) (*SubscriptionRule, error) {
	if args == nil || args.FilterType == nil {
		return nil, errors.New("missing required argument 'FilterType'")
	}
	if args == nil || args.NamespaceName == nil {
		return nil, errors.New("missing required argument 'NamespaceName'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.SubscriptionName == nil {
		return nil, errors.New("missing required argument 'SubscriptionName'")
	}
	if args == nil || args.TopicName == nil {
		return nil, errors.New("missing required argument 'TopicName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["action"] = nil
		inputs["correlationFilter"] = nil
		inputs["filterType"] = nil
		inputs["name"] = nil
		inputs["namespaceName"] = nil
		inputs["resourceGroupName"] = nil
		inputs["sqlFilter"] = nil
		inputs["subscriptionName"] = nil
		inputs["topicName"] = nil
	} else {
		inputs["action"] = args.Action
		inputs["correlationFilter"] = args.CorrelationFilter
		inputs["filterType"] = args.FilterType
		inputs["name"] = args.Name
		inputs["namespaceName"] = args.NamespaceName
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["sqlFilter"] = args.SqlFilter
		inputs["subscriptionName"] = args.SubscriptionName
		inputs["topicName"] = args.TopicName
	}
	s, err := ctx.RegisterResource("azure:eventhub/subscriptionRule:SubscriptionRule", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SubscriptionRule{s: s}, nil
}

// GetSubscriptionRule gets an existing SubscriptionRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubscriptionRule(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SubscriptionRuleState, opts ...pulumi.ResourceOpt) (*SubscriptionRule, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["action"] = state.Action
		inputs["correlationFilter"] = state.CorrelationFilter
		inputs["filterType"] = state.FilterType
		inputs["name"] = state.Name
		inputs["namespaceName"] = state.NamespaceName
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["sqlFilter"] = state.SqlFilter
		inputs["subscriptionName"] = state.SubscriptionName
		inputs["topicName"] = state.TopicName
	}
	s, err := ctx.ReadResource("azure:eventhub/subscriptionRule:SubscriptionRule", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SubscriptionRule{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SubscriptionRule) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SubscriptionRule) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.
func (r *SubscriptionRule) Action() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["action"])
}

// A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.
func (r *SubscriptionRule) CorrelationFilter() *pulumi.Output {
	return r.s.State["correlationFilter"]
}

// Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.
func (r *SubscriptionRule) FilterType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["filterType"])
}

// Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.
func (r *SubscriptionRule) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.
func (r *SubscriptionRule) NamespaceName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namespaceName"])
}

// The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.
func (r *SubscriptionRule) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.
func (r *SubscriptionRule) SqlFilter() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["sqlFilter"])
}

// The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.
func (r *SubscriptionRule) SubscriptionName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["subscriptionName"])
}

// The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.
func (r *SubscriptionRule) TopicName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["topicName"])
}

// Input properties used for looking up and filtering SubscriptionRule resources.
type SubscriptionRuleState struct {
	// Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.
	Action interface{}
	// A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.
	CorrelationFilter interface{}
	// Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.
	FilterType interface{}
	// Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.
	NamespaceName interface{}
	// The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.
	SqlFilter interface{}
	// The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.
	SubscriptionName interface{}
	// The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.
	TopicName interface{}
}

// The set of arguments for constructing a SubscriptionRule resource.
type SubscriptionRuleArgs struct {
	// Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.
	Action interface{}
	// A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.
	CorrelationFilter interface{}
	// Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.
	FilterType interface{}
	// Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.
	Name interface{}
	// The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.
	NamespaceName interface{}
	// The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.
	SqlFilter interface{}
	// The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.
	SubscriptionName interface{}
	// The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.
	TopicName interface{}
}
