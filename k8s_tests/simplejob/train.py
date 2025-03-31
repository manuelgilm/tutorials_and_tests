from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd
import mlflow 

# Generate a synthetic dataset
def generate_data(n_samples=1000, n_features=20, n_classes=2):
    X, y = make_classification(n_samples=n_samples, n_features=n_features, n_classes=n_classes, random_state=42)
    return pd.DataFrame(X), pd.Series(y)

# Train a Random Forest model
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Save the model to a file
def save_model(model, filename='model.pkl'):
    joblib.dump(model, filename)

def train(experiment):
    # Generate data
    X, y = generate_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    with mlflow.start_run(experiment_id = experiment.experiment_id) as run:
        # Log the model parameters and metrics
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", accuracy_score(y_test, model.predict(X_test)))

        # Log the model
        mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestModel")

    # # Save the model
    # save_model(model)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy:.2f}')

if __name__ == "__main__":
    import os 
    import time
    service_port = os.environ.get("MLFLOW_SERVICE_SERVICE_PORT")
    service_host = os.environ.get("MLFLOW_SERVICE_SERVICE_HOST")
    print("MLflow Service Host and Port:")
    print(service_port, service_host)
    MLFLOW_TRACKING_URI = f"http://{service_host}:{service_port}"
    os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI  # Set the MLflow tracking URI in the environment variable
    time.sleep(10)  # Wait for the MLflow server to start
    experiment = mlflow.set_experiment("RandomForest_Experiment")  # Set the experiment name
    train(experiment)