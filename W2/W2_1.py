import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

sns.set(style='darkgrid')

df = pd.read_csv('monthly-temp.csv')
print(df.head())

# Group the dataset by Source
df1 = df[ df['Source'] == 'GCAG' ] 

df2 = df[ df['Source'] == 'GISTEMP' ] 

print(df1.head())
print(df2.head())

# Timeseries line plot
# (df1)
fig = px.line(df1, x='Date', y='Mean', title='Global Temparture (Source: GCAG)')
# Output the Website with the plot
# fig.show()

# Output the html file 
# fig.write_html('Result01.html')

# (df2)
fig = px.line(df2, x='Date', y='Mean', title='Global Temparture (Source: GISTEMP)')
# fig.show()

# Draw two line plot together (df)
fig = px.line(df, x='Date', y='Mean', color = 'Source', line_group='Source', hover_name='Source')
# fig.show()

# 一行2个8x5大小的子图
fig,axs=plt.subplots(1,2,figsize=(8,5))
sns.histplot(data= df1, x='Mean', color='red', label='GCAG Temp', kde=True, ax=axs[0])
sns.histplot(data= df2, x='Mean', color='blue', label='GISTEMP', kde=True, ax=axs[1])

plt.legend()
# plt.show()
# plt.savefig('Result04.png')


