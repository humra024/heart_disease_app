import pandas as pd
import numpy as np
import warnings
from sklearn.ensemble import RandomForestClassifier as rf
import streamlit as st
import pickle
model=pickle.load(open('model_hd.pkl','rb'))
import webbrowser

# from sklearn.exceptions import InconsistentVersionWarning 
# warnings.simplefilter("error", InconsistentVersionWarning)

# try:
#     est = pickle.loads("model_pickle.pickle")
# except InconsistentVersionWarning as w:
#     print(w.original_sklearn_version)


# import joblib
# loaded_rf = joblib.load("model_joblib_heart")

def predict_heart(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    input=np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    prediction=model.predict(input)
    # pred='{0:.{1}f}'.format(prediction[0][0], 2)
    # return float(pred)
    return prediction


def main():
    st.title("Heart Disease Analysis and Prediction")
    html_temp = """
    <div style="background-color:#e6005c ;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Prediction ML App </h2>
    </div>
    <br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    #url = 'https://public.tableau.com/shared/MB93XXTDN?:display_count=n&:origin=viz_share_link'

    #if st.button('Heart Disease Dashboard'):
    #    webbrowser.open_new_tab(url)
    st.subheader('Heart Disease Dashboard:')
    link = 'https://public.tableau.com/views/heart-diseasedashboard/HeartDiseaseDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'
    st.markdown(link, unsafe_allow_html=True)

    st.subheader('Heart Disease Prediction:')
    
    # 'age':52,
    # 'sex':1,
    # 'cp':0,
    # 'trestbps':125,
    # 'chol':212,
    # 'fbs':0,
    # 'restecg':1,
    # 'thalach':168,
    # 'exang':0,
    # 'oldpeak':1.0,
    # 'slope':2,
    # 'ca':2,
    # # 'thal':3
    
    
    age = st.text_input("Age",placeholder="Enter age")
    sex = st.selectbox("Sex",("Female","Male"))
    if sex=="Female":
        sex=0
    else:
        sex=1
    cp = st.selectbox("Chest Pain Type",("Typical Angina","Atypical Angina","Non Anginal Pain","Asymptomatic"))
    if cp=="Typical Angina":
        cp=0
    elif cp=="Atypical Angina":
        cp=1
    elif cp=="Non Anginal Pain":
        cp=2
    elif cp=="Asymptomatic":
        cp=3
    trestbps = st.number_input("Resting Blood Pressure (mmHg)",min_value=90,max_value=200)
    chol = st.number_input("Cholestrol (mg/dL)",min_value=120,max_value=570)
    fbs = st.selectbox("Fasting Blood Sugar",("Non-Diabetic","Diabetic"))
    if fbs=="Non-Diabetic":
        fbs=0
    else:
        fbs=1
    restecg = st.selectbox("Resting Electrocardiographic Results",("Normal","Abnormal ST-T wave","Left Ventricular Hypertrophy"))
    if restecg=="Normal":
        restecg=0
    elif restecg=="Abnormal ST-T wave":
        restecg=1
    else:
        restecg=2
    thalach = st.number_input("Maximum Heart Rate (bpm)",70,210)
    exang = st.selectbox("Exercise Induced Angina",("False","True"))
    if exang=="False":
        exang=0
    else:
        exang=1
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest",0.0,7.0)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment",('Upsloping','Horizontal','Downsloping'))
    if slope=="Upsloping":
        slope=0
    elif slope=="Horizontal":
        slope=1
    else:
        slope=2
    ca = st.selectbox("Number of Major Vessels (0-3) Colored by Flourosopy",(0,1,2,3,4))
    thal = st.selectbox("Thallium Scintigraphy",("Normal","Fixed","Reversible"))
    if thal=="Normal":
        thal=1
    elif thal=="Fixed":
        thal=2
    elif thal=="Reversible":
        thal=3
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
       </div>
    """
    if st.button("Predict"):
       
        try:
            age = int(age)
            sex = int(sex)
            cp = int(cp)
            trestbps = int(trestbps)
            chol = int(chol)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = int(thalach)
            exang = int(exang)
            oldpeak = float(oldpeak)
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)
        except ValueError:
            st.error("Please enter valid numerical values for input.")
            return
        
        
        output=predict_heart(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

        if output[0] == 0:
            st.success("No Heart Diseases")
        else:
            st.error("Possibility of Heart Diseases")
    
            
if __name__=='__main__':
    main()
