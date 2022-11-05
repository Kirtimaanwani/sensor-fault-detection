import os,sys
from sensor.exception import SensorException
from sensor.logger import logging

from sensor.entity.config_entity import ModelEvaluationConfig
from sensor.entity.artifact_entity import DataValidationArtifact,ModelTrainerArtifact,ModelEvaluationArtifact

from sensor.ml.metric.classification_metric import get_classification_score
from sensor.ml.model.estimator import SensorModel, TargetValueMapping
from sensor.utils.main_utils import save_object, load_object, write_yaml_file
from sensor.ml.model.estimator import ModelResolver
from sensor.constant.training_pipeline import TARGET_COLUMN
import pandas  as  pd

class ModelEvaluation:


    def __init__(self,
                    model_eval_config:ModelEvaluationConfig,
                        data_validation_artifact:DataValidationArtifact,
                            model_trainer_artifact:ModelTrainerArtifact):
        
        try:
            self.model_eval_config = model_eval_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)
    


    def initiate_model_evaluation(self)->ModelEvaluationArtifact:
        try:
            logging.info("Initiating model evaluation")
            valid_train_file_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path = self.data_validation_artifact.valid_test_file_path

            # valid train and test file dataframe
            train_df = pd.read_csv(valid_train_file_path)
            test_df = pd.read_csv(valid_test_file_path)

            # concatinating train and test and doing TargetValueMapping
            df = pd.concat([train_df,test_df])
            y_true = df[TARGET_COLUMN]
            y_true.replace(TargetValueMapping().to_dict(),inplace=True)
            df.drop(TARGET_COLUMN,axis=1,inplace=True)

            # getting trained model file path
            train_model_file_path = self.model_trainer_artifact.trained_model_file_path
            model_resolver = ModelResolver()
            is_model_accepted=True


            if not model_resolver.is_model_exists():
                model_evaluation_artifact = ModelEvaluationArtifact(
                    is_model_accepted=is_model_accepted, 
                    improved_accuracy=None, 
                    best_model_path=None, 
                    trained_model_path=train_model_file_path, 
                    train_model_metric_artifact=self.model_trainer_artifact.test_metric_artifact, 
                    best_model_metric_artifact=None)
                logging.info(f"Model evaluation artifact: {model_evaluation_artifact}")
                return model_evaluation_artifact

            latest_model_path = model_resolver.get_best_model_path()
            latest_model = load_object(file_path=latest_model_path)
            train_model = load_object(file_path=train_model_file_path)

        except Exception as e :
            raise SensorException(e,sys)


