import pytest
import pytest_check as soft_assert
from test_data.expected.status_code import StatusCode
from test_data.expected.product_expected_data import ProductExpected
from jsonschema import validate as validate_schema

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.product
@pytest.mark.testcase("TC_PROD_011: Delete product with valid id")
def test_delete_prod_with_valid_id(product_service, valid_product_id):

    # Send request
    http_response = product_service.delete_product_by_id(valid_product_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.NO_CONTENT


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_012: Delete product with non existing id")
def test_delete_prod_with_non_existing_id(product_service, non_existing_id, delete_prod_schema):

    # Send request
    http_response = product_service.delete_product_by_id(non_existing_id)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.NOT_FOUND
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response schema
    validate_schema(instance=response_body, schema=delete_prod_schema)

    # Validate response body
    soft_assert.is_in(ProductExpected.ID_NOT_FOUND, response_body["message"])


@pytest.mark.product
@pytest.mark.regression
@pytest.mark.testcase("TC_PROD_013: Delete product with invalid id format")
def test_delete_prod_with_invalid_id_format(product_service, invalid_id_format):

    # Send request
    http_response = product_service.delete_product_by_id(invalid_id_format)

    # Validate status code and content type
    assert http_response.status_code == StatusCode.BAD_REQUEST
    assert http_response.headers["Content-Type"].startswith(ProductExpected.CONTENT_TYPE)

    response_body = http_response.json()

    # Validate response body
    soft_assert.is_in(ProductExpected.INVALID_ID_FORMAT, response_body["message"])
