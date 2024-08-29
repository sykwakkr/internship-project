import logging

# Determine which log message are actually written to the log file.
# logging.DEBUG will capture and log message at all levels, including DEBUG, INFO, WARNING, ERROR, and Critical
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler that will write log message to a file named 'test_automation.log'
handler = logging.FileHandler('./test_automation.log')
handler.setLevel(logging.DEBUG)

# Define the format for long message, including timestamp, logger name, log level, and the actual message
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set logger with handler and formatter
handler.setFormatter(formatter)
logger.addHandler(handler)