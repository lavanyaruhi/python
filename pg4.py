# example of the datasets by manipulation of the csv file to to crud operations

import pandas as pd
df=pd.read_csv('C:\PythoCode\online-retail.csv')
# print the first "n" rows in the data frames [default n=5
df.head()
print(df)


print("\n**********************************************************\n")
# add new datafrace that is updated in the file but not in excel csv file
df['LinePrice']=df['Quality']*df['UnitPrice']
df.head()
print(df)

print("\n**************************************\n")
df_customers=df.groupby('CustomerId').agg(
    orders=('InvoiceNo','nunique'),
    skus=('StockCode','nunique'),
    quality=('Quality','sum'),
    revenue=('LinePrice','sum')
).reset_index()

df_customers.head()
print(df_customers)
