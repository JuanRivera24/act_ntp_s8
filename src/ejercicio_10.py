import pandas as pd
import requests

def dataframe_api():
    url = "https://playground.mockoon.com/users"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            print("Primeras 5 filas del DataFrame:")
            print(df.head())
            print("\nInformación del DataFrame:")
            print(df.info())
        else:
            print(f"Error en la petición: Código {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)

if __name__ == "__main__":
    dataframe_api()
