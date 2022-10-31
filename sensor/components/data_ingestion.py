import sys, os
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from pandas import DataFrame
from sensor.data_access.sensor_data import SensorData
from sklearn.model_selection import train_test_split


class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:     
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)




    def export_data_into_feature_store(self) -> DataFrame:
        """
        Export mongo db collection records as DataFrame into feature store
        """
        try:   
            logging.info("Exporting data from mongo database to feature store...")  
            sensor_data = SensorData()
            dataframe = sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)  # here not provided  database name since its already taken in mongo_db_connection 
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            # now Creating folder for feature store
            logging.info("Creating folder for feature store")
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info("Exporting csv in feature store")
            dataframe.to_csv(feature_store_file_path, index=False, header=False)
            
            return dataframe

        except Exception as e:
            raise SensorException(e, sys)




    def split_data_as_train_test(self, dataframe: DataFrame)->None:
        """
        Feature store dataset will be split into train and test file
        """
        try:
            logging.info("Performing train test  split on the dataframe")
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio
                )
            
            logging.info("train test split DONE")
            logging.info("Preparing to exit split_data_as_train_test method of Data_Ingestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            logging.info("Creating folder for training file and test file")
            os.makedirs(dir_path, exist_ok=True)

            logging.info("Exporring train and test file")
            
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)

            logging.info("Exported train and test file")
            logging.info("Exited split_data_as_train_test method of Data_Ingestion class")


        except Exception as e:
            raise SensorException(e, sys)






    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Initiating data ingestion...")
            dataframe = self.export_data_into_feature_store()
            
            self.split_data_as_train_test(dataframe=dataframe)

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                    test_file_path=self.data_ingestion_config.test_file_path)
            
            logging.info("Getting data_ingestion_artifact")
            return data_ingestion_artifact

        except Exception as e:
            raise SensorException(e, sys)
    