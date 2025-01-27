from lib.logger import Logger, LogLevel
from constants import (
    ROOT_DIR
)


LOG_LEVEL_CONTEXT = LogLevel.DEBUG.name

def main():
    logger = Logger(log_file=f"{ROOT_DIR}/logs/activity.log", log_level=LOG_LEVEL_CONTEXT)
    logger.debug("Starting application")

    
    logger.debug("Ending application")


if __name__ == "__main__":
    main()
