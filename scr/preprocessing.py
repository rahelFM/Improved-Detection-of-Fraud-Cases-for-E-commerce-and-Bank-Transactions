import pandas as pd

fraud_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\Fraud_Data.csv")
ip_country_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\IpAddress_to_Country.csv")
creditcard_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\creditcard.csv\\creditcard.csv")
#missing value handling
print(fraud_df.isnull().sum())
print(ip_country_df.isnull().sum())
print(creditcard_df.isnull().sum())
#daata cleaning
fraud_df.drop_duplicates(inplace=True)
creditcard_df.drop_duplicates(inplace=True)
#check and convert timestamp
fraud_df['signup_time'] = pd.to_datetime(fraud_df['signup_time'])
fraud_df['purchase_time'] = pd.to_datetime(fraud_df['purchase_time'])

