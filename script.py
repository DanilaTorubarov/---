import pandas as pd # type: ignore
data=pd.read_csv('titanic.csv')
print((data['Pclass']==1).sum())