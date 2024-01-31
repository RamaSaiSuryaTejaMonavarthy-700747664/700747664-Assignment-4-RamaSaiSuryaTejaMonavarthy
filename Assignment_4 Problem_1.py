import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'data.csv'
df = pd.read_csv(file_path)

# Show basic statistical description about the data
print(df.describe())

# Check for null values and replace them with the mean
df.fillna(df.mean(), inplace=True)

# Select all four columns and aggregate the data using: min, max, count, mean
columns_to_aggregate = df.columns  # Use all columns
aggregated_data = df[columns_to_aggregate].agg(['min', 'max', 'count', 'mean'])
print(aggregated_data)

# Filter the dataframe to select the rows with calories values between 500 and 1000
filtered_df1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]

# Filter the dataframe to select the rows with calories values > 500 and pulse < 100
filtered_df2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]

# Create a new dataframe df_modified without the "Maxpulse" column
df_modified = df.drop('Maxpulse', axis=1)

# Delete the "Maxpulse" column from the main df dataframe
df.drop('Maxpulse', axis=1, inplace=True)

# Convert the datatype of Calories column to int
df['Calories'] = df['Calories'].astype(int)

# Create a scatter plot for Duration and Calories
df.plot.scatter(x='Duration', y='Calories', title='Scatter Plot: Duration vs Calories')
plt.show()
