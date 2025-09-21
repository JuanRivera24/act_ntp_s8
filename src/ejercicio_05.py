import pandas as pd

def dataframe_lista_diccionarios():
    empleados = [
        {"empleado": "Ana", "salario": 2500, "departamento": "Ventas"},
        {"empleado": "Luis", "salario": 3000, "departamento": "TI"},
        {"empleado": "María", "salario": 2800, "departamento": "Recursos Humanos"}
    ]
    df = pd.DataFrame(empleados)
    print("DataFrame de empleados:")
    print(df)
    print("\nFila 0:")
    print(df.loc[0])

if __name__ == "__main__":
    dataframe_lista_diccionarios()
