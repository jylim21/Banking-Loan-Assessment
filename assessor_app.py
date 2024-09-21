from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

model = joblib.load('dt_model.sav')
scaler=joblib.load('scaler.gz')

features=['revol_util','int_rate','grade','funded_amnt','term','dti','sub_grade','loan_prncp_perc']#,'issue_to_credit_pull'

def clean_data(df):
    # try:
    df = df[['term','grade','sub_grade','int_rate','revol_util','total_rec_prncp','total_rec_int','dti','funded_amnt']]
    #df['last_credit_pull_d'] = pd.to_datetime(df['last_credit_pull_d'], format='%b-%y')
    #df['issue_d'] = pd.to_datetime(df['issue_d'], format='%b-%y')
    #df['issue_to_credit_pull']=round((df['last_credit_pull_d']-df['issue_d'])/np.timedelta64(1,'M'))
    df['term']=df['term'].replace({' 36 months':36, ' 60 months':60}).astype(int)
    df['grade']=df['grade'].replace({'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6})
    df['sub_grade']=df['sub_grade'].str[1].astype(int)
    # df['int_rate']=df['int_rate'].str.replace('%','').astype(float)
    # df['revol_util']=df['revol_util'].str.replace('%','').astype(float)
    df['loan_prncp_perc']=df['total_rec_prncp']/(df['total_rec_prncp']+df['total_rec_int'])
    # except ValueError:
        # raise ValueError("Invalid Data Type")
    # raw_data = np.array([df['revol_util'], df['int_rate'], df['grade'], df['funded_amnt'], df['term'], df['dti'], df['sub_grade'], df['loan_prncp_perc'] ]) #, df['issue_to_credit_pull']
    # raw_data = np.array([features])
    scaled_data=df[features]
    # scaled_data = scaler.transform(df[features])
    return scaled_data


def home():
    return "Welcome to the ML Model API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        df = request.get_json()
        # df = pd.json_normalize(df)
        df=pd.DataFrame(df)
        
        # Clean the input data
        cleaned_data = clean_data(df)
        
        # Make a prediction
        predictions = model.predict(cleaned_data)
        
        # Return the result as JSON
        return jsonify({'predictions': predictions.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)