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
                          icons=['home', 'heart'],
                          default_index=0)

# Heart Disease Prediction Page
if (selected == 'Home'):
    st.title('Heart Disease Prediction')
    col1, col2 = st.beta_columns((2,1))
    with col1:
        st.write("Heart disease has been one of the leading cause of death since a past few years.\n")
        st.write("209 out of 1 lakh people are dying out of Heart Disease")
        st.write("Start taking care of your heart before it falls apart.")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("desktop-wallpaper-cardio-cardiology.jpg")
        with right_column:
            st.image("healthy-heart.jpg")
    with col2: 
        st.image("doctor.jpg")
        
        
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    
    # Group data together
    hist_data = [x1, x2, x3]
    
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    
    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])
    
    # Plot!
    st.plotly_chart(fig, use_container_width=True)


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
