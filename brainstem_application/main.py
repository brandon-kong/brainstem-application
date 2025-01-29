import sys
from lib.logger import Logger, LogLevel

from utils.menu import Menu
from utils.printer import Printer

from constants import ROOT_DIR


LOG_LEVEL_CONTEXT = LogLevel.DEBUG.name
logger = Logger(log_file=f"{ROOT_DIR}/logs/activity.log", log_level=LOG_LEVEL_CONTEXT, create_log_directory=True)


def exit_program():
    Printer.error("Exiting program...")
    logger.debug("Ending application...")

    sys.exit(0)


def main():
    logger.debug("Starting application...")

    options = {
        "Perform K-means clustering": lambda: print("Performing K-means clustering"),
        "Perform PCA": lambda: print("Performing PCA"),
        "Perform t-SNE": lambda: print("Performing t-SNE"),
    }

    menu = Menu(options, include_exit=True, include_back=False)
    menu.run()

    exit_program()


if __name__ == "__main__":
    main()
