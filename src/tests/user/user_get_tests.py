import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.user_expected_data import UserExpected
from jsonschema import validate as validate_schema

@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_001: Get all users")
def test_get_all_users(user_service, get_users_schema):

    # Send request
    http_response = user_service.get_all_users()

    # Validate status code and content type
    assert http_response.status_code == StatusCode.OK
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=get_users_schema)
    
    # Validate response body
    soft_assert.is_true(response_body["success"])


@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_002: Get user with valid id")
def test_get_user_with_valid_id(user_service, get_user_schema, valid_user_id):

    # Send request
    http_response = user_service.get_user_by_id(valid_user_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.OK
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=get_user_schema)

    # Validate response body
    soft_assert.equal(response_body["data"]["id"], valid_user_id)


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_003: Get user with invalid id format")
def test_get_user_with_invalid_id_format(user_service, invalid_id_format):

    # Send request
    http_response = user_service.get_user_by_id(invalid_id_format)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(UserExpected.INVALID_ID_FORMAT, response_body["message"])


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_004: Get user with non existing id")
def test_get_user_with_non_existing_id(user_service, non_existing_id):

    # Send request
    http_response = user_service.get_user_by_id(non_existing_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.NOT_FOUND
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(UserExpected.ID_NOT_FOUND, response_body["message"])
