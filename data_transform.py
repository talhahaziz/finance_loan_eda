import pandas as pd 
import numpy as np 
from datetime import datetime 

#this file will be used to transform the data 


class DataTransform:

    def __init__(self, df):
        '''
        Initialize with a DataFrame to be transformed
        
        Args:
            df: pandas DataFrame containing loan payment data
        '''
        self.df = df.copy() #creates a copy of the df so the original is not modified

    
    def check_data_types(self):
        print("Current data types:")
        print(self.df.dtypes)

        return self

    def convert_to_datetime(self, column: str, date_format: str):
        """
        Converts a column to datetime format.

        Args:
            column (str): The name of the column to convert.
            date_format (str, optional): The format of the date in the column. Defaults to None.
        """
        try:
            self.df[column] = pd.to_datetime(self.df[column], format=date_format, errors="coerce")
            print(f"column labelled {column} has successfully been converted to datetime.")
        except Exception as e:
            print(f"Error converting the {column} to datetime: {e} ")

    def convert_to_numeric(self, column: str):
        """
        Converts a column to numeric format.
        Args:
            column (str): The name of the column to convert.
        """
        try:
            self.df[column] = pd.to_numeric(self.df[column], errors="coerce")
            print(f"successfully converted the {column} column values to numeric integeres")
        except Exception as e:
            print(f"Error converting the {column} into integer: {e}")

    def remove_symbol(self, column: str, symbol: str):
        """
        Removes symbols from the column 

        Args:
            colums(str): the name of the column i want to remove the symbol from
            symbol(str): the symbol i want to remove
        """
        try:
            self.df[column] = self.df[column].astype(str).str.replace(symbol, '', regex=False) #incase the column type is numeric (float/int) the astype will convert it into a string
            print(f"successfully removed '{symbol}' from the {column} column")
        except Exception as e:
            print(f"Error removing the '{symbol}' from the {column} column: {e}")

    def to_category(self, *columns):
        """
        converts specified columns to a category 
        """

        for column in columns:
            try:
                self.df[columns] = self.df[column].astype("category")
            except Exception as e:
                print(f"failed to specify categorise '{column}': {e}")
            

    def to_Int(self, column):
        """
        Converts specified columns to integer format, coercing errors to NaN.

        Args:
            column: Column names to be converted to integer.
        """
        try:
            self.df[column] = pd.to_numeric(self.df[column], errors="coerce").astype("Int64")
        except Exception as e:
            print(f"error converting {column} to integer : {e}")

    def summary(self) -> None:
        """
        Prints a summary of the DataFrame including data types and missing values.
        """
        print("DataFrame Summary:")
        print(self.df.info())
        print("\nMissing Values:")
        print(self.df.isnull().sum())

