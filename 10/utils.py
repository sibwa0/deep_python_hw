import argparse


# logger
# def setup_logger(
#     name,
#     log_file,
#     level=logging.INFO,
#     formatter=logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s')
# ):
#     handler = logging.FileHandler(log_file, mode="w")
#     # handler = logging.StreamHandler(log_file)
#     handler.setFormatter(formatter)
#     handler.setLevel(level)

#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     logger.addHandler(handler)

#     return logger


# console input
def console_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", action="store_true")

    return parser


LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "log_file": {
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
        },
        "minimum": {
            "format": "%(name)s\t%(levelname)s\t%(message)s",
        },
    },
    "handlers": {
        "default": {
            "class": "logging.FileHandler",
            "mode": "w",
            "filename": "cache.log",
            "formatter": "log_file",
        },
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "minimum",
        },
    },
    "loggers": {
        "to_file": {
            "handlers": ["default"],
            "level": "ERROR",
        },
        "to_stdout": {
            "level": "INFO",
            "handlers": ["stdout"],
        },
    },
}
