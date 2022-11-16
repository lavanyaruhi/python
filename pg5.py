import pandas as pd


#making data frame from csv file
data=pd.read_csv("nba.csv", index_col="Name")

#retriveing the multiple columns by indexing operator
first=data[["Age",'Salary','Height']]
print(first)

first=data.loc[['Raul Neto', 'Jeff Withey']]
print(first)


