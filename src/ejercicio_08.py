import pandas as pd
import json
import os

def lectura_json():
    filename = "vehiculos.json"
    if not os.path.exists(filename):
        vehiculos = [
            {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
            {"marca": "Ford", "modelo": "Fiesta", "año": 2019},
            {"marca": "Honda", "modelo": "Civic", "año": 2021}
        ]
        with open(filename, "w") as file:
            json.dump(vehiculos, file)
    df = pd.read_json(filename)
    print("DataFrame desde JSON:")
    print(df)
    print("\nTipos de datos:")
    print(df.dtypes)

if __name__ == "__main__":
    lectura_json()
