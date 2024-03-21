import pandas as pd
import sqlite3
from datetime import datetime

conn = sqlite3.connect('Healthcare_Data.sqlite')

df1 = pd.read_csv('datasets/Heart_Disease_Prediction.csv')

df1.to_sql('Heart_Disease', conn, index=False, if_exists='replace', dtype={'index': 'INTEGER PRIMARY KEY'})