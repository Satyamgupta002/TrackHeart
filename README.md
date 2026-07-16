## TrackHeart – AI Powered Heart Disease Risk Prediction

An intelligent Machine Learning application that predicts the likelihood of heart disease from patient health information and generates an interactive health report.


---

## Overview

TrackHeart is an end-to-end Machine Learning project that combines data preprocessing, model training, probability estimation, and an interactive Streamlit dashboard to provide heart disease risk assessment.

Instead of simply predicting whether a patient is at risk, the application also:

- Calculates BMI
- Estimates prediction confidence
- Generates personalized health recommendations
- Creates downloadable PDF reports
- Presents all results through a modern responsive dashboard

---

## Features

- End-to-End Machine Learning Pipeline
- Automatic Data Cleaning
- Missing Value Imputation
- Feature Scaling
- One-Hot Encoding
- Logistic Regression Classifier
- Probability Prediction
- BMI Calculator
- Personalized Health Recommendations
- Downloadable PDF Report
- Interactive Streamlit Dashboard
- Responsive Modern UI

---

## Tech Stack

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Frontend

- Streamlit
- HTML
- CSS
---

## Machine Learning Pipeline

Dataset

↓

Data Cleaning

↓

Duplicate Removal

↓

Missing Value Imputation

↓

Feature Encoding

↓

Feature Scaling

↓

Train/Test Split

↓

Logistic Regression

↓

Model Evaluation

↓

Model Serialization

↓

Interactive Streamlit Application

---

## Input Features

- Country
- Occupation
- Gender
- Age
- Height
- Weight
- Blood Pressure
- Cholesterol
- Glucose
- Smoking
- Alcohol Consumption
- Physical Activity

---

## Output

- Heart Disease Risk
- Prediction Probability
- BMI
- Health Status
- Lifestyle Recommendations
- Downloadable Report

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/TrackHeart.git
```

Move inside project

```bash
cd TrackHeart
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train model

```bash
python train.py
```

Run Streamlit

```bash
streamlit run app.py
```

---

## Model Performance

The model was evaluated on a held-out test dataset using standard classification metrics.

| Metric | Score |
|---------|-------|
| Accuracy | **71.59%** |
| Precision | **73.38%** |
| Recall | **67.72%** |
| F1 Score | **70.44%** |

### Confusion Matrix

```
                Predicted
               0          1
Actual 0    5285       1719
Actual 1    2258       4738
```

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|------|-----------:|--------:|---------:|--------:|
| 0 | 0.70 | 0.75 | 0.73 | 7004 |
| 1 | 0.73 | 0.68 | 0.70 | 6996 |
| **Accuracy** | | | **0.72** | **14000** |
| **Macro Avg** | **0.72** | **0.72** | **0.72** | **14000** |
| **Weighted Avg** | **0.72** | **0.72** | **0.72** | **14000** |

---

### Performance Summary

- Achieved **71.59% test accuracy** on unseen patient data.
- Balanced **precision (73.38%)** and **recall (67.72%)** for reliable risk prediction.
- Achieved an overall **F1-score of 70.44%**, indicating balanced classification performance.
- Model outputs prediction probabilities to provide confidence along with binary classification.

---

## Author

**Satyam Gupta** <br>
B.Tech in Electronics and Communication Engineering <br>
MANIT Bhopal

If you found this project useful, consider giving it a ⭐.
