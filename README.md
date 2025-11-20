# Loan_approval_project
# 🏦 Loan Approval Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a loan application will be **approved or rejected** using Machine Learning.
By analyzing applicant income, employment status, loan amount, credit history, and other factors, the model helps automate loan decisions for financial institutions.

---

## 🚀 Features

* Complete data cleaning & preprocessing
* Exploratory Data Analysis (EDA) with graphs
* Feature engineering
* Multiple ML models compared
* Performance evaluation (Accuracy, Precision, Recall, F1, Confusion Matrix)
* Final optimal model selection
* Ready for integration with a web app (Flask/Streamlit)

---

## 🗂️ Dataset Description

| Feature           | Description              |
| ----------------- | ------------------------ |
| Gender            | Male/Female              |
| Married           | Yes/No                   |
| Dependents        | 0/1/2/3+                 |
| Education         | Graduate/Not Graduate    |
| Self_Employed     | Yes/No                   |
| ApplicantIncome   | Applicant monthly income |
| CoapplicantIncome | Income of co-applicant   |
| LoanAmount        | Loan amount requested    |
| Loan_Amount_Term  | Loan duration in days    |
| Credit_History    | 1 = Good, 0 = Bad        |
| Property_Area     | Urban/Semiurban/Rural    |
| Loan_Status       | Target variable (Y/N)    |

---

## 📊 Exploratory Data Analysis (EDA)

The EDA includes:

* Univariate analysis
* Bivariate analysis
* Outlier detection
* Correlation heatmap
* Loan approval trends by income, education, credit history
* Feature importance graphs

---

## 🧠 Machine Learning Models Used

The following algorithms were trained and compared:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* XGBoost (optional)

---

## 📈 Model Evaluation

Metrics used:

* Accuracy Score
* Confusion Matrix
* Precision, Recall, F1-Score
* ROC Curve & AUC

The Random Forest / Logistic Regression model performed best (depends on your result).

---

## 📦 Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost (if used)
* Flask/Streamlit (optional deployment)

---

## 📁 Project Structure

```
Loan-Approval-Prediction/
│
├── dataset/               
├── notebooks/             
├── src/                   
├── models/                
├── static/                
├── templates/             
├── app.py                 
└── README.md              
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/loan-approval-prediction.git
cd loan-approval-prediction
```

### 2️⃣ Install required libraries

```
pip install -r requirements.txt
```

### 3️⃣ Run Jupyter Notebook (for training)

```
jupyter notebook
```

### 4️⃣ Run Web Application (if included)

```
python app.py
```

---

## 🔮 Results & Conclusion

* The model accurately predicts loan approval using applicant and loan-related features.
* **Credit History, Applicant Income, Loan Amount, and Loan Term** are the most impactful features.
* The trained model can help banks automate their loan screening system efficiently.

---

## 📚 References (IEEE Format)

1. T. Hastie, R. Tibshirani, and J. Friedman, *The Elements of Statistical Learning*, Springer, 2009.
2. Scikit-learn Documentation, 2024.
3. Kaggle, *Loan Prediction Dataset*.

---

## 👨‍💻 Members

**Pranav Kishor Sutar**
**Mohit Manilal Patel**
**Bhavesh Dinesh Patil**
**Bhavesh Devaram Chaudhari**

##Under the Guidance of:
Prof. Kaminee Patil




