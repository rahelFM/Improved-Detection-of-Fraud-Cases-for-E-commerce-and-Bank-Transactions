import pandas as pd

credit_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\creditcard.csv\\creditcard.csv")
fraud_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\Fraud_Data.csv")
ip_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\IpAddress_to_Country.csv")
X_credit = credit_df.drop("Class", axis=1)
y_credit = credit_df["Class"]
X_fraud = fraud_df.drop("class", axis=1)
y_fraud = fraud_df["class"]

#handling class imbalance
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_credit, y_credit, test_size=0.2, random_state=42, stratify=y_credit)

sm = SMOTE(random_state=42)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)


#model training
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, roc_auc_score

# Initialize models
lr = LogisticRegression(max_iter=1000, class_weight='balanced')
rf = RandomForestClassifier(n_estimators=100, random_state=42)
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# Voting ensemble
ensemble = VotingClassifier(estimators=[
    ('lr', lr), ('rf', rf), ('xgb', xgb)
], voting='soft')

# Fit and evaluate
ensemble.fit(X_train_res, y_train_res)
y_pred = ensemble.predict(X_test)

print(classification_report(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, ensemble.predict_proba(X_test)[:, 1]))
import joblib
joblib.dump(ensemble, "fraud_model.pkl")
