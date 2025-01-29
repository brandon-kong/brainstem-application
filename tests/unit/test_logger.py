import os
import unittest

from brainstem_application.lib.logger import Logger
from brainstem_application.constants import ROOT_DIR

# Logger configurations
LOG_FILE = f"{ROOT_DIR}/logs/test/test.log"
LOG_FILE_NEW_DIR = f"{ROOT_DIR}/logs/test_new_dir/test.log"
LOG_LEVEL = "DEBUG"
PRINT_TO_CONSOLE = False
CREATE_LOG_DIR = True


class TestLogger(unittest.TestCase):
    def test_log_creation(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        self.assertEqual(logger.log_file, LOG_FILE)
        self.assertEqual(logger.log_level, LOG_LEVEL)
        self.assertEqual(logger.print_to_console, PRINT_TO_CONSOLE)

    def test_invalid_log_file(self):
        with self.assertRaises(ValueError):
            Logger(log_file=None)

    def test_invalid_log_creation_parameters(self):
        with self.assertRaises(ValueError):
            Logger(log_file=None)

    def test_log_positive(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        logger.log("This is a test log message", "INFO")

    def test_log_negative(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        with self.assertRaises(ValueError):
            logger.log(123, "INFO")
        with self.assertRaises(ValueError):
            logger.log("This is a test log message", "INVALID")

    def test_debug_positive(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        logger.debug("This is a test debug message")

    def test_info_positive(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        logger.info("This is a test info message")

    def test_warning_positive(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        logger.warning("This is a test warning message")

    def test_error_positive(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        logger.error("This is a test error message")

    def test_critical_positive(self):
        logger = Logger(
            log_file=LOG_FILE,
            log_level=LOG_LEVEL,
            print_to_console=PRINT_TO_CONSOLE,
            create_log_directory=CREATE_LOG_DIR,
        )
        logger.critical("This is a test critical message")

    def test_log_print_to_console(self):
        logger = Logger(log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=True)
        logger.log("This is a test message", "DEBUG")

    def test_no_logger_found(self):
        with self.assertRaises(ValueError):
            Logger(
                log_file="INVALID/INVALID.log",
                log_level=LOG_LEVEL,
                print_to_console=True,
                create_log_directory=False,
            )

    def test_create_new_directory(self):
        logger = Logger(
            log_file=LOG_FILE_NEW_DIR,
            log_level=LOG_LEVEL,
            print_to_console=True,
            create_log_directory=True,
        )
        logger.log("This is a test message", "DEBUG")

        # check if the directory was created
        dirs = LOG_FILE_NEW_DIR.split("/")
        last_dir = "/".join(dirs[: len(dirs) - 1])
        self.assertTrue(os.path.exists(last_dir))

    def test_set_log_level(self):
        logger = Logger(
            log_file=LOG_FILE, log_level=LOG_LEVEL, print_to_console=PRINT_TO_CONSOLE
        )

        self.assertEqual(logger.log_level, LOG_LEVEL)

        logger.set_log_level("CRITICAL")

        self.assertEqual(logger.log_level, "CRITICAL")

    def tearDown(self):
        dirs = LOG_FILE_NEW_DIR.split("/")
        last_dir = "/".join(dirs[: len(dirs) - 1])

        if os.path.exists(LOG_FILE_NEW_DIR):
            os.remove(LOG_FILE_NEW_DIR)
            os.rmdir(last_dir)

        return super().tearDown()
