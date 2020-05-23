import pandas as pd
import numpy as np

df = pd.read_csv("linc_seg.csv",delimiter=";")
df_array = np.asarray(df)
flat_list = [item for sublist in df_array for item in sublist]
print(flat_list)