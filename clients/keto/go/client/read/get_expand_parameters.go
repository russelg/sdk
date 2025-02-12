// Code generated by go-swagger; DO NOT EDIT.

package read

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
	"github.com/go-openapi/swag"
)

// NewGetExpandParams creates a new GetExpandParams object,
// with the default timeout for this client.
//
// Default values are not hydrated, since defaults are normally applied by the API server side.
//
// To enforce default values in parameter, use SetDefaults or WithDefaults.
func NewGetExpandParams() *GetExpandParams {
	return &GetExpandParams{
		timeout: cr.DefaultTimeout,
	}
}

// NewGetExpandParamsWithTimeout creates a new GetExpandParams object
// with the ability to set a timeout on a request.
func NewGetExpandParamsWithTimeout(timeout time.Duration) *GetExpandParams {
	return &GetExpandParams{
		timeout: timeout,
	}
}

// NewGetExpandParamsWithContext creates a new GetExpandParams object
// with the ability to set a context for a request.
func NewGetExpandParamsWithContext(ctx context.Context) *GetExpandParams {
	return &GetExpandParams{
		Context: ctx,
	}
}

// NewGetExpandParamsWithHTTPClient creates a new GetExpandParams object
// with the ability to set a custom HTTPClient for a request.
func NewGetExpandParamsWithHTTPClient(client *http.Client) *GetExpandParams {
	return &GetExpandParams{
		HTTPClient: client,
	}
}

/* GetExpandParams contains all the parameters to send to the API endpoint
   for the get expand operation.

   Typically these are written to a http.Request.
*/
type GetExpandParams struct {

	// MaxDepth.
	//
	// Format: int64
	MaxDepth int64

	/* Namespace.

	   Namespace of the Subject Set
	*/
	Namespace string

	/* Object.

	   Object of the Subject Set
	*/
	Object string

	/* Relation.

	   Relation of the Subject Set
	*/
	Relation string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithDefaults hydrates default values in the get expand params (not the query body).
//
// All values with no default are reset to their zero value.
func (o *GetExpandParams) WithDefaults() *GetExpandParams {
	o.SetDefaults()
	return o
}

// SetDefaults hydrates default values in the get expand params (not the query body).
//
// All values with no default are reset to their zero value.
func (o *GetExpandParams) SetDefaults() {
	// no default values defined for this parameter
}

// WithTimeout adds the timeout to the get expand params
func (o *GetExpandParams) WithTimeout(timeout time.Duration) *GetExpandParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the get expand params
func (o *GetExpandParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the get expand params
func (o *GetExpandParams) WithContext(ctx context.Context) *GetExpandParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the get expand params
func (o *GetExpandParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the get expand params
func (o *GetExpandParams) WithHTTPClient(client *http.Client) *GetExpandParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the get expand params
func (o *GetExpandParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithMaxDepth adds the maxDepth to the get expand params
func (o *GetExpandParams) WithMaxDepth(maxDepth int64) *GetExpandParams {
	o.SetMaxDepth(maxDepth)
	return o
}

// SetMaxDepth adds the maxDepth to the get expand params
func (o *GetExpandParams) SetMaxDepth(maxDepth int64) {
	o.MaxDepth = maxDepth
}

// WithNamespace adds the namespace to the get expand params
func (o *GetExpandParams) WithNamespace(namespace string) *GetExpandParams {
	o.SetNamespace(namespace)
	return o
}

// SetNamespace adds the namespace to the get expand params
func (o *GetExpandParams) SetNamespace(namespace string) {
	o.Namespace = namespace
}

// WithObject adds the object to the get expand params
func (o *GetExpandParams) WithObject(object string) *GetExpandParams {
	o.SetObject(object)
	return o
}

// SetObject adds the object to the get expand params
func (o *GetExpandParams) SetObject(object string) {
	o.Object = object
}

// WithRelation adds the relation to the get expand params
func (o *GetExpandParams) WithRelation(relation string) *GetExpandParams {
	o.SetRelation(relation)
	return o
}

// SetRelation adds the relation to the get expand params
func (o *GetExpandParams) SetRelation(relation string) {
	o.Relation = relation
}

// WriteToRequest writes these params to a swagger request
func (o *GetExpandParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// query param max-depth
	qrMaxDepth := o.MaxDepth
	qMaxDepth := swag.FormatInt64(qrMaxDepth)
	if qMaxDepth != "" {

		if err := r.SetQueryParam("max-depth", qMaxDepth); err != nil {
			return err
		}
	}

	// query param namespace
	qrNamespace := o.Namespace
	qNamespace := qrNamespace
	if qNamespace != "" {

		if err := r.SetQueryParam("namespace", qNamespace); err != nil {
			return err
		}
	}

	// query param object
	qrObject := o.Object
	qObject := qrObject
	if qObject != "" {

		if err := r.SetQueryParam("object", qObject); err != nil {
			return err
		}
	}

	// query param relation
	qrRelation := o.Relation
	qRelation := qrRelation
	if qRelation != "" {

		if err := r.SetQueryParam("relation", qRelation); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
