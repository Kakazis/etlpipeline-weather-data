from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

user = os.getenv("POSTGRES_USER")
password = quote_plus(os.getenv("POSTGRES_PASSWORD"))
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DB")

def get_engine():
    logging.info(f"→ Conectando em {host}:5432/{database}")
    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:5432/{database}"
    )
engine = get_engine()

def load_weather_data(table_name:str, df):
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='append',
        index=False
    )
    
    logging.info(f"✅ Dados carregados com sucesso!\n") 
    
    df_check = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    logging.info(f"Total de registros na tabela: {len(df_check)}\n")