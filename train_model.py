# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Load the dataset
data = pd.read_csv('salaries.csv')

# Select relevant features for prediction
features = ['experience_level', 'employment_type', 'job_title', 'employee_residence', 'remote_ratio', 'company_location', 'company_size']
target = 'salary_in_usd'

# Convert categorical variables to numerical using one-hot encoding
data = pd.get_dummies(data, columns=features, drop_first=True)

# Exclude 'salary_currency' from the features
data = data.drop(columns=['salary_currency'])

# Split the data into train and test sets
X = data.drop(columns=[target])
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Example of using the model for prediction
example_data = X_test.iloc[0].values.reshape(1, -1)
predicted_salary = model.predict(example_data)
print('Predicted Salary:', predicted_salary[0])
