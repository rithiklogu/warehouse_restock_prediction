from pathlib import Path

from src.config.settings import settings
from src.logger.logger import logger
from src.utils.common import load_yaml
from src.exception.custom_exception import CustomException

import sys

logger.info("Foundation Test Started")

print(settings.random_state)

config = load_yaml(Path("config/config.yaml"))

print(config)

try:

    x = 10 / 0

except Exception as e:

    logger.exception(e)

    try:
        raise CustomException(e, sys)
    except Exception as ex:
        print(ex)

logger.success("Foundation Test Completed")