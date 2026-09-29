import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.user_expected_data import UserExpected


@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_005: Create user with valid details")
def test_create_user_with_valid_details(user_service, user_with_valid_details):
    # Send request
    http_response = user_service.create_user(user_with_valid_details)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.CREATED
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_not_none(response_body["data"]["id"])
    soft_assert.equal(response_body["data"]["name"], user_with_valid_details["name"])
    soft_assert.equal(response_body["data"]["email"], user_with_valid_details["email"])
    soft_assert.equal(response_body["data"]["role"], user_with_valid_details["role"])


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_006: Create user with empty name")
def test_create_user_with_empty_name(user_service, user_with_empty_name):

    # Send request
    http_response = user_service.create_user(user_with_empty_name)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(UserExpected.USER_NAME_MUST_CONTAIN_AT_LEAST_1_CHARACTER, response_body["message"])


@pytest.mark.user
@pytest.mark.regression
@pytest.mark.testcase("TC_USER_007: Create user with invalid email format")
def test_create_user_with_invalid_email_format(user_service, user_with_invalid_email_format):

    # Send request
    http_response = user_service.create_user(user_with_invalid_email_format)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(UserExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(UserExpected.EMAIL_WITH_INVALID_FORMAT, response_body["message"])