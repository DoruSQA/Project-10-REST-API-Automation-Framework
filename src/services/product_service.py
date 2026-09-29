from services.base_service import BaseService


class ProductService(BaseService):

    BASE_URL = "https://demo.totalshiftleft.ai"
    ROUTE = "/api/v1/products"

    def get_all_products(self):
        return self._request(
            "GET",
            self.BASE_URL + self.ROUTE
        )

    def get_product_by_id(self, id):
        return self._request(
            "GET",
            self.BASE_URL + self.ROUTE + "/" + id
        )

    def create_product(self, payload):
        return self._request(
            "POST",
            self.BASE_URL + self.ROUTE,
            json_body=payload
        )

    def update_product(self, id, payload):
        return self._request(
            "PUT",
            self.BASE_URL + self.ROUTE + "/" + id,
            json_body=payload
        )

    def delete_product_by_id(self, id):
        return self._request(
            "DELETE",
            self.BASE_URL + self.ROUTE + "/" + id
        )

    @staticmethod
    def get_valid_id(payload):
        service = ProductService()

        response = service.create_product(payload)

        return response.json()["data"]["id"]
