# Improved Detection of Fraud Cases for E-commerce and Bank Transactions

This repository contains a data science pipeline for detecting fraud in both e-commerce and bank transactions using machine learning models. It includes preprocessing, exploratory data analysis, feature engineering, model building, and explainability using SHAP.

---

## 📁 Project Structure

Improved-Detection-of-Fraud-Cases/
│
├── data/ # Contains datasets
│ ├── creditcard.csv # Bank transaction dataset
│ ├── creditcard.csv.zip # Compressed version of the above
│ ├── Fraud_Data.csv # E-commerce fraud detection dataset
│ └── IpAddress_to_Country.csv # Mapping of IP addresses to country info
│
├── scr/ # Source code directory
│ ├── eda.py # Exploratory Data Analysis
│ ├── preprocessing.py # Data cleaning and transformation
│ └── feature_engineering.py # Feature creation (e.g., time_since_signup)
│
├── .gitignore # Git ignore file
├── README.md # Project documentation
└── requirements.txt # Python dependencies


## 🧠 Objective

The goal of this project is to develop models that can accurately detect fraudulent transactions. The project focuses on:

- Understanding fraud patterns in both banking and e-commerce contexts.
- Handling class imbalance.
- Building and evaluating Logistic Regression and Ensemble models.
- Interpreting predictions using SHAP explainability.

---

## 🧾 Datasets

- **`creditcard.csv`**: Contains anonymized bank transaction data with a `Class` column (1 = fraud, 0 = non-fraud).
- **`Fraud_Data.csv`**: Contains e-commerce transaction data with features like `purchase_time`, `signup_time`, `ip_address`, and the fraud label.
- **`IpAddress_to_Country.csv`**: Used to enrich IP address data with geographic information.
## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Improved-Detection-of-Fraud-Cases.git
   cd Improved-Detection-of-Fraud-Cases
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required dependencies:

pip install -r requirements.txt
🧪 How to Run
Each module can be run individually or integrated into a pipeline:

Run preprocessing:

python scr/preprocessing.py
Run feature engineering:

python scr/feature_engineering.py
Run EDA:

python scr/eda.py
📝 Model training and evaluation modules can be added separately or integrated in modeling.py.

📊 Features Engineered
time_since_signup: Time (in seconds) between account creation and first purchase.

ip_country: Country derived from ip_address using IpAddress_to_Country.csv.

Other user behavior and transactional features (TBD).

📌 Future Improvements
Add models (Logistic Regression, Random Forest, XGBoost).

Address class imbalance using SMOTE or class weighting.

Build SHAP-based model explainability reports.

Evaluate metrics: ROC AUC, Precision, Recall, F1-Score.

🧑‍💻 Authors
Rahel Sileshi Abdisa – [10 Academy Week 8 Project]

📄 License
This project is open source under the MIT License.


