# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.10.6
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ory_hydra_client
from ory_hydra_client.models.login_request import LoginRequest  # noqa: E501
from ory_hydra_client.rest import ApiException

class TestLoginRequest(unittest.TestCase):
    """LoginRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoginRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ory_hydra_client.models.login_request.LoginRequest()  # noqa: E501
        if include_optional :
            return LoginRequest(
                challenge = '0', 
                client = ory_hydra_client.models.client_represents_an_o_auth_2/0_client/.Client represents an OAuth 2.0 Client.(
                    allowed_cors_origins = [
                        '0'
                        ], 
                    audience = [
                        '0'
                        ], 
                    backchannel_logout_session_required = True, 
                    backchannel_logout_uri = '0', 
                    client_id = '0', 
                    client_name = '0', 
                    client_secret = '0', 
                    client_secret_expires_at = 56, 
                    client_uri = '0', 
                    contacts = [
                        '0'
                        ], 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    frontchannel_logout_session_required = True, 
                    frontchannel_logout_uri = '0', 
                    grant_types = [
                        '0'
                        ], 
                    jwks = ory_hydra_client.models.jose_json_web_key_set.JoseJSONWebKeySet(), 
                    jwks_uri = '0', 
                    logo_uri = '0', 
                    metadata = ory_hydra_client.models.json_raw_message_represents_a_json/raw_message_that_works_well_with_json,_sql,_and_swagger/.JSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger.(), 
                    owner = '0', 
                    policy_uri = '0', 
                    post_logout_redirect_uris = [
                        '0'
                        ], 
                    redirect_uris = [
                        '0'
                        ], 
                    request_object_signing_alg = '0', 
                    request_uris = [
                        '0'
                        ], 
                    response_types = [
                        '0'
                        ], 
                    scope = 'a', 
                    sector_identifier_uri = '0', 
                    subject_type = '0', 
                    token_endpoint_auth_method = '0', 
                    token_endpoint_auth_signing_alg = '0', 
                    tos_uri = '0', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    userinfo_signed_response_alg = '0', ), 
                oidc_context = ory_hydra_client.models.contains_optional_information_about_the_open_id_connect_request/.Contains optional information about the OpenID Connect request.(
                    acr_values = [
                        '0'
                        ], 
                    display = '0', 
                    id_token_hint_claims = ory_hydra_client.models.id_token_hint_claims.id_token_hint_claims(), 
                    login_hint = '0', 
                    ui_locales = [
                        '0'
                        ], ), 
                request_url = '0', 
                requested_access_token_audience = [
                    '0'
                    ], 
                requested_scope = [
                    '0'
                    ], 
                session_id = '0', 
                skip = True, 
                subject = '0'
            )
        else :
            return LoginRequest(
                challenge = '0',
                client = ory_hydra_client.models.client_represents_an_o_auth_2/0_client/.Client represents an OAuth 2.0 Client.(
                    allowed_cors_origins = [
                        '0'
                        ], 
                    audience = [
                        '0'
                        ], 
                    backchannel_logout_session_required = True, 
                    backchannel_logout_uri = '0', 
                    client_id = '0', 
                    client_name = '0', 
                    client_secret = '0', 
                    client_secret_expires_at = 56, 
                    client_uri = '0', 
                    contacts = [
                        '0'
                        ], 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    frontchannel_logout_session_required = True, 
                    frontchannel_logout_uri = '0', 
                    grant_types = [
                        '0'
                        ], 
                    jwks = ory_hydra_client.models.jose_json_web_key_set.JoseJSONWebKeySet(), 
                    jwks_uri = '0', 
                    logo_uri = '0', 
                    metadata = ory_hydra_client.models.json_raw_message_represents_a_json/raw_message_that_works_well_with_json,_sql,_and_swagger/.JSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger.(), 
                    owner = '0', 
                    policy_uri = '0', 
                    post_logout_redirect_uris = [
                        '0'
                        ], 
                    redirect_uris = [
                        '0'
                        ], 
                    request_object_signing_alg = '0', 
                    request_uris = [
                        '0'
                        ], 
                    response_types = [
                        '0'
                        ], 
                    scope = 'a', 
                    sector_identifier_uri = '0', 
                    subject_type = '0', 
                    token_endpoint_auth_method = '0', 
                    token_endpoint_auth_signing_alg = '0', 
                    tos_uri = '0', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    userinfo_signed_response_alg = '0', ),
                request_url = '0',
                requested_access_token_audience = [
                    '0'
                    ],
                requested_scope = [
                    '0'
                    ],
                skip = True,
                subject = '0',
        )

    def testLoginRequest(self):
        """Test LoginRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
