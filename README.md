# Banking Loan Assessment App

**Disclaimer**: *This app is intended for educational purpose only, usage in actual work purposes are **NOT recommended** as this model is trained based on my client's data only which is likely to be biased, I will NOT be responsible for any financial losses incurred due to inaccurate predictions made by this app.*

This is an app I made for my client who is also a banker, it predicts whether an active loan will be successfully paid off or defaulted based on the following features:
- *term*                : **int** -> term of loan in months.
- *grade*               : **str** -> primary grade of credit profile (any one of A,B,C,D,E)
- *sub_grade*           : **str** -> sub-grade of credit profile (eg. A3, C1, B2 etc.)
- *int_rate*            : **float** -> interest rate *per annum* contracted on the loan
- *revol_util*          : **float** -> revolving line utilization rate, which is the percentage of credit used over total available credit
- *total_rec_prncp*     : **float** -> Principal compenent of total paid amount by debtor
- *total_rec_int*       : **float** -> Interest component of total paid amount by debtor
- *dti*                 : **float** -> debt-to-income ratio of debtor (also known as 'debt service ratio, DSR)
- *funded_amnt*         : **int** -> loan amount funded
- *last_credit_pull_d*  : **date** -> Year Month where the credit profile of debtor is last pulled from CTOS in the format "MMM-yy"
- *issue_d*             : **date** -> Year Month of the date of issuance of loan

## How to use
Ensure you have Docker installed.
1. Clone the repo
   ```
   git clone https://github.com/jylim21/Banking-Loan-Assessment.git
   cd Banking-Loan-Assessment
   ```
2. Build and run Docker image/container
   ```
   docker build -t assessor_app .
   docker run -p 5000:5000 assessor_app
   ```
