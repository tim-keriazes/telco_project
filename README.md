___ 
# Classification Project: Telco Churn
### By Tim Keriazes

___
### About the Project

### Objective:

My goal for this project was to discover the driving factors for customer churn at Telco. I will do this through the acquistition, preparation, and exploration of the telco customer data set. This will enable statistical testing, modeling, and model evaluations to be conducted in order to accurately predict customer churn and its driving factors. With that knowledge I will provide Telco a set of recommended actions to reduce churn and increase customer retention.

### Initial Hypothesis/Questions:
My intitial hypothesis was that the biggest driver to churn was the high cost of service for month to month customers, conversely, I believed that those locked in a annual or multi-year contracts would be far less likely to churn. Additional factors may be payment type customer utilizes, and customer tenure (which is inherently related to contract type), and internet service type.

### Project Planning:
I will explore my hypothesis through the acquistition, preparation, and exploration of the telco customer data set. This will enable statistical testing, modeling, and model evaluations to be conducted in order to accurately predict customer churn and its driving factors.
___
### Data Dictionary:

# <a name="data-dictionary"></a>Data Dictionary
|    index    |                              column/feature name                             | dtype                                        |  key/description  |                                                        |
|:-----------------:|:--------------------------------------------------------------------:|--------------------------------------------|:-------:|:------------------------------------------------------------------:|
 |0   |senior_citizen                         |7032 non-null   int64   |1 = senior citizen, 0 = not senior citizen
 |1  |tenure                                 |7032 non-null   int64   |Length in Months
 |2   |monthly_charges                        |7032 non-null   float64 |Monthly charges in dollars
 |3   |total_charges                          |7032 non-null   float64 |Total charges in dollars annually
 |4   |churn                                  |7032 non-null   object  | Yes or No 
 |5   |contract_type                          |7032 non-null   object  |Month to Month, One Year, Two Year
 |6   |internet_service_type                  |7032 non-null   object  |DSl, Fiber optic, none
 |7   |payment_type                           |7032 non-null   object  |Mailed Check, Electronic Check, Credit Card (automatic), Bank Transfer(automatic)
 |8   |gender_encoded                         |7032 non-null   int64   |1 = female, 0 = male
 |9   |partner_encoded                        |7032 non-null   int64   |1 = Yes, 0 = No
 |10  |dependents_encoded                     |7032 non-null   int64   |1 = Yes, 0 = No
 |11  |phone_service_encoded                  |7032 non-null   int64   |1 = Yes, 0 = No
 |12  |paperless_billing_encoded              |7032 non-null   int64   |1 = Yes, 0 = No
 |13  |churn_encoded                          |7032 non-null   int64   |1 = Yes, 0 = No
 |14  |multiple_lines_No phone service        |7032 non-null   uint8   |1 = Yes, 0 = No
 |15  |multiple_lines_Yes                     |7032 non-null   uint8   |1 = Yes, 0 = No
 |16  |online_security_No internet service    |7032 non-null   uint8   |1 = Yes, 0 = No
 |17  |online_security_Yes                    |7032 non-null   uint8   |1 = Yes, 0 = No
 |18  |online_backup_No internet service      |7032 non-null   uint8   |1 = Yes, 0 = No
 |19  |online_backup_Yes                      |7032 non-null   uint8   |1 = Yes, 0 = No
 |20  |device_protection_No internet service  |7032 non-null   uint8   |1 = Yes, 0 = No
 |21  |device_protection_Yes                  |7032 non-null   uint8   |1 = Yes, 0 = No
 |22  |tech_support_No internet service       |7032 non-null   uint8   |1 = Yes, 0 = No
 |23  |tech_support_Yes                       |7032 non-null   uint8   |1 = Yes, 0 = No
 |24  |streaming_tv_No internet service       |7032 non-null   uint8   |1 = Yes, 0 = No
 |25  |streaming_tv_Yes                       |7032 non-null   uint8   |1 = Yes, 0 = No
 |26  |streaming_movies_No internet service   |7032 non-null   uint8   |1 = Yes, 0 = No
 |27  |streaming_movies_Yes                   |7032 non-null   uint8   |1 = Yes, 0 = No
 |28  |contract_type_One year                 |7032 non-null   uint8   |1 = Yes, 0 = No
 |29  |contract_type_Two year                 |7032 non-null   uint8   |1 = Yes, 0 = No
 |30  |internet_service_type_Fiber optic      |7032 non-null   uint8   |1 = Yes, 0 = No
 |31  |internet_service_type_None             |7032 non-null   uint8   |1 = Yes, 0 = No
 |32  |payment_type_Credit card (automatic)   |7032 non-null   uint8   |1 = Yes, 0 = No
 |33  |payment_type_Electronic check          |7032 non-null   uint8   |1 = Yes, 0 = No
 |34  |payment_type_Mailed check              |7032 non-null   uint8   |1 = Yes, 0 = No

___
### Key Findings:
___
### The overall churn rate for customers at Telco is 26.6%.
  - Fiber optic customers make up 44.0% of customer base and churn at 18.4%.
  - Month to month contract customers make up 55.1% of customer base and churn at 23.5%.
  - Electronic check payment type customers make up 33.6% of customer base and churn at 15.2%.
  - Senior citizens make up 16% of customer base and churn at 41.7%
___  
### Median tenure of churned customers: 10 months.
  - Median tenure of month to month customers that have churned: 7 months.
  - Median tenure of electronic check payment customers that have churned: 9 months.
___
### Average monthly charges: $64.80.
  - Average monthly charges of customers who have churned: $74.44, 9.64 higher than average.
  - Average monthly charges of fiber customers: $88.13, $23.33 higher than average.
  - Average monthly charges of month to month customers: $73.02, $8.22 higher than average.
  - Average monthly charges of electronic check payment customers: $78.70, $13.90 higher than average.
___
## Tested Hypotheses and Results
#### 1. Ho : Mean of monthly charges of churned customers >= Mean of monthly charges of all customers
####    Ha : Mean of monthly charges of churned customers < Mean of monthly charges of all customers
#### We fail to reject Ho
___
#### 2. Ho: mean length tenure of churned customers is <= mean length tenure of all customers
####    Ha: mean length tenure of churned customers is > mean length tenure of all customers
#### We fail to reject Ho
___
#### 3. Charges of customers who churn significantly different than those who do not churn
####    Ho: Charges of customers who churn equals that of those who don't churn.
####    Ha: Charges of customers who churn is not equal to that of those who don't churn.
#### We reject Ho, -t value and 0 p, significantly different
___
#### 4. Ho : Mean of monthly charges of churned fiber customers >= Mean of monthly charges of all customers
####    Ha : Mean of monthly charges of churned fiber customers < Mean of monthly charges of all customers
#### We fail to reject Ho
___
#### 5. Ho : Mean of monthly charges of churned month to month customers >= Mean of monthly charges of all customers
####    Ha : Mean of monthly charges of churned month to month customers < Mean of monthly charges of all customers
#### We fail to reject Ho
___
#### 6. Ho : Mean of monthly charges of churned electronic check customers >= Mean of monthly charges of all customers
####    Ha : Mean of monthly charges of churned electronic customers < Mean of monthly charges of all customers
#### We fail to reject Ho
___

## Instructions to reproduce the project and findings:

1. Prep Your Repo, ensure you can pull db from mysql using credentials from your env.py and my acquire.py
2. Import appropriate libraries and functions. utilize my prepare.py, aqcuire.py, explore.py
2. Acquire Data: Read TELCO data from MySQL using the get_telco_data() function in acquire.py
3. Clean, Prep & Split Data: Using functions tied to each other in prepare.py file:  prep_telco_data(), train_validate_test()
5. Explore Data: List all categorical & quantitative variables/features. Run exploratory stats functions on Uni-/Bi-/Multi-Variate data found in explore.py and telco_churn_report.ipynb
    - Hypothesis Testing
6. Identify Baseline: establish baseline prediction and accuracy
7. Modeling
    - Train
    - Validate
    - Test
8. Predict on Test Model
9. Export Predictions to CSV
