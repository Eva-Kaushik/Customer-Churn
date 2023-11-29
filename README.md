# Customer-Churn
Churn Prediction and Customer Segmentation Readme
Overview
This repository contains code and documentation for a Churn Prediction and Customer Segmentation system. The system utilizes machine learning models, specifically the XGBoost algorithm, to identify potential churn risks and categorize customers into different clusters based on their behavior patterns. The aim is to provide actionable insights for customer retention strategies.

Churn_Prediction_Segmentation_Documentation.pdf: Detailed documentation explaining the system architecture, model training, and interpretation of results.
Churn Prediction and Customer Segmentation Process
High-Risk Churn Clusters
1. Over-Utilizers:
a. High Credit Utilization, Late Payments:
- High Credit Utilization Rate
- Payment Timeliness set to 'Late'
- Interpretation: Customer relies heavily on the credit card but struggles to make timely payments.
- Recommended Action: Offer financial counseling, reduce interest rates temporarily.

b. Recurrent Late Fee Charges with Outstanding Debt:
- Payment Timeliness often set to 'Late'
- High Outstanding Debt
- Interpretation: Financial strain on the customer leading to a search for better financial options.
- Recommended Action: Offer debt consolidation, payment plans, waive late fees for automatic payments.

c. High Installment Usage with High Outstanding Debt:
- Frequent use of Installment Plan
- High Outstanding Debt
- Interpretation: Customer might be stretching their financial capacity.
- Recommended Action: Offer debt consolidation, payment plans, waive late fees for automatic payments.

2. Inactive Users:
a. Inactive Online, Poor Email Engagement:
- High Days Since Last Login
- Low Open Email Rate
- Interpretation: Customer isn't engaging online or with email campaigns, an early sign of disengagement.
- Recommended Action: Launch re-engagement email campaigns, improve online user experience.

b. New Users with Minimal Interactions:
- Recently acquired customers
- Low Interaction ID count
- Interpretation: Newly acquired customers not engaging much, showing signs of potential churn.
- Recommended Action: Implement robust onboarding process, assign dedicated customer success agents.

c. Inactive yet High Fees:
- High Days Since Last Transaction
- High Annual Fee
- Interpretation: Customers are charged high fees but aren't using the card, potential churn.
- Recommended Action: Re-evaluate fee structure, offer fee waivers, introduce lower fee card variant.

3. Complaint-heavy Users:
a. High Complaints, Poor Resolution Status:
- High Number of Complaints
- Resolution Status set to 'Pending' or 'Escalated'
- Interpretation: Customer has many grievances, not being resolved promptly.
- Recommended Action: Prioritize resolution, assign dedicated customer service representatives.

b. Low Digital Engagement but High Complaints:
- Low Open Email Rate and high Days Since Last Login
- High Number of Complaints
- Interpretation: Customers experiencing issues with digital channels leading to dissatisfaction.
- Recommended Action: Enhance digital user experience, conduct surveys to pinpoint issues.

Moderate-Risk Churn Clusters
1. Sporadic Users:
a. Usage only on Weekends or Holidays:
- High Weekend vs Weekday Spending or Holiday Spending
- Interpretation: Card might be a secondary option used only during leisure times.
- Recommended Action: Target with exclusive weekday offers, provide incentives for more frequent usage.

b. Promo Engagement without Transactions:
- High engagement with promotions (Promo Code usage)
- Low Transaction Amount or Transaction Frequency
- Interpretation: Customer is interested in offers but isn't making transactions.
- Recommended Action: Reassess promotional strategies, align with customer preferences.

2. High Balancers:
a. High Balance, Minimum Payments:
- High Current Balance
- Payment Timeliness set to 'Late' or 'Very Late'
- Low Minimum Payment relative to Current Balance
- Interpretation: Customer may be struggling financially, potential default or churn.
- Recommended Action: Offer personalized payment plans, financial counseling, reassess reward points allocation.

b. High Balance with Low Reward Points:
- High Current Balance
- Low Reward Points Earned
- Interpretation: Card might not offer competitive rewards for spending.
- Recommended Action: Offer personalized payment plans, financial counseling, reassess reward points allocation.

3. New Users with Low Engagement:
a. Low Sentiment, High Interaction without Resolution:
- Negative Sentiment Score
- High Number of Interactions with unresolved status
- Interpretation: Customer has frequent issues, expresses negative sentiment, strong churn indicator.
- Recommended Action: Assign dedicated support teams, offer personalized promotions.

Low-Risk Churn Clusters
1. Loyal Users:
a. High Transaction, Low Reward Redemption:
- High Transaction Amount
- Low Reward Points Redeemed
- Interpretation: Customer spends a lot but doesn't engage with the rewards program.
- Recommended Action: Launch awareness campaigns on reward redemptions, revamp rewards program.

b. Infrequent Usage, High Credit Limit:
- Low Transaction Frequency
- High Max Credit Limit
- Interpretation: Customer has high credit limit but doesn't use the card frequently.
- Recommended Action: Engage with personalized offers, understand needs better through surveys.

2. Financially Conscious Users:
a. Frequent Changes in Communication Preferences:
- Regular updates to Communication Preference
- Interpretation: Suggests low tolerance for misaligned or non-personalized communication.
- Recommended Action: Ensure strict adherence to communication preferences, periodically review and update strategies.

3. Reward Maximizers:
a. High Spending during Sales but No Discount Engagement:
- High Transaction Amount during known sale periods
- No usage of Promo Code or low Discount Applied
- Interpretation: Customer spends during sales but doesn't use card's discount offers.
- Recommended Action: Promote discount offers more aggressively during sale seasons, consider partnerships for exclusive discounts.
