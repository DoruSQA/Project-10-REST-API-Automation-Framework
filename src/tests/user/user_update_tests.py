import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.user_expected_data import UserExpected
from jsonschema import validate as validate_schema


@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_008: Update user with valid details")
def test_update_user_with_valid_details(user_service, valid_user_id, updated_user_payload, update_user_schema):

    # Send request
    http_response = user_service.update_user(valid_user_id, updated_user_payload)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.OK
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=update_user_schema)

    # Validate response body
    soft_assert.is_not_none(response_body["data"]["id"])
    soft_assert.equal(response_body["data"]["name"], updated_user_payload["name"])
    soft_assert.equal(response_body["data"]["email"], updated_user_payload["email"])
    soft_assert.equal(response_body["data"]["role"], updated_user_payload["role"])


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_009: Update user with empty name")
def test_update_user_with_empty_name(user_service, valid_user_id, updated_user_with_empty_name):

    # Send request
    http_response = user_service.update_user(valid_user_id, updated_user_with_empty_name)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(UserExpected.USER_NAME_MUST_CONTAIN_AT_LEAST_1_CHARACTER, response_body["message"])


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_010: Update user with invalid role")
def test_update_user_with_negative_price(user_service, valid_user_id, updated_user_with_invalid_role):

    # Send request
    http_response = user_service.update_user(valid_user_id, updated_user_with_invalid_role)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(UserExpected.INVALID_ROLE, response_body["message"])