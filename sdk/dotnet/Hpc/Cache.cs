// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Hpc
{
    /// <summary>
    /// Manages a HPC Cache.
    /// 
    /// &gt; **Note**: During the first several months of the GA release, a request must be made to the Azure HPC Cache team to add your subscription to the access list before it can be used to create a cache instance. Fill out [this form](https://aka.ms/onboard-hpc-cache) to request access.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hpc_cache.html.markdown.
    /// </summary>
    public partial class Cache : Pulumi.CustomResource
    {
        /// <summary>
        /// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
        /// </summary>
        [Output("cacheSizeInGb")]
        public Output<int> CacheSizeInGb { get; private set; } = null!;

        /// <summary>
        /// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// A list of IP Addresses where the HPC Cache can be mounted.
        /// </summary>
        [Output("mountAddresses")]
        public Output<ImmutableArray<string>> MountAddresses { get; private set; } = null!;

        /// <summary>
        /// The name of the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
        /// </summary>
        [Output("skuName")]
        public Output<string> SkuName { get; private set; } = null!;

        /// <summary>
        /// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;


        /// <summary>
        /// Create a Cache resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cache(string name, CacheArgs args, CustomResourceOptions? options = null)
            : base("azure:hpc/cache:Cache", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Cache(string name, Input<string> id, CacheState? state = null, CustomResourceOptions? options = null)
            : base("azure:hpc/cache:Cache", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Cache resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Cache Get(string name, Input<string> id, CacheState? state = null, CustomResourceOptions? options = null)
        {
            return new Cache(name, id, state, options);
        }
    }

    public sealed class CacheArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("cacheSizeInGb", required: true)]
        public Input<int> CacheSizeInGb { get; set; } = null!;

        /// <summary>
        /// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("skuName", required: true)]
        public Input<string> SkuName { get; set; } = null!;

        /// <summary>
        /// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        public CacheArgs()
        {
        }
    }

    public sealed class CacheState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("cacheSizeInGb")]
        public Input<int>? CacheSizeInGb { get; set; }

        /// <summary>
        /// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("mountAddresses")]
        private InputList<string>? _mountAddresses;

        /// <summary>
        /// A list of IP Addresses where the HPC Cache can be mounted.
        /// </summary>
        public InputList<string> MountAddresses
        {
            get => _mountAddresses ?? (_mountAddresses = new InputList<string>());
            set => _mountAddresses = value;
        }

        /// <summary>
        /// The name of the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("skuName")]
        public Input<string>? SkuName { get; set; }

        /// <summary>
        /// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public CacheState()
        {
        }
    }
}