from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status
import os
import mlflow

app = FastAPI()

@app.get("/")
def read_root():
    print("MLFLOW_TRACKING_URI:", os.environ.get("MLFLOW_TRACKING_URI", None))
    
    return {"Hello": "World"}

@app.get("/list_experiments")
def get_experiment(experiment_name: str = "default"):
    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", None)
    if tracking_uri is None:
        return JSONResponse(
            content={"error": "MLFLOW_TRACKING_URI environment variable not set."},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    print("MLFLOW_TRACKING_URI:", tracking_uri)
    
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        return JSONResponse(
            content={"error": f"Experiment {experiment_name} not found."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return JSONResponse(
        content={
            "experiment_id": experiment.experiment_id,
            "experiment_name": experiment.name,
        }
    )
