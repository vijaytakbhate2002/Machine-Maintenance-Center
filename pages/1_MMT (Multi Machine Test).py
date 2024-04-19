import pandas as pd
import logging
import streamlit as st
from typing import Union
import joblib
import os

st.subheader("Multi Machine Test", divider='rainbow')

def uploader() -> None:
    CSV_PATH = "app_data\\user.csv"
    csv_file = st.file_uploader("Upload csv file")
    
    if csv_file is not None:
        with open(CSV_PATH, "wb") as f:
            f.write(csv_file.read())
        df = pd.read_csv(CSV_PATH)
    
    if os.path.exists(CSV_PATH):
        st.markdown("<h3 style='font-size: 24px;'>Uploaded CSV</h3>", unsafe_allow_html=True)
        df = pd.read_csv(CSV_PATH)
        st.write(df.head())

class CsvPrediction:
    """Args: csv_path
        (this class will do all processes required before prediction 
        after data processing it will predict classes of given csv file and return pandas df)
        Return: Dataframe or None"""
    
    # features = joblib.load("model_building\\params\\columns.pkl")
    features = ['Type', 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    encoder = joblib.load("model_building\\params\\encoder.pkl")
    model = joblib.load("model_building\\models\\rfc_98.pkl")

    def __init__(self, csv_path:str) -> None:
        """"constructor which get csv file path as parameter"""
        self.csv_path = csv_path

    def read_csv(self) -> Union[pd.DataFrame, None]:
        """Args: None 
            (this fucntion reads csv file)
            Return: Dataframe or None"""
        try:
            df = pd.read_csv(self.csv_path)
            return df
        except Exception as e:
            logging.error(e)
            return None

    def feature_selection(self, df:pd.DataFrame) -> Union[pd.DataFrame, None]:
        """Args: None
            (this fucntion helps to get only required columns from whole df
            and these columns are arranged similarly as arranged while model training)
            Return: Dataframe or None"""
        
        global extra_cols
        extra_cols = df[[x for x in df.columns if x not in self.features]]
        if df is not None:
            try:
                return df[self.features]
            except:
                logging.error("feature_selection error")
                st.error(f"Missing required columns, required_columns = {self.features}")
        else:
            return None

    def process_data(self, df:pd.DataFrame) -> pd.DataFrame:
        """ Args: None
            (this function does label encoding process)
            Return: Dataframe or None"""
        
        df['Type'] = self.encoder.fit_transform(df['Type'])
        return df

    def prediction(self, df:pd.DataFrame) -> pd.DataFrame:
        """Args: None
            (predicting output and adding predicted column to df with reverse labeling)
            Return: Dataframe or None"""
        
        temp = self.model.predict(df)
        predictions = []
        for val in temp:
            if val == 0:
                predictions.append('pass')
            elif val == 1:
                predictions.append('fail')
            else:
                predictions.append(None)
        df['predictions'] = predictions
        df = pd.concat([extra_cols, df], axis='columns')
        return df

    def manager(self) -> str:
        """Args: None
            (this function manages all process step by step)
            Return: Dataframe or None"""
        
        df = self.read_csv()
        if df is not None:
            df = self.feature_selection(df=df)
            if df is not None:
                df = self.process_data(df=df)
                if df is not None:
                    df = self.prediction(df=df)
                    return df
                else:
                    logging.error("prediction function returned None")
            else:
                logging.error("process_data function returned None")
        else:
            logging.error("feature_selection function returned None")

class BunchPrediction:
    USER_FILE_PATH = "app_data\\user.csv"
    PREDICTED_FILE_PATH = "app_data\\predicted.csv"

    def CSV_file_process(self)-> Union[pd.DataFrame, None]:
        """ Args: no any
            (this function predicts for all data points from csv and return df with added column 'predictions')
            Return: dataframe or none """
        obj = CsvPrediction(self.USER_FILE_PATH)
        df = obj.manager()
        return df

    def csv_view(self, df:pd.DataFrame) -> None:
        """ Args: df
            (This function saves csv and shows it on web interface)
            Return: None """
        
        failed_df = df[df['predictions'] == 'fail']
        passed_df = df[df['predictions'] == 'pass']
        col1, col2 = st.columns(2)
        col1.markdown("<h3 style='font-size: 24px;'>Failed Machines</h3>", unsafe_allow_html=True)
        col1.write(failed_df)
        col2.markdown("<h3 style='font-size: 24px;'>Passed Machines</h3>", unsafe_allow_html=True)
        col2.write(passed_df)

        st.markdown("<h3 style='font-size: 24px;'>CSV with predictions</h3>", unsafe_allow_html=True)
        df.to_csv(self.PREDICTED_FILE_PATH)
        st.write(df)


    def manager(self) -> None:
        """Args: no any
            (centrealized process function)
            Return: None"""
        uploader()
        df = self.CSV_file_process()
        if df is not None:
            self.csv_view(df)
        else:
            logging.warning(F"{self.PREDICTED_FILE_PATH} not found")

if __name__ == '__main__':
    obj = BunchPrediction()
    obj.manager()
