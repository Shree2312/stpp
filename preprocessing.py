import pandas as pd


def load_data(file_path):
    """Load the raw task dataset."""
    return pd.read_csv(file_path)
def clean_data(df):
    """Clean and validate the task dataset."""
    
    # Convert date columns to datetime
    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
    df["deadline_date"] = pd.to_datetime(df["deadline_date"], errors="coerce")

    # Fill missing numeric values with their median
    df["estimated_effort"] = df["estimated_effort"].fillna(
        df["estimated_effort"].median()
    )
    df["business_impact"] = df["business_impact"].fillna(
        df["business_impact"].median()
    )

    # Fill missing task types
    df["task_type"] = df["task_type"].fillna("Other")

    # Remove duplicate task IDs
    df = df.drop_duplicates(subset="task_id")

    # Keep only valid ranges
    df = df[
        (df["estimated_effort"] > 0)
        & (df["business_impact"].between(1, 10))
        & (df["urgency"].between(1, 10))
        & (df["dependency_count"] >= 0)
    ]

    # Remove rows with invalid dates
    df = df.dropna(subset=["created_date", "deadline_date"])

    return df
def engineer_features(df):
    """Create the ML features required by the model."""

    df["days_to_deadline"] = (
        df["deadline_date"] - df["created_date"]
    ).dt.days

    return df
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def build_preprocessor():
    """Build the reusable preprocessing pipeline."""

    numeric_features = [
        "days_to_deadline",
        "estimated_effort",
        "business_impact",
        "urgency",
        "dependency_count",
    ]

    categorical_features = ["task_type"]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features)
    ])

    return preprocessor
def prepare_data(df):
    """Prepare the dataset for machine learning."""

    df = clean_data(df)
    df = engineer_features(df)

    feature_columns = [
        "days_to_deadline",
        "estimated_effort",
        "business_impact",
        "urgency",
        "dependency_count",
        "task_type",
    ]

    X = df[feature_columns]
    y = df["priority_label"]

    return X, y