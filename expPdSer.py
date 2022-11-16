import numpy as np
# import pandas
import pandas as pd

#creating a empty series
ser=pd.Series()

#data to be listed
s=pd.Series([3,-5,7,4,8,9], index=['a','b','c','d','e','f'])

#using numpy to give a list of data into the panda series
#simple array
data=np.array(['l','a','n','i','c',])

#providing index
sr=pd.Series(data, index=[10,11,12,13,14])

#providing list
s1=pd.Series([10,11,12,13,14],data) ; s2=pd.Series([10,11,12,13,14])

print(ser)
print(s)
print(sr)
print(s1)
print(s2)
