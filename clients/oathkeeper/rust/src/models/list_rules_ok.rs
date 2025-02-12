/*
 * ORY Oathkeeper
 *
 * ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.
 *
 * The version of the OpenAPI document: v0.0.0-alpha.62
 * Contact: hi@ory.am
 * Generated by: https://openapi-generator.tech
 */

/// ListRulesOk : A list of rules



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct ListRulesOk {
    /// payload
    #[serde(rename = "Payload", skip_serializing_if = "Option::is_none")]
    pub payload: Option<Vec<crate::models::SwaggerRule>>,
}

impl ListRulesOk {
    /// A list of rules
    pub fn new() -> ListRulesOk {
        ListRulesOk {
            payload: None,
        }
    }
}


