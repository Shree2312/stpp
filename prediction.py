import os
import joblib
import pandas as pd


def get_model_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "models", "priority_model.pkl")
    if os.path.exists(model_path):
        return model_path
    return "models/priority_model.pkl"


def predict_priority(
    days_to_deadline,
    estimated_effort,
    business_impact,
    urgency,
    dependency_count,
    task_type="General"
):
    """Predict the priority of a task using the saved ML model."""

    model_path = get_model_path()
    model_data = joblib.load(model_path)

    model = model_data["model"]
    preprocessor = model_data["preprocessor"]

    task = pd.DataFrame([{
        "days_to_deadline": days_to_deadline,
        "estimated_effort": estimated_effort,
        "business_impact": business_impact,
        "urgency": urgency,
        "dependency_count": dependency_count,
        "task_type": task_type
    }])

    task_processed = preprocessor.transform(task)

    prediction = model.predict(task_processed)

    return prediction[0]