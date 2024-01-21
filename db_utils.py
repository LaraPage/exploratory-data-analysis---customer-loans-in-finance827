import yaml
from sqlalchemy import create_engine
import pandas as pd



# Extract loan payments data from  RDS database.
class RDSDatabaseConnector:

    # load credentials.yaml file and extract credentials.
    def load_credentials(file_path='credentials.yaml'):
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    
    # Initialising a SQLalchemy engine using the credentials
    def __init__engine(self, configuration_file_path):
        credentials = self.load_credentials(configuration_file_path)
        engine = create_engine(f"postgresql+psycopg2://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
        return engine.connect()
    
    #Extract data from the 'loan payments' table and return it as a Pandas DataFrame
    def extract_loan_payments_data(self, engine):
        df = pd.read_sql_table(table_name="loan_payments", con=engine)
        return df
    
    # Save the Pandas DataFrame as a .csv file
    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")

    # Load data from a .csv file into a Pandas DataFrame
    def load_data_to_dataframe(self, file_path):
        df = pd.read_csv(file_path)
        print(f"Data loaded from {file_path}")
        print(f"DataFrame shape: {df.shape}")
        return df


import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:

    def load_credentials(self, file_path='C:/Users/Lara/.vscode/EDA_project_customer_loans_in_finance/milestone_1/credentials.yaml'):
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    def __init__(self, configuration_file_path):
        credentials = self.load_credentials(configuration_file_path)
        self.engine = create_engine(f"postgresql+psycopg2://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")

    def extract_loan_payments_data(self):
        df = pd.read_sql_table(table_name="loan_payments", con=self.engine)
        return df

    def save_to_csv_file(self, df, file_path):
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")

    def load_data_to_dataframe(self, file_path):
        df = pd.read_csv(file_path)
        print(f"Data loaded from {file_path}")
        print(f"DataFrame shape: {df.shape}")
        return df

if __name__ == "__main__":
    db_conn = RDSDatabaseConnector('credentials.yaml')
    df = db_conn.extract_loan_payments_data()
    print(df)
    