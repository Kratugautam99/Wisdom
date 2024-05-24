import pandas as pd
import seaborn as sns
import openpyxl
from matplotlib import pyplot as plt
df = pd.read_excel('test CSVs/linechart.xlsx')
plt.figure(figsize=(10,4))
plt.plot(df['Quarter'],df['Fridge'],color='red',label='Fridge')
plt.plot(df['Quarter'],df['Washing Machine'],color='blue',label='Washing Machine')
plt.plot(df['Quarter'],df['Dishwasher'],color='green',label='Dishwasher')
plt.title('Product Sales')
plt.ylabel('Revenue(in $)')
plt.xlabel('Financial Quarter')
plt.legend()
plt.show()
total_sales=df[['Fridge','Dishwasher','Washing Machine']].sum()
print(total_sales,total_sales.index)
plt.pie(total_sales,labels=total_sales.index,autopct='%1.2f%%',explode=(0.1,0.3,0),shadow=True,startangle=27)
plt.title('Product Sales')
plt.show()
df.plot(kind='bar',x='Quarter',ylabel='Reveue(in $)')#you can set_index('Quarter'), so it will take x as index by default.
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.title('Product Sales')
plt.show()
df1 = pd.read_excel('test CSVs/histograms.xlsx')
sns.histplot(data=df1,x='Exam_Score',kde=True)#aka[sns.histplot(df1['Exam_Score'],kde=True)]histogram is better in seaborn library than matplotlib library{plt.hist(){it doesnot have kde argument also} instead of sns.histplot() can also be used}.
plt.ylabel('Count')
plt.title('Exam Scores')
plt.show()
df2 = pd.read_excel('test CSVs/scatter_plot.xlsx')
sns.scatterplot(data=df2, x='area_square_ft',y='price')#aka[sns.scatterplot(df2['area_square_ft])] Running plt.ylabel separately will return some other way of representing data.
sns.lineplot(data=df2, x='area_square_ft', y='price', color='black')#aka[sns.scatterplot(df2['area_square_ft'])]
plt.title('Real Estate')
plt.show()


