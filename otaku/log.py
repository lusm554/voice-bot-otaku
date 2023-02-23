import logging

def get_logger(name: str = None):
    """ Generate logger by name. """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        f"%(asctime)s %(name)s[%(lineno)d] - %(levelname)s: %(message)s", datefmt="%m-%d-%Y %H:%M:%S %Z%z"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
