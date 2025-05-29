## Finance-Loan-EDA

Exploratory Data Analysis of a customer loan portfolio to uncover trends, patterns, and risks within a financial institution. This project aims to support informed decisions on loan approvals, pricing, and risk management by using statistical and visualization techniques to improve portfolio performance and profitability.

# Task 1 - RDSDatabse Connector Setup

Created a 'credentials.yaml' file and included the AWS database RDS connection details. The RDSDatabase connector will use these to connect to the database securely.

### 🔧 Class Initialisation

1. Initiated the class RDSDatabaseConnector:

```python
class RDSDatabaseConnector:

    def __init__(self, credentials: str):
        """
        Initialising the database connector with the connector dict
        """
        self.credentials = load_credentials(credentials)
```

### ⚙️ Database Engine Setup

2. Created the `init_db_engine()`method which initialises SQAlchemy engine using the credentials from the YAML file and the following connection:

```python
engine = create_engine(f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}"
          f"@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}")
```

### 📥 Data Extraction

3. The `extract_data()` method handles the data extraction of the loan payment data from the RDSDatabase, Executed the SQL Query to select all records from the `loan_payments` table then used the `pd.read.sql()` function to load the query results into DataFrame the `return extract` will return the dataframe containing all the loan peyment records.

```python
def extract_data(self):
    engine = self.init_db_engine()
    query = "SELECT * FROM loan_payments"
    extract = pd.read_sql(query, engine)
    return extract
```

### 💾 Data Save & Loading

4. the `save_data()` method handles saving the data into a csv file on my local device the csv will then be used to load the data and query it to clean the data

```python
def load_data(self, file):
    with open(file, 'r') as f:
        df = pd.read_csv(f)

    return df
```

# Task 2 - Exploratory Data Analysis

I created a new file named **db_analysis.py** which will be used to load the data in pandas to manipulate the data to print what I need to see such as the shape, columns, etc...

By using the function known as main gaurd as shown below:

```python
if __name__ == "__main__":
    main()
```

I can run only the selected code that lies within the `main()` which essentially tells python to - Only run the `main()` function if this file is being run directly, not if it’s being imported as a module somewhere else.

## Formatting Table

Created the data_tranform.py file which will be used to format the table correctly so its prepared for data extraction. The `DataTranform()`class will be used to handle the format conversions

- Checking data types of columns
- Converting string columns datetime/numeric types
- Removing unwanted symbols (like $, %, etc.) from

### 🔧 Class Initialisation

1.  Data Tranform class initalise

```python
class DataTransform:
    def __init__(self, df):
        '''
        Args:
            df: pandas DataFrame containing loan payment data
        '''
        self.df = df.copy() #copy is created to avoid messing up the original
```

### 📦 Tranformation Functions

Functions overview:

| Method                     | Purpose                                                 |
| -------------------------- | ------------------------------------------------------- |
| check_data_types()         | Prints current data types of all columns                |
| convert_to_datetime()      | Converts a column to datetime using a given format      |
| convert_to_numeric(column) | Converts values to numeric (int/float)                  |
| to_category(columns)       | Categorises the chosen column to a cateogry - 0,1,2 etc |
| to_int(column)             | Converts column to integer                              |
| summary()                  | Prints summary of the data types                        |

## Extract information from DataFrame

After converting the columns into a more appropriate format I made the class `DataFrameInfo` in a new python file to extract info from the DataFrame to give insights into the data.

The purpose of this file is to streamline exploratory data analysis (EDA) by automating the display of basic statistics, null values, distinct counts, and overall structure of the dataset.

### Information Extraction

| Method             | Purpose                                                          |
| ------------------ | ---------------------------------------------------------------- |
| describe_columns() | Displays basic info on each column (dtype, non-null count)       |
| get_stats()        | Prints statistical summary incl. mean, std, min, max, and median |
| count_distinct()   | Displays count of distinct values in each column                 |
| count_nulls()      | Shows count and percentage of missing/null values per column     |
| display_shape()    | Prints the number of rows and columns in the DataFrame           |
