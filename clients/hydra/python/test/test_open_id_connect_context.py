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
from ory_hydra_client.models.open_id_connect_context import OpenIDConnectContext  # noqa: E501
from ory_hydra_client.rest import ApiException

class TestOpenIDConnectContext(unittest.TestCase):
    """OpenIDConnectContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OpenIDConnectContext
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ory_hydra_client.models.open_id_connect_context.OpenIDConnectContext()  # noqa: E501
        if include_optional :
            return OpenIDConnectContext(
                acr_values = [
                    '0'
                    ], 
                display = '0', 
                id_token_hint_claims = ory_hydra_client.models.id_token_hint_claims.id_token_hint_claims(), 
                login_hint = '0', 
                ui_locales = [
                    '0'
                    ]
            )
        else :
            return OpenIDConnectContext(
        )

    def testOpenIDConnectContext(self):
        """Test OpenIDConnectContext"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
