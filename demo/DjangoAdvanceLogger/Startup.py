import logging
import requests

logger = logging.getLogger("django")


class Startup:
    def __init__(self):
        logger.info("start app", extra={"extraParams": "test"})
        logger.debug("start app")
        logger.error('test')
        requests.get('https://reqres.in/api/users?page=2')