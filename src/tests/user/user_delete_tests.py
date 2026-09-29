import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.user_expected_data import UserExpected
from jsonschema import validate as validate_schema

@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_011: Delete user with valid id")
def test_delete_user_with_valid_id(user_service, valid_user_id):

    # Send request
    http_response = user_service.delete_user_by_id(valid_user_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.NO_CONTENT


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_012: Delete user with non existing id")
def test_delete_user_with_non_existing_id(user_service, non_existing_id, delete_user_schema):

    # Send request
    http_response = user_service.delete_user_by_id(non_existing_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.NOT_FOUND
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=delete_user_schema)

    # Validate response body
    soft_assert.is_in(UserExpected.ID_NOT_FOUND, response_body["message"])


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER013: Delete user with invalid id format")
def test_delete_prod_with_invalid_id_format(user_service, invalid_id_format):

    # Send request
    http_response = user_service.delete_user_by_id(invalid_id_format)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(UserExpected.INVALID_ID_FORMAT, response_body["message"])