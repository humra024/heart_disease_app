import sklearn
# print(sklearn.__version__) 1.22 required here and in model file
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv('heart_disease.csv')
data=data.drop_duplicates()

categorical_val=[] #categorical columns
continuous_val=[] #numerical columns

for column in data.columns:
    if data[column].nunique()<=10:  #if no. of unique values < 10
        categorical_val.append(column)
    else:
        continuous_val.append(column)
        
data['cp'].unique()
categorical_val.remove('sex') #only 0 and 1 value so encoding not required
categorical_val.remove('target') #for sex and target column
# data=pd.get_dummies(data, columns=categorical_val, drop_first=True) 

st=StandardScaler()
data[continuous_val]=st.fit_transform(data[continuous_val]) 

X=data.drop('target', axis=1)
y=data['target']
print(X.shape)

rf=RandomForestClassifier()
rf.fit(X,y)

pickle.dump(rf,open('model_hd.pkl','wb'))


new_data=pd.DataFrame({
    'age':52,
    'sex':1,
    'cp':0,
    'trestbps':125,
    'chol':212,
    'fbs':0,
    'restecg':1,
    'thalach':168,
    'exang':0,
    'oldpeak':1.0,
    'slope':2,
    'ca':2,
    'thal':3
    
    # 'age':58,
    # 'sex':0,
    # 'cp':0,
    # 'trestbps':100,
    # 'chol':248,
    # 'fbs':0,
    # 'restecg':0,
    # 'thalach':122,
    # 'exang':0,
    # 'oldpeak':1.0,
    # 'slope':1,
    # 'ca':0,
    # 'thal':2
},index=[0])

p=rf.predict(new_data)
if p[0]==0:
    print("No Heart Diseases")
else:
    print("Possibility of Heart Diseases")
