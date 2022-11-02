import yaml
from sensor.exception import SensorException
import os, sys
from sensor.logger import logging


def read_yaml_file(file_path: str) -> dict:
    logging.info(f"Reading yaml file from {[file_path]}")
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file) 
    except Exception as e:
        raise SensorException(e, sys)


def write_yaml_file(file_path: str, content: object, replace: bool = False)->None:
    logging.info(f"Writting yaml file at {[file_path]}, replace: {[replace]}")

    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise SensorException(e, sys)