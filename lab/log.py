import logging
import sys
import json
import os

class JasonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        log = {
               "timestamp": self.formatTime(record),
               "level": record.levelname,
               "message": record.getMessage()
               }
        return json.dumps(log)
def setup_logging():
    log_level = os.environ.get("LOG_LEVEL", "DEBUG")
    log_format = os.environ.get("LOG_FORMAT", "TEXT")

    stdout_handler = logging.StreamHandler(sys.stdout)
    logger = logging.getLogger("myapp")
    file_handler = logging.FileHandler("myapp.log")
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)
    logger.setLevel(log_level)
    if log_format == "JSON":
        stdout_handler.setFormatter(JasonFormatter())
        file_handler.setFormatter(JasonFormatter())
    else:
        stdout_handler.setFormatter(logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)d:%(funcName)s:%(message)s"))
        file_handler.setFormatter(logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)d:%(funcName)s:%(message)s"))
    return logger