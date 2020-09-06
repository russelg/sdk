// Code generated by go-swagger; DO NOT EDIT.

package engines

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"

	"github.com/ory/keto-client-go/models"
)

// NewAddOryAccessControlPolicyRoleMembersParams creates a new AddOryAccessControlPolicyRoleMembersParams object
// with the default values initialized.
func NewAddOryAccessControlPolicyRoleMembersParams() *AddOryAccessControlPolicyRoleMembersParams {
	var ()
	return &AddOryAccessControlPolicyRoleMembersParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewAddOryAccessControlPolicyRoleMembersParamsWithTimeout creates a new AddOryAccessControlPolicyRoleMembersParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewAddOryAccessControlPolicyRoleMembersParamsWithTimeout(timeout time.Duration) *AddOryAccessControlPolicyRoleMembersParams {
	var ()
	return &AddOryAccessControlPolicyRoleMembersParams{

		timeout: timeout,
	}
}

// NewAddOryAccessControlPolicyRoleMembersParamsWithContext creates a new AddOryAccessControlPolicyRoleMembersParams object
// with the default values initialized, and the ability to set a context for a request
func NewAddOryAccessControlPolicyRoleMembersParamsWithContext(ctx context.Context) *AddOryAccessControlPolicyRoleMembersParams {
	var ()
	return &AddOryAccessControlPolicyRoleMembersParams{

		Context: ctx,
	}
}

// NewAddOryAccessControlPolicyRoleMembersParamsWithHTTPClient creates a new AddOryAccessControlPolicyRoleMembersParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewAddOryAccessControlPolicyRoleMembersParamsWithHTTPClient(client *http.Client) *AddOryAccessControlPolicyRoleMembersParams {
	var ()
	return &AddOryAccessControlPolicyRoleMembersParams{
		HTTPClient: client,
	}
}

/*AddOryAccessControlPolicyRoleMembersParams contains all the parameters to send to the API endpoint
for the add ory access control policy role members operation typically these are written to a http.Request
*/
type AddOryAccessControlPolicyRoleMembersParams struct {

	/*Body*/
	Body *models.AddOryAccessControlPolicyRoleMembersBody
	/*Flavor
	  The ORY Access Control Policy flavor. Can be "regex", "glob", and "exact".

	*/
	Flavor string
	/*ID
	  The ID of the ORY Access Control Policy Role.

	*/
	ID string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) WithTimeout(timeout time.Duration) *AddOryAccessControlPolicyRoleMembersParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) WithContext(ctx context.Context) *AddOryAccessControlPolicyRoleMembersParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) WithHTTPClient(client *http.Client) *AddOryAccessControlPolicyRoleMembersParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithBody adds the body to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) WithBody(body *models.AddOryAccessControlPolicyRoleMembersBody) *AddOryAccessControlPolicyRoleMembersParams {
	o.SetBody(body)
	return o
}

// SetBody adds the body to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) SetBody(body *models.AddOryAccessControlPolicyRoleMembersBody) {
	o.Body = body
}

// WithFlavor adds the flavor to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) WithFlavor(flavor string) *AddOryAccessControlPolicyRoleMembersParams {
	o.SetFlavor(flavor)
	return o
}

// SetFlavor adds the flavor to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) SetFlavor(flavor string) {
	o.Flavor = flavor
}

// WithID adds the id to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) WithID(id string) *AddOryAccessControlPolicyRoleMembersParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the add ory access control policy role members params
func (o *AddOryAccessControlPolicyRoleMembersParams) SetID(id string) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *AddOryAccessControlPolicyRoleMembersParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	if o.Body != nil {
		if err := r.SetBodyParam(o.Body); err != nil {
			return err
		}
	}

	// path param flavor
	if err := r.SetPathParam("flavor", o.Flavor); err != nil {
		return err
	}

	// path param id
	if err := r.SetPathParam("id", o.ID); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
