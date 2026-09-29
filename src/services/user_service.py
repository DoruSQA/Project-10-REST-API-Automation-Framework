import json
import logging
import time

import requests


logger = logging.getLogger("api")


class UserService:
    BASE_URL = "https://demo.totalshiftleft.ai"
    ROUTE = "/api/v1/users"

    def _log_request(self, method, url, payload=None):
        endpoint = url.replace(self.BASE_URL, "")

        logger.info("REQUEST")
        logger.info("  %s %s", method, endpoint)

        if payload is not None:
            logger.info("  Body:")
            logger.info(
                "%s",
                json.dumps(
                    payload,
                    indent=4,
                    ensure_ascii=False
                )
            )

    def _log_response(self, response, duration):
        endpoint = response.url.replace(self.BASE_URL, "")

        logger.info("RESPONSE")
        logger.info("  Status: %s", response.status_code)
        logger.info("  Time:   %.3fs", duration)

        try:
            response_body = response.json()

            logger.info("  Body:")
            logger.info(
                "%s",
                json.dumps(
                    response_body,
                    indent=4,
                    ensure_ascii=False
                )
            )

        except ValueError:
            logger.info("  Body: %s", response.text)

    def get_all_users(self):
        url = UserService.BASE_URL + UserService.ROUTE

        self._log_request("GET", url)

        start = time.perf_counter()
        response = requests.get(url)
        duration = time.perf_counter() - start

        self._log_response(response, duration)

        return response

    def get_user_by_id(self, id):
        url = UserService.BASE_URL + UserService.ROUTE + "/" + id

        self._log_request("GET", url)

        start = time.perf_counter()
        response = requests.get(url)
        duration = time.perf_counter() - start

        self._log_response(response, duration)

        return response

    def create_user(self, payload):
        url = UserService.BASE_URL + UserService.ROUTE

        self._log_request("POST", url, payload)

        start = time.perf_counter()
        response = requests.post(
            url,
            json=payload
        )
        duration = time.perf_counter() - start

        self._log_response(response, duration)

        return response

    def update_user(self, id, payload):
        url = UserService.BASE_URL + UserService.ROUTE + "/" + id

        self._log_request("PUT", url, payload)

        start = time.perf_counter()
        response = requests.put(
            url,
            json=payload
        )
        duration = time.perf_counter() - start

        self._log_response(response, duration)

        return response

    def delete_user_by_id(self, id):
        url = UserService.BASE_URL + UserService.ROUTE + "/" + id

        self._log_request("DELETE", url)

        start = time.perf_counter()
        response = requests.delete(url)
        duration = time.perf_counter() - start

        self._log_response(response, duration)

        return response

    @staticmethod
    def get_valid_id(payload):
        url = UserService.BASE_URL + UserService.ROUTE

        logger.info("REQUEST")
        logger.info("  POST %s", UserService.ROUTE)
        logger.info("  Body:")
        logger.info(
            "%s",
            json.dumps(
                payload,
                indent=4,
                ensure_ascii=False
            )
        )

        start = time.perf_counter()
        response = requests.post(
            url,
            json=payload
        )
        duration = time.perf_counter() - start

        logger.info("RESPONSE")
        logger.info("  Status: %s", response.status_code)
        logger.info("  Time:   %.3fs", duration)

        try:
            response_body = response.json()

            logger.info("  Body:")
            logger.info(
                "%s",
                json.dumps(
                    response_body,
                    indent=4,
                    ensure_ascii=False
                )
            )

        except ValueError:
            logger.info("  Body: %s", response.text)

        return response.json()["data"]["id"]
