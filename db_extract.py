from db_utils import RDSDatabaseConnector
import pandas as pd



def main():
    connector = RDSDatabaseConnector("credentials.yaml")

    loading_csv = connector.load_data("loan_payments.csv")
    print({loading_csv.shape})
    print(loading_csv.head(10))

if __name__ == "__main__":
    main()