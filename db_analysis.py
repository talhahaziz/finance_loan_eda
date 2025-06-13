from db_utils import RDSDatabaseConnector
from data_transform import DataTransform
from data_frame_info import DataFrameInfo
from DataFrameTransform import DataFrameTransform
from plotter import Plotter
import pandas as pd

def main():
    
    df = pd.read_csv("loan_payments.csv")

    transform = DataTransform(df)  # Load the CSV file into a DataFrame
    transform.check_data_types()  # Check the data types of the DataFrame
    
    info = DataFrameInfo(df)

   


def connection():
    connector = RDSDatabaseConnector("credentials.yaml") #despite only needing the load_data from the class, the class still needs to be initialised with the credentials 
    loading_csv = connector.load_data("loan_payments.csv") # Now i can call the load.data() function and pass the file i want to load 
    print(f" No. of rows: No. of columns {loading_csv.shape}") #This will tell me the amount of rows and columns in the data respectively 
    print(loading_csv.head(10)) #This will print the first 10 fields(columns), first and last 4 records(rows) because there's so may rows it will miss out everything in between

if __name__ == "__main__":
    main()