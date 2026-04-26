
import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# load model
model = pickle.load(open('model_lr.pkl','rb'))

# give title
st.title("Student Grade Prediction")

gender = st.selectbox('Gender',('male','female'))
Attendance = st.number_input('Attendance',min_value=50.0 , max_value=100.0,value=85.0)
StudyHours = st.number_input('StudyHours',min_value=1.0 , max_value=24.0,value=10.0)
PreviousGrade = st.number_input('PreviousGrade',min_value=33.0 , max_value=100.0,value=80.0)
ExtracurricularActivities = st.number_input('ExtracurricularActivities',min_value=0.0 , max_value=3.0,value=1.0)
parentalSupport = st.selectbox('ParentalSupport',('High','Medium','Low'))
onlineClassesTaken = st.selectbox('Online Classes Taken',('True','False'))


# encoding

# smoker
OnlineClassesTaken = 1 if onlineClassesTaken=='True' else 0
# gender
Gender	= 1 if gender=='male' else 0
# region
ParentalSupport_dict ={'Low':0,'Medium':1,'High':2}
ParentalSupport = ParentalSupport_dict[parentalSupport]

# dataframe
input_features = pd.DataFrame({
    'Gender':[Gender],
    'Attendance':[Attendance],
    'StudyHours':[StudyHours],
    'PreviousGrade':[PreviousGrade],
    'ExtracurricularActivities':[ExtracurricularActivities],
    'ParentalSupport':[ParentalSupport],
    'OnlineClassesTaken':[OnlineClassesTaken]

})

# predictions
if st.button('Predict'):
  predictions=model.predict(input_features)
  st.success(f"Price Prediction: {predictions}")