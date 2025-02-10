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

log_level = os.environ.get("LOG_LEVEL", "DEBUG")
log_format = os.environ.get("LOG_FORMAT", "TEXT")

handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger("myapp")
logger.addHandler(handler)
logger.setLevel(log_level)
if log_format == "JSON":
    handler.setFormatter(JasonFormatter())
else:
    handler.setFormatter(logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)d:%(funcName)s:%(message)s"))
class InvalidServerError(Exception):
    pass

valid_server = {
    "nginx", "docker", "apache", "tomcat", "mysql", "mariadb", "postgresql", "mongodb", "redis", "memcached",
    "terraform", "ansible", "vagrant", "docker-compose", "kubernetes", "helm", "istio", "prometheus-operator"
}


def check_service_status(server_name):
    try:
        if server_name == "":
            raise InvalidServerError("Server name is empty.")
        if not server_name.isalnum():
            raise InvalidServerError("Server name must be alphanumeric.")
        if server_name not in valid_server:
            raise InvalidServerError("Server is not recognized.")
        else:
            return "Runing"
    except InvalidServerError:
        raise ValueError

while True:
        server_name = input("Enter a server name:\n")
        server_name.strip()
        try:
            status = check_service_status(server_name)
            logger.info("Valid Server name.")
        except ValueError as err:
            logger.error("Invalid Server name.")
