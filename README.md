# Loan Verification Prediction using Decision Tree and Random Forest

## 📌 Project Overview

This project focuses on predicting loan verification status using Machine Learning classification algorithms. The goal is to classify customers into different verification categories based on their financial information.

Two Machine Learning models were implemented and compared:

- Decision Tree Classifier
- Random Forest Classifier

The project evaluates the performance of both models and analyzes their prediction capabilities using accuracy, confusion matrices, and classification reports.

---

## 🎯 Problem Statement

Financial institutions often verify customer information before approving loans. The objective of this project is to predict the verification status of customers using key financial attributes.

### Input Features

- Loan Amount
- Annual Income
- Total Payment

### Target Variable

- Verification Status

Possible Classes:

- Verified
- Source Verified
- Not Verified

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn

---

## 📂 Project Workflow

### 1. Data Loading

The loan dataset is loaded using Pandas.

### 2. Feature Selection

Selected Features:

- `loan_amount`
- `annual_income`
- `total_payment`

Target Column:

- `verification_status`

### 3. Train-Test Split

The dataset is divided into training and testing sets:

- 50% Training Data
- 50% Testing Data

### 4. Model Training

#### Decision Tree Classifier

A tree-based machine learning algorithm that predicts outcomes by learning decision rules from data.

#### Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### 5. Model Evaluation

The following evaluation metrics were used:

- Accuracy Score
- Confusion Matrix
- Classification Report
- Precision
- Recall
- F1-Score

### 6. Prediction Testing

The trained models were tested using new customer information to predict verification status.

---

# 📊 Case 1: Model Performance Comparison

Both models were trained and evaluated using the same dataset and testing conditions.

## Decision Tree Results

**Accuracy:** 43.39%

### Strengths

- Easy to understand
- Fast training
- Simple implementation

### Limitations

- Higher risk of overfitting
- Lower overall prediction accuracy

---

## Random Forest Results

**Accuracy:** 47.80%

### Strengths

- Better generalization
- Improved prediction performance
- Reduced overfitting

### Limitations

- Slightly higher computational cost
- Less interpretable than a single decision tree

---

## Comparison Summary

| Metric | Decision Tree | Random Forest |
|----------|----------|----------|
| Accuracy | 43.39% | 47.80% |
| Precision | Lower | Higher |
| Recall | Lower | Higher |
| F1 Score | Lower | Higher |
| Stability | Lower | Higher |
| Overfitting Risk | Higher | Lower |

### 🏆 Winner

**Random Forest** achieved the best overall performance with higher accuracy and better classification metrics.

---

# 🧪 Case 2: Customer Prediction Comparison

A new customer record was tested on both models.

## Customer Details

| Feature | Value |
|----------|----------|
| Loan Amount | 8000 |
| Annual Income | 48000 |
| Total Payment | 3939 |

---

## Decision Tree Prediction

```text
Verified
```

---

## Random Forest Prediction

```text
Verified
```

---

## Result Analysis

Both models successfully predicted the customer as:

### ✅ Verified

This indicates agreement between the two models for the given customer data.

Although both models produced the same prediction, Random Forest remains the preferred model because it demonstrated better overall performance during evaluation.

---

# 📈 Key Learnings

Through this project, I gained hands-on experience in:

- Machine Learning Classification
- Decision Tree Algorithms
- Random Forest Algorithms
- Data Preprocessing
- Model Training
- Model Evaluation
- Confusion Matrix Analysis
- Precision, Recall, and F1-Score
- Model Comparison Techniques

---

# 🚀 Future Improvements

Potential enhancements for this project include:

- Feature Engineering
- Hyperparameter Tuning
- Cross Validation
- Class Imbalance Handling
- Feature Importance Analysis
- Streamlit Web Application Deployment
- Additional Classification Models

---

# 📸 Results

## Decision Tree Performance

- Accuracy: **43.39%**
- Classification Report
- Confusion Matrix

## Random Forest Performance

- Accuracy: **47.80%**
- Classification Report
- Confusion Matrix

The **Random Forest** model achieved better overall performance compared to the **Decision Tree** model, making it the preferred model for this loan verification classification task.

---

# 📷 Project Output

The repository contains the source code and implementation of:

- Decision Tree Classifier
- Random Forest Classifier
- Model Evaluation Metrics
- Customer Verification Prediction

The project demonstrates the complete Machine Learning workflow, including:

- Data Preprocessing
- Feature Selection
- Train-Test Split
- Model Training
- Performance Evaluation
- Customer Verification Prediction

Sample outputs such as accuracy scores, confusion matrices, classification reports, and prediction results can be generated by running the provided Python scripts.

---

## 🏆 Conclusion

- Decision Tree Accuracy: **43.39%**
- Random Forest Accuracy: **47.80%**

Random Forest outperformed Decision Tree in terms of overall classification performance, achieving higher accuracy, precision, recall, and F1-score. Both models successfully predicted the customer verification status as **Verified** for the given test case.

---

## 👨‍💻 Author

**Keerthiga S**

Aspiring Data Analyst | Data Science Enthusiast

### Skills

- Python
- SQL
- Power BI
- Excel
- Machine Learning
