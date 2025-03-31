from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd
# Generate a synthetic dataset
def generate_data(n_samples=100000, n_features=20, n_classes=2):
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

def train():
    # Generate data
    X, y = generate_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Save the model
    save_model(model)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy:.2f}')

if __name__ == "__main__":
    train()