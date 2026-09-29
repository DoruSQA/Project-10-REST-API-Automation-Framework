import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.product_expected_data import ProductExpected
from jsonschema import validate as validate_schema


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.product
@pytest.mark.testcase("TC_PROD_008: Update product with valid details")
def test_update_prod_with_valid_details(product_service, valid_product_id, updated_prod_payload, update_prod_schema):

    # Send request
    http_response = product_service.update_product(valid_product_id, updated_prod_payload)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.OK
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=update_prod_schema)

    # Validate response body
    soft_assert.is_not_none(response_body["data"]["id"])
    soft_assert.equal(response_body["data"]["name"], updated_prod_payload["name"])
    soft_assert.equal(response_body["data"]["price"], updated_prod_payload["price"])
    soft_assert.equal(response_body["data"]["stock"], updated_prod_payload["stock"])


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_009: Update product with empty name")
def test_update_prod_with_empty_name(product_service, valid_product_id, updated_prod_with_empty_name):

    # Send request
    http_response = product_service.update_product(valid_product_id, updated_prod_with_empty_name)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(ProductExpected.PROD_NAME_MUST_CONTAIN_AT_LEAST_1_CHARACTER, response_body["message"])


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_010: Update product with negative price")
def test_update_prod_with_negative_price(product_service, valid_product_id, updated_prod_with_negative_price):

    # Send request
    http_response = product_service.update_product(valid_product_id, updated_prod_with_negative_price)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(ProductExpected.PRICE_GREATER_THAN_0, response_body["message"])
