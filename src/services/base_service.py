import requests
import logging
import time
import json


logger = logging.getLogger("api")


class BaseService:

    def _request(self, method, url, json_body=None):
        logger.info("REQUEST")
        logger.info(
            f"  {method} {url.replace(self.BASE_URL, '')}"
        )

        if json_body is not None:
            logger.info("  Body:")
            logger.info(
                json.dumps(
                    json_body,
                    indent=4,
                    ensure_ascii=False
                )
            )

        start_time = time.perf_counter()

        response = requests.request(
            method=method,
            url=url,
            json=json_body
        )

        duration = time.perf_counter() - start_time

        logger.info("RESPONSE")
        logger.info(f"  Status: {response.status_code}")
        logger.info(f"  Time:   {duration:.3f}s")
        logger.info("  Body:")

        try:
            logger.info(
                json.dumps(
                    response.json(),
                    indent=4,
                    ensure_ascii=False
                )
            )
        except ValueError:
            logger.info(response.text)

        return response
