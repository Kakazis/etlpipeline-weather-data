import requests
import json
from pathlib import Path 

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

api_key = '78faacaa5c6adf3fcf9ef2700fa7f853'
url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={api_key}'

def extract_weather_data(url:str) -> list:
    response = requests.get(url)
    data = response.json() #transforma a resposta da API em um dicionario

    if response.status_code != 200:
        logging.error("Erro na requisição")
        return[]
    if not data:
        logging.warning("Nenhum dado retornado")
        return[]

    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"Arquivo salvo em {output_path}")
    return data

extract_weather_data(url)