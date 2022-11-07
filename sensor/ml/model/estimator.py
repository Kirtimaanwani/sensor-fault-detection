
from sensor.exception import SensorException
import os, sys
<<<<<<< HEAD
from sensor.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
from sensor.logger import logging


=======
from sensor.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
from sensor.logger import logging
>>>>>>> c593cf0cd05d9bb24747d50a988be696f9ea7ef8
class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1

    def to_dict(self):
        return self.__dict__

    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))


#A code to train model and check the accuracy.

class SensorModel:

    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise SensorException(e, sys)
    
    def predict(self,x):
        try:
            #with this predict function , directly do preprocessing and prediction-----in future if wanna to add more steps of feature engineering , it can be added here
           
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise SensorException(e, sys)


<<<<<<< HEAD
class ModelResolver:
    """
    class to check if any model exists in the saved model directory and return path and status for latest model which is in latest timestamp directory
    """
    def __init__(self,model_dir=SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise SensorException(e, sys)
    

    def get_best_model_path(self)->str:
        try:
            timestamps = list(map(int,os.listdir(self.model_dir)))  # getting list of timestamp diractory in saved model
            latest_timestamp = max(timestamps)      # getting latest timestamp directory
            latest_model_path= os.path.join(self.model_dir,
                                                f"{latest_timestamp}",
                                                    MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise SensorException(e, sys)


    def is_model_exists(self)->bool:
        try:
            if not os.path.exists(self.model_dir):  # if model directory does not exist -> return false

                logging.info(f"{self.model_dir} does not exist")
                return False
            timestamps = os.listdir(self.model_dir)

            if len(timestamps)==0:          # if model directory exists but no timestamp directory init -> return false
                logging.info(f"{self.model_dir} exists but no timestamp directory exists")
                return False      
                
            latest_model_path = self.get_best_model_path()   # if timestamp directory exists , if model file not exist -> return false
            if not os.path.exists(latest_model_path):
                logging.info(f"{self.model_dir}/latest_timestamp directory exists but no model.pkl file exists")
                return False
            
            logging.info(f"Model file exists in {self.model_dir}")
            return True                 # correct latest model exists-> return true
        except Exception as e:
            raise SensorException(e, sys)


=======

class ModelResolver:

    def __init__(self,model_dir=SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir

        except Exception as e:
            raise e

    def get_best_model_path(self,)->str:
        try:
            logging.info("getting best model file path")
            timestamps = list(map(int,os.listdir(self.model_dir)))
            latest_timestamp = max(timestamps)
            latest_model_path= os.path.join(self.model_dir,f"{latest_timestamp}",MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise e

    def is_model_exists(self)->bool:
        try:
            logging.info("Checking if model is already exists or not")
            if not os.path.exists(self.model_dir):
                logging.info("saved model  directory not found")
                return False

            timestamps = os.listdir(self.model_dir)
            if len(timestamps)==0:
                logging.info("timestamp folder not found in saved models")
                return False
            
            latest_model_path = self.get_best_model_path()

            if not os.path.exists(latest_model_path):
                logging.info("Latest Model not found")
                return False

            logging.info("Model Exists")
            return True
        except Exception as e:
            raise e
>>>>>>> c593cf0cd05d9bb24747d50a988be696f9ea7ef8

