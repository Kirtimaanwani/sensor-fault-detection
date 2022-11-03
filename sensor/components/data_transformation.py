import sys, os

import numpy as np
import pandas as pd
from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
from sklearn.pipeline import pipeline
from sklearn.preprocessing import RobustScaler

from sensor.constant.training_pipeline import TARGET_COLUMN
from sensor.entity.artifact_entity import (
                                            DataValidationArtifact, 
                                                DataTransformationArtifact
                                                    )
from sensor.entity.config_entity import DataTransformationConfig
from sensor.exception import SensorException
from sensor.logger import logging

from sensor.ml.model.estimator import TargerValueMapping
from sensor.utils.mail_utils import (
                                     save_numpy_array_data, 
                                        save_object
                                            )


class DataTransformation:

    def __init__(self,
                    data_validation_artifact: DataValidationArtifact, 
                        data_transformation_config: DataTransformationConfig
                            ):
        """
        :param data_validation_artifact: Output reference of data ingestion artifact stage
        :param data_transformation_config: configuration for data transformation
        """
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config

        except Exception as e:
            raise SensorException(e, sys)


    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            logging.info("reading csv and returning DataFrame in Data Transformation component")
            return pd.read_csv(file_path)

        except Exception as e:
            raise SensorException(e, sys)


    @classmethod
    def get_data_transformer_object(cls)-> pipeline:
        try:
            robust_scaler = RobustScaler()
            simple_imputer = SimpleImputer(strategy="constant", fill_value=0)
            
            preprocessor = Pipeline(steps=[
                                            ('Imputer', simple_imputer),        # Replacing missing values with zero
                                                ('RobustScaler', robust_scaler) # keeping every feature in same range and handling outliers
                                            ]   
            )
            return preprocessor
            
        except Exception as e:
            raise SensorException(e, sys)


    def initiate_data_transformation(self, )->DataTransformationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)








