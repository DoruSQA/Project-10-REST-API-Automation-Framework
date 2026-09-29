import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.product_expected_data import ProductExpected


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.product
@pytest.mark.testcase("TC_PROD_005: Create product with valid details")
def test_create_product_with_valid_details(product_service, product_with_valid_details):
    # Send request
    http_response = product_service.create_product(product_with_valid_details)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.CREATED
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_not_none(response_body["data"]["id"])
    soft_assert.equal(response_body["data"]["name"], product_with_valid_details["name"])
    soft_assert.equal(response_body["data"]["price"], product_with_valid_details["price"])
    soft_assert.equal(response_body["data"]["stock"], product_with_valid_details["stock"])


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_006: Create product with empty name")
def test_create_product_with_empty_name(product_service, product_with_empty_name):

    # Send request
    http_response = product_service.create_product(product_with_empty_name)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(ProductExpected.PROD_NAME_MUST_CONTAIN_AT_LEAST_1_CHARACTER, response_body["message"])


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_007: Create product with negative price")
def test_create_product_with_negative_price(product_service, product_with_negative_price):

    # Send request
    http_response = product_service.create_product(product_with_negative_price)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(ProductExpected.PRICE_GREATER_THAN_0, response_body["message"])