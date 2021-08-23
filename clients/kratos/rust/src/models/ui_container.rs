/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.7.1-alpha.2
 * Contact: hi@ory.sh
 * Generated by: https://openapi-generator.tech
 */

/// UiContainer : Container represents a HTML Form. The container can work with both HTTP Form and JSON requests



#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct UiContainer {
    /// Action should be used as the form action URL `<form action=\"{{ .Action }}\" method=\"post\">`.
    #[serde(rename = "action")]
    pub action: String,
    #[serde(rename = "messages", skip_serializing_if = "Option::is_none")]
    pub messages: Option<Vec<crate::models::UiText>>,
    /// Method is the form method (e.g. POST)
    #[serde(rename = "method")]
    pub method: String,
    #[serde(rename = "nodes")]
    pub nodes: Vec<crate::models::UiNode>,
}

impl UiContainer {
    /// Container represents a HTML Form. The container can work with both HTTP Form and JSON requests
    pub fn new(action: String, method: String, nodes: Vec<crate::models::UiNode>) -> UiContainer {
        UiContainer {
            action,
            messages: None,
            method,
            nodes,
        }
    }
}


