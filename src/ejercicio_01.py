import pandas as pd

def analisis_ventas():
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165])
    print("Serie de Ventas Diarias:")
    print(ventas)
    print("\nVenta en el día 3:", ventas[3])
    print("\nPromedio de ventas:", ventas.mean())
    print("\nVentas ordenadas:")
    print(ventas.sort_values())

if __name__ == "__main__":
    analisis_ventas()
