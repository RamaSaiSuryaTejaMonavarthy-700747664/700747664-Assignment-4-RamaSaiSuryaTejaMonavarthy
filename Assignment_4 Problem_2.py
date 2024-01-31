import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Import the data
data = pd.read_csv('Salary_Data.csv')

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['YearsExperience']], data['Salary'], test_size=1/3, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict salaries for both train and test sets
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate mean squared error
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
print(f'Mean Squared Error (Train): {mse_train}')
print(f'Mean Squared Error (Test): {mse_test}')

# Visualize the data and regression line
plt.scatter(X_train, y_train, label='Train Data')
plt.scatter(X_test, y_test, label='Test Data', marker='x')
plt.plot(X_train, y_train_pred, color='red', label='Regression Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary Prediction')
plt.legend()
plt.show()


