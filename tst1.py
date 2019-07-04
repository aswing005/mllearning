import pandas as pd
import math
df=pd.read_csv('D:\ml\Salary_Data.csv')
df['monthly sal']=df['Salary']/12
df.fillna(10000,inplace=True)
#forecast='Salary'
#fo=int(math.ceil(0.1*len(df)))
#df=df.shift(periods=3)
#df.dropna(inplace=True)
print(df)
