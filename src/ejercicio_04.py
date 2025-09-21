import pandas as pd

def dataframe_diccionario():
    datos = {
        "Producto": ["Laptop", "Smartphone", "Tablet"],
        "Precio": [1200, 800, 400],
        "Categoria": ["Electrónica", "Electrónica", "Electrónica"]
    }
    df = pd.DataFrame(datos)
    print("DataFrame de productos:")
    print(df)
    print("\nColumna Precio:")
    print(df["Precio"])
    print("\nInformación del DataFrame:")
    print(df.info())

if __name__ == "__main__":
    dataframe_diccionario()
