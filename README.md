### Finance-Loan-EDA

Exploratory Data Analysis of a customer loan portfolio to uncover trends, patterns, and risks within a financial institution. This project aims to support informed decisions on loan approvals, pricing, and risk management by using statistical and visualization techniques to improve portfolio performance and profitability.

## Task 1 - RDSDatabse Connector Setup

- Created my 'credentials.yaml' and included the AWS database connection details

- Initiated the class RDSDatabaseConnector:

  ```python
      class RDSDatabaseConnector:

          def __init__(self, credentials: str):
              """
              Initialising the database connector with the connector dict
              """
              self.credentials = load_credentials(credentials)
  ```

  1. Created the `init_db_engine()`function which initialises SQAlchemy engine using the following connection:

  ```python
  engine = create_engine(f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}"
          f"@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}")
  ```

  1. The `extract_data()` method handles the data extraction of the loan payment data from the RDSDatabase, Executed the SQL Query to select all records from the `loan_payments` table then used the `pd.read.sql()` function to load the query results into DataFrame the `return extract` will return the dataframe containing all the loan peyment records.

  ```python
  def extract_data(self):
      engine = self.init_db_engine()
      query = "SELECT * FROM loan_payments"
      extract = pd.read_sql(query, engine)
      return extract
  ```

  1. the `save_data()` method handles saving the data into a csv file on my local device the csv will then be used to load the data and query it to clean the data

  ```python
  def load_data(self, file):
      with open(file, 'r') as f:
          df = pd.read_csv(f)

      return df
  ```
