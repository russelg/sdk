"""
    ORY Keto

    Ory Keto is a cloud native access control server providing best-practice patterns (RBAC, ABAC, ACL, AWS IAM Policies, Kubernetes Roles, ...) via REST APIs.  # noqa: E501

    The version of the OpenAPI document: v0.7.0-alpha.0
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_keto_client
from ory_keto_client.api.read_api import ReadApi  # noqa: E501


class TestReadApi(unittest.TestCase):
    """ReadApi unit test stubs"""

    def setUp(self):
        self.api = ReadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_check(self):
        """Test case for get_check

        Check a relation tuple  # noqa: E501
        """
        pass

    def test_get_expand(self):
        """Test case for get_expand

        Expand a Relation Tuple  # noqa: E501
        """
        pass

    def test_get_relation_tuples(self):
        """Test case for get_relation_tuples

        Query relation tuples  # noqa: E501
        """
        pass

    def test_post_check(self):
        """Test case for post_check

        Check a relation tuple  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
