import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        return pd.read_csv(self.file_path)

    def load_json(self):
        return pd.read_json(self.file_path)

    def load_excel(self):
        return pd.read_excel(self.file_path)

    def preprocess_data(self, df):
        # Placeholder for data preprocessing steps
        df.dropna(inplace=True)
        return df

# Example usage
# data_loader = DataLoader('your_dataset.csv')
# df = data_loader.load_csv()
# preprocessed_df = data_loader.preprocess_data(df)