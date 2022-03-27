import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np
sns.set(style='darkgrid')


df = pd.read_csv('world-cities.csv')

print(df.head())

# count num of cities per country
grouped_df = df.groupby("country")
count_df = grouped_df.count()

# 重新设置索引（0，1，2，3，4，5.。。。。。）
count_df = count_df.reset_index()

print(count_df)

# Bar chart
num_cities = count_df['name']
bars = count_df['country']

# y= 0,1,2,3,4,5,...... len-1
y_pos = np.arange(len(bars))

# x轴标记值
# plt.xticks(y_pos, bars)

plt.plot(num_cities)
plt.show()

# Pie chart
plt.pie(num_cities)
plt.show()

# Map
fig = px.scatter_geo(count_df, locations='country', locationmode='country names',
                     hover_name='country', size='subcountry')
fig.show()