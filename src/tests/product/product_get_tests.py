import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.product_expected_data import ProductExpected
from jsonschema import validate as validate_schema

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.product
@pytest.mark.testcase("TC_PROD_001: Get all products")
def test_get_all_products(product_service, get_products_schema):

    # Send request
    http_response = product_service.get_all_products()

    # Validate status code and content type
    assert http_response.status_code == StatusCode.OK
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=get_products_schema)
    
    # Validate response body
    soft_assert.is_true(response_body["success"])


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.product
@pytest.mark.testcase("TC_PROD_002: Get product with valid id")
def test_get_product_with_valid_id(product_service, get_product_schema, valid_product_id):

    # Send request
    http_response = product_service.get_product_by_id(valid_product_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.OK
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=get_product_schema)

    # Validate response body
    soft_assert.equal(response_body["data"]["id"], valid_product_id)


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_003: Get product with invalid id format")
def test_get_product_with_invalid_id_format(product_service, invalid_id_format):

    # Send request
    http_response = product_service.get_product_by_id(invalid_id_format)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(ProductExpected.INVALID_ID_FORMAT, response_body["message"])
    

@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_004: Get product with non existing id")
def test_get_product_with_non_existing_id(product_service, non_existing_id):

    # Send request
    http_response = product_service.get_product_by_id(non_existing_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.NOT_FOUND
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(ProductExpected.ID_NOT_FOUND, response_body["message"])



