# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.10.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class OAuth2Client(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'allowed_cors_origins': 'list[str]',
        'audience': 'list[str]',
        'backchannel_logout_session_required': 'bool',
        'backchannel_logout_uri': 'str',
        'client_id': 'str',
        'client_name': 'str',
        'client_secret': 'str',
        'client_secret_expires_at': 'int',
        'client_uri': 'str',
        'contacts': 'list[str]',
        'created_at': 'datetime',
        'frontchannel_logout_session_required': 'bool',
        'frontchannel_logout_uri': 'str',
        'grant_types': 'list[str]',
        'jwks': 'object',
        'jwks_uri': 'str',
        'logo_uri': 'str',
        'metadata': 'object',
        'owner': 'str',
        'policy_uri': 'str',
        'post_logout_redirect_uris': 'list[str]',
        'redirect_uris': 'list[str]',
        'request_object_signing_alg': 'str',
        'request_uris': 'list[str]',
        'response_types': 'list[str]',
        'scope': 'str',
        'sector_identifier_uri': 'str',
        'subject_type': 'str',
        'token_endpoint_auth_method': 'str',
        'token_endpoint_auth_signing_alg': 'str',
        'tos_uri': 'str',
        'updated_at': 'datetime',
        'userinfo_signed_response_alg': 'str'
    }

    attribute_map = {
        'allowed_cors_origins': 'allowed_cors_origins',
        'audience': 'audience',
        'backchannel_logout_session_required': 'backchannel_logout_session_required',
        'backchannel_logout_uri': 'backchannel_logout_uri',
        'client_id': 'client_id',
        'client_name': 'client_name',
        'client_secret': 'client_secret',
        'client_secret_expires_at': 'client_secret_expires_at',
        'client_uri': 'client_uri',
        'contacts': 'contacts',
        'created_at': 'created_at',
        'frontchannel_logout_session_required': 'frontchannel_logout_session_required',
        'frontchannel_logout_uri': 'frontchannel_logout_uri',
        'grant_types': 'grant_types',
        'jwks': 'jwks',
        'jwks_uri': 'jwks_uri',
        'logo_uri': 'logo_uri',
        'metadata': 'metadata',
        'owner': 'owner',
        'policy_uri': 'policy_uri',
        'post_logout_redirect_uris': 'post_logout_redirect_uris',
        'redirect_uris': 'redirect_uris',
        'request_object_signing_alg': 'request_object_signing_alg',
        'request_uris': 'request_uris',
        'response_types': 'response_types',
        'scope': 'scope',
        'sector_identifier_uri': 'sector_identifier_uri',
        'subject_type': 'subject_type',
        'token_endpoint_auth_method': 'token_endpoint_auth_method',
        'token_endpoint_auth_signing_alg': 'token_endpoint_auth_signing_alg',
        'tos_uri': 'tos_uri',
        'updated_at': 'updated_at',
        'userinfo_signed_response_alg': 'userinfo_signed_response_alg'
    }

    def __init__(self, allowed_cors_origins=None, audience=None, backchannel_logout_session_required=None, backchannel_logout_uri=None, client_id=None, client_name=None, client_secret=None, client_secret_expires_at=None, client_uri=None, contacts=None, created_at=None, frontchannel_logout_session_required=None, frontchannel_logout_uri=None, grant_types=None, jwks=None, jwks_uri=None, logo_uri=None, metadata=None, owner=None, policy_uri=None, post_logout_redirect_uris=None, redirect_uris=None, request_object_signing_alg=None, request_uris=None, response_types=None, scope=None, sector_identifier_uri=None, subject_type=None, token_endpoint_auth_method=None, token_endpoint_auth_signing_alg=None, tos_uri=None, updated_at=None, userinfo_signed_response_alg=None, local_vars_configuration=None):  # noqa: E501
        """OAuth2Client - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_cors_origins = None
        self._audience = None
        self._backchannel_logout_session_required = None
        self._backchannel_logout_uri = None
        self._client_id = None
        self._client_name = None
        self._client_secret = None
        self._client_secret_expires_at = None
        self._client_uri = None
        self._contacts = None
        self._created_at = None
        self._frontchannel_logout_session_required = None
        self._frontchannel_logout_uri = None
        self._grant_types = None
        self._jwks = None
        self._jwks_uri = None
        self._logo_uri = None
        self._metadata = None
        self._owner = None
        self._policy_uri = None
        self._post_logout_redirect_uris = None
        self._redirect_uris = None
        self._request_object_signing_alg = None
        self._request_uris = None
        self._response_types = None
        self._scope = None
        self._sector_identifier_uri = None
        self._subject_type = None
        self._token_endpoint_auth_method = None
        self._token_endpoint_auth_signing_alg = None
        self._tos_uri = None
        self._updated_at = None
        self._userinfo_signed_response_alg = None
        self.discriminator = None

        if allowed_cors_origins is not None:
            self.allowed_cors_origins = allowed_cors_origins
        if audience is not None:
            self.audience = audience
        if backchannel_logout_session_required is not None:
            self.backchannel_logout_session_required = backchannel_logout_session_required
        if backchannel_logout_uri is not None:
            self.backchannel_logout_uri = backchannel_logout_uri
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if client_secret is not None:
            self.client_secret = client_secret
        if client_secret_expires_at is not None:
            self.client_secret_expires_at = client_secret_expires_at
        if client_uri is not None:
            self.client_uri = client_uri
        if contacts is not None:
            self.contacts = contacts
        if created_at is not None:
            self.created_at = created_at
        if frontchannel_logout_session_required is not None:
            self.frontchannel_logout_session_required = frontchannel_logout_session_required
        if frontchannel_logout_uri is not None:
            self.frontchannel_logout_uri = frontchannel_logout_uri
        if grant_types is not None:
            self.grant_types = grant_types
        if jwks is not None:
            self.jwks = jwks
        if jwks_uri is not None:
            self.jwks_uri = jwks_uri
        if logo_uri is not None:
            self.logo_uri = logo_uri
        if metadata is not None:
            self.metadata = metadata
        if owner is not None:
            self.owner = owner
        if policy_uri is not None:
            self.policy_uri = policy_uri
        if post_logout_redirect_uris is not None:
            self.post_logout_redirect_uris = post_logout_redirect_uris
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris
        if request_object_signing_alg is not None:
            self.request_object_signing_alg = request_object_signing_alg
        if request_uris is not None:
            self.request_uris = request_uris
        if response_types is not None:
            self.response_types = response_types
        if scope is not None:
            self.scope = scope
        if sector_identifier_uri is not None:
            self.sector_identifier_uri = sector_identifier_uri
        if subject_type is not None:
            self.subject_type = subject_type
        if token_endpoint_auth_method is not None:
            self.token_endpoint_auth_method = token_endpoint_auth_method
        if token_endpoint_auth_signing_alg is not None:
            self.token_endpoint_auth_signing_alg = token_endpoint_auth_signing_alg
        if tos_uri is not None:
            self.tos_uri = tos_uri
        if updated_at is not None:
            self.updated_at = updated_at
        if userinfo_signed_response_alg is not None:
            self.userinfo_signed_response_alg = userinfo_signed_response_alg

    @property
    def allowed_cors_origins(self):
        """Gets the allowed_cors_origins of this OAuth2Client.  # noqa: E501


        :return: The allowed_cors_origins of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_cors_origins

    @allowed_cors_origins.setter
    def allowed_cors_origins(self, allowed_cors_origins):
        """Sets the allowed_cors_origins of this OAuth2Client.


        :param allowed_cors_origins: The allowed_cors_origins of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._allowed_cors_origins = allowed_cors_origins

    @property
    def audience(self):
        """Gets the audience of this OAuth2Client.  # noqa: E501


        :return: The audience of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this OAuth2Client.


        :param audience: The audience of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._audience = audience

    @property
    def backchannel_logout_session_required(self):
        """Gets the backchannel_logout_session_required of this OAuth2Client.  # noqa: E501

        Boolean value specifying whether the RP requires that a sid (session ID) Claim be included in the Logout Token to identify the RP session with the OP when the backchannel_logout_uri is used. If omitted, the default value is false.  # noqa: E501

        :return: The backchannel_logout_session_required of this OAuth2Client.  # noqa: E501
        :rtype: bool
        """
        return self._backchannel_logout_session_required

    @backchannel_logout_session_required.setter
    def backchannel_logout_session_required(self, backchannel_logout_session_required):
        """Sets the backchannel_logout_session_required of this OAuth2Client.

        Boolean value specifying whether the RP requires that a sid (session ID) Claim be included in the Logout Token to identify the RP session with the OP when the backchannel_logout_uri is used. If omitted, the default value is false.  # noqa: E501

        :param backchannel_logout_session_required: The backchannel_logout_session_required of this OAuth2Client.  # noqa: E501
        :type: bool
        """

        self._backchannel_logout_session_required = backchannel_logout_session_required

    @property
    def backchannel_logout_uri(self):
        """Gets the backchannel_logout_uri of this OAuth2Client.  # noqa: E501

        RP URL that will cause the RP to log itself out when sent a Logout Token by the OP.  # noqa: E501

        :return: The backchannel_logout_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._backchannel_logout_uri

    @backchannel_logout_uri.setter
    def backchannel_logout_uri(self, backchannel_logout_uri):
        """Sets the backchannel_logout_uri of this OAuth2Client.

        RP URL that will cause the RP to log itself out when sent a Logout Token by the OP.  # noqa: E501

        :param backchannel_logout_uri: The backchannel_logout_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._backchannel_logout_uri = backchannel_logout_uri

    @property
    def client_id(self):
        """Gets the client_id of this OAuth2Client.  # noqa: E501

        ID  is the id for this client.  # noqa: E501

        :return: The client_id of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OAuth2Client.

        ID  is the id for this client.  # noqa: E501

        :param client_id: The client_id of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this OAuth2Client.  # noqa: E501

        Name is the human-readable string name of the client to be presented to the end-user during authorization.  # noqa: E501

        :return: The client_name of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this OAuth2Client.

        Name is the human-readable string name of the client to be presented to the end-user during authorization.  # noqa: E501

        :param client_name: The client_name of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def client_secret(self):
        """Gets the client_secret of this OAuth2Client.  # noqa: E501

        Secret is the client's secret. The secret will be included in the create request as cleartext, and then never again. The secret is stored using BCrypt so it is impossible to recover it. Tell your users that they need to write the secret down as it will not be made available again.  # noqa: E501

        :return: The client_secret of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this OAuth2Client.

        Secret is the client's secret. The secret will be included in the create request as cleartext, and then never again. The secret is stored using BCrypt so it is impossible to recover it. Tell your users that they need to write the secret down as it will not be made available again.  # noqa: E501

        :param client_secret: The client_secret of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def client_secret_expires_at(self):
        """Gets the client_secret_expires_at of this OAuth2Client.  # noqa: E501

        SecretExpiresAt is an integer holding the time at which the client secret will expire or 0 if it will not expire. The time is represented as the number of seconds from 1970-01-01T00:00:00Z as measured in UTC until the date/time of expiration.  This feature is currently not supported and it's value will always be set to 0.  # noqa: E501

        :return: The client_secret_expires_at of this OAuth2Client.  # noqa: E501
        :rtype: int
        """
        return self._client_secret_expires_at

    @client_secret_expires_at.setter
    def client_secret_expires_at(self, client_secret_expires_at):
        """Sets the client_secret_expires_at of this OAuth2Client.

        SecretExpiresAt is an integer holding the time at which the client secret will expire or 0 if it will not expire. The time is represented as the number of seconds from 1970-01-01T00:00:00Z as measured in UTC until the date/time of expiration.  This feature is currently not supported and it's value will always be set to 0.  # noqa: E501

        :param client_secret_expires_at: The client_secret_expires_at of this OAuth2Client.  # noqa: E501
        :type: int
        """

        self._client_secret_expires_at = client_secret_expires_at

    @property
    def client_uri(self):
        """Gets the client_uri of this OAuth2Client.  # noqa: E501

        ClientURI is an URL string of a web page providing information about the client. If present, the server SHOULD display this URL to the end-user in a clickable fashion.  # noqa: E501

        :return: The client_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._client_uri

    @client_uri.setter
    def client_uri(self, client_uri):
        """Sets the client_uri of this OAuth2Client.

        ClientURI is an URL string of a web page providing information about the client. If present, the server SHOULD display this URL to the end-user in a clickable fashion.  # noqa: E501

        :param client_uri: The client_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._client_uri = client_uri

    @property
    def contacts(self):
        """Gets the contacts of this OAuth2Client.  # noqa: E501


        :return: The contacts of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this OAuth2Client.


        :param contacts: The contacts of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._contacts = contacts

    @property
    def created_at(self):
        """Gets the created_at of this OAuth2Client.  # noqa: E501

        CreatedAt returns the timestamp of the client's creation.  # noqa: E501

        :return: The created_at of this OAuth2Client.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OAuth2Client.

        CreatedAt returns the timestamp of the client's creation.  # noqa: E501

        :param created_at: The created_at of this OAuth2Client.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def frontchannel_logout_session_required(self):
        """Gets the frontchannel_logout_session_required of this OAuth2Client.  # noqa: E501

        Boolean value specifying whether the RP requires that iss (issuer) and sid (session ID) query parameters be included to identify the RP session with the OP when the frontchannel_logout_uri is used. If omitted, the default value is false.  # noqa: E501

        :return: The frontchannel_logout_session_required of this OAuth2Client.  # noqa: E501
        :rtype: bool
        """
        return self._frontchannel_logout_session_required

    @frontchannel_logout_session_required.setter
    def frontchannel_logout_session_required(self, frontchannel_logout_session_required):
        """Sets the frontchannel_logout_session_required of this OAuth2Client.

        Boolean value specifying whether the RP requires that iss (issuer) and sid (session ID) query parameters be included to identify the RP session with the OP when the frontchannel_logout_uri is used. If omitted, the default value is false.  # noqa: E501

        :param frontchannel_logout_session_required: The frontchannel_logout_session_required of this OAuth2Client.  # noqa: E501
        :type: bool
        """

        self._frontchannel_logout_session_required = frontchannel_logout_session_required

    @property
    def frontchannel_logout_uri(self):
        """Gets the frontchannel_logout_uri of this OAuth2Client.  # noqa: E501

        RP URL that will cause the RP to log itself out when rendered in an iframe by the OP. An iss (issuer) query parameter and a sid (session ID) query parameter MAY be included by the OP to enable the RP to validate the request and to determine which of the potentially multiple sessions is to be logged out; if either is included, both MUST be.  # noqa: E501

        :return: The frontchannel_logout_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._frontchannel_logout_uri

    @frontchannel_logout_uri.setter
    def frontchannel_logout_uri(self, frontchannel_logout_uri):
        """Sets the frontchannel_logout_uri of this OAuth2Client.

        RP URL that will cause the RP to log itself out when rendered in an iframe by the OP. An iss (issuer) query parameter and a sid (session ID) query parameter MAY be included by the OP to enable the RP to validate the request and to determine which of the potentially multiple sessions is to be logged out; if either is included, both MUST be.  # noqa: E501

        :param frontchannel_logout_uri: The frontchannel_logout_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._frontchannel_logout_uri = frontchannel_logout_uri

    @property
    def grant_types(self):
        """Gets the grant_types of this OAuth2Client.  # noqa: E501


        :return: The grant_types of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this OAuth2Client.


        :param grant_types: The grant_types of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._grant_types = grant_types

    @property
    def jwks(self):
        """Gets the jwks of this OAuth2Client.  # noqa: E501


        :return: The jwks of this OAuth2Client.  # noqa: E501
        :rtype: object
        """
        return self._jwks

    @jwks.setter
    def jwks(self, jwks):
        """Sets the jwks of this OAuth2Client.


        :param jwks: The jwks of this OAuth2Client.  # noqa: E501
        :type: object
        """

        self._jwks = jwks

    @property
    def jwks_uri(self):
        """Gets the jwks_uri of this OAuth2Client.  # noqa: E501

        URL for the Client's JSON Web Key Set [JWK] document. If the Client signs requests to the Server, it contains the signing key(s) the Server uses to validate signatures from the Client. The JWK Set MAY also contain the Client's encryption keys(s), which are used by the Server to encrypt responses to the Client. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.  # noqa: E501

        :return: The jwks_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """Sets the jwks_uri of this OAuth2Client.

        URL for the Client's JSON Web Key Set [JWK] document. If the Client signs requests to the Server, it contains the signing key(s) the Server uses to validate signatures from the Client. The JWK Set MAY also contain the Client's encryption keys(s), which are used by the Server to encrypt responses to the Client. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.  # noqa: E501

        :param jwks_uri: The jwks_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._jwks_uri = jwks_uri

    @property
    def logo_uri(self):
        """Gets the logo_uri of this OAuth2Client.  # noqa: E501

        LogoURI is an URL string that references a logo for the client.  # noqa: E501

        :return: The logo_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._logo_uri

    @logo_uri.setter
    def logo_uri(self, logo_uri):
        """Sets the logo_uri of this OAuth2Client.

        LogoURI is an URL string that references a logo for the client.  # noqa: E501

        :param logo_uri: The logo_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._logo_uri = logo_uri

    @property
    def metadata(self):
        """Gets the metadata of this OAuth2Client.  # noqa: E501


        :return: The metadata of this OAuth2Client.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OAuth2Client.


        :param metadata: The metadata of this OAuth2Client.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def owner(self):
        """Gets the owner of this OAuth2Client.  # noqa: E501

        Owner is a string identifying the owner of the OAuth 2.0 Client.  # noqa: E501

        :return: The owner of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this OAuth2Client.

        Owner is a string identifying the owner of the OAuth 2.0 Client.  # noqa: E501

        :param owner: The owner of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def policy_uri(self):
        """Gets the policy_uri of this OAuth2Client.  # noqa: E501

        PolicyURI is a URL string that points to a human-readable privacy policy document that describes how the deployment organization collects, uses, retains, and discloses personal data.  # noqa: E501

        :return: The policy_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._policy_uri

    @policy_uri.setter
    def policy_uri(self, policy_uri):
        """Sets the policy_uri of this OAuth2Client.

        PolicyURI is a URL string that points to a human-readable privacy policy document that describes how the deployment organization collects, uses, retains, and discloses personal data.  # noqa: E501

        :param policy_uri: The policy_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._policy_uri = policy_uri

    @property
    def post_logout_redirect_uris(self):
        """Gets the post_logout_redirect_uris of this OAuth2Client.  # noqa: E501


        :return: The post_logout_redirect_uris of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._post_logout_redirect_uris

    @post_logout_redirect_uris.setter
    def post_logout_redirect_uris(self, post_logout_redirect_uris):
        """Sets the post_logout_redirect_uris of this OAuth2Client.


        :param post_logout_redirect_uris: The post_logout_redirect_uris of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._post_logout_redirect_uris = post_logout_redirect_uris

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this OAuth2Client.  # noqa: E501


        :return: The redirect_uris of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this OAuth2Client.


        :param redirect_uris: The redirect_uris of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

    @property
    def request_object_signing_alg(self):
        """Gets the request_object_signing_alg of this OAuth2Client.  # noqa: E501

        JWS [JWS] alg algorithm [JWA] that MUST be used for signing Request Objects sent to the OP. All Request Objects from this Client MUST be rejected, if not signed with this algorithm.  # noqa: E501

        :return: The request_object_signing_alg of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._request_object_signing_alg

    @request_object_signing_alg.setter
    def request_object_signing_alg(self, request_object_signing_alg):
        """Sets the request_object_signing_alg of this OAuth2Client.

        JWS [JWS] alg algorithm [JWA] that MUST be used for signing Request Objects sent to the OP. All Request Objects from this Client MUST be rejected, if not signed with this algorithm.  # noqa: E501

        :param request_object_signing_alg: The request_object_signing_alg of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._request_object_signing_alg = request_object_signing_alg

    @property
    def request_uris(self):
        """Gets the request_uris of this OAuth2Client.  # noqa: E501


        :return: The request_uris of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._request_uris

    @request_uris.setter
    def request_uris(self, request_uris):
        """Sets the request_uris of this OAuth2Client.


        :param request_uris: The request_uris of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._request_uris = request_uris

    @property
    def response_types(self):
        """Gets the response_types of this OAuth2Client.  # noqa: E501


        :return: The response_types of this OAuth2Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        """Sets the response_types of this OAuth2Client.


        :param response_types: The response_types of this OAuth2Client.  # noqa: E501
        :type: list[str]
        """

        self._response_types = response_types

    @property
    def scope(self):
        """Gets the scope of this OAuth2Client.  # noqa: E501

        Scope is a string containing a space-separated list of scope values (as described in Section 3.3 of OAuth 2.0 [RFC6749]) that the client can use when requesting access tokens.  # noqa: E501

        :return: The scope of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OAuth2Client.

        Scope is a string containing a space-separated list of scope values (as described in Section 3.3 of OAuth 2.0 [RFC6749]) that the client can use when requesting access tokens.  # noqa: E501

        :param scope: The scope of this OAuth2Client.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and not re.search(r'([a-zA-Z0-9\.\*]+\s?)+', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/([a-zA-Z0-9\.\*]+\s?)+/`")  # noqa: E501

        self._scope = scope

    @property
    def sector_identifier_uri(self):
        """Gets the sector_identifier_uri of this OAuth2Client.  # noqa: E501

        URL using the https scheme to be used in calculating Pseudonymous Identifiers by the OP. The URL references a file with a single JSON array of redirect_uri values.  # noqa: E501

        :return: The sector_identifier_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._sector_identifier_uri

    @sector_identifier_uri.setter
    def sector_identifier_uri(self, sector_identifier_uri):
        """Sets the sector_identifier_uri of this OAuth2Client.

        URL using the https scheme to be used in calculating Pseudonymous Identifiers by the OP. The URL references a file with a single JSON array of redirect_uri values.  # noqa: E501

        :param sector_identifier_uri: The sector_identifier_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._sector_identifier_uri = sector_identifier_uri

    @property
    def subject_type(self):
        """Gets the subject_type of this OAuth2Client.  # noqa: E501

        SubjectType requested for responses to this Client. The subject_types_supported Discovery parameter contains a list of the supported subject_type values for this server. Valid types include `pairwise` and `public`.  # noqa: E501

        :return: The subject_type of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this OAuth2Client.

        SubjectType requested for responses to this Client. The subject_types_supported Discovery parameter contains a list of the supported subject_type values for this server. Valid types include `pairwise` and `public`.  # noqa: E501

        :param subject_type: The subject_type of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._subject_type = subject_type

    @property
    def token_endpoint_auth_method(self):
        """Gets the token_endpoint_auth_method of this OAuth2Client.  # noqa: E501

        Requested Client Authentication method for the Token Endpoint. The options are client_secret_post, client_secret_basic, private_key_jwt, and none.  # noqa: E501

        :return: The token_endpoint_auth_method of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._token_endpoint_auth_method

    @token_endpoint_auth_method.setter
    def token_endpoint_auth_method(self, token_endpoint_auth_method):
        """Sets the token_endpoint_auth_method of this OAuth2Client.

        Requested Client Authentication method for the Token Endpoint. The options are client_secret_post, client_secret_basic, private_key_jwt, and none.  # noqa: E501

        :param token_endpoint_auth_method: The token_endpoint_auth_method of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._token_endpoint_auth_method = token_endpoint_auth_method

    @property
    def token_endpoint_auth_signing_alg(self):
        """Gets the token_endpoint_auth_signing_alg of this OAuth2Client.  # noqa: E501

        Requested Client Authentication signing algorithm for the Token Endpoint.  # noqa: E501

        :return: The token_endpoint_auth_signing_alg of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._token_endpoint_auth_signing_alg

    @token_endpoint_auth_signing_alg.setter
    def token_endpoint_auth_signing_alg(self, token_endpoint_auth_signing_alg):
        """Sets the token_endpoint_auth_signing_alg of this OAuth2Client.

        Requested Client Authentication signing algorithm for the Token Endpoint.  # noqa: E501

        :param token_endpoint_auth_signing_alg: The token_endpoint_auth_signing_alg of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._token_endpoint_auth_signing_alg = token_endpoint_auth_signing_alg

    @property
    def tos_uri(self):
        """Gets the tos_uri of this OAuth2Client.  # noqa: E501

        TermsOfServiceURI is a URL string that points to a human-readable terms of service document for the client that describes a contractual relationship between the end-user and the client that the end-user accepts when authorizing the client.  # noqa: E501

        :return: The tos_uri of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._tos_uri

    @tos_uri.setter
    def tos_uri(self, tos_uri):
        """Sets the tos_uri of this OAuth2Client.

        TermsOfServiceURI is a URL string that points to a human-readable terms of service document for the client that describes a contractual relationship between the end-user and the client that the end-user accepts when authorizing the client.  # noqa: E501

        :param tos_uri: The tos_uri of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._tos_uri = tos_uri

    @property
    def updated_at(self):
        """Gets the updated_at of this OAuth2Client.  # noqa: E501

        UpdatedAt returns the timestamp of the last update.  # noqa: E501

        :return: The updated_at of this OAuth2Client.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OAuth2Client.

        UpdatedAt returns the timestamp of the last update.  # noqa: E501

        :param updated_at: The updated_at of this OAuth2Client.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def userinfo_signed_response_alg(self):
        """Gets the userinfo_signed_response_alg of this OAuth2Client.  # noqa: E501

        JWS alg algorithm [JWA] REQUIRED for signing UserInfo Responses. If this is specified, the response will be JWT [JWT] serialized, and signed using JWS. The default, if omitted, is for the UserInfo Response to return the Claims as a UTF-8 encoded JSON object using the application/json content-type.  # noqa: E501

        :return: The userinfo_signed_response_alg of this OAuth2Client.  # noqa: E501
        :rtype: str
        """
        return self._userinfo_signed_response_alg

    @userinfo_signed_response_alg.setter
    def userinfo_signed_response_alg(self, userinfo_signed_response_alg):
        """Sets the userinfo_signed_response_alg of this OAuth2Client.

        JWS alg algorithm [JWA] REQUIRED for signing UserInfo Responses. If this is specified, the response will be JWT [JWT] serialized, and signed using JWS. The default, if omitted, is for the UserInfo Response to return the Claims as a UTF-8 encoded JSON object using the application/json content-type.  # noqa: E501

        :param userinfo_signed_response_alg: The userinfo_signed_response_alg of this OAuth2Client.  # noqa: E501
        :type: str
        """

        self._userinfo_signed_response_alg = userinfo_signed_response_alg

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OAuth2Client):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuth2Client):
            return True

        return self.to_dict() != other.to_dict()
