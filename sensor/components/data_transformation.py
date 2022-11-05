import sys, os

import numpy as np
import pandas as pd
from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler

from sensor.constant.training_pipeline import TARGET_COLUMN
from sensor.entity.artifact_entity import (
                                            DataValidationArtifact, 
                                                DataTransformationArtifact
                                                    )
from sensor.entity.config_entity import DataTransformationConfig
from sensor.exception import SensorException
from sensor.logger import logging

from sensor.ml.model.estimator import TargetValueMapping
from sensor.utils.main_utils import (
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
            logging.info("reading csv and returning DataFrame ")
            return pd.read_csv(file_path)

        except Exception as e:
            raise SensorException(e, sys)


    @classmethod
    def get_data_transformer_object(cls)-> Pipeline:
        """
        :creates a pipeline object:
        :return: Pipeline object
        """
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
            logging.info("Reading data for train dataset")
            train_df = DataTransformation.read_data(
                                                    file_path= self.data_validation_artifact.valid_train_file_path
                                                        )
            logging.info("Reading data for test dataset")
            test_df = DataTransformation.read_data(
                                                    file_path= self.data_validation_artifact.valid_test_file_path
                                                        )
            logging.info("getting transformer object")                                           
            preprocessor = self.get_data_transformer_object()



        # for trainng data frame
            logging.info("splitting training data as input_feature_train_df and target_feature_train_df")

            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            # replacing target ccategorical to numerical categories like 0 and 1  {'neg': 0, 'pos': 1}
            target_feature_train_df = target_feature_train_df.replace(TargetValueMapping().to_dict())



        # for testng data frame
            logging.info("splitting test data as input_feature_test_df and target_feature_test_df")        

            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(TargetValueMapping().to_dict())
            


        # Transforming according to preprocessor object
            logging.info("fitting of transformer object on input_feature_train_df")
            preprocessor_object = preprocessor.fit(input_feature_train_df)


            logging.info("Transform on input_feature_train_df and input_feature_test_df")
            # for training data frame
            transformed_input_feature_train_df = preprocessor_object.transform(input_feature_train_df)
            # for test data frame
            transformed_input_feature_test_df = preprocessor_object.transform(input_feature_test_df)


        # Using SMOTETomek 
            logging.info("Using SMOTETomek pn train and test data")
            smt = SMOTETomek(sampling_strategy= "minority")
            # on training data frame
            input_feature_train_final, target_feature_train_final = smt.fit_resample(
                                                                                    transformed_input_feature_train_df, 
                                                                                        target_feature_train_df)
            # on test data frame
            input_feature_test_final, target_feature_test_final = smt.fit_resample(
                                                                                    transformed_input_feature_test_df, 
                                                                                        target_feature_test_df)
        # concatinating input feature and target feature
            # for training data frame
            train_arr = np.c_[
                                input_feature_train_final, 
                                np.array(target_feature_train_final)
                             ]
            # for testing data frame
            test_arr = np.c_[
                                input_feature_test_final, 
                                np.array(target_feature_test_final)
                             ]

        # saving numpy array
            # for training data frame
            logging.info("saving numpy array of train and test data")
            save_numpy_array_data(
                                    file_path=self.data_transformation_config.transformed_train_file_path, 
                                    array=train_arr
                                    )
            # for testing data frame
            save_numpy_array_data(
                                    file_path=self.data_transformation_config.transformed_test_file_path, 
                                    array=test_arr
                                    )
        # saving preprocessor object
            logging.info("saving preprocessor object")
        
            save_object(
                        file_path=self.data_transformation_config.transformed_object_file_path, 
                        obj=preprocessor_object)
            
            # Creating Data Trabsforation Artifact
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            )
            logging.info(f"Data Transformation Artifact:[{data_transformation_artifact}]\n\n")
            return data_transformation_artifact
        except Exception as e:
            raise SensorException(e, sys)








