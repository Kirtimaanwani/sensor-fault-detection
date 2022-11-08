# Have constants related only to the traning pipeline.

import os
# from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME


SAVED_MODEL_DIR =os.path.join("saved_models")
# Defining common constant variable for traning pipeline
TARGET_COLUMN = "class"
PIPELINE_NAME: str = "sensor"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "sensor.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"  # used to write columns which are to be droopped in schema.yaml file


""" 
Data Ingestion related constant start with DATA_INGESTION variable Name
"""
DATA_INGESTION_COLLECTION_NAME:str = "consumer_sample_for_sensor" # same as ""from sensor.constant.database import COLLECTION_NAME""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2  # test_size


"""
Data Validation related constant start with DATA_VALIDATION_variable_Name
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "drift_report.yaml"

"""
Data Transformation related constants starts with DATA_TRANS_variable_Name
"""
DATA_TRANS_DIR_NAME:str = "data_transformation"
DATA_TRANS_TRANSFORMED_DATA_DIR:str = "transformed"
DATA_TRANS_TRANSFORMED_OBJECT_DIR:str = "transformed_object"

"""
Model Trainer related constants starts with MODEL_TRAINER_var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float =  0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05


"""
Model Evaluation relate constants starts with MODEL_EVAL_var_name
"""
MODEL_EVALUATION_DIR_NAME: str = "model_evaluation"
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_EVALUATION_REPORT_NAME= "report.yaml"


"""
Model Pusher relate constants starts with MODEL_PUSHER_var_name
"""

MODEL_PUSHER_DIR_NAME = "model_pusher"
MODEL_PUSHER_SAVED_MODEL_DIR = SAVED_MODEL_DIR