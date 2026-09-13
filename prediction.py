import joblib
import pandas as pd


def predict_priority(
    days_to_deadline,
    estimated_effort,
    business_impact,
    urgency,
    dependency_count,
    task_type
):
    """Predict the priority of a task using the saved ML model."""

    model_data = joblib.load("models/priority_model.pkl")

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