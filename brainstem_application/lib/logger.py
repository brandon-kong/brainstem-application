"""
lib/logger.py

...
"""

from enum import Enum


class LogLevel(Enum):
    """ An enumeration of log levels for messages.

    Attributes:
        DEBUG (str): A debug-level log message.
        INFO (str): An info-level log message.
        WARNING (str): A warning-level log message.
        ERROR (str): An error-level log message.
        CRITICAL (str): A critical-level log message.
    """
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class Logger:
    """ A Logger class for managing and recording log messages with varying severity levels.

    Attributes:
        log_file (str): The file path where log messages will be written.
        log_level (str): The minimum log level for messages to be recorded. Options include 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.

    Methods:
        __init__(log_file: str, log_level: str = 'INFO'):
            Initializes the Logger with the specified log file and log level.

        log(message: str, level: str = 'INFO'):
            Logs a message with the specified severity level.

        debug(message: str):
            Logs a debug-level message.

        info(message: str):
            Logs an info-level message.

        warning(message: str):
            Logs a warning-level message.

        error(message: str):
            Logs an error-level message.

        critical(message: str):
            Logs a critical-level message.

        set_log_level(level: str):
            Sets the minimum log level for recording messages.

        _should_log(level: str) -> bool:
            Determines if a message should be logged based on the current log level.

        _write_to_file(message: str):
            Writes the log message to the specified log file.
    """

    def __init__(self,
                 print_to_console: bool = False,
                 log_file: str = None,
                 log_level: str = 'INFO'
                 ):
        """ Initializes the Logger with the specified log file and log level.

        Args:
            print_to_console (bool): Whether or not to print log messages to the console.
            log_file (str): The file path where log messages will be written.
            log_level (str): The minimum log level for messages to be recorded. Options include 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
        """
        Logger._verify_log_file(log_file)

        self.print_to_console = print_to_console
        self.log_file = log_file
        self.log_level = log_level

    @staticmethod
    def _verify_log_file(log_file: str):
        """ Verifies that the log file is valid and can be written to. """
        if log_file is None:
            raise ValueError("No log file specified.")
        try:
            with open(log_file, 'a') as f:
                pass
        except Exception as e:
            raise ValueError(f"Invalid log file: {e}")
