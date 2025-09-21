import pandas as pd
import csv
import os

def lectura_csv():
    filename = "cursos.csv"
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["curso", "instructor", "duracion"])
            writer.writerow(["Python", "Ana", "40h"])
            writer.writerow(["Java", "Luis", "35h"])
            writer.writerow(["SQL", "María", "30h"])
    try:
        df = pd.read_csv(filename)
        print("DataFrame leído desde CSV:")
        print(df)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")

if __name__ == "__main__":
    lectura_csv()
