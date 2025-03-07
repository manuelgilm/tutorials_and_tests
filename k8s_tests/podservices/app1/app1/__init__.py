from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status
import os
import mlflow

app = FastAPI()

def get_url(service_name: str):
    o_service_host = os.environ.get(f"APP1-SERVICE_SERVICE_HOST", None)
    o_service_port = os.environ.get(f"APP1-SERVICE_SERVICE_PORT", None)
    service_host = os.environ.get(f"{service_name.upper()}_SERVICE_HOST", None)
    service_port = os.environ.get(f"{service_name.upper()}_SERVICE_PORT", None)
    if service_host is None and service_port is None:
        return None
    return f"http://{service_host}:{service_port}"

@app.get("/")
def read_root():
    print("MLFLOW_TRACKING_URI:", os.environ.get("MLFLOW_TRACKING_URI", None))
    mlflow_service = os.environ.get("MLFLOW_SERVICE", "mlflow-service")
    service_url = get_url(mlflow_service) if mlflow_service is not None else None
    os.environ["MLFLOW_TRACKING_URI"] = service_url if service_url is not None else "NONE"
    
    return {
        "Hello": "World",
        "MLflow": service_url,
        "MLFLOW_TRACKING_URI": os.environ.get("MLFLOW_TRACKING_URI", None),
        "MLFLOW_SERVICE": mlflow_service,
        "o_service_host": os.environ.get("APP1-SERVICE_SERVICE_HOST", None),
        "o_service_port": os.environ.get("APP1-SERVICE_SERVICE_PORT", None)}

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
