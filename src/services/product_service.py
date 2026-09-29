import requests

class ProductService:
    BASE_URL = "https://demo.totalshiftleft.ai"
    ROUTE = "/api/v1/products"

    def get_all_products(self):
        return requests.get(ProductService.BASE_URL+ProductService.ROUTE)

    def get_product_by_id(self, id):
        return requests.get(ProductService.BASE_URL+ProductService.ROUTE+"/"+id)

    def create_product(self, payload):
        return requests.post(ProductService.BASE_URL+ProductService.ROUTE,json=payload)

    def update_product(self, id, payload):
        return requests.put(ProductService.BASE_URL+ProductService.ROUTE+"/"+id, json=payload)

    def delete_product_by_id(self, id):
        return requests.delete(ProductService.BASE_URL+ProductService.ROUTE+"/"+id)
        
    @staticmethod
    def get_valid_id(payload):
        response= requests.post(ProductService.BASE_URL+ProductService.ROUTE,json=payload)
        return response.json()["data"]["id"]

