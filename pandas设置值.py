import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])

df.iloc[2,2] = 111
print(df)

df.loc['20130101', 'B']=222
print(df)

df.A[df['A'] > 4] = 4
print(df)

df[df['A'] > 4] = 4
print(df)

df['F'] = np.nan
print(df)

df['G']  = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
print(df)