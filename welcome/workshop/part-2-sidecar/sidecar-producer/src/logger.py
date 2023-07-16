import json
import logging
from datetime import datetime

class JsonLogger:
    def __init__(self, debug=False):
        self.debug = debug
        self.logger = logging.getLogger()
        if self.debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        
        # Ensure we only have one handler to avoid duplicate logs
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            self.logger.addHandler(handler)

    def log(self, message, level='info'):
        message['timestamp'] = datetime.now().isoformat()
        json_message = json.dumps(message)
        if level == 'info':
            self.logger.info(json_message)
        elif level == 'error':
            self.logger.error(json_message)
        elif self.debug and level == 'debug':
            self.logger.debug(json_message)
