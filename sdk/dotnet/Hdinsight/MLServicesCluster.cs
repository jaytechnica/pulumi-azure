// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.HDInsight
{
    /// <summary>
    /// Manages a HDInsight ML Services Cluster.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_ml_services_cluster.html.markdown.
    /// </summary>
    public partial class MLServicesCluster : Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        /// </summary>
        [Output("clusterVersion")]
        public Output<string> ClusterVersion { get; private set; } = null!;

        /// <summary>
        /// The SSH Connectivity Endpoint for the Edge Node of the HDInsight ML Cluster.
        /// </summary>
        [Output("edgeSshEndpoint")]
        public Output<string> EdgeSshEndpoint { get; private set; } = null!;

        /// <summary>
        /// A `gateway` block as defined below.
        /// </summary>
        [Output("gateway")]
        public Output<Outputs.MLServicesClusterGateway> Gateway { get; private set; } = null!;

        /// <summary>
        /// The HTTPS Connectivity Endpoint for this HDInsight ML Services Cluster.
        /// </summary>
        [Output("httpsEndpoint")]
        public Output<string> HttpsEndpoint { get; private set; } = null!;

        /// <summary>
        /// Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// A `roles` block as defined below.
        /// </summary>
        [Output("roles")]
        public Output<Outputs.MLServicesClusterRoles> Roles { get; private set; } = null!;

        /// <summary>
        /// Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.
        /// </summary>
        [Output("rstudio")]
        public Output<bool> Rstudio { get; private set; } = null!;

        /// <summary>
        /// The SSH Connectivity Endpoint for this HDInsight ML Services Cluster.
        /// </summary>
        [Output("sshEndpoint")]
        public Output<string> SshEndpoint { get; private set; } = null!;

        /// <summary>
        /// One or more `storage_account` block as defined below.
        /// </summary>
        [Output("storageAccounts")]
        public Output<ImmutableArray<Outputs.MLServicesClusterStorageAccounts>> StorageAccounts { get; private set; } = null!;

        /// <summary>
        /// A map of Tags which should be assigned to this HDInsight ML Services Cluster.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>> Tags { get; private set; } = null!;

        /// <summary>
        /// Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        /// </summary>
        [Output("tier")]
        public Output<string> Tier { get; private set; } = null!;


        /// <summary>
        /// Create a MLServicesCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MLServicesCluster(string name, MLServicesClusterArgs args, CustomResourceOptions? options = null)
            : base("azure:hdinsight/mLServicesCluster:MLServicesCluster", name, args, MakeResourceOptions(options, ""))
        {
        }

        private MLServicesCluster(string name, Input<string> id, MLServicesClusterState? state = null, CustomResourceOptions? options = null)
            : base("azure:hdinsight/mLServicesCluster:MLServicesCluster", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing MLServicesCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MLServicesCluster Get(string name, Input<string> id, MLServicesClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new MLServicesCluster(name, id, state, options);
        }
    }

    public sealed class MLServicesClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        /// </summary>
        [Input("clusterVersion", required: true)]
        public Input<string> ClusterVersion { get; set; } = null!;

        /// <summary>
        /// A `gateway` block as defined below.
        /// </summary>
        [Input("gateway", required: true)]
        public Input<Inputs.MLServicesClusterGatewayArgs> Gateway { get; set; } = null!;

        /// <summary>
        /// Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// A `roles` block as defined below.
        /// </summary>
        [Input("roles", required: true)]
        public Input<Inputs.MLServicesClusterRolesArgs> Roles { get; set; } = null!;

        /// <summary>
        /// Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.
        /// </summary>
        [Input("rstudio", required: true)]
        public Input<bool> Rstudio { get; set; } = null!;

        [Input("storageAccounts", required: true)]
        private InputList<Inputs.MLServicesClusterStorageAccountsArgs>? _storageAccounts;

        /// <summary>
        /// One or more `storage_account` block as defined below.
        /// </summary>
        public InputList<Inputs.MLServicesClusterStorageAccountsArgs> StorageAccounts
        {
            get => _storageAccounts ?? (_storageAccounts = new InputList<Inputs.MLServicesClusterStorageAccountsArgs>());
            set => _storageAccounts = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A map of Tags which should be assigned to this HDInsight ML Services Cluster.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("tier", required: true)]
        public Input<string> Tier { get; set; } = null!;

        public MLServicesClusterArgs()
        {
        }
    }

    public sealed class MLServicesClusterState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        /// </summary>
        [Input("clusterVersion")]
        public Input<string>? ClusterVersion { get; set; }

        /// <summary>
        /// The SSH Connectivity Endpoint for the Edge Node of the HDInsight ML Cluster.
        /// </summary>
        [Input("edgeSshEndpoint")]
        public Input<string>? EdgeSshEndpoint { get; set; }

        /// <summary>
        /// A `gateway` block as defined below.
        /// </summary>
        [Input("gateway")]
        public Input<Inputs.MLServicesClusterGatewayGetArgs>? Gateway { get; set; }

        /// <summary>
        /// The HTTPS Connectivity Endpoint for this HDInsight ML Services Cluster.
        /// </summary>
        [Input("httpsEndpoint")]
        public Input<string>? HttpsEndpoint { get; set; }

        /// <summary>
        /// Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// A `roles` block as defined below.
        /// </summary>
        [Input("roles")]
        public Input<Inputs.MLServicesClusterRolesGetArgs>? Roles { get; set; }

        /// <summary>
        /// Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.
        /// </summary>
        [Input("rstudio")]
        public Input<bool>? Rstudio { get; set; }

        /// <summary>
        /// The SSH Connectivity Endpoint for this HDInsight ML Services Cluster.
        /// </summary>
        [Input("sshEndpoint")]
        public Input<string>? SshEndpoint { get; set; }

        [Input("storageAccounts")]
        private InputList<Inputs.MLServicesClusterStorageAccountsGetArgs>? _storageAccounts;

        /// <summary>
        /// One or more `storage_account` block as defined below.
        /// </summary>
        public InputList<Inputs.MLServicesClusterStorageAccountsGetArgs> StorageAccounts
        {
            get => _storageAccounts ?? (_storageAccounts = new InputList<Inputs.MLServicesClusterStorageAccountsGetArgs>());
            set => _storageAccounts = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A map of Tags which should be assigned to this HDInsight ML Services Cluster.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("tier")]
        public Input<string>? Tier { get; set; }

        public MLServicesClusterState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class MLServicesClusterGatewayArgs : Pulumi.ResourceArgs
    {
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public MLServicesClusterGatewayArgs()
        {
        }
    }

    public sealed class MLServicesClusterGatewayGetArgs : Pulumi.ResourceArgs
    {
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public MLServicesClusterGatewayGetArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesArgs : Pulumi.ResourceArgs
    {
        [Input("edgeNode", required: true)]
        public Input<MLServicesClusterRolesEdgeNodeArgs> EdgeNode { get; set; } = null!;

        [Input("headNode", required: true)]
        public Input<MLServicesClusterRolesHeadNodeArgs> HeadNode { get; set; } = null!;

        [Input("workerNode", required: true)]
        public Input<MLServicesClusterRolesWorkerNodeArgs> WorkerNode { get; set; } = null!;

        [Input("zookeeperNode", required: true)]
        public Input<MLServicesClusterRolesZookeeperNodeArgs> ZookeeperNode { get; set; } = null!;

        public MLServicesClusterRolesArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesEdgeNodeArgs : Pulumi.ResourceArgs
    {
        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesEdgeNodeArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesEdgeNodeGetArgs : Pulumi.ResourceArgs
    {
        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesEdgeNodeGetArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesGetArgs : Pulumi.ResourceArgs
    {
        [Input("edgeNode", required: true)]
        public Input<MLServicesClusterRolesEdgeNodeGetArgs> EdgeNode { get; set; } = null!;

        [Input("headNode", required: true)]
        public Input<MLServicesClusterRolesHeadNodeGetArgs> HeadNode { get; set; } = null!;

        [Input("workerNode", required: true)]
        public Input<MLServicesClusterRolesWorkerNodeGetArgs> WorkerNode { get; set; } = null!;

        [Input("zookeeperNode", required: true)]
        public Input<MLServicesClusterRolesZookeeperNodeGetArgs> ZookeeperNode { get; set; } = null!;

        public MLServicesClusterRolesGetArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesHeadNodeArgs : Pulumi.ResourceArgs
    {
        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesHeadNodeArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesHeadNodeGetArgs : Pulumi.ResourceArgs
    {
        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesHeadNodeGetArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesWorkerNodeArgs : Pulumi.ResourceArgs
    {
        [Input("minInstanceCount")]
        public Input<int>? MinInstanceCount { get; set; }

        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("targetInstanceCount", required: true)]
        public Input<int> TargetInstanceCount { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesWorkerNodeArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesWorkerNodeGetArgs : Pulumi.ResourceArgs
    {
        [Input("minInstanceCount")]
        public Input<int>? MinInstanceCount { get; set; }

        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("targetInstanceCount", required: true)]
        public Input<int> TargetInstanceCount { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesWorkerNodeGetArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesZookeeperNodeArgs : Pulumi.ResourceArgs
    {
        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesZookeeperNodeArgs()
        {
        }
    }

    public sealed class MLServicesClusterRolesZookeeperNodeGetArgs : Pulumi.ResourceArgs
    {
        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("virtualNetworkId")]
        public Input<string>? VirtualNetworkId { get; set; }

        [Input("vmSize", required: true)]
        public Input<string> VmSize { get; set; } = null!;

        public MLServicesClusterRolesZookeeperNodeGetArgs()
        {
        }
    }

    public sealed class MLServicesClusterStorageAccountsArgs : Pulumi.ResourceArgs
    {
        [Input("isDefault", required: true)]
        public Input<bool> IsDefault { get; set; } = null!;

        [Input("storageAccountKey", required: true)]
        public Input<string> StorageAccountKey { get; set; } = null!;

        [Input("storageContainerId", required: true)]
        public Input<string> StorageContainerId { get; set; } = null!;

        public MLServicesClusterStorageAccountsArgs()
        {
        }
    }

    public sealed class MLServicesClusterStorageAccountsGetArgs : Pulumi.ResourceArgs
    {
        [Input("isDefault", required: true)]
        public Input<bool> IsDefault { get; set; } = null!;

        [Input("storageAccountKey", required: true)]
        public Input<string> StorageAccountKey { get; set; } = null!;

        [Input("storageContainerId", required: true)]
        public Input<string> StorageContainerId { get; set; } = null!;

        public MLServicesClusterStorageAccountsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class MLServicesClusterGateway
    {
        public readonly bool Enabled;
        public readonly string Password;
        public readonly string Username;

        [OutputConstructor]
        private MLServicesClusterGateway(
            bool enabled,
            string password,
            string username)
        {
            Enabled = enabled;
            Password = password;
            Username = username;
        }
    }

    [OutputType]
    public sealed class MLServicesClusterRoles
    {
        public readonly MLServicesClusterRolesEdgeNode EdgeNode;
        public readonly MLServicesClusterRolesHeadNode HeadNode;
        public readonly MLServicesClusterRolesWorkerNode WorkerNode;
        public readonly MLServicesClusterRolesZookeeperNode ZookeeperNode;

        [OutputConstructor]
        private MLServicesClusterRoles(
            MLServicesClusterRolesEdgeNode edgeNode,
            MLServicesClusterRolesHeadNode headNode,
            MLServicesClusterRolesWorkerNode workerNode,
            MLServicesClusterRolesZookeeperNode zookeeperNode)
        {
            EdgeNode = edgeNode;
            HeadNode = headNode;
            WorkerNode = workerNode;
            ZookeeperNode = zookeeperNode;
        }
    }

    [OutputType]
    public sealed class MLServicesClusterRolesEdgeNode
    {
        public readonly string? Password;
        public readonly ImmutableArray<string> SshKeys;
        public readonly string? SubnetId;
        public readonly string Username;
        public readonly string? VirtualNetworkId;
        public readonly string VmSize;

        [OutputConstructor]
        private MLServicesClusterRolesEdgeNode(
            string? password,
            ImmutableArray<string> sshKeys,
            string? subnetId,
            string username,
            string? virtualNetworkId,
            string vmSize)
        {
            Password = password;
            SshKeys = sshKeys;
            SubnetId = subnetId;
            Username = username;
            VirtualNetworkId = virtualNetworkId;
            VmSize = vmSize;
        }
    }

    [OutputType]
    public sealed class MLServicesClusterRolesHeadNode
    {
        public readonly string? Password;
        public readonly ImmutableArray<string> SshKeys;
        public readonly string? SubnetId;
        public readonly string Username;
        public readonly string? VirtualNetworkId;
        public readonly string VmSize;

        [OutputConstructor]
        private MLServicesClusterRolesHeadNode(
            string? password,
            ImmutableArray<string> sshKeys,
            string? subnetId,
            string username,
            string? virtualNetworkId,
            string vmSize)
        {
            Password = password;
            SshKeys = sshKeys;
            SubnetId = subnetId;
            Username = username;
            VirtualNetworkId = virtualNetworkId;
            VmSize = vmSize;
        }
    }

    [OutputType]
    public sealed class MLServicesClusterRolesWorkerNode
    {
        public readonly int? MinInstanceCount;
        public readonly string? Password;
        public readonly ImmutableArray<string> SshKeys;
        public readonly string? SubnetId;
        public readonly int TargetInstanceCount;
        public readonly string Username;
        public readonly string? VirtualNetworkId;
        public readonly string VmSize;

        [OutputConstructor]
        private MLServicesClusterRolesWorkerNode(
            int? minInstanceCount,
            string? password,
            ImmutableArray<string> sshKeys,
            string? subnetId,
            int targetInstanceCount,
            string username,
            string? virtualNetworkId,
            string vmSize)
        {
            MinInstanceCount = minInstanceCount;
            Password = password;
            SshKeys = sshKeys;
            SubnetId = subnetId;
            TargetInstanceCount = targetInstanceCount;
            Username = username;
            VirtualNetworkId = virtualNetworkId;
            VmSize = vmSize;
        }
    }

    [OutputType]
    public sealed class MLServicesClusterRolesZookeeperNode
    {
        public readonly string? Password;
        public readonly ImmutableArray<string> SshKeys;
        public readonly string? SubnetId;
        public readonly string Username;
        public readonly string? VirtualNetworkId;
        public readonly string VmSize;

        [OutputConstructor]
        private MLServicesClusterRolesZookeeperNode(
            string? password,
            ImmutableArray<string> sshKeys,
            string? subnetId,
            string username,
            string? virtualNetworkId,
            string vmSize)
        {
            Password = password;
            SshKeys = sshKeys;
            SubnetId = subnetId;
            Username = username;
            VirtualNetworkId = virtualNetworkId;
            VmSize = vmSize;
        }
    }

    [OutputType]
    public sealed class MLServicesClusterStorageAccounts
    {
        public readonly bool IsDefault;
        public readonly string StorageAccountKey;
        public readonly string StorageContainerId;

        [OutputConstructor]
        private MLServicesClusterStorageAccounts(
            bool isDefault,
            string storageAccountKey,
            string storageContainerId)
        {
            IsDefault = isDefault;
            StorageAccountKey = storageAccountKey;
            StorageContainerId = storageContainerId;
        }
    }
    }
}
