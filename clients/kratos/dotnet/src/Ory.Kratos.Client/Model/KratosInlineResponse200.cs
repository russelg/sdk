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
    /// KratosInlineResponse200
    /// </summary>
    [DataContract(Name = "inline_response_200")]
    public partial class KratosInlineResponse200 : IEquatable<KratosInlineResponse200>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="KratosInlineResponse200" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected KratosInlineResponse200() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="KratosInlineResponse200" /> class.
        /// </summary>
        /// <param name="status">Always \&quot;ok\&quot;. (required).</param>
        public KratosInlineResponse200(string status = default(string))
        {
            // to ensure "status" is required (not null)
            this.Status = status ?? throw new ArgumentNullException("status is a required property for KratosInlineResponse200 and cannot be null");
        }

        /// <summary>
        /// Always \&quot;ok\&quot;.
        /// </summary>
        /// <value>Always \&quot;ok\&quot;.</value>
        [DataMember(Name = "status", IsRequired = true, EmitDefaultValue = false)]
        public string Status { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class KratosInlineResponse200 {\n");
            sb.Append("  Status: ").Append(Status).Append("\n");
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
            return this.Equals(input as KratosInlineResponse200);
        }

        /// <summary>
        /// Returns true if KratosInlineResponse200 instances are equal
        /// </summary>
        /// <param name="input">Instance of KratosInlineResponse200 to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(KratosInlineResponse200 input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Status == input.Status ||
                    (this.Status != null &&
                    this.Status.Equals(input.Status))
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
                if (this.Status != null)
                    hashCode = hashCode * 59 + this.Status.GetHashCode();
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
