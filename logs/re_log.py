import logging
from logging.handlers import RotatingFileHandler


def async_uvicorn_logger():
    logger = logging.getLogger('uvicorn.access')
    handler = RotatingFileHandler(filename='logs/api.log', mode='a', encoding='UTF-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s %(message)s'))
    logger.addHandler(handler)


def _log_re():
    logger = logging.getLogger('uvicorn.access')
    if not logger.handlers:
        logger = logging.getLogger('uvicorn.access')
        handler = RotatingFileHandler(filename='logs/api.log', mode='a', encoding='UTF-8')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s %(message)s'))
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s %(message)s'))
        logger.addHandler(console_handler)
        logger.addHandler(handler)
    return logger


def log(*args):
    logger = _log_re()
    for item in args:
        logger.info(item)
