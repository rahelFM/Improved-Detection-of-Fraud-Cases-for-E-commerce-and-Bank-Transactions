import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fraud_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\Fraud_Data.csv")
ip_country_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\IpAddress_to_Country.csv")
creditcard_df = pd.read_csv("D:\\KAIM5\\week8\\Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\creditcard.csv\\creditcard.csv")
fraud_df['class'].value_counts(normalize=True)  # Imbalance check
fraud_df['age'].hist()
fraud_df['purchase_value'].hist()

#Correlation matrix

sns.countplot(x='sex', hue='class', data=fraud_df)
sns.boxplot(x='class', y='purchase_value', data=fraud_df)

import ipaddress

# If ip_address is numeric
fraud_df['ip_int'] = fraud_df['ip_address'].astype(int)

# Then merge with IP-to-country mapping
ip_country_df['lower_bound_ip_address'] = ip_country_df['lower_bound_ip_address'].astype(int)
ip_country_df['upper_bound_ip_address'] = ip_country_df['upper_bound_ip_address'].astype(int)
ip_country_df.sort_values('lower_bound_ip_address', inplace=True)

fraud_df.sort_values('ip_int', inplace=True)

# Use merge_asof for efficient interval matching
fraud_df = pd.merge_asof(
    fraud_df,
    ip_country_df[['lower_bound_ip_address', 'upper_bound_ip_address', 'country']],
    left_on='ip_int',
    right_on='lower_bound_ip_address',
    direction='backward'
)

# Filter where IP is within the range
fraud_df = fraud_df[fraud_df['ip_int'] <= fraud_df['upper_bound_ip_address']]
