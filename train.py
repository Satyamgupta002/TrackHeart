import warnings
warnings.filterwarnings("ignore")

import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# ======================================================
# Load Dataset
# ======================================================

df = pd.read_csv("data/heart_disease.csv")

print("=" * 60)
print("Dataset Loaded Successfully")
print("=" * 60)

# Drop unnecessary columns
df.drop(columns=["id", "date"], inplace=True, errors="ignore")

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nDataset Shape :", df.shape)

# ======================================================
# Separate Features and Target
# ======================================================

X = df.drop("disease", axis=1)
y = df["disease"]

# ======================================================
# Identify Column Types
# ======================================================

from pandas.api.types import is_numeric_dtype

categorical_features = []
numerical_features = []

for col in X.columns:

    if is_numeric_dtype(X[col]):
        numerical_features.append(col)
    else:
        categorical_features.append(col)

print("Categorical:", categorical_features)
print("Numerical:", numerical_features)

print("\nCategorical Features :", categorical_features)
print("Numerical Features :", numerical_features)

# ======================================================
# Preprocessing
# ======================================================

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numerical_features),
    ("cat", categorical_transformer, categorical_features)
])

# ======================================================
# Final Pipeline
# ======================================================

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# ======================================================
# Train Test Split
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ======================================================
# Train Model
# ======================================================

pipeline.fit(X_train, y_train)

# ======================================================
# Prediction
# ======================================================

predictions = pipeline.predict(X_test)

# ======================================================
# Evaluation
# ======================================================

print("\nAccuracy :", accuracy_score(y_test, predictions))
print("Precision :", precision_score(y_test, predictions))
print("Recall :", recall_score(y_test, predictions))
print("F1 Score :", f1_score(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report")
print(classification_report(y_test, predictions))

# ======================================================
# Save Model
# ======================================================

os.makedirs("models", exist_ok=True)

joblib.dump(pipeline, "models/disease_model.pkl")

print("\nModel Saved Successfully")
