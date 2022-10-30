# Have constants related only to the traning pipeline.

import os
from sensor.constant.s3_bucket import TRAINING_BUCKET_NAME

# Defining common constant variable for traning pipeline
TARGET_CLASS = "class"
PIPELINE_NAME: str = "sensor"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "sensor.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_NAME = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"  # used to write columns which are to be droopped in schema.yaml file


""" 
Data Ingestion related constant start with DATA_INGESTION variable Name
"""
DATA_INGESTION_COLLECTION_NAME:str = "consumer_sample_for_sensor" # same as ""from sensor.constant.database import COLLECTION_NAME""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2  # test_size


