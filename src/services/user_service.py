import requests

class UserService:
    BASE_URL = "https://demo.totalshiftleft.ai"
    ROUTE = "/api/v1/users"

    def get_all_users(self):
        return requests.get(UserService.BASE_URL+UserService.ROUTE)

    def get_user_by_id(self, id):
        return requests.get(UserService.BASE_URL+UserService.ROUTE+"/"+id)

    def create_user(self, payload):
        return requests.post(UserService.BASE_URL+UserService.ROUTE,json=payload)

    def update_user(self, id, payload):
        return requests.put(UserService.BASE_URL+UserService.ROUTE+"/"+id, json=payload)

    def delete_user_by_id(self, id):
        return requests.delete(UserService.BASE_URL+UserService.ROUTE+"/"+id)
        
    @staticmethod
    def get_valid_id(payload):
        response= requests.post(UserService.BASE_URL+UserService.ROUTE,json=payload)
        return response.json()["data"]["id"]
