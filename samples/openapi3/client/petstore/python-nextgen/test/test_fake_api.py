# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import petstore_api
from petstore_api.api.fake_api import FakeApi  # noqa: E501


class TestFakeApi(unittest.TestCase):
    """FakeApi unit test stubs"""

    def setUp(self):
        self.api = petstore_api.api.fake_api.FakeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fake_health_get(self):
        """Test case for fake_health_get

        Health check endpoint  # noqa: E501
        """
        pass

    def test_fake_http_signature_test(self):
        """Test case for fake_http_signature_test

        test http signature authentication  # noqa: E501
        """
        pass

    def test_fake_outer_boolean_serialize(self):
        """Test case for fake_outer_boolean_serialize

        """
        pass

    def test_fake_outer_composite_serialize(self):
        """Test case for fake_outer_composite_serialize

        """
        pass

    def test_fake_outer_number_serialize(self):
        """Test case for fake_outer_number_serialize

        """
        pass

    def test_fake_outer_string_serialize(self):
        """Test case for fake_outer_string_serialize

        """
        pass

    def test_test_body_with_file_schema(self):
        """Test case for test_body_with_file_schema

        """
        pass

    def test_test_body_with_query_params(self):
        """Test case for test_body_with_query_params

        """
        pass

    def test_test_client_model(self):
        """Test case for test_client_model

        To test \"client\" model  # noqa: E501
        """
        pass

    def test_test_endpoint_parameters(self):
        """Test case for test_endpoint_parameters

        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트   # noqa: E501
        """
        pass

    def test_test_enum_parameters(self):
        """Test case for test_enum_parameters

        To test enum parameters  # noqa: E501
        """
        pass

    def test_test_group_parameters(self):
        """Test case for test_group_parameters

        Fake endpoint to test group parameters (optional)  # noqa: E501
        """
        pass

    def test_test_inline_additional_properties(self):
        """Test case for test_inline_additional_properties

        test inline additionalProperties  # noqa: E501
        """
        pass

    def test_test_json_form_data(self):
        """Test case for test_json_form_data

        test json serialization of form data  # noqa: E501
        """
        pass

    def test_test_query_parameter_collection_format(self):
        """Test case for test_query_parameter_collection_format

        """
        pass

    def test_headers_parameter(self):
        """Test case for the _headers are passed by the user

        To test any optional parameter  # noqa: E501
        """
        api = petstore_api.api.PetApi()
        with patch("petstore_api.api_client.ApiClient.call_api") as mock_method:
            value_headers = {"Header1": "value1"}
            api.find_pets_by_status(["available"], _headers=value_headers)
            args, _ = mock_method.call_args
            self.assertEqual(args, ('/pet/findByStatus', 'GET', {}, [('status', ['available'])], {'Accept': 'application/json', 'Header1': 'value1'})
)

if __name__ == '__main__':
    unittest.main()
