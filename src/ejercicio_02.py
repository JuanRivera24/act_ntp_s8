import pandas as pd

def calificaciones_estudiantes():
    calificaciones = pd.Series([85, 92, 78], index=["Matemáticas", "Ciencias", "Historia"])
    print("Serie de Calificaciones:")
    print(calificaciones)
    print("\nCalificación en Ciencias:", calificaciones["Ciencias"])
    print("\nInformación de la Serie:")
    print(calificaciones.describe())
    print("\nSuma:", calificaciones.sum())
    print("Promedio:", calificaciones.mean())

if __name__ == "__main__":
    calificaciones_estudiantes()
