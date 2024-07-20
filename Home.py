import streamlit as st
import joblib
import base64
from config import config

MODEL_PATH = "model_building\\models\\rfc_98.pkl"
model = joblib.load(MODEL_PATH)

st.header("Machine Maintenance Center", divider='rainbow')

def main_web() -> None:
    """ Args: no any
        (this function helps to present widest section of webpage, It initialize four buttons
        of basic information about project and developer contact details)
        Return: None"""
    
    st.markdown("<h3 style='font-size: 24px;'>Project and Developer information</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)  
    with  col1.expander(label='Project information'): 
        markdown_text = """
        ## Introduction
        This is a predictive maintenance application that has a binary classification of the failure status of the machine. 
        This streamlit application is built for single- and multiple-machine failure detection work. MMT represents Multi Machine Test and SMT represents Single Machine Test.

        ## Dataset Details
        - **Number of Data Points:** 10,000
        - **Features:** 14
        - **UID:** Unique identifier ranging from 1 to 10,000
        - **productID:** Consists of letters L, M, or H indicating low (50%), medium (30%), and high (20%) product quality variants, along with a variant-specific serial number
        - **air temperature [K]:** Generated using a random walk process, normalized to a standard deviation of 2 K around 300 K
        - **process temperature [K]:** Generated using a random walk process, normalized to a standard deviation of 1 K, added to the air temperature plus 10 K
        - **rotational speed [rpm]:** Calculated from power of 2860 W, overlaid with normally distributed noise
        - **torque [Nm]:** Normally distributed around 40 Nm with standard deviation = 10 Nm, no negative values
        - **tool wear [min]:** Quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process
        - **Machine Failure Label:** Indicates whether the machine has failed in this particular data point
        """
        st.markdown(markdown_text)

    with  col2.expander(label='Visuals'):
        images = ["static\\newplot.png", "static\\newplot (1).png", "static\\newplot (2).png", "static\\newplot (3).png", "static\\newplot (4).png"]
        st.image("static\\newplot (1).png")
        st.image("static\\newplot (2).png")
        st.image("static\\newplot (3).png")
        st.image("static\\newplot (4).png")

    with  col2.expander(label='Contact details'): 
        contacts_info = """
        Contacts:
        - **Name:** Vijay Dipak Takbhate
        - **Email:** [vijaytakbhate20@gmail.com](mailto:vijaytakbhate20@gmail.com)

        Work Profiles:
        - **LinkedIn:** [Vijay Takbhate](https://www.linkedin.com/in/vijay-takbhate-b9231a236/)
        - **Github:** [vijaytakbhate2002](https://github.com/vijaytakbhate2002/Microsoft-Machine-Failure-Detection.git)
        - **Kaggle:** [vijay20213](https://www.kaggle.com/vijay20213)
        """
        st.markdown(contacts_info)

    with  col1.expander(label='Resume'):
        pdf_file_path = config.RESUME
        def read_pdf_file(pdf_file_path):
            with open(pdf_file_path, "rb") as file:
                pdf_contents = file.read()
            return base64.b64encode(pdf_contents).decode("utf-8")

        encoded_pdf = read_pdf_file(pdf_file_path)
        st.markdown(f'<embed src="data:application/pdf;base64,{encoded_pdf}" width="700" height="1000"></embed>', unsafe_allow_html=True)


if __name__ == '__main__':
    main_web()
