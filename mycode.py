import pandas as pd
import os
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Score': [85.5, 92.0, 88.0, 91.5]
}

df = pd.DataFrame(data)

print(df)
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample.csv')
df.to_csv(file_path,index=False)
