import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('bank_marketing.joblib')

st.title(':bank: Bank Marketing Prediction App')
st.write('Please input the data for prediction:')
age = st.number_input('Age', min_value=0, max_value=100, step=1)
job = st.selectbox('Select Job', options=["blue-collar", "services", "admin.", "entrepreneur", "self-employed", "technician", "management", "student", "retired", "housemaid", "unemployed"])
marital = st.selectbox('Select Marital Status', options=["married", "single", "divorced"])
education = st.selectbox('Select Education', options=["basic.9y", "high.school", "university.degree", "professional.course", "basic.6y", "basic.4y", "illiterate"])
default = st.selectbox('Select Has Credit in Default?', options=["no", "yes"])
housing = st.selectbox('Select Has Housing Loan?', options=["no", "yes"])
loan = st.selectbox('Select Has Personal Loan?', options=["no", "yes"])
contact = st.selectbox('Select Contact Communication Type', options=["cellular", "telephone"])
month = st.selectbox('Select Last Contact Month', options=["may", "jun", "nov", "sep", "jul", "aug", "mar", "oct", "apr", "dec"])
day_of_week = st.selectbox('Select Last Contact Day of the Week', options=["mon", "tue", "wed", "thu", "fri"])
campaign = st.number_input('Enter Number of Contacts Performed', min_value=0, step=1)
emp_var_rate = st.number_input('Enter Employment Variation Rate')
cons_price_idx = st.number_input('Enter Consumer Price Index')
cons_conf_idx = st.number_input('Enter Consumer Confidence Index')
euribor3m = st.number_input('Enter Euribor 3 Month Rate')
nr_employed = st.number_input('Enter Number of Employees')

def predict():
    if marital== 'married':
        marital1=1
    elif marital=='single':
        marital1=2
    elif marital=='divorced':
        marital1=0
    else:
        marital1=3
       
       
    if job=='admin':
        job1=0
    elif job=='bluecollar':
        job1=1
    elif job=='technician':
        job1=9
    elif job=='services':
        job1=7
    elif job=='management':
        job1=4
    elif job=='retired':
        job1=8
    elif job=='entrepreneur':
        job1=5
    elif job=='selfemployed':
        job1=6
    elif job=='housemaid"':
        job1=2
    elif job=='unemployed':
        job1= 3     
    else:
        job1=1

    if education=='universitydegree':
        education1=6
    elif education=='highschool':
        education1=3
    elif education=='basic9y':
        education1=5
    elif education=='professionalcourse':
        education1=2
    elif education=='basic.4y':
        education1=0
    elif education=='basic6y':
        education1=1
    else:
        education1=4

    if contact=='telephone':
        contact1=1
    else:
        contact1=0

    if housing =='yes':
        housing1=0
    else:
        housing1=1

    if default=='yes':
        default1=1
    else:
        default1=0

    if loan=='yes':
        loan1=1
    else:
        loan1=0

    if month=='may':
        month1=6
    elif month=='jul':
        month1=3
    elif month=='aug':
        month1=1
    elif month=='jun':
        month1=4
    elif month=='nov':
        month1=7
    elif month=='apr':
        month1=0
    elif month=='oct':
        month1=8
    elif month=='sep':
        month1=5
    elif month=='mar':
        month1=9
    else:
        month1=2


    if day_of_week=='thu':
        day_of_week1=2
    elif day_of_week=='mon':
        day_of_week1=1
    elif day_of_week=='wed':
        day_of_week1=3
    elif day_of_week=='tue':
        day_of_week1=0
    else:
        day_of_week1=4


    cols = pd.DataFrame([{'age':age, 'job':job1, 'marital':marital1,'education':education1,'default':default,'housing':housing, 'loan':loan, 'contact':contact1,
                          'month': month1,  'day_of_week': day_of_week1, 'campaign': campaign,
                          'emp_var_rate':emp_var_rate, 'cons_price_idx':cons_price_idx, 'cons_conf_idx':cons_conf_idx,'euribor3m': euribor3m,'nr_employed':nr_employed}], index=[0])
       
    prediction = model.predict(cols)
   
    if prediction[0] == 1:
        st.success('This person can take bank deposit')
    else:
        st.error('This person do not take bank deposit')

trigger = st.button('Predict', on_click=predict)
