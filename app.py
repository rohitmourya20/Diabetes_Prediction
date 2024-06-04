import streamlit as st
import numpy as np
import pickle

# loading the trained model
model = pickle.load(open('diabetes_model.pkl','rb'))

# Streamlit UI 
st.title('Diabetes Prediction')

# Input fields for user to enter data 
preg = st.number_input('Pregnancies',0,20)
glu = st.number_input('Glucose',0,200)
bp = st.number_input('Blood Pressure',0,150)
skin_thick = st.number_input('Skin Thickness',0,100)
insulin = st.number_input('Insulin',0,900)
bmi = st.number_input('BMI',0.0,70.0)
dpf = st.number_input('Diabetese Pedigree Function',0.0,2.5)
age = st.number_input('Age',0,120)

# When user click the button
if st.button('Predict'):
    user_data = np.array([[preg,glu,bp,skin_thick,insulin,bmi,dpf,age]])
    prediction = model.predict(user_data)

    if prediction[0]==1:
        st.write('The model predict you have diabetes.')
    else:
        st.write("The model predict you don't have diabetes.")