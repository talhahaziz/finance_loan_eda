from db_utils import RDSDatabaseConnector
import pandas as pd



def main():
    connector = RDSDatabaseConnector("credentials.yaml") #despite only needing the load_data from the class, the class still needs to be initialised with the credentials 
    loading_csv = connector.load_data("loan_payments.csv") # Now i can call the load.data() function and pass the file i want to load 
    print(f" No. of rows: No. of columns {loading_csv.shape}") #This will tell me the amount of rows and columns in the data respectively 
    print(loading_csv.head(10)) #This will print the first 10 fields(columns), first and last 4 records(rows) because there's so may rows it will miss out everything in between

if __name__ == "__main__":
    main()