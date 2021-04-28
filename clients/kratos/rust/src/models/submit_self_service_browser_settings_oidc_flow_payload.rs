/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.0.0-alpha.38
 * Contact: hi@ory.sh
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct SubmitSelfServiceBrowserSettingsOidcFlowPayload {
    /// Flow ID is the flow's ID.  in: query
    #[serde(rename = "flow", skip_serializing_if = "Option::is_none")]
    pub flow: Option<String>,
    /// Link this provider  Either this or `unlink` must be set.  type: string in: body
    #[serde(rename = "link", skip_serializing_if = "Option::is_none")]
    pub link: Option<String>,
    /// Unlink this provider  Either this or `link` must be set.  type: string in: body
    #[serde(rename = "unlink", skip_serializing_if = "Option::is_none")]
    pub unlink: Option<String>,
}

impl SubmitSelfServiceBrowserSettingsOidcFlowPayload {
    pub fn new() -> SubmitSelfServiceBrowserSettingsOidcFlowPayload {
        SubmitSelfServiceBrowserSettingsOidcFlowPayload {
            flow: None,
            link: None,
            unlink: None,
        }
    }
}


