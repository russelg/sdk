/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.0.0-alpha.38
 * Contact: hi@ory.sh
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Ory.Kratos.Client.Client.OpenAPIDateConverter;

namespace Ory.Kratos.Client.Model
{
    /// <summary>
    /// PluginConfigRootfs plugin config rootfs
    /// </summary>
    [DataContract(Name = "PluginConfigRootfs")]
    public partial class KratosPluginConfigRootfs : IEquatable<KratosPluginConfigRootfs>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="KratosPluginConfigRootfs" /> class.
        /// </summary>
        /// <param name="diffIds">diff ids.</param>
        /// <param name="type">type.</param>
        public KratosPluginConfigRootfs(List<string> diffIds = default(List<string>), string type = default(string))
        {
            this.DiffIds = diffIds;
            this.Type = type;
        }

        /// <summary>
        /// diff ids
        /// </summary>
        /// <value>diff ids</value>
        [DataMember(Name = "diff_ids", EmitDefaultValue = false)]
        public List<string> DiffIds { get; set; }

        /// <summary>
        /// type
        /// </summary>
        /// <value>type</value>
        [DataMember(Name = "type", EmitDefaultValue = false)]
        public string Type { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class KratosPluginConfigRootfs {\n");
            sb.Append("  DiffIds: ").Append(DiffIds).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as KratosPluginConfigRootfs);
        }

        /// <summary>
        /// Returns true if KratosPluginConfigRootfs instances are equal
        /// </summary>
        /// <param name="input">Instance of KratosPluginConfigRootfs to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(KratosPluginConfigRootfs input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.DiffIds == input.DiffIds ||
                    this.DiffIds != null &&
                    input.DiffIds != null &&
                    this.DiffIds.SequenceEqual(input.DiffIds)
                ) && 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.DiffIds != null)
                    hashCode = hashCode * 59 + this.DiffIds.GetHashCode();
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
