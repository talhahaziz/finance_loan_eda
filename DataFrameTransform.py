import pandas as pd


#This file is being used to impute null values, drop columns with high null values and count null values in the df

class DataFrameTransform:

    def __init__(self, df):
        """
        Args:
            df: pandas DataFrame
        """
        self.df = df

    def count_null(self):
        """
        prints df with null count and percentage for each column
        """

        null_count = self.df.isnull().sum()
        null_percent = self.df.isnull().mean() * 100
        result = pd.DataFrame(f"null count is: {null_count}, null percentage is: {null_percent}")
        return result
    
    def drop_columns(self, threshold=30.0):
        """
        Drops columns where percentage of null values exceeds the threshold.

        Args:
            threshold: percentage (0-100) above which a column will be dropped
        """
        null_percent = self.df.isnull().mean() * 100
        cols_to_drop = null_percent[null_percent > threshold].index
        self.df.drop(columns=cols_to_drop, inplace=True)
        print(f"Dropped columns (>{threshold}% NULLs): {list(cols_to_drop)}")

    def impute_null(self, method="median"):
        """
        Inputes null values in the DataFrame using the specified method.
        
        Args:
            method (str): Method to use for imputing null values. Options are 'mean', 'median', 'mode'.
        """
        
        for col in self.df.select_dtypes(include=['float64', 'int64']).columns:
            if method == "mean":
                value = self.df[col].mean()
            elif method == "median":
                value = self.df[col].median()
          
            else:
                raise ValueError("Invalid method. Use 'mean', 'median")
            self.df[col].fillna(value, inplace=True)
            print(f"Null values in column {col} replaced with {method} value: {value}")