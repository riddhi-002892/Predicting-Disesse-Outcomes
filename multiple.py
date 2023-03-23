"""
Created on Wed Mar 22 13:26:24 2023

@author: ridhs
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


covid = pickle.load(open('covid.sav', 'rb'))

diabetes = pickle.load(open('diabetes.sav', 'rb'))

heart_disease = pickle.load(open('heart_disease.sav','rb'))

kidney_stone = pickle.load(open('kidney_stone.sav','rb'))

parkinsons = pickle.load(open('parkinsons_model.sav','rb'))





with st.sidebar:
    
    selected = option_menu('Disease List',
                          
                          ['Covid',
                           'Diabetes',
                           'Heart Disease',
                           'Kidney Stone',
                           'Parkinsons',],
                          icons=['person','activity','heart','activity','person',],
                          default_index=0)

# Covid
if (selected == 'Covid'):
    
    # page title
    st.title('Covid Predictor')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('**Age**')
        
    with col2:
        BMI = st.text_input('**BMI**')
        
    with col3:
        Diabetis = st.text_input('**Diabetis**')
    with col1:
        Cardio_Vascular_Diseases=st.text_input('**Cardio Vascular Diseases**')

    with col2:
        Sickle_cell_diesases = st.text_input('**Sickle Cell Diesases**')
        
    with col3:
        Immuno_deficiency_disease = st.text_input('**Immuno Deficiency Disease**')
        
    with col1:
        Down_syndrome = st.text_input('**Down Syndrome**')
        
    with col2:
        Cancer = st.text_input('**Cancer**')
        
    with col3:
        Chronic_Respiratory_disease = st.text_input('**Chronic Respiratory Disease**')
        
    with col1:
        Hypertension = st.text_input('**Hypertension**')
        
    with col2:
        Vaccinated = st.text_input('**Vaccinated**')
        
  
    covid_diagnosis = ''
    
    if st.button('Covid Test Result'):
        Covid_prediction = covid.predict([[age, BMI, Diabetis, Cardio_Vascular_Diseases,Sickle_cell_diesases, Immuno_deficiency_disease, Down_syndrome,Cancer,Chronic_Respiratory_disease,Hypertension,Vaccinated]])                          
        
        if (Covid_prediction[0] == 1):
          covid_diagnosis = 'Your Report is Covid Positive'
        else:
          covid_diagnosis = 'Your Report is Covid Negetive'
        
    st.success(covid_diagnosis)

#Diabetes
if (selected == 'Diabetes'):
    
    # page title
    st.title('Diabetes Predictor')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('**Number of Pregnancies**')
        
    with col2:
        Glucose = st.text_input('**Glucose Level**')
    
    with col1:
        BloodPressure = st.text_input('**Blood Pressure Value**')
    
    with col2:
        SkinThickness = st.text_input('**Skin Thickness Value**')
    
    with col1:
        Insulin = st.text_input('**Insulin Level**')
    
    with col2:
        BMI = st.text_input('**BMI Value**')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('**Diabetes Pedigree Function Value**')
    
    with col2:
        Age = st.text_input('**Age of the Person**')
    
    
    diab_diagnosis = ''
    
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'You are  Diabetic'
        else:
          diab_diagnosis = 'You are not Diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease
if (selected == 'Heart Disease'):
    
    # page title
    st.title('Heart Disease Predictor')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('**Age**')
        
    with col2:
        sex = st.text_input('**Sex**')
        
    with col3:
        cp = st.text_input('**Chest Pain Types**')
        
    with col1:
        trestbps = st.text_input('**Resting Blood Pressure**')
        
    with col2:
        chol = st.text_input('**Serum Cholestoral in (mg/dl)**')
        
    with col3:
        fbs = st.text_input('**Fasting Blood Sugar (>120 mg/dl)**')
        
    with col1:
        restecg = st.text_input('**Resting Electrocardiographic Results**')
        
    with col2:
        thalach = st.text_input('**Maximum Heart Rate Achieved**')
        
    with col3:
        exang = st.text_input('**Exercise Induced Angina**')
        
    with col1:
        oldpeak = st.text_input('**ST Depression Induced by Exercise**')
        
    with col2:
        slope = st.text_input('**Slope Peak Exercise ST Segment**')
        
    with col3:
        ca = st.text_input('**Major Vessels Colored by Flourosopy**')
        
    with col1:
        thal = st.text_input('**Thal:   0 = Normal, 1 = Fixed Defect, 2 = Reversable Defect**')
        
        
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'You have heart disease'
        else:
          heart_diagnosis = 'You don"t have any heart disease'
        
    st.success(heart_diagnosis)
        
#kidney_stone
# kidney stone  Prediction Page
if (selected == 'Kidney Stone'):
    
    # page title
    st.title('Kidney Stone Predictor')
    
    col1, col2 = st.columns(2)
    
    with col1:
        gravity = st.text_input('**Gravity**')
        
    with col2:
        ph = st.text_input('**PH Level**')
    with col1:
        osmo=st.text_input('**Osmo**')

    with col2:
        cond= st.text_input('**Cond**')
        

    with col1:
        urea = st.text_input('**Urea**')
        
    with col2:
        calc = st.text_input('**Calc**')
    
    kidney_stone_diagnosis = ''
    
    
    if st.button('Kidney Stone Test Result'):
        kidney_stone_prediction = kidney_stone.predict([[gravity, ph, osmo, cond,urea, calc]])                          
        
        if (kidney_stone_prediction[0] == 1):
          kidney_stone_diagnosis = 'The person has kidney stone'
        else:
          kidney_stone_diagnosis = 'The person doesnot have a kidney stone'
        
    st.success(kidney_stone_diagnosis)
    
    
    
        
# Parkinson's
if (selected == "Parkinsons"):
    
    st.title("Parkinson's Predictor")
    
    col1, col2, col3, col4 = st.columns(4)  
    
    with col1:
        fo = st.text_input('**MDVP:Fo(Hz)**')
        
    with col2:
        fhi = st.text_input('**MDVP:Fhi(Hz)**')
        
    with col3:
        flo = st.text_input('**MDVP:Flo(Hz)**')
        
    with col4:
        Jitter_percent = st.text_input('**MDVP:Jitter(%)**')
        
    with col1:
        Jitter_Abs = st.text_input('**MDVP:Jitter(Abs)**')
        
    with col2:
        RAP = st.text_input('**MDVP:RAP**')
        
    with col3:
        PPQ = st.text_input('**MDVP:PPQ**')
        
    with col4:
        DDP = st.text_input('**Jitter:DDP**')
        
    with col1:
        Shimmer = st.text_input('**MDVP:Shimmer**')
        
    with col2:
        Shimmer_dB = st.text_input('**MDVP:Shimmer(dB)**')
        
    with col3:
        APQ3 = st.text_input('**Shimmer:APQ3**')
        
    with col4:
        APQ5 = st.text_input('**Shimmer:APQ5**')
        
    with col1:
        APQ = st.text_input('**MDVP:APQ**')
        
    with col2:
        DDA = st.text_input('**Shimmer:DDA**')
        
    with col3:
        NHR = st.text_input('**NHR**')
        
    with col4:
        HNR = st.text_input('**HNR**')
        
    with col1:
        RPDE = st.text_input('**RPDE**')
        
    with col2:
        DFA = st.text_input('**DFA**')
        
    with col3:
        spread1 = st.text_input('**Spread1**')
        
    with col4:
        spread2 = st.text_input('**Spread2**')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    parkinsons_diagnosis = ''
       
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


