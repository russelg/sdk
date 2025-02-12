/*
 * ORY Oathkeeper
 *
 * ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.
 *
 * The version of the OpenAPI document: v0.0.0-alpha.62
 * Contact: hi@ory.am
 * Generated by: https://openapi-generator.tech
 */

/// SwaggerUpdateRuleParameters : SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters swagger update rule parameters



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct SwaggerUpdateRuleParameters {
    #[serde(rename = "Body", skip_serializing_if = "Option::is_none")]
    pub body: Option<Box<crate::models::SwaggerRule>>,
    /// in: path
    #[serde(rename = "id")]
    pub id: String,
}

impl SwaggerUpdateRuleParameters {
    /// SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters SwaggerUpdateRuleParameters swagger update rule parameters
    pub fn new(id: String) -> SwaggerUpdateRuleParameters {
        SwaggerUpdateRuleParameters {
            body: None,
            id,
        }
    }
}


