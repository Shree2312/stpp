import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from preprocessing import load_data, prepare_data, build_preprocessor
def train_model():
    """Train the Decision Tree priority prediction model."""

    data_path = "data/tasks.csv"

    # Load and prepare the dataset
    df = load_data(data_path)
    X, y = prepare_data(df)

    # Split the data into 80% training and 20% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Build the preprocessing pipeline
    preprocessor = build_preprocessor()

    # Preprocess the training data
    X_train_processed = preprocessor.fit_transform(X_train)

    # Preprocess the test data using the same fitted preprocessor
    X_test_processed = preprocessor.transform(X_test)

    # Create the Decision Tree model
    model = DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    )

    # Train the model
    model.fit(X_train_processed, y_train)

    return model, preprocessor, X_test_processed, y_test
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted")
    recall = recall_score(y_test, predictions, average="weighted")
    f1 = f1_score(y_test, predictions, average="weighted")

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

    return accuracy, precision, recall, f1
def save_model(model, preprocessor):
    """Save the trained model and preprocessing pipeline."""

    model_data = {
        "model": model,
        "preprocessor": preprocessor
    }

    joblib.dump(model_data, "models/priority_model.pkl")

    print("Model saved to models/priority_model.pkl")
if __name__ == "__main__":
    model, preprocessor, X_test, y_test = train_model()

    evaluate_model(model, X_test, y_test)

    save_model(model, preprocessor)