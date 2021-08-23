/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * API version: v0.7.1-alpha.2
 * Contact: hi@ory.sh
 */

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package client

import (
	"encoding/json"
)

// SubmitSelfServiceLoginFlowWithPasswordMethodBody struct for SubmitSelfServiceLoginFlowWithPasswordMethodBody
type SubmitSelfServiceLoginFlowWithPasswordMethodBody struct {
	// Sending the anti-csrf token is only required for browser login flows.
	CsrfToken *string `json:"csrf_token,omitempty"`
	// Method should be set to \"password\" when logging in using the identifier and password strategy.
	Method string `json:"method"`
	// The user's password.
	Password string `json:"password"`
	// Identifier is the email or username of the user trying to log in.
	PasswordIdentifier string `json:"password_identifier"`
}

// NewSubmitSelfServiceLoginFlowWithPasswordMethodBody instantiates a new SubmitSelfServiceLoginFlowWithPasswordMethodBody object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewSubmitSelfServiceLoginFlowWithPasswordMethodBody(method string, password string, passwordIdentifier string) *SubmitSelfServiceLoginFlowWithPasswordMethodBody {
	this := SubmitSelfServiceLoginFlowWithPasswordMethodBody{}
	this.Method = method
	this.Password = password
	this.PasswordIdentifier = passwordIdentifier
	return &this
}

// NewSubmitSelfServiceLoginFlowWithPasswordMethodBodyWithDefaults instantiates a new SubmitSelfServiceLoginFlowWithPasswordMethodBody object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewSubmitSelfServiceLoginFlowWithPasswordMethodBodyWithDefaults() *SubmitSelfServiceLoginFlowWithPasswordMethodBody {
	this := SubmitSelfServiceLoginFlowWithPasswordMethodBody{}
	return &this
}

// GetCsrfToken returns the CsrfToken field value if set, zero value otherwise.
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetCsrfToken() string {
	if o == nil || o.CsrfToken == nil {
		var ret string
		return ret
	}
	return *o.CsrfToken
}

// GetCsrfTokenOk returns a tuple with the CsrfToken field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetCsrfTokenOk() (*string, bool) {
	if o == nil || o.CsrfToken == nil {
		return nil, false
	}
	return o.CsrfToken, true
}

// HasCsrfToken returns a boolean if a field has been set.
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) HasCsrfToken() bool {
	if o != nil && o.CsrfToken != nil {
		return true
	}

	return false
}

// SetCsrfToken gets a reference to the given string and assigns it to the CsrfToken field.
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) SetCsrfToken(v string) {
	o.CsrfToken = &v
}

// GetMethod returns the Method field value
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetMethod() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Method
}

// GetMethodOk returns a tuple with the Method field value
// and a boolean to check if the value has been set.
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetMethodOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Method, true
}

// SetMethod sets field value
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) SetMethod(v string) {
	o.Method = v
}

// GetPassword returns the Password field value
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetPassword() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Password
}

// GetPasswordOk returns a tuple with the Password field value
// and a boolean to check if the value has been set.
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetPasswordOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Password, true
}

// SetPassword sets field value
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) SetPassword(v string) {
	o.Password = v
}

// GetPasswordIdentifier returns the PasswordIdentifier field value
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetPasswordIdentifier() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.PasswordIdentifier
}

// GetPasswordIdentifierOk returns a tuple with the PasswordIdentifier field value
// and a boolean to check if the value has been set.
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) GetPasswordIdentifierOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.PasswordIdentifier, true
}

// SetPasswordIdentifier sets field value
func (o *SubmitSelfServiceLoginFlowWithPasswordMethodBody) SetPasswordIdentifier(v string) {
	o.PasswordIdentifier = v
}

func (o SubmitSelfServiceLoginFlowWithPasswordMethodBody) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.CsrfToken != nil {
		toSerialize["csrf_token"] = o.CsrfToken
	}
	if true {
		toSerialize["method"] = o.Method
	}
	if true {
		toSerialize["password"] = o.Password
	}
	if true {
		toSerialize["password_identifier"] = o.PasswordIdentifier
	}
	return json.Marshal(toSerialize)
}

type NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody struct {
	value *SubmitSelfServiceLoginFlowWithPasswordMethodBody
	isSet bool
}

func (v NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody) Get() *SubmitSelfServiceLoginFlowWithPasswordMethodBody {
	return v.value
}

func (v *NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody) Set(val *SubmitSelfServiceLoginFlowWithPasswordMethodBody) {
	v.value = val
	v.isSet = true
}

func (v NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody) IsSet() bool {
	return v.isSet
}

func (v *NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableSubmitSelfServiceLoginFlowWithPasswordMethodBody(val *SubmitSelfServiceLoginFlowWithPasswordMethodBody) *NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody {
	return &NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody{value: val, isSet: true}
}

func (v NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableSubmitSelfServiceLoginFlowWithPasswordMethodBody) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


