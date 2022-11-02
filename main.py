from sensor.exception import SensorException
import sys, os  
from sensor.logger import logging

from sensor.pipeline.training_pipeline import TrainPipeline


if __name__ == '__main__':
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()


