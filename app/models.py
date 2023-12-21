from django.db import models
import requests
from django.conf import settings

class Movement(models.Model):
    date = models.DateField()
    time = models.TimeField()
    moneda_from = models.CharField(max_length=100)
    cantidad_from = models.FloatField()
    moneda_to = models.CharField(max_length=100)
    cantidad_to = models.FloatField()

    def __str__(self):
        return f"Movement on {self.date} from {self.moneda_from} to {self.moneda_to}"

class APICall:
    def __init__(self):
        self.api_key = settings.API_KEY

    def get_exchange_rate(self, from_currency, to_currency):
        url = f'https://rest.coinapi.io/v1/exchangerate/{from_currency}/{to_currency}?apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and 'rate' in data:
            return data['rate']
        elif response.status_code == 400:
            raise ValueError('Error en la petición')
        elif response.status_code == 401:
            raise ValueError('Clave API incorrecta')
        elif response.status_code == 403:
            raise ValueError('API KEY no tiene suficientes privilegios')
        elif response.status_code == 429:
            raise ValueError('Excedido el límite de peticiones diarias')
        elif response.status_code == 550:
            raise ValueError('Sin datos disponibles')
        else:
            return None

    def get_eur_exchange_rate(self):
        url = f'https://rest.coinapi.io/v1/exchangerate/EUR?apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and 'rates' in data:
            return data['rates']
        elif response.status_code == 400:
            raise ValueError('Error en la petición')
        elif response.status_code == 401:
            raise ValueError('Clave API incorrecta')
        elif response.status_code == 403:
            raise ValueError('API KEY no tiene suficientes privilegios')
        elif response.status_code == 429:
            raise ValueError('Excedido el límite de peticiones diarias')
        elif response.status_code == 550:
            raise ValueError('Sin datos disponibles')
        else:
            return None