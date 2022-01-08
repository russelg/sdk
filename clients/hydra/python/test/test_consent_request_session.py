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
from ory_hydra_client.models.consent_request_session import ConsentRequestSession  # noqa: E501
from ory_hydra_client.rest import ApiException

class TestConsentRequestSession(unittest.TestCase):
    """ConsentRequestSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConsentRequestSession
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ory_hydra_client.models.consent_request_session.ConsentRequestSession()  # noqa: E501
        if include_optional :
            return ConsentRequestSession(
                access_token = ory_hydra_client.models.access_token.access_token(), 
                id_token = ory_hydra_client.models.id_token.id_token()
            )
        else :
            return ConsentRequestSession(
        )

    def testConsentRequestSession(self):
        """Test ConsentRequestSession"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
