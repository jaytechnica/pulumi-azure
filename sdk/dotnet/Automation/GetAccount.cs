// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Automation
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to access information about an existing Automation Account Registration Information.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/automation_account.html.markdown.
        /// </summary>
        public static Task<GetAccountResult> GetAccount(GetAccountArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAccountResult>("azure:automation/getAccount:getAccount", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetAccountArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Automation Account.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Specifies the name of the Resource Group where the Automation Account exists.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public GetAccountArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetAccountResult
    {
        /// <summary>
        /// The Assigned Automation Account Registration endpoint
        /// </summary>
        public readonly string Endpoint;
        public readonly string Name;
        /// <summary>
        /// The primary key for the Automation Account Registration information
        /// </summary>
        public readonly string PrimaryKey;
        public readonly string ResourceGroupName;
        /// <summary>
        /// The primary key for the Automation Account Registration information
        /// </summary>
        public readonly string SecondaryKey;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetAccountResult(
            string endpoint,
            string name,
            string primaryKey,
            string resourceGroupName,
            string secondaryKey,
            string id)
        {
            Endpoint = endpoint;
            Name = name;
            PrimaryKey = primaryKey;
            ResourceGroupName = resourceGroupName;
            SecondaryKey = secondaryKey;
            Id = id;
        }
    }
}