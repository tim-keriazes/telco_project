___ 
# Classification Project: Telco Churn

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
Your readme should include a data dictionary, which is important to provide in order to define and disambiguate each of the variables you are analyzing.


___
# <a name="data-dictionary"></a>Data Dictionary
|    column_name    |                              description                             | key                                        |  dtype  |                            value_counts                            |
|:-----------------:|:--------------------------------------------------------------------:|--------------------------------------------|:-------:|:------------------------------------------------------------------:|
| customer_id       | TELCO customer id                                                    |                                            | object  | 3943 non-null                                                      |
| gender            | customer gender                                                      | 1 = male, 0 = female                       | int64   | 3943 non-null, 1=male 0=female                        |
| senior_citizen    | customer senior citizen (age) status                                 | 1 = senior citizen, 0 = not senior citizen | int64   | 3943 non-null, 1=senior citizen 0=not senior citizen   |
| tenure            | TELCO customer tenure in months                                      |                                            | int64   | 3943 non-null, min: 0 mo, max: 72 mo                               |
| phone_service     | tracks if customer has TELCO phone service                           | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 3572, 0=no: 371                              |
| multiple_lines    | tracks if TELCO phone customer has multiple lines                    | 1 = yes, 0 = no, 3 = no phone service      | int64   | 3943 non-null, 1=yes: 1696, 0=no: 1876, 3=no phone service: 371    |
| online_security   | tracks if TELCO internet customer uses online security               | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1130, 0=no: 1973, 3=no internet service: 840 |
| online_backup     | tracks if TELCO internet customer uses online backup                 | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1396, 0=no: 1705, 3=no internet service: 840 |
| device_protection | tracks if TELCO internet customer uses device protection             | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1351, 0=no: 1752, 3=no internet service: 840 |
| tech_support      | tracks if TELCO internet customer uses tech support                  | 1 = yes, 0 = no, 3 = no internet service   | int64   | 3943 non-null, 1=yes: 1133, 0=no: 1970, 3=no internet service: 840 |
| paperless_billing | tracks if TELCO customer is signed up for paperless billing          | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2335, 0=no: 1608                             |
| monthly_charges   | lists expected month bill for TELCO customer                         |                                            | float64 | 3943 non-null                                                      |
| total_charges     | lists total charges billed to customer over their TELCO lifetime     |                                            | float64 | 3943 non-null                                                      |
| churn             | tracks if customer has left TELCO                                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1046, 0=no: 2897,                            |
| pymt_type_abt     | tracks if TELCO customer pays using Automatic Bank Transfers         | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 875, 0=no: 3068                              |
| pymt_type_acc     | tracks if TELCO customer pays using Automatic Credit Card payments   | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 883, 0=no: 3060                              |
| pymt_type_echk    | tracks if TELCO customer pays using Electronic Check payments        | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1290, 0=no: 2653                             |
| pymt_type_mchk    | tracks if TELCO customer pays using Electronic Check payments        | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 895, 0=no: 3048                              |
| intserv_dsl       | tracks if TELCO internet customer has DSL                            | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1369, 0=no: 2574                             |
| intserv_fiber     | tracks if TELCO internet customer has Fiber Optic                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1734, 0=no: 2209                             |
| contract_1yr      | tracks if TELCO customer has a 1 year contract                       | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 822, 0=no: 3121                              |
| contract_2yr      | tracks if TELCO customer has a 2 year contract                       | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 947, 0=no: 2996                              |
| contract_m2m      | tracks if TELCO customer has a 2 year contract                       | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2174, 0=no: 1769                             |
| phone_multi_line  | tracks if TELCO phone customer has multiple lines                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1696, 0=no: 2247                             |
| phone_sgl_line    | tracks if TELCO phone customer has multiple lines                    | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1876, 0=no: 2067                             |
| sgl_dependents    | tracks if TELCO customer is Single With Dependents                   | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1153, 0=no: 2790                             |
| sgl_no_dep        | tracks if TELCO customer is Single WithOUT Dependents                | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 1803, 0=no: 2140                             |
| fam_house         | tracks if TELCO customer is NOT Single With Dependents               | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 987, 0=no: 2956                              |
| stream_media      | tracks if TELCO internet customer streams any media (TV/movies)      | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2804, 0=no: 1139                             |
| online_feats      | tracks if TELCO internet customer is using online security or backup | 1 = yes, 0 = no                            | int64   | 3943 non-null, 1=yes: 2733, 0=no: 1210                             |
| auto_billpay      | tracks if TELCO customer is signed up for Automatic Billpay          | 1 = yes, 0 = no 1=yes: 1758, 0=no: 2158                             |
| sen_int           | tracks if TELCO customer is a senior citizen with internet           | 1 = yes, 0 = no                                                    |
| sen_int_techsup   | tracks if senior citizen internet customer used tech support         | 1 = yes, 0 = no  

















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

1. [Prep Your Repo](final_telco.ipynb#prep-your-repo)
2. [Import](final_telco.ipynb#import)
2. [Acquire Data](final_telco.ipynb#acquire-data)
3. [Clean, Prep & Split Data](final_telco.ipynb#clean-prep-and-split-df)
5. [Explore Data](final_telco.ipynb#explore-data)
    - [Hypothesis Testing](final_telco.ipynb#hypothesis-testing)
6. [Identify Baseline](final_telco.ipynb#identify-baseline)
7. [Modeling](final_telco.ipynb#modeling)
    - [Train](final_telco.ipynb#train)
    - [Validate](final_telco.ipynb#validate)
    - [Test](final_telco.ipynb#test)
8. [Predict on Test Model](final_telco.ipynb#predict-on-test-model)
9. [Export Predictions to CSV](final_telco.ipynb#export-predictions-to-csv)
