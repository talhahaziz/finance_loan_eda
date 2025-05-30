import matplotlib.pyplot as plt

class Plotter:

    def __init__(self, df):

        self.df =df

    def plot_nulls(self, title='Null Values per Column'):
        """
        Plots the number of null values in each column of the DataFrame.
        
        Args:
            title (str): Title of the plot.
        """
        null_counts = self.df.isnull().sum()
        null_counts = null_counts[null_counts > 0]

        if null_counts.empty:
            print("no nulls were found")
            return
        
        null_counts.plot(kind='bar', color='skyblue')
        plt.title(title)
        plt.xlabel('Columns')
        plt.ylabel('Null Count')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
