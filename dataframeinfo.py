import pandas as pd 
from datatransform import DataTransform


class DataFrameInfo:

    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a DataFrame to get information about.
        
        Args:
            df: pandas DataFrame containing data
        """
        self.df = df

    def describe_columns(self):
        """
        Prints the description of each column in the DataFrame.
        """
        print("DataFrame Description:")
        print(self.df.info)

    def get_stats(self):
        """
        Prints basic statistics of the DataFrame.
        """
        stats = self.df.describe().T
        stats['median'] = self.df.median(numeric_only=True)
        print("DataFrame Statistics:")
        print(stats)

    def count_distinct(self):
        """
        Counts distinct values in each column of the DataFrame.
        """
        distinct_counts = self.df.nunique()
        print("Distinct Value Counts:")
        print(distinct_counts)

    def count_nulls(self):
        """
        Counts null values in each column of the DataFrame.
        """
        null_counts = self.df.isnull().sum()
        null_percentage = (self.df.isnull().mean()) * 100
        print(pd.DataFrame({"Count": null_counts, "Percentage": null_percentage}))

    def display_shape(self):
        """
        Displays the shape of the DataFrame.
        """
        print(f"DataFrame Shape: {self.df.shape}")

    
