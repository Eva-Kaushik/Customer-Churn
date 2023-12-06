import pandas as pd
import numpy as np
import random
import string  # Import the 'string' module
from datetime import datetime, timedelta

# Function to generate a random authorization code
def generate_authorization_code(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a random date within a specified range
def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

# Create a DataFrame with a 'Status' column
data = {'Status': ['active', 'churned', 'active', 'churned', 'active']}
df = pd.DataFrame(data)

# Define date range for random dates as datetime objects
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 1, 1)

# Initialize 'Start_Date' and 'End_Date' columns with NaN values
df['Start_Date'] = pd.NaT
df['End_Date'] = pd.NaT

# Generate random start and end dates for churned customers
churned_indices = df[df['Status'] == 'churned'].index
df.loc[churned_indices, 'Start_Date'] = [generate_random_date(start_date, end_date) for _ in churned_indices]
df['End_Date'] = df['Start_Date'] + pd.to_timedelta(pd.offsets.Day(random.randint(1, 365)), 'D')

# Calculate the 'Lifetime' column only for churned customers
df['Lifetime'] = (df['End_Date'] - df['Start_Date']).dt.days


# Define possible values for the specified columns
possible_values = {
    'Agent_Notes': ['Note1', 'Note2', 'Note3', 'None'],
    'Authorization_Status': ['Approved', 'Declined', 'Error', 'Referred', 'Not Authenticated', 'Expired Card', 'Insufficient Funds', 'Invalid Card', 'Issuer Unavailable', 'Timeout'],
    'Billing_Cycle': ['Cycle1', 'Cycle2', 'Cycle3', 'None'],
    'Customer_Feedback': ['Feedback1', 'Feedback2', 'Feedback3', 'None'],
    'Device_ID': ['Device1', 'Device2', 'Device3', 'None'],
    'Interaction_Time': ['Time1', 'Time2', 'Time3', 'None'],
    'IP_Address': ['IP1', 'IP2', 'IP3', 'None'],
    'Merchant_Category': ['Category1', 'Category2', 'Category3', 'None'],
    'Merchant_ID': ['ID1', 'ID2', 'ID3', 'None'],
    'Merchant_Location': ['Location1', 'Location2', 'Location3', 'None'],
    'Payment_Gateway': ['Gateway1', 'Gateway2', 'Gateway3', 'None'],
    'Previous_Resolution_Status': ['Status1', 'Status2', 'Status3', 'None'],
    'Promo_Code': ['Promo1', 'Promo2', 'Promo3', 'None'],
    'Receipt_ID': ['Receipt1', 'Receipt2', 'Receipt3', 'None'],
    'Referral_Source': ['Source1', 'Source2', 'Source3', 'None'],
    'Response_to_Last_Promotion': ['Response1', 'Response2', 'Response3', 'None'],
    'Topics_Discussed': ['Topic1', 'Topic2', 'Topic3', 'None'],
    'Has_Promotion_Used': ['Yes', 'No'],
}

# Number of samples (rows)
num_samples = 7000
data = []

# Function to generate a random value from the specified list of possible values
def generate_random_value(column_name):
    return random.choice(possible_values[column_name])

# Initialize columns with generic values
for _ in range(num_samples):
    # Define date range for random dates
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)

    record = {
        'Age': random.randint(18, 80),
        'Agent_ID': random.randint(1000, 9999),
        'Agent_Notes': generate_random_value('Agent_Notes'),
        'Annual_Fee': random.uniform(0, 100),
        'Authorization_Code': generate_authorization_code(),
        'Authorization_Status': generate_random_value('Authorization_Status'),
        'Avg_Monthly_Spend': random.uniform(0, 2000),
        'Balance_Transferred': random.uniform(0, 5000),
        'Billing_Cycle': generate_random_value('Billing_Cycle'),
        'Card_Cancelled': random.choice(['Yes', 'No']),
        'Card_Expiry_Date': generate_random_date(start_date, end_date),  # Random date
        'Card_ID': random.randint(10000, 99999),
        'Card_Tier': random.choice(['Platinum', 'Gold', 'Silver', 'Bronze', 'Basic']),
        'Channel': random.choice(['Web', 'Mobile App', 'In-Person', 'Phone']),
        'Channel_Preference': random.choice(['Email', 'SMS', 'Push Notification']),
        'Churn_Risk_Flag': random.choice(['Yes', 'No']),
        'Communication_Preference': random.choice(['Email', 'SMS', 'Phone']),
        'Complaint_Count': random.randint(0, 10),
        'CAC': random.uniform(0, 500),
        'Credit_Utilization_Rate': round(random.uniform(0, 1), 2),
        'Currency_Type': 'USD',
        'Current_Balance': random.uniform(0, 5000),
        'Customer_Feedback': generate_random_value('Customer_Feedback'),
        'Customer_ID': random.randint(10000, 99999),
        'Customer_Lifetime_Value': random.uniform(100, 10000),
        'Days_Since_Last_Customer_Service_Interaction': random.randint(0, 365),
        'Days_Since_Last_Login': random.randint(0, 30),
        'Days_Since_Last_Transaction': random.randint(0, 365),
        'Declined_Transactions': random.randint(1, 10),
        'Device_ID': generate_random_value('Device_ID'),
        'Device_Used': random.choice(['Web', 'Mobile App', 'Desktop']),
        'Discount_Applied': random.uniform(0, 100),
        'Exchange_Rate': 1.0,
        'Follow_Up_Date': generate_random_date(start_date, end_date),  # Random date
        'Follow_Up_Required': random.choice(['Yes', 'No']),
        'Geographic_Region': random.choice(['North', 'South', 'East', 'West', 'Central']),
        'Has_Balance_Transfer': random.choice(['Yes', 'No']),
        'Has_Promotion_Used': generate_random_value('Has_Promotion_Used'),
        'Holiday_Spending': random.uniform(0, 100),
        'Income_Level': random.choice(['Low', 'Medium', 'High']),
        'Initial_Response_Time': random.uniform(0, 60),
        'Installment_Plan': random.choice(['Yes', 'No']),
        'Interaction_Date': generate_random_date(start_date, end_date),  # Random date
        'Interaction_Duration': random.uniform(0, 60),
        'Interaction_ID': random.randint(10000, 99999),
        'Interaction_ID_count': random.randint(1, 5),
        'Interaction_Time': generate_random_value('Interaction_Time'),
        'Interaction_Type': random.choice(['Email', 'Chat', 'Phone']),
        'Interaction_Frequency': random.uniform(0, 60),
        'Interest_Charges': random.uniform(0, 100),
        'Interest_Revenue': random.uniform(0, 100),
        'IP_Address': generate_random_value('IP_Address'),
        'Is_Fraud': random.choice(['Yes', 'No']),
        'Likely_to_Leave': random.choice(['Yes', 'No']),
        'Max_Credit_Limit': random.uniform(1000, 10000),
        'Merchant_Category': generate_random_value('Merchant_Category'),
        'Merchant_ID': generate_random_value('Merchant_ID'),
        'Merchant_Location': generate_random_value('Merchant_Location'),
        'Min_Payment': random.uniform(0, 100),
        'Network_Engagement_Rate': round(random.uniform(0, 1), 2),
        'Network_Size': random.randint(10, 1000),
        'NPS_Score': random.randint(0, 10),
        'Num_Complaints': random.randint(0, 10),
        'Number_of_Installments': random.randint(1, 12),
        'Number_of_Referrals': random.randint(0, 10),
        'Occupation': random.choice(['Student', 'Professional', 'Retired', 'Unemployed']),
        'Open_Email_Rate': round(random.uniform(0, 1), 2),
        'Outstanding_Debt': random.uniform(0, 5000),
        'Payment_Gateway': generate_random_value('Payment_Gateway'),
        'Payment_History_Length': random.randint(1, 10),
        'Payment_Method': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer']),
        'Payment_Timeliness': random.choice(['On Time', 'Slightly Late']),
        'Payment_to_Income_Ratio': round(random.uniform(0, 1), 2),
        'Preferred_Contact_Method': random.choice(['Email', 'Phone', 'SMS']),
        'Preferred_Reward_Type': random.choice(['Travel', 'Cashback', 'Points']),
        'Previous_Interaction_Date': 'None',
        'Previous_Resolution_Status': 'None',
        'Promo_Code': random.choice(['Yes', 'No']),
        'Queue_Time': random.uniform(0, 60),
        'Receipt_ID': 'None',
        'Referral_Reward_Points': random.uniform(0, 100),
        'Referral_Source': 'None',
        'Region': random.choice(['North', 'South', 'East', 'West', 'Central']),
        'Resolution_Status': random.choice(['Resolved', 'Pending']),
        'Resolution_Time': random.uniform(0, 60),
        'Response_to_Last_Promotion': 'None',
        'Reward_Points_Earned': random.uniform(1, 1000),
        'Reward_Points_Redeemed': random.uniform(1, 1000),
        'Reward_Type': random.choice(['Travel', 'Cashback', 'Points']),
        'Revenue': random.uniform(100, 1000),  
        'Sale_Period': random.choice(['Yes', 'No']),
        'Sentiment_Score': round(random.uniform(-1, 1), 2),
        'Satisfaction_Score': random.randint(1, 10),
        'Settlement_Date': 'None',
        'Shopping_Platform_Preference': random.choice(['Online', 'In-Store']),
        'Social_Media_Follow': random.choice(['Yes', 'No']),
        'Spending_Category_Preference': random.choice(['Groceries', 'Electronics', 'Clothing']),
        'Status': random.choice(['Active', 'Churned']),
        'Summer_Spending': random.uniform(0, 100),
        'Survey_Date': 'None',
        'Satisfaction_Score': random.randint(1, 10),
        'Tax_Amount': random.uniform(0, 100),
        'Topics_Discussed': 'None',
        'Total_Transactions_in_Period': random.randint(0, 100),
        'Transaction_Amount': random.uniform(0, 1000),
        'Transaction_Frequency': random.randint(4, 10),
        'Weekend_vs_Weekday_Spending': random.randint(4, 10),
    }
    data.append(record)

    

# Assuming data is previously defined and contains relevant information
df = pd.DataFrame(data)

# Calculate the number of interactions based on relevant columns
df['num_interactions'] = df['Complaint_Count'] + df['Interaction_ID_count'] + df['Num_Complaints']

def customer_segmentation(row):
    # Over Utilizers Rules
    if row["Credit_Utilization_Rate"] > 0.8 and row["Payment_Timeliness"] == "Late":
        return "Over Utilizer", "Rule 1", "High"
    elif row["Payment_Timeliness"] == "Late" and row["Outstanding_Debt"] > 4000:
        return "Over Utilizer", "Rule 2", "High"
    elif row["Installment_Plan"] == "Yes" and row["Outstanding_Debt"] > 4000:
        return "Over Utilizer", "Rule 3", "High"

    # Inactive Users Rules
    elif row["Days_Since_Last_Login"] > 25 and row["Open_Email_Rate"] < 0.2:
        return "Inactive", "Rule 4", "High"
    elif row["Interaction_ID_count"] < 2:
        return "Inactive", "Rule 5", "High"
    elif row["Days_Since_Last_Transaction"] > 30 and row["Annual_Fee"] > 80:
        return "Inactive", "Rule 6", "High"

    # Complaint-heavy Users
    elif row["Num_Complaints"] > 5 and (row["Resolution_Status"] == 'Pending' or row["Resolution_Status"] == 'Escalated'):
        return "Complaint-heavy", "Rule 7", "High"
    elif row["Open_Email_Rate"] < 0.2 and row["Days_Since_Last_Login"] > 25 and row["Num_Complaints"] > 5:
        return "Complaint-heavy", "Rule 8", "High"

    # Sporadic Users Rules
    elif row["Weekend_vs_Weekday_Spending"] > 8 and row["Transaction_Frequency"] < 5:
        return "Sporadic", "Rule 9", "Medium"
    elif row["Days_Since_Last_Transaction"] > 300 and row["Annual_Fee"] < 20:
        return "Sporadic", "Rule 10", "Medium"
    elif row["Interaction_ID_count"] == 1 and row["Transaction_Amount"] < 100:
        return "Sporadic", "Rule 11", "Medium"
		
    # Loyal Users Rules
    elif row["Interaction_Frequency"] > 7 and row["Payment_History_Length"] > 5:
        return "Loyal User", "Rule 12", "Low"
    elif row["Reward_Points_Redeemed"] > 500 and row["Satisfaction_Score"] > 7:
        return "Loyal User", "Rule 13", "Low"

    # Financially Conscious Users Rules
    elif row["Credit_Utilization_Rate"] < 0.2 and row["Payment_Timeliness"] == "On Time":
        return "Financially Conscious", "Rule 14", "Low"
    elif row["Payment_to_Income_Ratio"] > 0.5 and row["Outstanding_Debt"] < 1000:
        return "Financially Conscious", "Rule 15", "Low"

    # Reward Maximisers Rules
    elif row["Has_Promotion_Used"] == "Yes" and row["Reward_Points_Redeemed"] > 700:
        return "Reward Maximiser", "Rule 16", "Low"
    elif row["Response_to_Last_Promotion"] == "Response1" and row["Social_Media_Follow"] == "Yes":
        return "Reward Maximiser", "Rule 17", "Low"

    # High Balancers Rules
    elif row["Current_Balance"] > 5000 and row["Payment_Timeliness"] in ['Late', 'Very Late']:
        return "High Balancer", "Rule 18", "Medium"
    elif row["Min_Payment"] < (row["Current_Balance"] * 0.05):
        return "High Balancer", "Rule 19", "Medium"
    elif row["Reward_Points_Earned"] < 10:
        return "High Balancer", "Rule 20", "Medium"

    # Low Engagement Rules
    elif row["Sentiment_Score"] < -0.5 and row["Interaction_ID_count"] < 5:
        return "Low Engagement", "Rule 21", "Medium"
    
    else:
        return "Regular", "None", "Not Applicable"
        
    return customer_type, rule, risk_level
    
    # Apply the customer segmentation function to the DataFrame
df['Customer_Type'], df['Rule_Matched'], df['Customer_Risk_Level'] = zip(*df.apply(customer_segmentation, axis=1))

# Verify the output
print(df[['Customer_Type', 'Rule_Matched', 'Customer_Risk_Level']].head())

# Calculate the churn rate based on the 'Status' column. I'm assuming Status has values "churned" and something else.
churn_rate = (df['Status'] == 'churned').mean()

# Add the 'Churn_rate' column to the DataFrame
df['Churn_rate'] = churn_rate

# Assuming 'Revenue' column exists and 'Status' column has a binary value where 'churned' indicates a churned customer.
df['churned_revenue'] = df[df['Status'] == 'churned']['Revenue'].sum()

# Save the DataFrame to a CSV file
df.to_csv('output_data.csv', index=False)