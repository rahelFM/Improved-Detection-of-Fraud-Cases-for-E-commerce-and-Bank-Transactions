import pandas as pd

# Load your dataset
fraud_df = pd.read_csv('Improved-Detection-of-Fraud-Cases-for-E-commerce-and-Bank-Transactions\\data\\Fraud_Data.csv')  # Update the path accordingly

# Convert string timestamps to datetime objects
fraud_df['purchase_time'] = pd.to_datetime(fraud_df['purchase_time'], errors='coerce')
fraud_df['signup_time'] = pd.to_datetime(fraud_df['signup_time'], errors='coerce')

# Now you can safely calculate time differences
fraud_df['time_since_signup'] = (fraud_df['purchase_time'] - fraud_df['signup_time']).dt.total_seconds()
