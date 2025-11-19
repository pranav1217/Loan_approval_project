import flask
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load model safely
with open('models/loan_application_model_lr.pickle', 'rb') as f:
    clf_lr = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

# -----------------------------
# Removed / commented routes
# -----------------------------

# @app.route('/')
# def main():
#     return flask.render_template('index.html')

# @app.route('/report')
# def report():
#     return flask.render_template('report.html')

# @app.route('/jointreport')
# def jointreport():
#     return flask.render_template('jointreport.html')

# -----------------------------
# ✅ ONLY ACTIVE ROUTE
# -----------------------------
@app.route("/", methods=['GET', 'POST'])
def Loan_Application():
    
    if flask.request.method == 'GET':
        return flask.render_template('Loan_Application.html')
    
    if flask.request.method == 'POST':

        genders_type = flask.request.form['genders_type']
        marital_status = flask.request.form['marital_status']
        dependents = flask.request.form['dependents']
        education_status = flask.request.form['education_status']
        self_employment = flask.request.form['self_employment']
        applicantIncome = float(flask.request.form['applicantIncome'])
        coapplicantIncome = float(flask.request.form['coapplicantIncome'])
        loan_amnt = float(flask.request.form['loan_amnt'])
        term_d = int(flask.request.form['term_d'])
        credit_history = int(flask.request.form['credit_history'])
        property_area = flask.request.form['property_area']

        output_dict = {
            'Applicant Income': applicantIncome,
            'Co-Applicant Income': coapplicantIncome,
            'Loan Amount': loan_amnt,
            'Loan Amount Term': term_d,
            'Credit History': credit_history,
            'Gender': genders_type,
            'Marital Status': marital_status,
            'Education Level': education_status,
            'No of Dependents': dependents,
            'Self Employment': self_employment,
            'Property Area': property_area
        }

        x = np.zeros(21)
        x[0] = applicantIncome
        x[1] = coapplicantIncome
        x[2] = loan_amnt
        x[3] = term_d
        x[4] = credit_history

        pred = clf_lr.predict([x])[0]
        
        if pred == 1:
            res = '🎉 Your Loan Application has been Approved!'
        else:
            res = '🙁 Your Loan Application has been Not Approved.'

        return flask.render_template(
            'Loan_Application.html',
            original_input=output_dict,
            result=res
        )

if __name__ == '__main__':
    app.run(debug=True)
