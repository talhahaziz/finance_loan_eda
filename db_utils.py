import yaml
import pandas as pd 
from sqlalchemy import create_engine, text

def load_credentials(filepath ="credentials.yaml"):
    with open(filepath, 'r') as c:
        db_dict = yaml.safe_load(c)
    
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
    
    def save_data(self, df, file):

        try:
            df.to_csv(file, index=False)
            print(f"Data successfully saved to {file}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, file):
        ''' load the csv into dataframe
        
        Args:
            file: the path to the csv file that will be read

        returns:
            a dataframe containing data from the csv file
        '''
        with open(file, 'r') as f:
            df = pd.read_csv(f)

        return df

if __name__ == "__main__":
        
    connector = RDSDatabaseConnector("credentials.yaml")
    loan_data = connector.extract_data()