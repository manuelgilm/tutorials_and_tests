import pickle
import cloudpickle

from pathlib import Path
from typing import Union

from mlflow.exceptions import MlflowException
from mlflow.models import Model
from mlflow import pyfunc
from mlflow.models.model import MLMODEL_FILE_NAME

from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE
import os
from src.flavor import save
from src.flavor.loaders import load_model

_MODEL_DATA_SUBPATH = "model.pkl"
SERIALIZATION_FORMAT_PICKLE = "pickle"
SERIALIZATION_FORMAT_CLOUDPICKLE = "cloudpickle"

SUPPORTED_SERIALIZATION_FORMATS = [
    SERIALIZATION_FORMAT_PICKLE,
    SERIALIZATION_FORMAT_CLOUDPICKLE,
]

FLAVOR_NAME = "circle"


def log_model(
    model, artifact_path, serialization_format=SERIALIZATION_FORMAT_PICKLE, **kwargs
):
    return Model.log(
        artifact_path=artifact_path,
        flavor=save,
        model=model,
        serialization_format=serialization_format,
        **kwargs,
    )


def save_model(model, path, mlflow_model, serialization_format):
    """ """
    if serialization_format not in SUPPORTED_SERIALIZATION_FORMATS:
        raise MlflowException(
            message=(
                f"Unrecognized serialization format: {serialization_format}. "
                "Please specify one of the following supported formats: "
                f"{SUPPORTED_SERIALIZATION_FORMATS}."
            ),
            error_code=INVALID_PARAMETER_VALUE,
        )

    mlflow_model = Model()
    model_data_path = os.path.join(path, _MODEL_DATA_SUBPATH)
    print("model_data_path: ", model_data_path)
    _save_model(
        model=model, path=model_data_path, serialization_format=serialization_format
    )

    pyfunc.add_to_model(
        mlflow_model,
        loader_module="src.flavor.loaders",
        model_path=_MODEL_DATA_SUBPATH,
    )

    mlflow_model.add_flavor(
        name=FLAVOR_NAME,
        circle_version="0.0.1",
        pickled_model=_MODEL_DATA_SUBPATH,
        serialization_format=serialization_format,
    )

    mlflow_model.save(os.path.join(path, MLMODEL_FILE_NAME))


def _save_model(model, path: Union[str, Path], serialization_format: str):
    """
    Save the model to a file using the specified serialization format.

    :param model: Any
    :param path: str
    :param serialization_format: str
    """
    # if isinstance(path, str):
    #     path = Path(path)
    print("Saving model to path: {}".format(path))
    with open(path, "wb") as file:
        if serialization_format == SERIALIZATION_FORMAT_PICKLE:
            pickle.dump(model, file)
        else:
            cloudpickle.dump(model, file)
