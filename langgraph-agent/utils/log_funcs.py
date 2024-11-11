import logging
import os
from logging.handlers import RotatingFileHandler

# Create a logs directory if it doesn't exist
logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Define the log file paths
actions_log_file = os.path.join(logs_dir, "actions.log")
errors_log_file = os.path.join(logs_dir, "errors.log")

# Create loggers
actions_logger = logging.getLogger("actions_logger")
errors_logger = logging.getLogger("errors_logger")

# Set log levels
actions_logger.setLevel(logging.INFO)
errors_logger.setLevel(logging.ERROR)

# Create file handlers
actions_handler = RotatingFileHandler(
    actions_log_file, maxBytes=100000, backupCount=1
)
errors_handler = RotatingFileHandler(
    errors_log_file, maxBytes=100000, backupCount=1
)

# Create log formats
actions_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
errors_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Add handlers and formats to loggers
actions_handler.setFormatter(actions_format)
errors_handler.setFormatter(errors_format)

actions_logger.addHandler(actions_handler)
errors_logger.addHandler(errors_handler)


# Convenience functions for logging
def log_action(message):
    actions_logger.info(message)


def log_error(message):
    errors_logger.error(message)
