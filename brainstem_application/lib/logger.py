"""
lib/logger.py

...
"""

import os
from datetime import datetime
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
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

    @staticmethod
    def get_level(level: str) -> int:
        if level not in LogLevel.__members__:
            raise ValueError(f"[LogLevel]: log level not valid. Got \"{str(level)}\"")
        return LogLevel[level].value


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
                 log_level: str = 'INFO',
                 create_log_directory: bool = False
                 ):
        """ Initializes the Logger with the specified log file and log level.

        Args:
            create_log_directory (bool): Whether to create the log directory if it doesn't exist.
            print_to_console (bool): Whether to print log messages to the console.
            log_file (str): The file path where log messages will be written.
            log_level (str): The minimum log level for messages to be recorded. Options include 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
        """
        logger_found = Logger._verify_log_file(log_file)

        if not logger_found and not create_log_directory:
            raise ValueError("[Logger]: Log file not found and was not created.")

        if not logger_found and create_log_directory:
            # create the directory if it doesn't exist
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

        self.print_to_console = print_to_console
        self.log_file = log_file
        self.log_level = log_level

    def log(self, message: str, level: str = 'INFO'):
        """ Logs a message with the specified severity level.

        Args:
            message (str): The message to log.
            level (str): The severity level of the message. Options include 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
        """
        if not isinstance(message, str):
            raise ValueError(f"[Logger]: message must be a valid string. Got \"{type(message)}\"")
        if level not in LogLevel.__members__:
            raise ValueError(f"[Logger]: log level not valid. Got \"{str(level)}\"")

        if self._should_log(level):
            message = f"{datetime.now().isoformat()} [{level}] {message}"
            self._write_to_file(message)
            if self.print_to_console:
                print(message)

    def debug(self, message: str):
        """ Logs a debug-level message.

        Args:
            message (str): The message to log.
        """
        self.log(message, 'DEBUG')

    def info(self, message: str):
        """ Logs an info-level message.

        Args:
            message (str): The message to log.
        """
        self.log(message, 'INFO')

    def warning(self, message: str):
        """ Logs a warning-level message.

        Args:
            message (str): The message to log.
        """
        self.log(message, 'WARNING')

    def error(self, message: str):
        """ Logs an error-level message.

        Args:
            message (str): The message to log.
        """
        self.log(message, 'ERROR')

    def critical(self, message: str):
        """ Logs a critical-level message.

        Args:
            message (str): The message to log.
        """
        self.log(message, 'CRITICAL')

    def set_log_level(self, level: str):
        """ Sets the minimum log level for recording messages.

        Args:
            level (str): The minimum log level for messages to be recorded. Options include 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
        """
        self.log_level = level

    def _should_log(self, level: str) -> bool:
        """ Determines if a message should be logged based on the current log level.

        Args:
            level (str): The severity level of the message. Options include 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.

        Returns:
            bool: True if the message should be logged, False otherwise.
        """
        return LogLevel.get_level(level) >= LogLevel.get_level(self.log_level)

    def _write_to_file(self, message: str):
        """ Writes the log message to the specified log file.

        Args:
            message (str): The message to log.
        """
        with open(self.log_file, 'a') as f:
            f.write(f"{message}\n")

    @staticmethod
    def _verify_log_file(log_file: str) -> bool:
        """ Verifies that the log file is valid and can be written to. """
        if log_file is None:
            raise ValueError("[Logger]: No log file specified.")
        try:
            with open(log_file, 'a') as f:
                return True
        except Exception as e:
            return False
