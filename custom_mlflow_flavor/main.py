from src.base import Circle

import mlflow
from src.flavor.save import log_model
import os 

if __name__ == "__main__":
    circle = Circle(1, 0, 0)

    print(circle.predict(0, 0))  # True

    with mlflow.start_run() as run:
        artifact_path = "model"
        try:
            log_model(circle, artifact_path)
        except Exception as e:
            print(e)
