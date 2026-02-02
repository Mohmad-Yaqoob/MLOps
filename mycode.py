import pandas as pd
import os

data = {'Name' : ['Mohmad', 'Yaqoob', 'Ajaz'],
        'Age' : [23, 34, 23],
        'city': ['India', 'Japan', 'USA']
    }
df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'Sample_data.csv')


df.to_csv(file_path, index=False)


print(f"CSV file saved to {file_path}")