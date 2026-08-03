import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Anil', 'Bharath', 'Charan', 'Deepa', 'Farah'],
    'Age': [24, 26, 25, 28, 27],
    'Salary': [35000, 42000, np.nan, 50000, 48000]
})

df_selected = df[['Age', 'Salary']].copy()
df_selected['Salary'] = df_selected['Salary'].fillna(df_selected['Salary'].mean())
df_transformed = (df_selected - df_selected.min()) / (df_selected.max() - df_selected.min())

print("Final Dataset:\n", df_transformed)
