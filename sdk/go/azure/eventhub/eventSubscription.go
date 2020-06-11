// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eventhub

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an EventGrid Event Subscription
//
// Deprecated: azure.eventhub.EventSubscription has been deprecated in favor of azure.eventgrid.EventSubscription
type EventSubscription struct {
	pulumi.CustomResourceState

	// A `advancedFilter` block as defined below.
	AdvancedFilter EventSubscriptionAdvancedFilterPtrOutput `pulumi:"advancedFilter"`
	// An `azureFunctionEndpoint` block as defined below.
	AzureFunctionEndpoint EventSubscriptionAzureFunctionEndpointPtrOutput `pulumi:"azureFunctionEndpoint"`
	// Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventSchemaV1_0`, `CustomInputSchema`. Defaults to `EventGridSchema`. Changing this forces a new resource to be created.
	EventDeliverySchema pulumi.StringPtrOutput `pulumi:"eventDeliverySchema"`
	// A `eventhubEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `eventhub_endpoint_id`
	EventhubEndpoint EventSubscriptionEventhubEndpointOutput `pulumi:"eventhubEndpoint"`
	// Specifies the id where the Event Hub is located.
	EventhubEndpointId pulumi.StringOutput `pulumi:"eventhubEndpointId"`
	// Specifies the expiration time of the event subscription (Datetime Format `RFC 3339`).
	ExpirationTimeUtc pulumi.StringPtrOutput `pulumi:"expirationTimeUtc"`
	// A `hybridConnectionEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `hybrid_connection_endpoint_id`
	HybridConnectionEndpoint EventSubscriptionHybridConnectionEndpointOutput `pulumi:"hybridConnectionEndpoint"`
	// Specifies the id where the Hybrid Connection is located.
	HybridConnectionEndpointId pulumi.StringOutput `pulumi:"hybridConnectionEndpointId"`
	// A list of applicable event types that need to be part of the event subscription.
	IncludedEventTypes pulumi.StringArrayOutput `pulumi:"includedEventTypes"`
	// A list of labels to assign to the event subscription.
	Labels pulumi.StringArrayOutput `pulumi:"labels"`
	// Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// A `retryPolicy` block as defined below.
	RetryPolicy EventSubscriptionRetryPolicyOutput `pulumi:"retryPolicy"`
	// Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
	Scope pulumi.StringOutput `pulumi:"scope"`
	// Specifies the id where the Service Bus Queue is located.
	ServiceBusQueueEndpointId pulumi.StringPtrOutput `pulumi:"serviceBusQueueEndpointId"`
	// Specifies the id where the Service Bus Topic is located.
	ServiceBusTopicEndpointId pulumi.StringPtrOutput `pulumi:"serviceBusTopicEndpointId"`
	// A `storageBlobDeadLetterDestination` block as defined below.
	StorageBlobDeadLetterDestination EventSubscriptionStorageBlobDeadLetterDestinationPtrOutput `pulumi:"storageBlobDeadLetterDestination"`
	// A `storageQueueEndpoint` block as defined below.
	StorageQueueEndpoint EventSubscriptionStorageQueueEndpointPtrOutput `pulumi:"storageQueueEndpoint"`
	// A `subjectFilter` block as defined below.
	SubjectFilter EventSubscriptionSubjectFilterPtrOutput `pulumi:"subjectFilter"`
	// (Optional) Specifies the name of the topic to associate with the event subscription.
	TopicName pulumi.StringOutput `pulumi:"topicName"`
	// A `webhookEndpoint` block as defined below.
	WebhookEndpoint EventSubscriptionWebhookEndpointPtrOutput `pulumi:"webhookEndpoint"`
}

// NewEventSubscription registers a new resource with the given unique name, arguments, and options.
func NewEventSubscription(ctx *pulumi.Context,
	name string, args *EventSubscriptionArgs, opts ...pulumi.ResourceOption) (*EventSubscription, error) {
	if args == nil || args.Scope == nil {
		return nil, errors.New("missing required argument 'Scope'")
	}
	if args == nil {
		args = &EventSubscriptionArgs{}
	}
	var resource EventSubscription
	err := ctx.RegisterResource("azure:eventhub/eventSubscription:EventSubscription", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEventSubscription gets an existing EventSubscription resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEventSubscription(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EventSubscriptionState, opts ...pulumi.ResourceOption) (*EventSubscription, error) {
	var resource EventSubscription
	err := ctx.ReadResource("azure:eventhub/eventSubscription:EventSubscription", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EventSubscription resources.
type eventSubscriptionState struct {
	// A `advancedFilter` block as defined below.
	AdvancedFilter *EventSubscriptionAdvancedFilter `pulumi:"advancedFilter"`
	// An `azureFunctionEndpoint` block as defined below.
	AzureFunctionEndpoint *EventSubscriptionAzureFunctionEndpoint `pulumi:"azureFunctionEndpoint"`
	// Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventSchemaV1_0`, `CustomInputSchema`. Defaults to `EventGridSchema`. Changing this forces a new resource to be created.
	EventDeliverySchema *string `pulumi:"eventDeliverySchema"`
	// A `eventhubEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `eventhub_endpoint_id`
	EventhubEndpoint *EventSubscriptionEventhubEndpoint `pulumi:"eventhubEndpoint"`
	// Specifies the id where the Event Hub is located.
	EventhubEndpointId *string `pulumi:"eventhubEndpointId"`
	// Specifies the expiration time of the event subscription (Datetime Format `RFC 3339`).
	ExpirationTimeUtc *string `pulumi:"expirationTimeUtc"`
	// A `hybridConnectionEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `hybrid_connection_endpoint_id`
	HybridConnectionEndpoint *EventSubscriptionHybridConnectionEndpoint `pulumi:"hybridConnectionEndpoint"`
	// Specifies the id where the Hybrid Connection is located.
	HybridConnectionEndpointId *string `pulumi:"hybridConnectionEndpointId"`
	// A list of applicable event types that need to be part of the event subscription.
	IncludedEventTypes []string `pulumi:"includedEventTypes"`
	// A list of labels to assign to the event subscription.
	Labels []string `pulumi:"labels"`
	// Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// A `retryPolicy` block as defined below.
	RetryPolicy *EventSubscriptionRetryPolicy `pulumi:"retryPolicy"`
	// Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
	Scope *string `pulumi:"scope"`
	// Specifies the id where the Service Bus Queue is located.
	ServiceBusQueueEndpointId *string `pulumi:"serviceBusQueueEndpointId"`
	// Specifies the id where the Service Bus Topic is located.
	ServiceBusTopicEndpointId *string `pulumi:"serviceBusTopicEndpointId"`
	// A `storageBlobDeadLetterDestination` block as defined below.
	StorageBlobDeadLetterDestination *EventSubscriptionStorageBlobDeadLetterDestination `pulumi:"storageBlobDeadLetterDestination"`
	// A `storageQueueEndpoint` block as defined below.
	StorageQueueEndpoint *EventSubscriptionStorageQueueEndpoint `pulumi:"storageQueueEndpoint"`
	// A `subjectFilter` block as defined below.
	SubjectFilter *EventSubscriptionSubjectFilter `pulumi:"subjectFilter"`
	// (Optional) Specifies the name of the topic to associate with the event subscription.
	TopicName *string `pulumi:"topicName"`
	// A `webhookEndpoint` block as defined below.
	WebhookEndpoint *EventSubscriptionWebhookEndpoint `pulumi:"webhookEndpoint"`
}

type EventSubscriptionState struct {
	// A `advancedFilter` block as defined below.
	AdvancedFilter EventSubscriptionAdvancedFilterPtrInput
	// An `azureFunctionEndpoint` block as defined below.
	AzureFunctionEndpoint EventSubscriptionAzureFunctionEndpointPtrInput
	// Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventSchemaV1_0`, `CustomInputSchema`. Defaults to `EventGridSchema`. Changing this forces a new resource to be created.
	EventDeliverySchema pulumi.StringPtrInput
	// A `eventhubEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `eventhub_endpoint_id`
	EventhubEndpoint EventSubscriptionEventhubEndpointPtrInput
	// Specifies the id where the Event Hub is located.
	EventhubEndpointId pulumi.StringPtrInput
	// Specifies the expiration time of the event subscription (Datetime Format `RFC 3339`).
	ExpirationTimeUtc pulumi.StringPtrInput
	// A `hybridConnectionEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `hybrid_connection_endpoint_id`
	HybridConnectionEndpoint EventSubscriptionHybridConnectionEndpointPtrInput
	// Specifies the id where the Hybrid Connection is located.
	HybridConnectionEndpointId pulumi.StringPtrInput
	// A list of applicable event types that need to be part of the event subscription.
	IncludedEventTypes pulumi.StringArrayInput
	// A list of labels to assign to the event subscription.
	Labels pulumi.StringArrayInput
	// Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// A `retryPolicy` block as defined below.
	RetryPolicy EventSubscriptionRetryPolicyPtrInput
	// Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
	Scope pulumi.StringPtrInput
	// Specifies the id where the Service Bus Queue is located.
	ServiceBusQueueEndpointId pulumi.StringPtrInput
	// Specifies the id where the Service Bus Topic is located.
	ServiceBusTopicEndpointId pulumi.StringPtrInput
	// A `storageBlobDeadLetterDestination` block as defined below.
	StorageBlobDeadLetterDestination EventSubscriptionStorageBlobDeadLetterDestinationPtrInput
	// A `storageQueueEndpoint` block as defined below.
	StorageQueueEndpoint EventSubscriptionStorageQueueEndpointPtrInput
	// A `subjectFilter` block as defined below.
	SubjectFilter EventSubscriptionSubjectFilterPtrInput
	// (Optional) Specifies the name of the topic to associate with the event subscription.
	TopicName pulumi.StringPtrInput
	// A `webhookEndpoint` block as defined below.
	WebhookEndpoint EventSubscriptionWebhookEndpointPtrInput
}

func (EventSubscriptionState) ElementType() reflect.Type {
	return reflect.TypeOf((*eventSubscriptionState)(nil)).Elem()
}

type eventSubscriptionArgs struct {
	// A `advancedFilter` block as defined below.
	AdvancedFilter *EventSubscriptionAdvancedFilter `pulumi:"advancedFilter"`
	// An `azureFunctionEndpoint` block as defined below.
	AzureFunctionEndpoint *EventSubscriptionAzureFunctionEndpoint `pulumi:"azureFunctionEndpoint"`
	// Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventSchemaV1_0`, `CustomInputSchema`. Defaults to `EventGridSchema`. Changing this forces a new resource to be created.
	EventDeliverySchema *string `pulumi:"eventDeliverySchema"`
	// A `eventhubEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `eventhub_endpoint_id`
	EventhubEndpoint *EventSubscriptionEventhubEndpoint `pulumi:"eventhubEndpoint"`
	// Specifies the id where the Event Hub is located.
	EventhubEndpointId *string `pulumi:"eventhubEndpointId"`
	// Specifies the expiration time of the event subscription (Datetime Format `RFC 3339`).
	ExpirationTimeUtc *string `pulumi:"expirationTimeUtc"`
	// A `hybridConnectionEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `hybrid_connection_endpoint_id`
	HybridConnectionEndpoint *EventSubscriptionHybridConnectionEndpoint `pulumi:"hybridConnectionEndpoint"`
	// Specifies the id where the Hybrid Connection is located.
	HybridConnectionEndpointId *string `pulumi:"hybridConnectionEndpointId"`
	// A list of applicable event types that need to be part of the event subscription.
	IncludedEventTypes []string `pulumi:"includedEventTypes"`
	// A list of labels to assign to the event subscription.
	Labels []string `pulumi:"labels"`
	// Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// A `retryPolicy` block as defined below.
	RetryPolicy *EventSubscriptionRetryPolicy `pulumi:"retryPolicy"`
	// Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
	Scope string `pulumi:"scope"`
	// Specifies the id where the Service Bus Queue is located.
	ServiceBusQueueEndpointId *string `pulumi:"serviceBusQueueEndpointId"`
	// Specifies the id where the Service Bus Topic is located.
	ServiceBusTopicEndpointId *string `pulumi:"serviceBusTopicEndpointId"`
	// A `storageBlobDeadLetterDestination` block as defined below.
	StorageBlobDeadLetterDestination *EventSubscriptionStorageBlobDeadLetterDestination `pulumi:"storageBlobDeadLetterDestination"`
	// A `storageQueueEndpoint` block as defined below.
	StorageQueueEndpoint *EventSubscriptionStorageQueueEndpoint `pulumi:"storageQueueEndpoint"`
	// A `subjectFilter` block as defined below.
	SubjectFilter *EventSubscriptionSubjectFilter `pulumi:"subjectFilter"`
	// (Optional) Specifies the name of the topic to associate with the event subscription.
	TopicName *string `pulumi:"topicName"`
	// A `webhookEndpoint` block as defined below.
	WebhookEndpoint *EventSubscriptionWebhookEndpoint `pulumi:"webhookEndpoint"`
}

// The set of arguments for constructing a EventSubscription resource.
type EventSubscriptionArgs struct {
	// A `advancedFilter` block as defined below.
	AdvancedFilter EventSubscriptionAdvancedFilterPtrInput
	// An `azureFunctionEndpoint` block as defined below.
	AzureFunctionEndpoint EventSubscriptionAzureFunctionEndpointPtrInput
	// Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventSchemaV1_0`, `CustomInputSchema`. Defaults to `EventGridSchema`. Changing this forces a new resource to be created.
	EventDeliverySchema pulumi.StringPtrInput
	// A `eventhubEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `eventhub_endpoint_id`
	EventhubEndpoint EventSubscriptionEventhubEndpointPtrInput
	// Specifies the id where the Event Hub is located.
	EventhubEndpointId pulumi.StringPtrInput
	// Specifies the expiration time of the event subscription (Datetime Format `RFC 3339`).
	ExpirationTimeUtc pulumi.StringPtrInput
	// A `hybridConnectionEndpoint` block as defined below.
	//
	// Deprecated: Deprecated in favour of `hybrid_connection_endpoint_id`
	HybridConnectionEndpoint EventSubscriptionHybridConnectionEndpointPtrInput
	// Specifies the id where the Hybrid Connection is located.
	HybridConnectionEndpointId pulumi.StringPtrInput
	// A list of applicable event types that need to be part of the event subscription.
	IncludedEventTypes pulumi.StringArrayInput
	// A list of labels to assign to the event subscription.
	Labels pulumi.StringArrayInput
	// Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// A `retryPolicy` block as defined below.
	RetryPolicy EventSubscriptionRetryPolicyPtrInput
	// Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
	Scope pulumi.StringInput
	// Specifies the id where the Service Bus Queue is located.
	ServiceBusQueueEndpointId pulumi.StringPtrInput
	// Specifies the id where the Service Bus Topic is located.
	ServiceBusTopicEndpointId pulumi.StringPtrInput
	// A `storageBlobDeadLetterDestination` block as defined below.
	StorageBlobDeadLetterDestination EventSubscriptionStorageBlobDeadLetterDestinationPtrInput
	// A `storageQueueEndpoint` block as defined below.
	StorageQueueEndpoint EventSubscriptionStorageQueueEndpointPtrInput
	// A `subjectFilter` block as defined below.
	SubjectFilter EventSubscriptionSubjectFilterPtrInput
	// (Optional) Specifies the name of the topic to associate with the event subscription.
	TopicName pulumi.StringPtrInput
	// A `webhookEndpoint` block as defined below.
	WebhookEndpoint EventSubscriptionWebhookEndpointPtrInput
}

func (EventSubscriptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eventSubscriptionArgs)(nil)).Elem()
}
