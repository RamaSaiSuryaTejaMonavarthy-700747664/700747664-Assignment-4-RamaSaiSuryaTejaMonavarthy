import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.csv'
df = pd.read_csv(file_path)

print(df.describe())

df.fillna(df.mean(), inplace=True)

columns_to_aggregate = df.columns 
aggregated_data = df[columns_to_aggregate].agg(['min', 'max', 'count', 'mean'])
print(aggregated_data)
filtered_df1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
filtered_df2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
df_modified = df.drop('Maxpulse', axis=1)
df.drop('Maxpulse', axis=1, inplace=True)
df['Calories'] = df['Calories'].astype(int)
df.plot.scatter(x='Duration', y='Calories', title='Scatter Plot: Duration vs Calories')
plt.show()
