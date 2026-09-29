import pytest
import json
from services.product_service import ProductService
from services.user_service import UserService

# Product related
@pytest.fixture
def product_service():
    return ProductService()

@pytest.fixture
def get_products_schema():
    with open("test_data/schemas/get_products.json") as file:
        return json.load(file)

@pytest.fixture
def get_product_schema():
    with open("test_data/schemas/get_product.json") as file:
        return json.load(file)


@pytest.fixture
def product_with_valid_details():
    with open("test_data/request_payload/product/create_product.json") as file:
        return json.load(file)

@pytest.fixture
def product_with_empty_name():
    with open("test_data/request_payload/product/create_product.json") as file:
        product = json.load(file)
        product["name"]=""
        return product


@pytest.fixture
def product_with_negative_price():
    with open("test_data/request_payload/product/create_product.json") as file:
        product = json.load(file)
        product["price"]=-1
        return product
    
@pytest.fixture
def valid_product_id():
    with open("test_data/request_payload/product/create_product.json") as file:
        payload = json.load(file)
        return ProductService.get_valid_id(payload)

@pytest.fixture
def invalid_id_format():
    return "abc"


@pytest.fixture
def non_existing_id():
    return "ffffffff-ffff-ffff-ffff-ffffffffffff"

@pytest.fixture
def updated_prod_payload():
    with open("test_data/request_payload/product/updated_product.json") as file:
        return json.load(file)

@pytest.fixture
def update_prod_schema():
    with open("test_data/schemas/update_product.json") as file:
        return json.load(file)

@pytest.fixture
def updated_prod_with_empty_name():
    with open("test_data/request_payload/product/updated_product.json") as file:
        payload = json.load(file)
        payload["name"]=""
        return payload

@pytest.fixture
def updated_prod_with_negative_price():
    with open("test_data/request_payload/product/updated_product.json") as file:
        payload = json.load(file)
        payload["price"]=-10
        return payload

@pytest.fixture
def delete_prod_schema():
    with open("test_data/schemas/delete_product.json") as file:
        return json.load(file)

# For raport
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    marker = item.get_closest_marker("testcase")

    if marker:
        report.testcase = marker.args[0]

# For raport
def pytest_html_results_table_row(report, cells):
    testcase = getattr(report, "testcase", None)

    if testcase:
        cells[1] = testcase



# User related
@pytest.fixture
def user_service():
    return UserService()

@pytest.fixture
def get_users_schema():
    with open("test_data/schemas/get_users.json") as file:
        return json.load(file)

@pytest.fixture
def get_user_schema():
    with open("test_data/schemas/get_user.json") as file:
        return json.load(file)

@pytest.fixture
def valid_user_id():
    with open("test_data/request_payload/user/create_user.json") as file:
        payload = json.load(file)
        return UserService.get_valid_id(payload)



@pytest.fixture
def delete_user_schema():
    with open("test_data/schemas/delete_user.json") as file:
        return json.load(file)


@pytest.fixture
def user_with_valid_details():
    with open("test_data/request_payload/user/create_user.json") as file:
        return json.load(file)


@pytest.fixture
def user_with_empty_name():
    with open("test_data/request_payload/user/create_user.json") as file:
        user = json.load(file)
        user["name"]=""
        return user

@pytest.fixture
def user_with_invalid_email_format():
    with open("test_data/request_payload/user/create_user.json") as file:
        user = json.load(file)
        user["email"]="invalid_email_format"
        return user

@pytest.fixture
def updated_user_payload():
    with open("test_data/request_payload/user/updated_user.json") as file:
        return json.load(file)

@pytest.fixture
def update_user_schema():
    with open("test_data/schemas/update_user.json") as file:
        return json.load(file)

@pytest.fixture
def updated_user_with_empty_name():
    with open("test_data/request_payload/user/updated_user.json") as file:
        payload = json.load(file)
        payload["name"]=""
        return payload


@pytest.fixture
def updated_user_with_invalid_role():
    with open("test_data/request_payload/user/updated_user.json") as file:
        payload = json.load(file)
        payload["role"]= "invalid_role"
        return payload