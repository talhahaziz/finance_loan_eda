import yaml
import pandas as pd 
from sqlalchemy import create_engine, text

def load_credentials(filepath ="credentials.yaml"):
    with open(filepath, 'r') as f:
        db_dict = yaml.safe_load(f)
    
    return db_dict

class RDSDatabaseConnector:

    def __init__(self, credentials: str):
        """
        Initialising the database connector with the connector dict 
        """
        self.credentials = load_credentials(credentials)

    def init_db_engine(self):
        """
        intialise SQLAlchemy engine to connect to database      
        """
        engine = create_engine(f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}"
            f"@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}")
        
        return engine
    
    def extract_data(self):
        """
        Extracts data from the loan_payments table
        Returns:
            pandas.DataFrame: The extracted data
        """
        engine = self.init_db_engine()
        query = "SELECT * FROM loan_payments"

        print("connectin to database..")
        extract = pd.read_sql(query, engine)

        print("successfully extracted the data.")
        return extract
    
    def save_data(self, df, filename ='loan_payments.csv'):

        try:
            df.to_csv(filename, index=False)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

if __name__ == "__main__":
        
    connector = RDSDatabaseConnector("credentials.yaml")
    loan_data = connector.extract_data()