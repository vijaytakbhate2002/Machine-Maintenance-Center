import numpy as np
import streamlit as st
from sklearn.base import ClassifierMixin
import logging
import joblib

st.subheader("Single Machine Test", divider='rainbow')
model = joblib.load("model_building\\models\\rfc_98.pkl")

def collection() -> list:
    """ Args: no any
        (collect required inputs from uer and return list of inputs)
        Return: list"""

    type_dict = {'L':0, 'M':1, 'H':2}
    type = st.selectbox(label='Enter Type: ',options=['L', 'M', 'H'])
    type = type_dict[type]
    air_temp = st.number_input(label="Air temperature: ", min_value=250.0, max_value=350.0)
    process_temp = st.number_input(label="Process temperature: ", min_value=250.0, max_value=350.0)
    rotational_speed = st.number_input(label="Rotational speed: ", min_value=1000, max_value=3000)
    torque = st.number_input(label="Torque: ", min_value=3, max_value=80)
    tool_wear = st.number_input(label="Tool wear: ", min_value=0, max_value=300)

    lis = [type, air_temp, process_temp, rotational_speed, torque, tool_wear]
    return lis

def single_prediction(model) -> str:
    """ Args: ClassifierMixin, list
        (this function helps to predict whether machine will fail or not)
        return: None """
    x = collection()
    x = np.array(x).reshape((1, -1))
    predicted_val = model.predict(x)
    if predicted_val == 1:
        return 'fail'
    elif predicted_val == 0:
        return 'no fail'
    else:
        logging.warning("predict function got warning")
        logging.warning("predcited_val is None expecting 0 or 1")
        return None
    
if __name__ == '__main__':
    res = single_prediction(model=model)
    with st.expander(label="predict"):
        if res == 'no fail':
            st.success('The machine is in best condition.')
        else:
            st.error('Alert! need to maintain the machine')
