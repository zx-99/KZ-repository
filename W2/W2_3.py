import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np
sns.set(style='darkgrid')

df = pd.read_csv("population_by_country_2020.csv")
print(df.head())

# Draw distribution plot (kdeplot)
sns.kdeplot(df['Population (2020)'], shade=True)
plt.show()

# Draw histogram plot
sns.histplot(df, x='Population (2020)', color='red', kde=True)
plt.show()

# Map
fig = px.scatter_geo(df, locations='Country (or dependency)', locationmode='country names',
                     hover_name='Country (or dependency)', size='Population (2020)',
                     projection='natural earth')
fig.show()