"""
Common utility functions.
"""

import json
import time
from functools import wraps
from pathlib import Path

import yaml

from src.logger.logger import logger


def load_yaml(path: Path):

    with open(path, "r", encoding="utf-8") as file:

        return yaml.safe_load(file)


def save_json(data, path: Path):

    with open(path, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4)


def load_json(path: Path):

    with open(path, "r", encoding="utf-8") as file:

        return json.load(file)


def create_directory(path: Path):

    path.mkdir(parents=True, exist_ok=True)


def execution_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        logger.info(
            "{} executed in {:.3f} seconds",
            func.__name__,
            elapsed,
        )

        return result

    return wrapper