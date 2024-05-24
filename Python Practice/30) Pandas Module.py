import pandas as pd 
#import openpyxl as op #for working with excels also.
df = pd.read_csv('test CSVs/movies.csv')#If you don't want to extract dataframe,  you can also create a dataframe by using pd.dataframe.
print(df,df.sample(4),df.head(4),df.tail(4),df['imdb_rating'],df.shape,sep="\n\n\n\n")
dfh = df[df.industry == 'Hollywood']
dfb = df[df.industry == 'Bollywood']
print(dfh,dfh)
#you can also use .imdh_rating.min()/max()/mean() and .rows or .columns and .industry.unique() for knowing rows and columns we can df.shape, df.rows and df.columns.
print(df.language.value_counts())
print(df[(df.release_year>=2000) & (df.release_year<=2010)])
print(df.describe(),df.info())
df['age'] = df["release_year"].apply(lambda x: 2024 - x)
df['profit'] = df.apply(lambda x: x['revenue'] - x['budget'],axis = 1)
df.set_index('title',inplace=True)#Reverse it by using df.reset_index(inplace=True).
print(df.loc['Avatar'])
#for list, l[0]  but for dataframe, df.iloc[0] or df.loc[Index] as we used set_index we can replace index with index.
#can use skiprows/header to skiprows and nrows to skipcolumns and names parameter to define names of all columns in the dataframe, na_values to make the not available value NaN in both list and dict format;
#In dict format you can be specific to a particular column and general in list format also can use fillna('0'/0),fillna({}) or ({}). It also has same features as na_values and also method='ffill' or 'bfill' with limit and axis,
#Interpolate it fillna with mean of f and b values, dropna drop the NaN rows we can ofcourse set thresh and how='all'or'any', you can use parse_dates to convert informal data type of dates to the one that pandas understand.These all parameter can be used in pd.read_csv function.
#you can do same with excel by opening it by using read_excel or write it with excel_writer and saving it by using to_excel. with index,header and sheetname parameter.also you merge files ny using pd.merge(file1,file2,on='parameter name').
#df.replace(list/str/dict,list/str/int) or df.replace(dict of elements to replace with other elements unlike dict with columns and elements to replace, new elements); can also be used with np.nan from numpy to do same as fillna.
df.loc[df['unit'] == 'Millions', 'profit'] *= 1000000
df.loc[df['unit'] == 'Thousands', 'profit'] *= 1000
g = df.groupby("industry")
for industry,data in g:
    print('\n')
    print('industry:',industry)
    print('max profit:',int(data.profit.max()))#data.loc[data.profit == data.profit.max(),'unit'].values[0] if we didn't changed the million rows and thousands rows as per their units.
# print(g.mean) #IDK why these aren't' working here even after putting () in front of them.
# print(g.min)
# print(g.max)
print(g.get_group('Bollywood'))
print(g.get_group('Hollywood'))
print(g.size())
print(g.describe())
#pd.concat([list dfs],keys=[specify keys],ignore_index=True,axis=1forcolmerging0forrowmerging)
#while creating the dateframe you can interchange specific index.
#you can merging with pd.merge(df1,df2,on='primary key',how='type of join like: inner,outer,left,right')
df.to_csv('test CSVs/finalmovies.csv')#can remove header and index by passing it False as parameter in this function.