import os, sys
from sensor.exception import SensorException
from sensor.logger import logging
import pandas as pd
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.config_entity import DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact

from sensor.utils.mail_utils import read_yaml_file



class DataValidation:

    def __init__(
                self,
                data_ingestion_artifact:DataIngestionArtifact,
                data_validation_config:DataValidationConfig):  
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)  # underscore for schema_config is used for protected variable
        except Exception as e:
            raise SensorException(e,sys)


    @staticmethod
    def read_data(file_path)->pd.DataFrame:

        f"""
        Reading data from [{file_path}] and returning its DataFrame
        """
        try:
            logging.info(f"Reading data from {[file_path]} and returning its DataFrame")
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e,sys)



    def validate_number_of_columns(self, dataframe: pd.DataFrame)->bool:
        try:
            logging.info("validating number of columns")
            number_of_columns = len(self._schema_config["columns"])

            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise SensorException(e,sys)


## assignment 
    def drop_zero_std_column(self, dataframe: pd.DataFrame)->bool:
        pass


    def is_numerical_column_exists(self, dataframe: pd.DataFrame)->bool:
        try:
            logging.info("validating Numerical columns")
            numerical_columns = self._schema_config["numerical_columns"]
            dataframe_columns = dataframe.columns

            numerical_column_present = True
            missing_numerical_columns = []
            for num_column in numerical_columns:
                if num_column not in dataframe_columns:
                    numerical_column_present = False
                    missing_numerical_columns.append(num_column)
            logging.info(f"Missing numerical columnes [{missing_numerical_columns}]")
            return numerical_column_present

        except Exception as e:
            raise SensorException(e,sys)



    def detect_data_drift(self):
        pass


    def initiate_data_validation(self)-> DataValidationArtifact:
        """
        Initiating data validation
        """
        try:
            logging.info("Initiating data validation")
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Reading data from Train and Test file Locations
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate Number of Columns
            error_message = ""
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} [Train DataFrame] does not contain all columns"
            
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} [Test DataFrame] does not contain all columns"
                
            
            # Validate Numerical Columns
            status = self.is_numerical_column_exists(dataframe= train_dataframe)
            if not status:
                error_message = f"{error_message} [Train DataFrame] does not contain all Numerical columns, check in logs for which columns are missing"
            
            status = self.is_numerical_column_exists(dataframe= test_dataframe)
            if not status:
                error_message = f"{error_message} [Test DataFrame] does not contain all Numerical columns, check in logs for which columns are missing"

            if len(error_message) > 0:
                raise Exception(error_message)
            

            # Checking Data DRIFT


        except Exception as e:
            raise SensorException(e, sys)

