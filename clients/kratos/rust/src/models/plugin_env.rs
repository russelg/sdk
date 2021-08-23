/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.7.1-alpha.2
 * Contact: hi@ory.sh
 * Generated by: https://openapi-generator.tech
 */

/// PluginEnv : PluginEnv plugin env



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PluginEnv {
    /// description
    #[serde(rename = "Description")]
    pub description: String,
    /// name
    #[serde(rename = "Name")]
    pub name: String,
    /// settable
    #[serde(rename = "Settable")]
    pub settable: Vec<String>,
    /// value
    #[serde(rename = "Value")]
    pub value: String,
}

impl PluginEnv {
    /// PluginEnv plugin env
    pub fn new(description: String, name: String, settable: Vec<String>, value: String) -> PluginEnv {
        PluginEnv {
            description,
            name,
            settable,
            value,
        }
    }
}


