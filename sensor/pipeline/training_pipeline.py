import sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.components.data_ingestion import DataIngestion

class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            
            # creating data Ingestion config
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")

            # passing dataIngestion config to DataIngestion class (of data_ingestion components)
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            # Initiating data ingestion to get data_ingestion_artifact
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(f"Data ingestion complete {data_ingestion_artifact}")


        except Exception as e:
            raise SensorException(e, sys)

    
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)


    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)    


    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)


    def run_pipeline(self):
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e, sys)
    

    