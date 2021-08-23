/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.7.1-alpha.2
 * Contact: hi@ory.sh
 * Generated by: https://openapi-generator.tech
 */

/// PluginConfigInterface : PluginConfigInterface The interface between Docker and the plugin



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct PluginConfigInterface {
    /// socket
    #[serde(rename = "Socket")]
    pub socket: String,
    /// types
    #[serde(rename = "Types")]
    pub types: Vec<crate::models::PluginInterfaceType>,
}

impl PluginConfigInterface {
    /// PluginConfigInterface The interface between Docker and the plugin
    pub fn new(socket: String, types: Vec<crate::models::PluginInterfaceType>) -> PluginConfigInterface {
        PluginConfigInterface {
            socket,
            types,
        }
    }
}


