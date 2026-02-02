import pandas as pd
import os

data = {'Name' : ['Mohmad', 'Yaqoob', 'Ajaz'],
        'Age' : [23, 34, 23],
        'city': ['India', 'Japan', 'USA']
    }
df = pd.DataFrame(data)

new_row = {'Name': 'GF1', 'Age': 24, 'city':'city1'}
df.loc[len(df.index)] = new_row

new_row1 = {'Name': 'GF2', 'Age': 32, 'city':'city2'}
df.loc[len(df.index)] = new_row1

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'Sample_data.csv')


df.to_csv(file_path, index=False)


print(f"CSV file saved to {file_path}")