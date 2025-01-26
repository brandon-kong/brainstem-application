import unittest

from brainstem_application.lib.logger import Logger

# Logger configurations
LOG_FILE = 'logs/test/test.log'
LOG_LEVEL = 'DEBUG'
PRINT_TO_CONSOLE = False


class TestLogger(unittest.TestCase):
    def test_log_creation(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=PRINT_TO_CONSOLE)
        self.assertEqual(logger.log_file, LOG_FILE)
        self.assertEqual(logger.log_level, LOG_LEVEL)
        self.assertEqual(logger.print_to_console, PRINT_TO_CONSOLE)

    def test_log_positive(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=False)
        logger.log('This is a test log message', 'INFO')

    def test_log_negative(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=False)
        with self.assertRaises(ValueError):
            logger.log(123, 'INFO')
        with self.assertRaises(ValueError):
            logger.log('This is a test log message', 'INVALID')

    def test_debug_positive(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=False)
        logger.debug('This is a test debug message')

    def test_info_positive(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=False)
        logger.info('This is a test info message')

    def test_warning_positive(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=False)
        logger.warning('This is a test warning message')

    def test_error_positive(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=False)
        logger.error('This is a test error message')

    def test_critical_positive(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=False)
        logger.critical('This is a test critical message')
