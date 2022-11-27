from sensor.exception import SensorException
import sys, os  
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline


from sensor.configuration.mongo_db_connection import MongoDBClient

import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.utils.main_utils import read_yaml_file
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from fastapi import FastAPI, File, UploadFile
from sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
import os
import pandas as pd

from io import StringIO
from fastapi.responses import StreamingResponse


app = FastAPI()
origins = ["*"]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:

        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()



        from sensor.logger import LOG_FILE_PATH

        with open(file=LOG_FILE_PATH, mode="r") as txt:
            logs = txt.read()

        # from sensor.logger import LOG_FILE_PATH
        return Response(f"""Training successful !!
                            {logs}""")
    except Exception as e:
        return Response(f"Error Occurred! {e}")





@app.post("/Predict/")
async def upload_csv(csv_file: UploadFile = File(...)):
    
    try:
        #get data from user csv file
        #conver csv file to dataframe

        df = pd.read_csv(csv_file.file)

        
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")
        
        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(),inplace=True)



        # decide how to return file to user

        stream = StringIO()

        df.to_csv(stream, index = False)

        response = StreamingResponse(iter([stream.getvalue()]),
                        media_type="text/csv"
        )

        response.headers["Content-Disposition"] = "attachment; filename=export.csv"

        return response

        

        # return Response(f"{df}")


    except Exception as e:
        raise Response(f"Error Occured! {e}")




if __name__=="__main__":
    # app_run(app, host=APP_HOST, port=APP_PORT)
    app_run(app)


# if __name__=="__main__":
#     try:
#         training_pipeline = TrainPipeline()
#         training_pipeline.run_pipeline()

#         from sensor.logger import LOG_FILE_PATH

#         with open(file=LOG_FILE_PATH, mode="r") as txt:
#             logs = txt.readall()

#             print(logs)
#     except Exception as e: 
#         raise SensorException(e, sys)




