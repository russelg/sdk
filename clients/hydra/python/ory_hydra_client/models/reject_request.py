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


class RejectRequest(object):
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
        'error': 'str',
        'error_debug': 'str',
        'error_description': 'str',
        'error_hint': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'error': 'error',
        'error_debug': 'error_debug',
        'error_description': 'error_description',
        'error_hint': 'error_hint',
        'status_code': 'status_code'
    }

    def __init__(self, error=None, error_debug=None, error_description=None, error_hint=None, status_code=None, local_vars_configuration=None):  # noqa: E501
        """RejectRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._error_debug = None
        self._error_description = None
        self._error_hint = None
        self._status_code = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if error_debug is not None:
            self.error_debug = error_debug
        if error_description is not None:
            self.error_description = error_description
        if error_hint is not None:
            self.error_hint = error_hint
        if status_code is not None:
            self.status_code = status_code

    @property
    def error(self):
        """Gets the error of this RejectRequest.  # noqa: E501

        The error should follow the OAuth2 error format (e.g. `invalid_request`, `login_required`).  Defaults to `request_denied`.  # noqa: E501

        :return: The error of this RejectRequest.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RejectRequest.

        The error should follow the OAuth2 error format (e.g. `invalid_request`, `login_required`).  Defaults to `request_denied`.  # noqa: E501

        :param error: The error of this RejectRequest.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_debug(self):
        """Gets the error_debug of this RejectRequest.  # noqa: E501

        Debug contains information to help resolve the problem as a developer. Usually not exposed to the public but only in the server logs.  # noqa: E501

        :return: The error_debug of this RejectRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_debug

    @error_debug.setter
    def error_debug(self, error_debug):
        """Sets the error_debug of this RejectRequest.

        Debug contains information to help resolve the problem as a developer. Usually not exposed to the public but only in the server logs.  # noqa: E501

        :param error_debug: The error_debug of this RejectRequest.  # noqa: E501
        :type: str
        """

        self._error_debug = error_debug

    @property
    def error_description(self):
        """Gets the error_description of this RejectRequest.  # noqa: E501

        Description of the error in a human readable format.  # noqa: E501

        :return: The error_description of this RejectRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this RejectRequest.

        Description of the error in a human readable format.  # noqa: E501

        :param error_description: The error_description of this RejectRequest.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

    @property
    def error_hint(self):
        """Gets the error_hint of this RejectRequest.  # noqa: E501

        Hint to help resolve the error.  # noqa: E501

        :return: The error_hint of this RejectRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_hint

    @error_hint.setter
    def error_hint(self, error_hint):
        """Sets the error_hint of this RejectRequest.

        Hint to help resolve the error.  # noqa: E501

        :param error_hint: The error_hint of this RejectRequest.  # noqa: E501
        :type: str
        """

        self._error_hint = error_hint

    @property
    def status_code(self):
        """Gets the status_code of this RejectRequest.  # noqa: E501

        Represents the HTTP status code of the error (e.g. 401 or 403)  Defaults to 400  # noqa: E501

        :return: The status_code of this RejectRequest.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RejectRequest.

        Represents the HTTP status code of the error (e.g. 401 or 403)  Defaults to 400  # noqa: E501

        :param status_code: The status_code of this RejectRequest.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if not isinstance(other, RejectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RejectRequest):
            return True

        return self.to_dict() != other.to_dict()
