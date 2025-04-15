import yaml
import pandas as pd 
from sqlalchemy import create_engine, text


class RDSDatabaseConnectior:

    def __init__(self, credentials: dict):
        """
        Initialising the database connector with the connector dict 
        """
        self.credentials = credentials