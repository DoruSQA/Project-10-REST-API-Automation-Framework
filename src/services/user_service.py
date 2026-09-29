from services.base_service import BaseService


class UserService(BaseService):

    BASE_URL = "https://demo.totalshiftleft.ai"
    ROUTE = "/api/v1/users"

    def get_all_users(self):
        return self._request(
            "GET",
            self.BASE_URL + self.ROUTE
        )

    def get_user_by_id(self, id):
        return self._request(
            "GET",
            self.BASE_URL + self.ROUTE + "/" + id
        )

    def create_user(self, payload):
        return self._request(
            "POST",
            self.BASE_URL + self.ROUTE,
            json_body=payload
        )

    def update_user(self, id, payload):
        return self._request(
            "PUT",
            self.BASE_URL + self.ROUTE + "/" + id,
            json_body=payload
        )

    def delete_user_by_id(self, id):
        return self._request(
            "DELETE",
            self.BASE_URL + self.ROUTE + "/" + id
        )

    @staticmethod
    def get_valid_id(payload):
        service = UserService()

        response = service.create_user(payload)

        return response.json()["data"]["id"]
