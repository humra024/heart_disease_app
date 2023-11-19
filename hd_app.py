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
    
    url = 'https://public.tableau.com/shared/MB93XXTDN?:display_count=n&:origin=viz_share_link'

    if st.button('Heart Disease Dashboard'):
        # webbrowser.open_new_tab(url)
        link = 'https://public.tableau.com/shared/MB93XXTDN?:display_count=n&:origin=viz_share_link'
        st.markdown(link, unsafe_allow_html=True)
    
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
    
    age = st.text_input("Age","")
    sex = st.text_input("Sex")
    cp = st.text_input("Chest Pain Type","")
    trestbps = st.text_input("Trestbps","")
    chol = st.text_input("Cholestrol","")
    fbs = st.text_input("FBS","")
    restecg = st.text_input("RestECG","")
    thalach = st.text_input("Thalach","")
    exang = st.text_input("Exange","")
    oldpeak = st.text_input("Oldpeak","")
    slope = st.text_input("Slope","")
    ca = st.text_input("CA","")
    thal = st.text_input("Thal","")
    
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
