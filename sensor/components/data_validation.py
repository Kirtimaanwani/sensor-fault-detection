from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.config_entity import DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import os, sys
from sensor.exception import SensorException
from sensor.logger import logging
import pandas as pd




class DataValidation:

    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        pass


    def validate_number_of_columns(self)->bool:
        pass


    def is_numerical_column_exists(self)->bool:
        pass    


    def detect_data_drift(self):
        pass


    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

