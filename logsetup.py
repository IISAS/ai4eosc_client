import logging.config
from os import path


def start_log():
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
    logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
