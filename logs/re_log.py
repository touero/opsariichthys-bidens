import logging


def _log_re(log_level=logging.INFO):
    logger = logging.getLogger('API')
    logger.setLevel(level=log_level)

    file_handler = logging.FileHandler(filename='logs/api.log', encoding='UTF-8')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s %(message)s')
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)

    if logger.handlers:
        logger.handlers.clear()

    logger.handlers = [file_handler, stream_handler]

    g_log = logger
    return g_log


def log(*args, **kwargs):
    msg = ', '.join(args)
    log_temp = kwargs.get('log_level', None)
    if log_temp is not None:
        if log_temp == 'info':
            log_level = logging.INFO
        elif log_temp == 'debug':
            log_level = logging.DEBUG
        elif log_temp == 'warning':
            log_level = logging.WARNING
        elif log_temp == 'error':
            log_level = logging.ERROR
        else:
            log_level = logging.INFO
        _log_re(log_level=log_level).info(f'==> {msg}')
    else:
        _log_re().info(f'==> {msg}')

