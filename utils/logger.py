import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log(response, json=None):
    logger.info(f"Request method: {response.request.method}")
    logger.info(f"Request url: {response.url}")
    logger.info(f"Request json body: {json}")
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response json body: {response.text}")
