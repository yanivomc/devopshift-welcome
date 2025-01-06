import logging
import json
import os
import sys

# Set log format dynamically
LOG_FORMAT = os.getenv("LOG_FORMAT", "json")  # 'json' or 'text'

# Create a JSON formatter class
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "timestamp": self.formatTime(record, self.datefmt),
            "message": record.getMessage(),
        }
        return json.dumps(log_record)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Apply the appropriate formatter
if LOG_FORMAT == "json":
    formatter = JSONFormatter()
else:
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

for handler in logging.getLogger().handlers:
    handler.setFormatter(formatter)


# Test logs
logging.info("Dynamic logging format enabled")