import pandas as pd
import numpy as np

def dataframe_numpy():
    ventas = np.array([
        [1500, 2000, 1800],
        [2200, 2100, 1900],
        [1700, 1600, 1750]
    ])
    df = pd.DataFrame(ventas, columns=["Q1", "Q2", "Q3"])
    print("DataFrame desde NumPy:")
    print(df)
    print("\nTipos de datos:")
    print(df.dtypes)

if __name__ == "__main__":
    dataframe_numpy()
