import pickle
import streamlit as st
import numpy as np
import plotly.figure_factory as ff
from streamlit_option_menu import option_menu


# loading the saved models

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:

    selected = option_menu('Disease Prediction System',

                          ['Home', 'Heart Disease Prediction'],
                          icons=['house', 'heart'],
                          default_index=0)

# Heart Disease Prediction Page
if (selected == 'Home'):
    st.title('Heart Disease Prediction')
    col1, col2 = st.columns((2,1))
    with col1:
        st.write("Heart disease are the leading cause of death globally, taking an estimated 17.9 million lives each year. Heart attacks account for 28% deaths in India\n")
        st.write("For every 1 lakh people there are 209 people who are dying out of Heart Disease. Early and accurate predictions and immediate diagnosis can help you live longer and happier.")
        st.write("Balanced diet and physical activity can keep your heart more healtier. Start taking care of your heart before it falls apart.")
        st.image("healthy-heart.jpg")
        
    with col2: 
        st.image("doctor.jpg")
        st.image("desktop-wallpaper-cardio-cardiology.jpg", width = 200)
        
        
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        options = {
            'Male': 1,
            'Female': 0
        }
        sex = st.selectbox('Gender', list(options.keys()))

    with col3:
        options = {
            'typical angina': 0,
            'atypical angina': 1,
            'non-anginal pain': 2,
            'asymptomatic': 3
        }
        cp = st.selectbox('Chest Pain types', list(options.keys()))

    with col1:
        trestbps = st.text_input('Resting Blood Pressure 90-200')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl 100-600')

    with col3:
        options = {
            '>120 mg/dl': 1,
            '<120 mg/dl': 0
        }
        fbs = st.selectbox('Fasting Blood Sugar', list(options.keys()))
    with col1:
        options = {
            'normal': 0,
            'ST-T wave abnormality': 1,
            'left ventricular hypertrophy': 2
        }
        restecg = st.selectbox('Resting Electrocardiographic results', list(options.key()))

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved 60 - 220')

    with col3:
        options = {
            'yes': 1, 
            'no': 0
        }
        exang = st.selectbox('Exercise Induced Angina', list(options.key()))

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise 0 - 6')

    with col2:
        options = {
            'upsloping': 0,
            'flat': 1, 
            'downsloping': 2
        }
        slope = st.selectbox('Slope of the peak exercise ST segment', list(options.keys()))

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy 0 - 3')

    with col2:
        options = {
            'error': 0,
            'fixed defect': 1,
            'normal': 2,
            'reversable defect': 3
        }
        thal = st.selectbox('thal', list(options.keys()))

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          

        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
