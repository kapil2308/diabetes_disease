import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('trained_model.sav','rb'))
#creating function
def diabetes_pred(imput):
     #imput=([[5,166,72,29,175,25.8,0.587,51]])
     pred=loaded_model.predict([imput])
     print(pred)
     if pred[0]==0:
                return'the person not diabetic'
     else:
                return'person is diabetic'

def main():
    #giving title
    st.title('Diabetes Prediction Web')
    #getting input from the user
    Pregnancies=st.text_input('Enter the Month of Pregnancies')
    Glucose=st.text_input('Enter the Glucose Level')
    BloodPressure=st.text_input('Enter the BloodPressure')
    SkinThickness=st.text_input('Enter the SkinThickness')
    Insulin=st.text_input('Enter the Insulin Level')
    BMI=st.text_input('Enter the BMI Value')
    DiabetesPedigreeFunction=st.text_input('Enter the DiabetesPedigreeFunction')	
    Age=st.text_input('Enter the Age')
    
    #code for prediction
    diagnosis=''
    #creating button
    if st.button('Diabetes Test Result'):
                diagnosis=diabetes_pred([ Pregnancies, Glucose,BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
if __name__ =='__main__':
                main()