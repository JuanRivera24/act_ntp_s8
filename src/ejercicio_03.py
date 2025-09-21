import pandas as pd

def operaciones_series():
    precios = pd.Series([100, 150, 200])
    descuentos = pd.Series([10, 20, 15])
    print("Precios:")
    print(precios)
    print("\nDescuentos:")
    print(descuentos)
    print("\nPrecios con descuento (elemento a elemento):")
    print(precios - descuentos)
    print("\nPrecios con IVA (16%):")
    print(precios * 1.16)

if __name__ == "__main__":
    operaciones_series()
