#exppd1df.py


import pandas as pd

#calling dataframe constructor
df=pd.DataFrame()
print(df)
print("*************************************************************")
#using dict data ---> DF
#data into the dataframe
data={'country': ['india','bengium','brazil'],
      'capital': ['New Delhi','Brussel','Brasilia'],
      'population': [1113435,3435234,235346375]
      }
df1=pd.DataFrame(data,columns=['country','capital','population'])
print(df1)
print("***************************************************")
lst=['greeks','for','greeks','is','portal','for','greeks']
df=pd.DataFrame(lst)
print(df)
print("******************************************")

#initializing data to the list
data={'name':['nayhi','neha','sana','lish'],'age':[23,33,22,21]}
df=pd.DataFrame(data)
print(df)

df1.to_csv('C:/PythonCode/file.csv')
