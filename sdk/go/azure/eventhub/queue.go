// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eventhub

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manage and manage a ServiceBus Queue.
type Queue struct {
	s *pulumi.ResourceState
}

// NewQueue registers a new resource with the given unique name, arguments, and options.
func NewQueue(ctx *pulumi.Context,
	name string, args *QueueArgs, opts ...pulumi.ResourceOpt) (*Queue, error) {
	if args == nil || args.NamespaceName == nil {
		return nil, errors.New("missing required argument 'NamespaceName'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["autoDeleteOnIdle"] = nil
		inputs["deadLetteringOnMessageExpiration"] = nil
		inputs["defaultMessageTtl"] = nil
		inputs["duplicateDetectionHistoryTimeWindow"] = nil
		inputs["enableBatchedOperations"] = nil
		inputs["enableExpress"] = nil
		inputs["enablePartitioning"] = nil
		inputs["location"] = nil
		inputs["lockDuration"] = nil
		inputs["maxDeliveryCount"] = nil
		inputs["maxSizeInMegabytes"] = nil
		inputs["name"] = nil
		inputs["namespaceName"] = nil
		inputs["requiresDuplicateDetection"] = nil
		inputs["requiresSession"] = nil
		inputs["resourceGroupName"] = nil
		inputs["supportOrdering"] = nil
	} else {
		inputs["autoDeleteOnIdle"] = args.AutoDeleteOnIdle
		inputs["deadLetteringOnMessageExpiration"] = args.DeadLetteringOnMessageExpiration
		inputs["defaultMessageTtl"] = args.DefaultMessageTtl
		inputs["duplicateDetectionHistoryTimeWindow"] = args.DuplicateDetectionHistoryTimeWindow
		inputs["enableBatchedOperations"] = args.EnableBatchedOperations
		inputs["enableExpress"] = args.EnableExpress
		inputs["enablePartitioning"] = args.EnablePartitioning
		inputs["location"] = args.Location
		inputs["lockDuration"] = args.LockDuration
		inputs["maxDeliveryCount"] = args.MaxDeliveryCount
		inputs["maxSizeInMegabytes"] = args.MaxSizeInMegabytes
		inputs["name"] = args.Name
		inputs["namespaceName"] = args.NamespaceName
		inputs["requiresDuplicateDetection"] = args.RequiresDuplicateDetection
		inputs["requiresSession"] = args.RequiresSession
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["supportOrdering"] = args.SupportOrdering
	}
	s, err := ctx.RegisterResource("azure:eventhub/queue:Queue", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Queue{s: s}, nil
}

// GetQueue gets an existing Queue resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQueue(ctx *pulumi.Context,
	name string, id pulumi.ID, state *QueueState, opts ...pulumi.ResourceOpt) (*Queue, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["autoDeleteOnIdle"] = state.AutoDeleteOnIdle
		inputs["deadLetteringOnMessageExpiration"] = state.DeadLetteringOnMessageExpiration
		inputs["defaultMessageTtl"] = state.DefaultMessageTtl
		inputs["duplicateDetectionHistoryTimeWindow"] = state.DuplicateDetectionHistoryTimeWindow
		inputs["enableBatchedOperations"] = state.EnableBatchedOperations
		inputs["enableExpress"] = state.EnableExpress
		inputs["enablePartitioning"] = state.EnablePartitioning
		inputs["location"] = state.Location
		inputs["lockDuration"] = state.LockDuration
		inputs["maxDeliveryCount"] = state.MaxDeliveryCount
		inputs["maxSizeInMegabytes"] = state.MaxSizeInMegabytes
		inputs["name"] = state.Name
		inputs["namespaceName"] = state.NamespaceName
		inputs["requiresDuplicateDetection"] = state.RequiresDuplicateDetection
		inputs["requiresSession"] = state.RequiresSession
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["supportOrdering"] = state.SupportOrdering
	}
	s, err := ctx.ReadResource("azure:eventhub/queue:Queue", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Queue{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Queue) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Queue) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ISO 8601 timespan duration of the idle interval after which the
// Queue is automatically deleted, minimum of 5 minutes.
func (r *Queue) AutoDeleteOnIdle() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["autoDeleteOnIdle"])
}

// Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
func (r *Queue) DeadLetteringOnMessageExpiration() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["deadLetteringOnMessageExpiration"])
}

// The ISO 8601 timespan duration of the TTL of messages sent to this
// queue. This is the default value used when TTL is not set on message itself.
func (r *Queue) DefaultMessageTtl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultMessageTtl"])
}

// The ISO 8601 timespan duration during which
// duplicates can be detected. Default value is 10 minutes. (`PT10M`)
func (r *Queue) DuplicateDetectionHistoryTimeWindow() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["duplicateDetectionHistoryTimeWindow"])
}

func (r *Queue) EnableBatchedOperations() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enableBatchedOperations"])
}

// Boolean flag which controls whether Express Entities
// are enabled. An express queue holds a message in memory temporarily before writing
// it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
// be set to `false`.
func (r *Queue) EnableExpress() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enableExpress"])
}

// Boolean flag which controls whether to enable
// the queue to be partitioned across multiple message brokers. Changing this forces
// a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
// be set to `true`.
func (r *Queue) EnablePartitioning() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enablePartitioning"])
}

// Specifies the supported Azure location where the resource exists.
// Changing this forces a new resource to be created.
func (r *Queue) Location() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["location"])
}

// The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
func (r *Queue) LockDuration() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["lockDuration"])
}

// Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
func (r *Queue) MaxDeliveryCount() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["maxDeliveryCount"])
}

// Integer value which controls the size of
// memory allocated for the queue. For supported values see the "Queue/topic size"
// section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
func (r *Queue) MaxSizeInMegabytes() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["maxSizeInMegabytes"])
}

// Specifies the name of the ServiceBus Queue resource. Changing this forces a
// new resource to be created.
func (r *Queue) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the ServiceBus Namespace to create
// this queue in. Changing this forces a new resource to be created.
func (r *Queue) NamespaceName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namespaceName"])
}

// Boolean flag which controls whether
// the Queue requires duplicate detection. Changing this forces
// a new resource to be created. Defaults to `false`.
func (r *Queue) RequiresDuplicateDetection() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["requiresDuplicateDetection"])
}

// Boolean flag which controls whether the Queue requires sessions.
// This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
// a queue can guarantee first-in-first-out delivery of messages.
// Changing this forces a new resource to be created. Defaults to `false`.
func (r *Queue) RequiresSession() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["requiresSession"])
}

// The name of the resource group in which to
// create the namespace. Changing this forces a new resource to be created.
func (r *Queue) ResourceGroupName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

func (r *Queue) SupportOrdering() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["supportOrdering"])
}

// Input properties used for looking up and filtering Queue resources.
type QueueState struct {
	// The ISO 8601 timespan duration of the idle interval after which the
	// Queue is automatically deleted, minimum of 5 minutes.
	AutoDeleteOnIdle interface{}
	// Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
	DeadLetteringOnMessageExpiration interface{}
	// The ISO 8601 timespan duration of the TTL of messages sent to this
	// queue. This is the default value used when TTL is not set on message itself.
	DefaultMessageTtl interface{}
	// The ISO 8601 timespan duration during which
	// duplicates can be detected. Default value is 10 minutes. (`PT10M`)
	DuplicateDetectionHistoryTimeWindow interface{}
	EnableBatchedOperations interface{}
	// Boolean flag which controls whether Express Entities
	// are enabled. An express queue holds a message in memory temporarily before writing
	// it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
	// be set to `false`.
	EnableExpress interface{}
	// Boolean flag which controls whether to enable
	// the queue to be partitioned across multiple message brokers. Changing this forces
	// a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
	// be set to `true`.
	EnablePartitioning interface{}
	// Specifies the supported Azure location where the resource exists.
	// Changing this forces a new resource to be created.
	Location interface{}
	// The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
	LockDuration interface{}
	// Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
	MaxDeliveryCount interface{}
	// Integer value which controls the size of
	// memory allocated for the queue. For supported values see the "Queue/topic size"
	// section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
	MaxSizeInMegabytes interface{}
	// Specifies the name of the ServiceBus Queue resource. Changing this forces a
	// new resource to be created.
	Name interface{}
	// The name of the ServiceBus Namespace to create
	// this queue in. Changing this forces a new resource to be created.
	NamespaceName interface{}
	// Boolean flag which controls whether
	// the Queue requires duplicate detection. Changing this forces
	// a new resource to be created. Defaults to `false`.
	RequiresDuplicateDetection interface{}
	// Boolean flag which controls whether the Queue requires sessions.
	// This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
	// a queue can guarantee first-in-first-out delivery of messages.
	// Changing this forces a new resource to be created. Defaults to `false`.
	RequiresSession interface{}
	// The name of the resource group in which to
	// create the namespace. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	SupportOrdering interface{}
}

// The set of arguments for constructing a Queue resource.
type QueueArgs struct {
	// The ISO 8601 timespan duration of the idle interval after which the
	// Queue is automatically deleted, minimum of 5 minutes.
	AutoDeleteOnIdle interface{}
	// Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
	DeadLetteringOnMessageExpiration interface{}
	// The ISO 8601 timespan duration of the TTL of messages sent to this
	// queue. This is the default value used when TTL is not set on message itself.
	DefaultMessageTtl interface{}
	// The ISO 8601 timespan duration during which
	// duplicates can be detected. Default value is 10 minutes. (`PT10M`)
	DuplicateDetectionHistoryTimeWindow interface{}
	EnableBatchedOperations interface{}
	// Boolean flag which controls whether Express Entities
	// are enabled. An express queue holds a message in memory temporarily before writing
	// it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
	// be set to `false`.
	EnableExpress interface{}
	// Boolean flag which controls whether to enable
	// the queue to be partitioned across multiple message brokers. Changing this forces
	// a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
	// be set to `true`.
	EnablePartitioning interface{}
	// Specifies the supported Azure location where the resource exists.
	// Changing this forces a new resource to be created.
	Location interface{}
	// The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
	LockDuration interface{}
	// Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
	MaxDeliveryCount interface{}
	// Integer value which controls the size of
	// memory allocated for the queue. For supported values see the "Queue/topic size"
	// section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
	MaxSizeInMegabytes interface{}
	// Specifies the name of the ServiceBus Queue resource. Changing this forces a
	// new resource to be created.
	Name interface{}
	// The name of the ServiceBus Namespace to create
	// this queue in. Changing this forces a new resource to be created.
	NamespaceName interface{}
	// Boolean flag which controls whether
	// the Queue requires duplicate detection. Changing this forces
	// a new resource to be created. Defaults to `false`.
	RequiresDuplicateDetection interface{}
	// Boolean flag which controls whether the Queue requires sessions.
	// This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
	// a queue can guarantee first-in-first-out delivery of messages.
	// Changing this forces a new resource to be created. Defaults to `false`.
	RequiresSession interface{}
	// The name of the resource group in which to
	// create the namespace. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	SupportOrdering interface{}
}
