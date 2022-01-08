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
from ory_hydra_client.models.accept_login_request import AcceptLoginRequest  # noqa: E501
from ory_hydra_client.rest import ApiException

class TestAcceptLoginRequest(unittest.TestCase):
    """AcceptLoginRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AcceptLoginRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ory_hydra_client.models.accept_login_request.AcceptLoginRequest()  # noqa: E501
        if include_optional :
            return AcceptLoginRequest(
                acr = '0', 
                context = ory_hydra_client.models.json_raw_message_represents_a_json/raw_message_that_works_well_with_json,_sql,_and_swagger/.JSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger.(), 
                force_subject_identifier = '0', 
                remember = True, 
                remember_for = 56, 
                subject = '0'
            )
        else :
            return AcceptLoginRequest(
                subject = '0',
        )

    def testAcceptLoginRequest(self):
        """Test AcceptLoginRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
