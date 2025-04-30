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
new_row_loc={'Name':'GF1', 'Age':'20','City':'Bangalore','Score':'56.97'}
df.loc[len(df.index)]=new_row_loc


print(df)
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample.csv')
df.to_csv(file_path,index=False)
