// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.CosmosDB
{
    /// <summary>
    /// Manages a CosmosDB (formally DocumentDB) Account.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cosmosdb_account.html.markdown.
    /// </summary>
    public partial class Account : Pulumi.CustomResource
    {
        /// <summary>
        /// The capabilities which should be enabled for this Cosmos DB account. Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        [Output("capabilities")]
        public Output<ImmutableArray<Outputs.AccountCapabilities>> Capabilities { get; private set; } = null!;

        /// <summary>
        /// A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.
        /// </summary>
        [Output("connectionStrings")]
        public Output<ImmutableArray<string>> ConnectionStrings { get; private set; } = null!;

        /// <summary>
        /// Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.
        /// </summary>
        [Output("consistencyPolicy")]
        public Output<Outputs.AccountConsistencyPolicy> ConsistencyPolicy { get; private set; } = null!;

        /// <summary>
        /// Enable automatic fail over for this Cosmos DB account.
        /// </summary>
        [Output("enableAutomaticFailover")]
        public Output<bool?> EnableAutomaticFailover { get; private set; } = null!;

        /// <summary>
        /// Enable multi-master support for this Cosmos DB account.
        /// </summary>
        [Output("enableMultipleWriteLocations")]
        public Output<bool?> EnableMultipleWriteLocations { get; private set; } = null!;

        /// <summary>
        /// The endpoint used to connect to the CosmosDB account.
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        [Output("failoverPolicies")]
        public Output<ImmutableArray<Outputs.AccountFailoverPolicies>> FailoverPolicies { get; private set; } = null!;

        /// <summary>
        /// Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.
        /// </summary>
        [Output("geoLocations")]
        public Output<ImmutableArray<Outputs.AccountGeoLocations>> GeoLocations { get; private set; } = null!;

        /// <summary>
        /// CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.
        /// </summary>
        [Output("ipRangeFilter")]
        public Output<string?> IpRangeFilter { get; private set; } = null!;

        /// <summary>
        /// Enables virtual network filtering for this Cosmos DB account.
        /// </summary>
        [Output("isVirtualNetworkFilterEnabled")]
        public Output<bool?> IsVirtualNetworkFilterEnabled { get; private set; } = null!;

        /// <summary>
        /// Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.
        /// </summary>
        [Output("kind")]
        public Output<string?> Kind { get; private set; } = null!;

        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The capability to enable - Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.
        /// </summary>
        [Output("offerType")]
        public Output<string> OfferType { get; private set; } = null!;

        /// <summary>
        /// The Primary master key for the CosmosDB Account.
        /// </summary>
        [Output("primaryMasterKey")]
        public Output<string> PrimaryMasterKey { get; private set; } = null!;

        /// <summary>
        /// The Primary read-only master Key for the CosmosDB Account.
        /// </summary>
        [Output("primaryReadonlyMasterKey")]
        public Output<string> PrimaryReadonlyMasterKey { get; private set; } = null!;

        /// <summary>
        /// A list of read endpoints available for this CosmosDB account.
        /// </summary>
        [Output("readEndpoints")]
        public Output<ImmutableArray<string>> ReadEndpoints { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The Secondary master key for the CosmosDB Account.
        /// </summary>
        [Output("secondaryMasterKey")]
        public Output<string> SecondaryMasterKey { get; private set; } = null!;

        /// <summary>
        /// The Secondary read-only master key for the CosmosDB Account.
        /// </summary>
        [Output("secondaryReadonlyMasterKey")]
        public Output<string> SecondaryReadonlyMasterKey { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>> Tags { get; private set; } = null!;

        /// <summary>
        /// Specifies a `virtual_network_rules` resource, used to define which subnets are allowed to access this CosmosDB account.
        /// </summary>
        [Output("virtualNetworkRules")]
        public Output<ImmutableArray<Outputs.AccountVirtualNetworkRules>> VirtualNetworkRules { get; private set; } = null!;

        /// <summary>
        /// A list of write endpoints available for this CosmosDB account.
        /// </summary>
        [Output("writeEndpoints")]
        public Output<ImmutableArray<string>> WriteEndpoints { get; private set; } = null!;


        /// <summary>
        /// Create a Account resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Account(string name, AccountArgs args, CustomResourceOptions? options = null)
            : base("azure:cosmosdb/account:Account", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Account(string name, Input<string> id, AccountState? state = null, CustomResourceOptions? options = null)
            : base("azure:cosmosdb/account:Account", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Account resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Account Get(string name, Input<string> id, AccountState? state = null, CustomResourceOptions? options = null)
        {
            return new Account(name, id, state, options);
        }
    }

    public sealed class AccountArgs : Pulumi.ResourceArgs
    {
        [Input("capabilities")]
        private InputList<Inputs.AccountCapabilitiesArgs>? _capabilities;

        /// <summary>
        /// The capabilities which should be enabled for this Cosmos DB account. Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        public InputList<Inputs.AccountCapabilitiesArgs> Capabilities
        {
            get => _capabilities ?? (_capabilities = new InputList<Inputs.AccountCapabilitiesArgs>());
            set => _capabilities = value;
        }

        /// <summary>
        /// Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.
        /// </summary>
        [Input("consistencyPolicy", required: true)]
        public Input<Inputs.AccountConsistencyPolicyArgs> ConsistencyPolicy { get; set; } = null!;

        /// <summary>
        /// Enable automatic fail over for this Cosmos DB account.
        /// </summary>
        [Input("enableAutomaticFailover")]
        public Input<bool>? EnableAutomaticFailover { get; set; }

        /// <summary>
        /// Enable multi-master support for this Cosmos DB account.
        /// </summary>
        [Input("enableMultipleWriteLocations")]
        public Input<bool>? EnableMultipleWriteLocations { get; set; }

        [Input("failoverPolicies")]
        private InputList<Inputs.AccountFailoverPoliciesArgs>? _failoverPolicies;
        public InputList<Inputs.AccountFailoverPoliciesArgs> FailoverPolicies
        {
            get => _failoverPolicies ?? (_failoverPolicies = new InputList<Inputs.AccountFailoverPoliciesArgs>());
            set => _failoverPolicies = value;
        }

        [Input("geoLocations")]
        private InputList<Inputs.AccountGeoLocationsArgs>? _geoLocations;

        /// <summary>
        /// Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.
        /// </summary>
        public InputList<Inputs.AccountGeoLocationsArgs> GeoLocations
        {
            get => _geoLocations ?? (_geoLocations = new InputList<Inputs.AccountGeoLocationsArgs>());
            set => _geoLocations = value;
        }

        /// <summary>
        /// CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.
        /// </summary>
        [Input("ipRangeFilter")]
        public Input<string>? IpRangeFilter { get; set; }

        /// <summary>
        /// Enables virtual network filtering for this Cosmos DB account.
        /// </summary>
        [Input("isVirtualNetworkFilterEnabled")]
        public Input<bool>? IsVirtualNetworkFilterEnabled { get; set; }

        /// <summary>
        /// Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("kind")]
        public Input<string>? Kind { get; set; }

        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The capability to enable - Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.
        /// </summary>
        [Input("offerType", required: true)]
        public Input<string> OfferType { get; set; } = null!;

        /// <summary>
        /// The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        [Input("virtualNetworkRules")]
        private InputList<Inputs.AccountVirtualNetworkRulesArgs>? _virtualNetworkRules;

        /// <summary>
        /// Specifies a `virtual_network_rules` resource, used to define which subnets are allowed to access this CosmosDB account.
        /// </summary>
        public InputList<Inputs.AccountVirtualNetworkRulesArgs> VirtualNetworkRules
        {
            get => _virtualNetworkRules ?? (_virtualNetworkRules = new InputList<Inputs.AccountVirtualNetworkRulesArgs>());
            set => _virtualNetworkRules = value;
        }

        public AccountArgs()
        {
        }
    }

    public sealed class AccountState : Pulumi.ResourceArgs
    {
        [Input("capabilities")]
        private InputList<Inputs.AccountCapabilitiesGetArgs>? _capabilities;

        /// <summary>
        /// The capabilities which should be enabled for this Cosmos DB account. Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        public InputList<Inputs.AccountCapabilitiesGetArgs> Capabilities
        {
            get => _capabilities ?? (_capabilities = new InputList<Inputs.AccountCapabilitiesGetArgs>());
            set => _capabilities = value;
        }

        [Input("connectionStrings")]
        private InputList<string>? _connectionStrings;

        /// <summary>
        /// A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.
        /// </summary>
        public InputList<string> ConnectionStrings
        {
            get => _connectionStrings ?? (_connectionStrings = new InputList<string>());
            set => _connectionStrings = value;
        }

        /// <summary>
        /// Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.
        /// </summary>
        [Input("consistencyPolicy")]
        public Input<Inputs.AccountConsistencyPolicyGetArgs>? ConsistencyPolicy { get; set; }

        /// <summary>
        /// Enable automatic fail over for this Cosmos DB account.
        /// </summary>
        [Input("enableAutomaticFailover")]
        public Input<bool>? EnableAutomaticFailover { get; set; }

        /// <summary>
        /// Enable multi-master support for this Cosmos DB account.
        /// </summary>
        [Input("enableMultipleWriteLocations")]
        public Input<bool>? EnableMultipleWriteLocations { get; set; }

        /// <summary>
        /// The endpoint used to connect to the CosmosDB account.
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        [Input("failoverPolicies")]
        private InputList<Inputs.AccountFailoverPoliciesGetArgs>? _failoverPolicies;
        public InputList<Inputs.AccountFailoverPoliciesGetArgs> FailoverPolicies
        {
            get => _failoverPolicies ?? (_failoverPolicies = new InputList<Inputs.AccountFailoverPoliciesGetArgs>());
            set => _failoverPolicies = value;
        }

        [Input("geoLocations")]
        private InputList<Inputs.AccountGeoLocationsGetArgs>? _geoLocations;

        /// <summary>
        /// Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.
        /// </summary>
        public InputList<Inputs.AccountGeoLocationsGetArgs> GeoLocations
        {
            get => _geoLocations ?? (_geoLocations = new InputList<Inputs.AccountGeoLocationsGetArgs>());
            set => _geoLocations = value;
        }

        /// <summary>
        /// CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.
        /// </summary>
        [Input("ipRangeFilter")]
        public Input<string>? IpRangeFilter { get; set; }

        /// <summary>
        /// Enables virtual network filtering for this Cosmos DB account.
        /// </summary>
        [Input("isVirtualNetworkFilterEnabled")]
        public Input<bool>? IsVirtualNetworkFilterEnabled { get; set; }

        /// <summary>
        /// Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("kind")]
        public Input<string>? Kind { get; set; }

        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The capability to enable - Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.
        /// </summary>
        [Input("offerType")]
        public Input<string>? OfferType { get; set; }

        /// <summary>
        /// The Primary master key for the CosmosDB Account.
        /// </summary>
        [Input("primaryMasterKey")]
        public Input<string>? PrimaryMasterKey { get; set; }

        /// <summary>
        /// The Primary read-only master Key for the CosmosDB Account.
        /// </summary>
        [Input("primaryReadonlyMasterKey")]
        public Input<string>? PrimaryReadonlyMasterKey { get; set; }

        [Input("readEndpoints")]
        private InputList<string>? _readEndpoints;

        /// <summary>
        /// A list of read endpoints available for this CosmosDB account.
        /// </summary>
        public InputList<string> ReadEndpoints
        {
            get => _readEndpoints ?? (_readEndpoints = new InputList<string>());
            set => _readEndpoints = value;
        }

        /// <summary>
        /// The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The Secondary master key for the CosmosDB Account.
        /// </summary>
        [Input("secondaryMasterKey")]
        public Input<string>? SecondaryMasterKey { get; set; }

        /// <summary>
        /// The Secondary read-only master key for the CosmosDB Account.
        /// </summary>
        [Input("secondaryReadonlyMasterKey")]
        public Input<string>? SecondaryReadonlyMasterKey { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        [Input("virtualNetworkRules")]
        private InputList<Inputs.AccountVirtualNetworkRulesGetArgs>? _virtualNetworkRules;

        /// <summary>
        /// Specifies a `virtual_network_rules` resource, used to define which subnets are allowed to access this CosmosDB account.
        /// </summary>
        public InputList<Inputs.AccountVirtualNetworkRulesGetArgs> VirtualNetworkRules
        {
            get => _virtualNetworkRules ?? (_virtualNetworkRules = new InputList<Inputs.AccountVirtualNetworkRulesGetArgs>());
            set => _virtualNetworkRules = value;
        }

        [Input("writeEndpoints")]
        private InputList<string>? _writeEndpoints;

        /// <summary>
        /// A list of write endpoints available for this CosmosDB account.
        /// </summary>
        public InputList<string> WriteEndpoints
        {
            get => _writeEndpoints ?? (_writeEndpoints = new InputList<string>());
            set => _writeEndpoints = value;
        }

        public AccountState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class AccountCapabilitiesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The capability to enable - Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public AccountCapabilitiesArgs()
        {
        }
    }

    public sealed class AccountCapabilitiesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The capability to enable - Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public AccountCapabilitiesGetArgs()
        {
        }
    }

    public sealed class AccountConsistencyPolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Consistency Level to use for this CosmosDB Account - can be either `BoundedStaleness`, `Eventual`, `Session`, `Strong` or `ConsistentPrefix`.
        /// </summary>
        [Input("consistencyLevel", required: true)]
        public Input<string> ConsistencyLevel { get; set; } = null!;

        /// <summary>
        /// When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is `5` - `86400` (1 day). Defaults to `5`. Required when `consistency_level` is set to `BoundedStaleness`.
        /// </summary>
        [Input("maxIntervalInSeconds")]
        public Input<int>? MaxIntervalInSeconds { get; set; }

        /// <summary>
        /// When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is `10` – `2147483647`. Defaults to `100`. Required when `consistency_level` is set to `BoundedStaleness`.
        /// </summary>
        [Input("maxStalenessPrefix")]
        public Input<int>? MaxStalenessPrefix { get; set; }

        public AccountConsistencyPolicyArgs()
        {
        }
    }

    public sealed class AccountConsistencyPolicyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Consistency Level to use for this CosmosDB Account - can be either `BoundedStaleness`, `Eventual`, `Session`, `Strong` or `ConsistentPrefix`.
        /// </summary>
        [Input("consistencyLevel", required: true)]
        public Input<string> ConsistencyLevel { get; set; } = null!;

        /// <summary>
        /// When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is `5` - `86400` (1 day). Defaults to `5`. Required when `consistency_level` is set to `BoundedStaleness`.
        /// </summary>
        [Input("maxIntervalInSeconds")]
        public Input<int>? MaxIntervalInSeconds { get; set; }

        /// <summary>
        /// When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is `10` – `2147483647`. Defaults to `100`. Required when `consistency_level` is set to `BoundedStaleness`.
        /// </summary>
        [Input("maxStalenessPrefix")]
        public Input<int>? MaxStalenessPrefix { get; set; }

        public AccountConsistencyPolicyGetArgs()
        {
        }
    }

    public sealed class AccountFailoverPoliciesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("priority", required: true)]
        public Input<int> Priority { get; set; } = null!;

        public AccountFailoverPoliciesArgs()
        {
        }
    }

    public sealed class AccountFailoverPoliciesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("priority", required: true)]
        public Input<int> Priority { get; set; } = null!;

        public AccountFailoverPoliciesGetArgs()
        {
        }
    }

    public sealed class AccountGeoLocationsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The failover priority of the region. A failover priority of `0` indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority `0`.
        /// </summary>
        [Input("failoverPriority", required: true)]
        public Input<int> FailoverPriority { get; set; } = null!;

        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// The string used to generate the document endpoints for this region. If not specified it defaults to `${cosmosdb_account.name}-${location}`. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority `0`.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        public AccountGeoLocationsArgs()
        {
        }
    }

    public sealed class AccountGeoLocationsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The failover priority of the region. A failover priority of `0` indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority `0`.
        /// </summary>
        [Input("failoverPriority", required: true)]
        public Input<int> FailoverPriority { get; set; } = null!;

        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// The string used to generate the document endpoints for this region. If not specified it defaults to `${cosmosdb_account.name}-${location}`. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority `0`.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        public AccountGeoLocationsGetArgs()
        {
        }
    }

    public sealed class AccountVirtualNetworkRulesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public AccountVirtualNetworkRulesArgs()
        {
        }
    }

    public sealed class AccountVirtualNetworkRulesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public AccountVirtualNetworkRulesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class AccountCapabilities
    {
        /// <summary>
        /// The capability to enable - Possible values are `EnableAggregationPipeline`, `EnableCassandra`, `EnableGremlin`, `EnableTable`, `MongoDBv3.4`, and `mongoEnableDocLevelTTL`.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private AccountCapabilities(string name)
        {
            Name = name;
        }
    }

    [OutputType]
    public sealed class AccountConsistencyPolicy
    {
        /// <summary>
        /// The Consistency Level to use for this CosmosDB Account - can be either `BoundedStaleness`, `Eventual`, `Session`, `Strong` or `ConsistentPrefix`.
        /// </summary>
        public readonly string ConsistencyLevel;
        /// <summary>
        /// When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is `5` - `86400` (1 day). Defaults to `5`. Required when `consistency_level` is set to `BoundedStaleness`.
        /// </summary>
        public readonly int? MaxIntervalInSeconds;
        /// <summary>
        /// When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is `10` – `2147483647`. Defaults to `100`. Required when `consistency_level` is set to `BoundedStaleness`.
        /// </summary>
        public readonly int? MaxStalenessPrefix;

        [OutputConstructor]
        private AccountConsistencyPolicy(
            string consistencyLevel,
            int? maxIntervalInSeconds,
            int? maxStalenessPrefix)
        {
            ConsistencyLevel = consistencyLevel;
            MaxIntervalInSeconds = maxIntervalInSeconds;
            MaxStalenessPrefix = maxStalenessPrefix;
        }
    }

    [OutputType]
    public sealed class AccountFailoverPolicies
    {
        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        public readonly string Location;
        public readonly int Priority;

        [OutputConstructor]
        private AccountFailoverPolicies(
            string id,
            string location,
            int priority)
        {
            Id = id;
            Location = location;
            Priority = priority;
        }
    }

    [OutputType]
    public sealed class AccountGeoLocations
    {
        /// <summary>
        /// The failover priority of the region. A failover priority of `0` indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority `0`.
        /// </summary>
        public readonly int FailoverPriority;
        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the Azure region to host replicated data.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// The string used to generate the document endpoints for this region. If not specified it defaults to `${cosmosdb_account.name}-${location}`. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority `0`.
        /// </summary>
        public readonly string? Prefix;

        [OutputConstructor]
        private AccountGeoLocations(
            int failoverPriority,
            string id,
            string location,
            string? prefix)
        {
            FailoverPriority = failoverPriority;
            Id = id;
            Location = location;
            Prefix = prefix;
        }
    }

    [OutputType]
    public sealed class AccountVirtualNetworkRules
    {
        /// <summary>
        /// The ID of the virtual network subnet.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private AccountVirtualNetworkRules(string id)
        {
            Id = id;
        }
    }
    }
}
